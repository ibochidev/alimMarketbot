import logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext, filters
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup,inline_keyboard
BOT_TOKEN = "6489036760:AAE3rhZQEN3GhVkbmRjotoKITwI0LUzGccY"
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext, filters
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import markdown
bot = Bot(token=BOT_TOKEN,parse_mode="HTML")
storage = MemoryStorage()  # Initialize MemoryStorage
dp = Dispatcher(bot, storage=storage)  # Pass the storage to the Dispatcher
dp.middleware.setup(LoggingMiddleware())
user_data_dict = {}
Userlist = []
Menu = ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["🛒Buyurtma berish","📃Batafsil ma`lumot",]
Menu.add(*buttons).add("☎Adminga bog`lanish","🌏Tilni o`zgartirish").add("💻Ijtimoiy tarmoqlar")

Menuru = ReplyKeyboardMarkup(resize_keyboard=True)
buttonsru = ["🛒Сделать заказ","📃 Больше информации"]
Menuru.add(*buttonsru).add("")

til = ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["🇺🇿O`zbek tili","🇷🇺Рус яазик",]
til.add(*buttons).add("🇬🇧English language")

admin = ReplyKeyboardMarkup(resize_keyboard=True)
admini = ["Maxsulot joylash","Foydalanuvchilar"]
admin.add(admini)
# States class
class UserForm(StatesGroup):
    name = State()
    age = State()
    email = State()
    image = State()
    accept = State()
    phone = State()
chat_id=5235865310,5235865310,5235865310,5235865310
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("<b>Assalomu aleykum xurmatli mijoz. \nSiz Alim Market bot orqali istalgan turdagi mahsulotlarimizni online ravishda sotib olishingiz mumkin</b>",reply_markup=Menu)


@dp.message_handler(text='💻Ijtimoiy tarmoqlar')
async def tarmoq(mess:types.Message):
    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Telegram', url='https://t.me/alim_market')
    but2 = types.InlineKeyboardButton('Instagram', url='https://instagram.com/sifatli_tavar.uz')
    but3 = types.InlineKeyboardButton('Facebook', url='https://facebook.com/alim_market')

    keyboard.add(but1,but3,but2)
    await mess.answer("<b>Bizning Ijtimoiy tarmoqlar👇👇</b>",reply_markup=keyboard)


@dp.message_handler(text='🌏Tilni o`zgartirish')
async def ddd(mess:types.Message):
    await mess.answer("Tilni tanlang",reply_markup=til)

@dp.message_handler(text='☎Adminga bog`lanish')
async def ddd(mess:types.Message):
    keyboard = types.InlineKeyboardMarkup()
    # Create some inline keyboard buttons
    but = types.InlineKeyboardButton('Ali', url='https://t.me/alim_marketuz')
    but1 = types.InlineKeyboardButton('Rustamjon', url='https://t.me/vediboi')
    keyboard.add(but1,but)
    await mess.reply("<b>Telefon raqami : </b><pre>+998935579955</pre>\n<b>Telefon raqami :</b> <pre>+998913670106</pre>", reply_markup=keyboard)
#
# @dp.message_handler(text='🇷🇺Рус яазик')
# async def tilru(mess: types.Message):
#     await mess.answer("",reply_markup=)
# /start buyrug'iga javob berish
tasdiqla = InlineKeyboardMarkup()
tasdiqla.add(InlineKeyboardButton(text='Tasdiqlash', callback_data='tasdiqlash'),InlineKeyboardButton(text='Rad etish', callback_data='rad etish'))




but5 = ReplyKeyboardMarkup(resize_keyboard=True)
but6= ["Amaliyotni to`xtatish"]
but5.add(*but6)
but7 = ReplyKeyboardMarkup(resize_keyboard=True)
but8= ["Adminga Yuborish","Amaliyotni to`xtatish"]
but7.add(*but8)
but9 = ReplyKeyboardMarkup(resize_keyboard=True)
but10= ["Bu maxsulotda razmer yo`q"]
but9.add(*but10)



b = ReplyKeyboardMarkup(resize_keyboard=True)
b10= ["To`lov qildim"]
b.add(*b10)
@dp.message_handler(text="Amaliyotni to`xtatish", state="*")
async def cancel(message: types.Message, state: FSMContext):
    current_state =await state.get_state()
    if current_state is None:
        return

    await state.finish()

    await message.answer("Amal bekor qilindi. Yana biror buyurtma berish uchun /start komandasini bosing.")


@dp.message_handler(text=['🛒Buyurtma berish'])
async def start(message: types.Message):
    await message.reply("Siz buyurtma qilmoqchi bolgan, Maxsulot nomini kiriting:",reply_markup=but5)
    await UserForm.name.set()



