import os
import asyncio
import subprocess
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode

BOT_TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_LINK = "https://t.me/PROFESSORXZAMINHACKER"
DEVELOPER_ID = "@SIGMAXZAMIN"

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


# 🔹 START COMMAND
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "🚀 <b>Multi Saver Bot</b>\n\n"
        "📥 Send any video link\n"
        "⚡ Fast & Simple\n\n"
        "👇 Send link to start\n\n"
        f"📢 Channel: <a href='{CHANNEL_LINK}'>Join</a>\n"
        f"👨‍💻 Developer: {DEVELOPER_ID}"
    )


# 🔹 HANDLE LINKS
@dp.message()
async def download_video(message: types.Message):
    url = message.text.strip()

    if not url.startswith("http"):
        await message.answer(
            "❌ <b>Invalid link</b>\n"
            "Send a valid video URL 🔗"
        )
        return

    processing = await message.answer("🚀 Processing...")

    file_name = "video.mp4"

    try:
        # 🔥 yt-dlp download
        cmd = [
            "yt-dlp",
            "-f", "mp4",
            "-o", file_name,
            url
        ]

        subprocess.run(cmd, check=True)

        await processing.delete()

        await message.answer_video(
            video=types.FSInputFile(file_name),
            caption=f"📥 <b>Downloaded Successfully</b>\n\n👨‍💻 {DEVELOPER_ID}"
        )

    except Exception as e:
        await processing.delete()
        await message.answer(
            "❌ <b>Download failed</b>\n"
            "Link not supported or error occurred"
        )

    finally:
        if os.path.exists(file_name):
            os.remove(file_name)


# 🔹 RUN BOT
async def main():
    print("Bot started successfully")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
