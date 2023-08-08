from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛒Buyurtma berish"),
            KeyboardButton(text="📃Batafsil ma`lumot")
        ],
        [
            KeyboardButton(text="☎Adminga bog`lanish"),
            KeyboardButton(text="🌏Tilni o`zgartirish")
        ],
        [
            KeyboardButton(text="💻Ijtimoiy tarmoqlar")
        ]
    ],
    resize_keyboard=True
)

check_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Tasdiqlash"),
            KeyboardButton(text="❌ Bekor qilish")
        ]
    ],
    resize_keyboard=True
)

tolov = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="to`lov qildim"),

        ]
    ],
    resize_keyboard=True
)