@dp.message_handler(state=UserForm.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)

    await message.reply(f"Siz buyurtma qilmoqchi bolgan, Maxsulot razmerini kiriting:",reply_markup=but9)
    await UserForm.age.set()


@dp.message_handler(state=UserForm.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)

    await message.reply("Siz buyurtma qilmoqchi bolgan, Maxsulot tavsifini kiriting:",reply_markup=but5)
    await UserForm.email.set()

@dp.message_handler(state=UserForm.email)
async def process_email(message: types.Message, state: FSMContext):
    email = message.text

    await state.update_data(email=email)
    user_data = await state.get_data()
    await UserForm.phone.set()
    await message.reply("Telefon raqamingizni kiriting: ")


@dp.message_handler(state=UserForm.phone)
async def process_email(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(phone=phone)

    await UserForm.image.set()
    await message.reply("<b>Siz buyurtma qilmoqchi bolgan, Maxsulotning taxminiy rasmini yuboring:</b>: ")



# Asosiy funksiya
@dp.message_handler(content_types=types.ContentType.PHOTO,state=UserForm.image)
async def process_email(message: types.Message, state: FSMContext):
    Photo = message.photo[-1]
    # Save the email to the state
    await state.update_data(image_id=Photo.file_id)
    await message.reply("Buyurtma adminga yuborilsinmi",reply_markup=but7)
    # Process collected data
    await UserForm.accept.set()

class Usernarxi(StatesGroup):
    cost = State()


class UserTolov(StatesGroup):
    name = State()


@dp.message_handler(text='Adminga Yuborish', state=UserForm.accept)
async def sss(mess:types.Message, state :  FSMContext):
    user_data = await state.get_data()

    # Process collected data
    image_id = user_data["image_id"]
    name = user_data['name']
    age = user_data['age']
    email = user_data['email']
    phone = user_data['phone']
    print(email, image_id, age, name,phone)

    import random
    order_id = f'alimshop{random.randint(100000, 999999)}'
    await bot.send_photo(chat_id=mess.from_user.id, photo=image_id, caption=f"<b>Rahmat! Sizning buyurtmangiz: </b>\n<b>Buyurtma id </b>#{order_id}\n<b>Nomi:</b><i> {name}\n</i><b>Razmeri :</b><i> {age}\n</i><b>Tansiv :</b><i> {email}</i> \n<b>Telefon raqam : <i>{phone}</i></b>",reply_markup=but7)

    await mess.answer("Buyurtma yuborildi siz bilan 5 daqiqada bog`lanamiz",reply_markup=Menu)
    await bot.send_photo(chat_id=-1001664527019, photo=image_id, caption=f"<b>Yangi buyurtma: </b>\n<b>Buyurtma idsi </b>#{order_id}\n<b>Nomi:</b><i> {name}\n</i><b>Razmeri :</b><i> {age}\n</i><b>Tansiv :</b><i> {email}</i>\n<b>Ismi :{mess.from_user.full_name}\n </b><b>id : {mess.from_user.id}\n</b><b>username : @{mess.from_user.username} </b>\n<b>telefon raqami : {phone} </b>",reply_markup=tasdiqla)

    await state.finish()

    @dp.callback_query_handler(text="tasdiqlash")
    async def dd(mees: types.CallbackQuery):
        await mees.message.answer("Tasdiqlandi")
        await mess.answer(f"Sizning buyurtmangiz tasdiqlandi to`lov qiling va botga chekni jonating\n karta raqam 860012345678 Ali Izzatulayev \n Jami summa 00.00",reply_markup=b)
@dp.message_handler(text="To`lov qildim")
async def tolov(meeees: types.Message ,state :  FSMContext):
    await meeees.answer("Iltimos Tolov qilgan chekninggizni yuboring")
    await UserTolov.name.set()

@dp.message_handler(content_types='photo', state=UserTolov.name)
async def tolof(mess: types.Message,state : FSMContext):
    Photo = mess.photo[-1]
    # Save the email to the state
    await state.update_data(image_id=Photo.file_id)
    aa = await state.get_data()
    
    photo = aa['image_id']
    await mess.answer('Siz qilgan tolov : 000 (chekdagi summa aliqlovchi func ishlatilmagan) ')
    await bot.send_photo(chat_id=-1001664527019 ,photo=photo, caption=f"Tolov qilingan summa : 00.0 \nfoydalanuvchi idsi : {mess.from_user.id}\nFoydalanuvchi : {mess.from_user.full_name}")
    await state.finish()





if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
