import telebot
import os
import subprocess
import time

TOKEN = os.getenv("BOT_TOKEN")

CHANNEL = "https://t.me/PROFESSORXZAMINHACKER"
DEV = "@SIGMAXZAMIN"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# ---------- START ----------
@bot.message_handler(commands=["start"])
def start(message):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        telebot.types.InlineKeyboardButton("🚀 Start Downloading", callback_data="start_dl"),
        telebot.types.InlineKeyboardButton("📢 Official Channel", url=CHANNEL),
        telebot.types.InlineKeyboardButton("👨‍💻 Developer", url="https://t.me/SIGMAXZAMIN")
    )

    bot.send_message(
        message.chat.id,
        f"""
🚀 <b>Multi Saver Bot</b>

Welcome <b>{message.from_user.first_name}</b> 👋

📥 Download Instagram Videos
⚡ Fast • Real • Clean

👇 Choose an option below
""",
        reply_markup=keyboard
    )

# ---------- BUTTON ----------
@bot.callback_query_handler(func=lambda call: call.data == "start_dl")
def ask_link(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "🔗 <b>Send your Instagram link</b>")

# ---------- HANDLE LINK ----------
@bot.message_handler(func=lambda m: "instagram.com" in m.text)
def download_video(message):
    rocket = bot.send_message(message.chat.id, "🚀")
    time.sleep(2)
    bot.delete_message(message.chat.id, rocket.message_id)

    bot.send_message(message.chat.id, "📥 <b>Downloading…</b>\nPlease wait ⚡")

    filename = f"{message.chat.id}.mp4"

    try:
        subprocess.run(
            ["yt-dlp", "-f", "mp4", "-o", filename, message.text],
            check=True
        )

        with open(filename, "rb") as video:
            bot.send_video(
                message.chat.id,
                video,
                caption=f"✅ <b>Download Complete</b>\n\n👨‍💻 {DEV}"
            )

        os.remove(filename)

    except:
        bot.send_message(
            message.chat.id,
            "❌ <b>Failed</b>\nVideo may be private or restricted"
        )

# ---------- INVALID ----------
@bot.message_handler(func=lambda m: True)
def invalid(message):
    bot.send_message(message.chat.id, "❌ <b>Send a valid Instagram link</b>")

print("🤖 REAL Multi Saver Bot Running")
bot.infinity_polling(skip_pending=True)
