from Rose import bot as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from Rose.utils.lang import *


fbuttons = InlineKeyboardMarkup(
        [
        [
            InlineKeyboardButton(
                text="𝗟𝗮𝗰𝗼𝘀𝘁𝗲 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 🇦🇿", url="https://t.me/LacosteSup"
            ),
            InlineKeyboardButton(
                text="👤Rəsmi Kanal", url="https://t.me/LacosteProject"
            )
        ], 
        [
            InlineKeyboardButton(
                text="⚒ Köməkçi", url="https://t.me/quliyevv_17"
            ),
            InlineKeyboardButton(
                text="💬 Chat", url="https://t.me/https://t.me/MorphinChat"
            )
        ], 
        [
            InlineKeyboardButton(
                text="🖥 Developer", url="https://t.me/Axhmedov"
            )
        ], 
        [
            InlineKeyboardButton("« Geri", callback_data='startcq')
        ]
        ]
)

keyboard =InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="🇱🇷 English", callback_data="languages_en"
            ),
            InlineKeyboardButton(
                text="🇱🇰 සිංහල", callback_data="languages_si"
            )
        ],
        [
            InlineKeyboardButton(
                text="🇮🇳 हिन्दी", callback_data="languages_hi"
            ),
            InlineKeyboardButton(
                text="🇮🇹 Italiano", callback_data="languages_it"
            )
        ],
        [
            InlineKeyboardButton(
                text="🇮🇳 తెలుగు", callback_data="languages_ta"
            ),
            InlineKeyboardButton(
                text="🇮🇩 Indonesia", callback_data="languages_id"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🇦🇪 عربي", callback_data="languages_ar"
            ),
            InlineKeyboardButton(
                text="🇮🇳 മലയാളം", callback_data="languages_ml"
            ), 
        ],
        [
            InlineKeyboardButton(
                text="🇲🇼 chichewa", callback_data="languages_ny"
            ), 
            InlineKeyboardButton(
                text="🇩🇪 german", callback_data="languages_ge"
            ), 
        ], 
        [  
            InlineKeyboardButton("« Geri", callback_data='startcq')
        ]
    ]
)

@app.on_callback_query(filters.regex("_langs"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    user = CallbackQuery.message.from_user.mention
    await app.send_message(
        CallbackQuery.message.chat.id,
        text= "The list of available languages:",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()
    
@app.on_callback_query(filters.regex("_about"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=_["menu"],
        reply_markup=fbuttons,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()

