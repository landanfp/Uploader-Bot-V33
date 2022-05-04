

import asyncio
from pyrogram import types, errors
from plugins.config import Config
from plugins.database.database import db

async def OpenSettings(m: Message, user_id: int):
    try:
        await m.edit(
            text="Here You Can Change or Configure Your Settings:",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(f"Upload as {'Video' if (await db.get_upload_as_doc(id=user_id)) is False else 'Document'} ✅", callback_data="triggerUploadMode")],
                    [InlineKeyboardButton("Show Thumbnail", callback_data="showThumbnail")],
                    [InlineKeyboardButton("Close", callback_data="close")]
                ]
            )
        )
    except MessageNotModified:
        pass
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await m.edit("You Are Spamming!")
    except Exception as err:
        raise err

