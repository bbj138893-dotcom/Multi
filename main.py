import telebot
import os
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_LINK = "https://t.me/PROFESSORXZAMINHACKER"
DEVELOPER_ID = "@SIGMAXZAMIN"
BOT_USERNAME = "@ZAMINXMILTISAVEBOT"

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")


def main_keyboard():
    kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("📥 Start Downloading")
    kb.add("📢 Official Channel", "👨‍💻 Developer")
    return kb


@bot.message_handler(commands=["start"])
def start(message):
    name = message.from_user.first_name
    text = f"""
━━━━━━━━━━━━━━━━━━━━━━━
🚀 <b>MULTI SAVER BOT</b>
━━━━━━━━━━━━━━━━━━━━━━━

👋 Welcome <b>{name}</b>

📥 Download from multiple platforms  
⚡ Fast • Clean • Simple  

👇 Press the button below to start

━━━━━━━━━━━━━━━━━━━━━━━
"""
    bot.send_message(message.chat.id, text, reply_markup=main_keyboard())


@bot.message_handler(func=lambda m: m.text == "📥 Start Downloading")
def ask_link(message):
    bot.send_message(
        message.chat.id,
        "📎 <b>Send your video link</b>\n\n"
        "Supported: Instagram • Facebook • Twitter • More\n\n"
        "⚠️ Invalid links will be rejected"
    )


@bot.message_handler(func=lambda m: m.text == "📢 Official Channel")
def channel(message):
    bot.send_message(
        message.chat.id,
        f"📢 <b>OFFICIAL CHANNEL</b>\n\n"
        f"Updates • Features • Tools\n\n"
        f"👉 Join now:\n{CHANNEL_LINK}"
    )


@bot.message_handler(func=lambda m: m.text == "👨‍💻 Developer")
def dev(message):
    bot.send_message(
        message.chat.id,
        f"👨‍💻 <b>Developer</b>\n\n{DEVELOPER_ID}"
    )


@bot.message_handler(func=lambda m: True)
def handle_link(message):
    if "http" not in message.text:
        bot.send_message(
            message.chat.id,
            "❌ <b>Invalid Link</b>\n\n"
            "Please send a valid video URL 🔗"
        )
        return

    temp = bot.send_message(message.chat.id, "🚀")
    time.sleep(2)
    bot.delete_message(message.chat.id, temp.message_id)

    bot.send_message(
        message.chat.id,
        f"""
━━━━━━━━━━━━━━━━━━━━━━━
📥 <b>Processing Link</b>

Your link is received  
Downloading will start shortly…

⚡ Please wait
━━━━━━━━━━━━━━━━━━━━━━━

👨‍💻 {DEVELOPER_ID}
"""
    )


print("🤖 Multi Saver Bot is running...")
bot.infinity_polling(skip_pending=True)
