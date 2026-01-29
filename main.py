import os
import asyncio
import logging
import subprocess
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ================= CONFIG =================
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_LINK = "https://t.me/PROFESSORXZAMINHACKER"
DEVELOPER_ID = "@SIGMAXZAMIN"

# ================= LOGGING =================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 *Multi Saver Bot*\n\n"
        "📥 Send any video link\n"
        "⚡ Fast & Simple\n\n"
        f"👨‍💻 Dev: {DEVELOPER_ID}",
        parse_mode="Markdown"
    )

# ================= DOWNLOAD FUNCTION =================
async def download_video(url: str, chat_id, app):
    try:
        cmd = [
            "yt-dlp",
            "-f",
            "mp4",
            "-o",
            "video.%(ext)s",
            url
        ]

        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        await process.communicate()

        for file in os.listdir():
            if file.startswith("video."):
                await app.bot.send_video(
                    chat_id=chat_id,
                    video=open(file, "rb"),
                    caption="📥 Downloaded Successfully\n"
                            f"👨‍💻 {DEVELOPER_ID}"
                )
                os.remove(file)
                return

        await app.bot.send_message(chat_id, "❌ Download failed")

    except Exception as e:
        await app.bot.send_message(chat_id, f"⚠️ Error:\n{e}")

# ================= HANDLE LINKS =================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    chat_id = update.message.chat_id

    rocket = await update.message.reply_text("🚀")
    await asyncio.sleep(2)
    await rocket.delete()

    if not text.startswith("http"):
        await update.message.reply_text(
            "❌ Invalid link\n\n"
            "📥 Send a valid video URL"
        )
        return

    await update.message.reply_text("📥 Downloading… please wait")
    await download_video(text, chat_id, context.application)

# ================= MAIN =================
def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN not found")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running")
    app.run_polling()

if __name__ == "__main__":
    main()
