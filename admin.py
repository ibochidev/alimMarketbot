from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from config import ADMINS


class IsSuperAdmin(BoundFilter):
    async def check(self, message: types.Message):
        user_id = message.from_user.id

        if str(user_id) in ADMINS:
            return True
        else:
            return False
