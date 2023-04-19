from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


shareMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔗 Botni ulashish", switch_inline_query="Video yuklab beruvchi Bot"),
        ],
    ],
)