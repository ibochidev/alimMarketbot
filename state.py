from aiogram.dispatcher.filters.state import State, StatesGroup

class UserState(StatesGroup):
    product_name = State()
    product_size = State()
    product_description = State()
    phone_number = State()
    product_photo = State()
    check_product = State()
class AdminState(StatesGroup):
    product_money = State()

class Tolov(StatesGroup):
    photo = State()
