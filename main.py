import telebot
import os
import subprocess
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_LINK = "https://t.me/PROFESSORXZAMINHACKER"
DEVELOPER_ID = "@SIGMAXZAMIN"

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        f"""
🚀 <b>Multi Saver Bot</b>

👋 Welcome <b>{message.from_user.first_name}</b>

📥 Instagram Video Downloader
⚡ Fast • Clean • Real

👇 Send Instagram link
"""
    )


@bot.message_handler(func=lambda m: True)
def download_instagram(message):
    url = message.text

    if "instagram.com" not in url:
        bot.send_message(
            message.chat.id,
            "❌ <b>Invalid Link</b>\n\nSend a valid Instagram video URL"
        )
        return

    temp = bot.send_message(message.chat.id, "🚀")
    time.sleep(2)
    bot.delete_message(message.chat.id, temp.message_id)

    bot.send_message(message.chat.id, "📥 <b>Downloading video…</b>\nPlease wait ⚡")

    try:
        filename = f"video_{message.chat.id}.mp4"

        subprocess.run(
            ["yt-dlp", "-o", filename, url],
            check=True
        )

        with open(filename, "rb") as video:
            bot.send_video(
                message.chat.id,
                video,
                caption=f"✅ <b>Downloaded</b>\n\n👨‍💻 {DEVELOPER_ID}"
            )

        os.remove(filename)

    except Exception as e:
        bot.send_message(
            message.chat.id,
            "❌ <b>Download failed</b>\n\nVideo may be private or restricted"
        )


print("🤖 Bot running with REAL downloader")
bot.infinity_polling(skip_pending=True)
