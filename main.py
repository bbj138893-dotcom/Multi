import re
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ================= CONFIG =================
BOT_TOKEN = "8249726471:AAFFvx1mI3vsQuEVy3Wz0i0WiCaobhY5FnQ"   # 👈 BotFather token yahan paste karo

BOT_USERNAME = "@ZAMINXMILTISAVEBOT"
CHANNEL_LINK = "https://t.me/PROFESSORXZAMINHACKER"
DEVELOPER_ID = "@SIGMAXZAMIN"
BOT_NAME = "MULTI SAVER BOT"
# ==========================================

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

user_waiting_for_link = set()

# ---------- Keyboards ----------
start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🚀 Start Downloading", callback_data="start_dl")],
    [InlineKeyboardButton(text="📢 Join Channel", url=CHANNEL_LINK)]
])

again_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📥 Download Another", callback_data="start_dl")],
    [InlineKeyboardButton(text="📢 Channel", url=CHANNEL_LINK)]
])

# ---------- Helpers ----------
def is_valid_link(text: str) -> bool:
    return bool(re.search(r"https?://", text))

# ---------- Handlers ----------
@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    text = (
        "━━━━━━━━━━━━━━━━━━━━━━━\n"
        "🚀 <b>MULTI SAVER BOT</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"👋 Welcome <b>{message.from_user.first_name}</b>\n\n"
        "➤ All social media saver\n"
        "➤ Fast & clean\n"
        "➤ No spam\n\n"
        "👇 Start by clicking the button below\n\n"
        f"👨‍💻 Developer: {DEVELOPER_ID}\n"
        f"🤖 Bot: {BOT_USERNAME}\n"
        "━━━━━━━━━━━━━━━━━━━━━━━"
    )
    await message.answer(text, reply_markup=start_kb)

@dp.callback_query(lambda c: c.data == "start_dl")
async def ask_link(call: types.CallbackQuery):
    user_waiting_for_link.add(call.from_user.id)
    await call.message.answer(
        "━━━━━━━━━━━━━━━━━━━━━━━\n"
        "📥 <b>SEND YOUR LINK</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "➤ Paste video / post link\n"
        "➤ Supported: social platforms\n\n"
        "❝ Fast • Simple • Clean ❞ ⚡\n"
        "━━━━━━━━━━━━━━━━━━━━━━━"
    )
    await call.answer()

@dp.message()
async def handle_link(message: types.Message):
    uid = message.from_user.id

    if uid not in user_waiting_for_link:
        return

    user_waiting_for_link.remove(uid)

    # 🚀 temp emoji (auto delete)
    rocket = await message.answer("🚀")
    await asyncio.sleep(1.5)
    await rocket.delete()

    if not is_valid_link(message.text):
        await message.answer(
            "━━━━━━━━━━━━━━━━━━━━━━━\n"
            "❌ <b>INVALID LINK</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "➤ Please send a valid URL\n"
            "➤ Example: https://...\n\n"
            "Try again 👇",
            reply_markup=again_kb
        )
        return

    # ⚠️ DEMO MODE (Downloader placeholder)
    await message.answer(
        "━━━━━━━━━━━━━━━━━━━━━━━\n"
        "🎉 <b>LINK RECEIVED</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "✅ Your link is valid\n"
        "⏳ Download engine coming next\n\n"
        "❝ One link. One action. ❞ ⚡\n\n"
        f"👨‍💻 Developer: {DEVELOPER_ID}\n"
        f"📢 Channel: {CHANNEL_LINK}\n"
        "━━━━━━━━━━━━━━━━━━━━━━━",
        reply_markup=again_kb
    )

# ---------- Run ----------
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
