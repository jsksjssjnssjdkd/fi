
import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, aimport re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

IMG_BOT1 = getenv("IMG_BOT1")

OWNER = getenv("OWNER")

NAME_BOT = getenv("NAME_BOT")


@app.on_message(
     command(["مبرمج السورس","المطور","مطور السورس","المبرمج"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a6c96cdbd066ca2388d06.jpg",
        caption=f"""◍ مش محتاجين نكتب كلام كتير خش ع اول زرار وانت هتعرف""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("• 𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍 ☤ ", url=f"https://t.me/WORLD_MUSIC_F"),
                ],
            ]
        ),
    )

@app.on_message(
    command(["البوت"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG_URL}",
        caption=f"اسمي {MUSIC_BOT_NAME} ينجم 😮‍💨💕", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- Devoleper Bot .", url=f"https://t.me/{OWNER}")
                ],[
                    InlineKeyboardButton(
                        "اضف البوت الي مجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
            ]
        ),
    )