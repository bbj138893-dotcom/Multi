import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ================= CONFIG =================
BOT_TOKEN = os.getenv("BOT_TOKEN")  # ❗ TOKEN YAHAN NAHI DALNA
BOT_USERNAME = "@ZAMINXMILTISAVEBOT"
CHANNEL_LINK = "https://t.me/PROFESSORXZAMINHACKER"
DEVELOPER_ID = "@SIGMAXZAMIN"

# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 Start Downloading", callback_data="start_download")],
        [InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"""
━━━━━━━━━━━━━━━━━━━━━━━
👋 Welcome {update.effective_user.first_name}

🔥 Multi Saver Bot
📥 Download from multiple platforms

➤ Click 🚀 Start Downloading
➤ Send your video link
➤ Get result instantly

👨‍💻 Developer: {DEVELOPER_ID}
━━━━━━━━━━━━━━━━━━━━━━━
""",
        reply_markup=reply_markup
    )

# ================= BUTTON =================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "start_download":
        msg = await query.message.reply_text(
            "🚀 Send your download link now"
        )
        # auto delete rocket message
        await asyncio.sleep(3)
        await msg.delete()

# ================= LINK HANDLER =================
async def link_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if not text.startswith("http"):
        await update.message.reply_text(
            "❌ Invalid link\n\nPlease send a valid URL 🔗"
        )
        return

    temp = await update.message.reply_text("🚀 Processing your link...")
    await asyncio.sleep(2)
    await temp.delete()

    await update.message.reply_text(
        f"""
━━━━━━━━━━━━━━━━━━━━━━━
✅ LINK RECEIVED

🔗 Your link:
{text}

⚠️ Downloader engine coming soon
(Structure ready ✔️)

👨‍💻 Developer: {DEVELOPER_ID}
📢 Channel: {CHANNEL_LINK}
━━━━━━━━━━━━━━━━━━━━━━━
"""
    )

# ================= MAIN =================
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, link_handler))
    app.add_handler(MessageHandler(filters.StatusUpdate.ALL, lambda u, c: None))
    app.add_handler(MessageHandler(filters.TEXT, link_handler))

    app.add_handler(
        MessageHandler(filters.ALL, lambda update, context: None)
    )

    app.add_handler(
        MessageHandler(filters.UpdateType.CALLBACK_QUERY, button_handler)
    )

    print("🤖 Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
