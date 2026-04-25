import asyncio
import logging
import os
import shlex
import subprocess
from typing import Sequence

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("telegram-hermes-bot")


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
HERMES_CMD = os.getenv("HERMES_CMD", "hermes --no-interactive")
HERMES_TIMEOUT_SECONDS = int(os.getenv("HERMES_TIMEOUT_SECONDS", "120"))
MAX_TELEGRAM_MESSAGE = 4096


def split_message(text: str, limit: int = MAX_TELEGRAM_MESSAGE) -> list[str]:
    return [text[i : i + limit] for i in range(0, len(text), limit)] or [""]


def hermes_command() -> Sequence[str]:
    command = shlex.split(HERMES_CMD)
    if not command:
        raise RuntimeError("HERMES_CMD is empty")
    return command


def call_hermes_sync(user_message: str) -> str:
    try:
        completed = subprocess.run(
            hermes_command(),
            input=user_message,
            text=True,
            capture_output=True,
            timeout=HERMES_TIMEOUT_SECONDS,
            check=False,
        )
    except FileNotFoundError as exc:
        raise RuntimeError(
            "Hermes command not found. Set HERMES_CMD to the exact CLI command."
        ) from exc
    except subprocess.TimeoutExpired as exc:
        raise TimeoutError(
            f"Hermes timed out after {HERMES_TIMEOUT_SECONDS} seconds."
        ) from exc

    stdout = (completed.stdout or "").strip()
    stderr = (completed.stderr or "").strip()

    if completed.returncode != 0:
        detail = stderr or stdout or f"exit code {completed.returncode}"
        raise RuntimeError(f"Hermes failed: {detail}")

    if not stdout:
        raise RuntimeError("Hermes returned an empty response.")

    return stdout


async def call_hermes(user_message: str) -> str:
    return await asyncio.to_thread(call_hermes_sync, user_message)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Send a message and I will pass it to Hermes.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or not update.message.text:
        return

    user_message = update.message.text.strip()
    if not user_message:
        await update.message.reply_text("Empty message.")
        return

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING,
    )

    try:
        response = await call_hermes(user_message)
    except TimeoutError as exc:
        logger.warning("Hermes timeout: %s", exc)
        response = str(exc)
    except Exception as exc:
        logger.exception("Hermes error")
        response = f"Error: {exc}"

    for chunk in split_message(response):
        await update.message.reply_text(chunk)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.exception("Telegram handler error", exc_info=context.error)


def main() -> None:
    if not TELEGRAM_BOT_TOKEN:
        raise SystemExit("Set TELEGRAM_BOT_TOKEN before running the bot.")

    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_error_handler(error_handler)

    logger.info("Bot started. Hermes command: %s", HERMES_CMD)
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
