from aiogram import executor, types
from aiogram.dispatcher import FSMContext
from config import dp, bot, db
from text import *
from keyboard import *
from admin import IsSuperAdmin
from state import  UserState, AdminState,Tolov

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message, state: FSMContext):
    await state.finish()
    try:
        db.add_user(user_id=message.from_user.id,name=message.from_user.full_name)
    except: pass
    await message.reply(start_handler,reply_markup=menu)

@dp.message_handler(text="🛒Buyurtma berish")
async def product_handler(message: types.Message, state: FSMContext):
    await message.reply(product_name_text)
    await UserState.product_name.set()

@dp.message_handler(state=UserState.product_name)
async def product_handler(message: types.Message, state: FSMContext):
    await state.update_data({"product_name": message.text})
    await message.reply(product_size_text)
    await UserState.product_size.set()

@dp.message_handler(state=UserState.product_size)
async def product_handler(message: types.Message, state: FSMContext):
    await state.update_data({"product_size": message.text})
    await message.reply(product_description_text)
    await UserState.product_description.set()

@dp.message_handler(state=UserState.product_description)
async def product_handler(message: types.Message, state: FSMContext):
    await state.update_data({"product_description": message.text})
    await message.reply(phone_number_text)
    await UserState.phone_number.set()

@dp.message_handler(state=UserState.phone_number)
async def product_handler(message: types.Message, state: FSMContext):
    await state.update_data({"phone_number": message.text})
    await message.reply(product_photo_text)
    await UserState.product_photo.set()


@dp.message_handler(state=UserState.product_photo, content_types=types.ContentTypes.PHOTO)
async def product_handler(message: types.Message, state: FSMContext):
    await state.update_data({"product_photo": message.photo[-1].file_id})
    await message.reply(check_product_text, reply_markup=check_keyboard)
    await UserState.check_product.set()


@dp.message_handler(state=UserState.check_product,text="✅ Tasdiqlash")
async def product_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    info = await state.get_data()

    product_name = info.get("product_name")
    product_size = info.get("product_size")
    product_description = info.get("product_description")
    phone_number = info.get("phone_number")
    product_photo = info.get("product_photo")

    to_screen = f"<b>Buyurtma id</b> #alimshop{message.message_id}\n" \
                        f"<b>Nomi:</b> {product_name}\n" \
                        f"<b>Razmeri:</b> {product_size}\n"\
                        f"<b>Tansiv:</b> {product_description}\n" \
                        f"<b>Telefon raqam:</b> {phone_number}\n"
    try:
        db.add_product(user_id=user_id, photo=product_photo, caption=to_screen, order_id=f"#alimshop{message.message_id}", info='rejected')
    except:pass
    await bot.send_photo(chat_id=user_id, photo=product_photo, caption=f"<b>Rahmat! Sizning buyurtmangiz: </b>\n{to_screen}")
    username = message.from_user.username
    if username == None: username = ''
    user_info = f"\n<b>Ism:</b> {message.from_user.full_name}\n<b>ID:</b> {message.from_user.id}\n<b>Username:</b> {username}"
    await bot.send_photo(chat_id=-1001664527019, photo=product_photo,
                         caption=f"<b>Yangi buyrutma: </b>\n{to_screen}{user_info}",
                         reply_markup=types.InlineKeyboardMarkup(row_width=2).add(types.InlineKeyboardButton("Tasdiqlash",callback_data=f"check|{message.from_user.id}|#alimshop{message.message_id}"),
                                                                                  types.InlineKeyboardButton('Rad etish', callback_data=f'refusal|{message.from_user.id}|#alimshop{message.message_id}')))
    await bot.send_message(chat_id=user_id,text=send_check,reply_markup=menu)
    await state.finish()

@dp.message_handler(state=UserState.check_product,text="❌ Bekor qilish")
async def product_handler(message: types.Message, state: FSMContext):
    await message.reply(text="Bekor qilindi ❌",reply_markup=menu)
    await state.finish()



@dp.callback_query_handler(IsSuperAdmin(),text_startswith="check", state="*")
async def admin_check_product(call: types.CallbackQuery, state: FSMContext):
    infolist = call.data.split('|')
    await call.answer(cache_time=3)
    await state.update_data({"user_id": infolist[1], 'order_id':infolist[2]})
    await call.message.reply("<b>Maxsulot narxini kiriting...</b>")
    await call.message.edit_reply_markup(reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Tasdiqlangan buyurtma...",callback_data=f"1")))
    await AdminState.product_money.set()

@dp.message_handler(state=AdminState.product_money)
async def admin_check_product(message: types.Message, state: FSMContext):
    info = await state.get_data()
    user_id = info.get("user_id")
    order_id = info.get("order_id")
    try:
        await bot.send_message(chat_id=user_id, text=f"{order_id} <b>ID raqamdagi buyurtmangiz tasdiqlandi...</b>\n<b>Narxi: {message.text}</b>\nIltimos tolovni amalga oshiring\nALIBEK IZZATULAYEV 8600 1234 5678",reply_markup=tolov)
        await message.reply("<b>Narxi yuborildi...</b>")

    except:
        await message.reply("<b>Foydalanuvchi botni tark etgan bo'lishi mumkin shu sabab narxni yuborib bo'lmadi...</b>")
@dp.message_handler(text='to`lov qildim')
async def Tolov_summa(mess : types.Message):
    await mess.answer("To`lov qilingan chekni yuboring")
    await Tolov.photo.set()


@dp.message_handler(content_types='photo', state=Tolov.photo)
async def summaphoto(photo: types.Message,state:FSMContext):
    await state.update_data({"photo_chek": photo.photo[-1].file_id})
    info = await state.get_data()

    photo_chek = info.get("photo_chek")
    await bot.send_photo(chat_id=-1001664527019,photo=photo_chek, caption=f'tolov qilindi \nism : {photo.from_user.full_name}\nusername : @{photo.from_user.username}\nfoydalanuvchi idsi {photo.from_user.id}')
    await photo.answer('Raxmat siz tolovni amalga oshirdingiz\nsizning maxsulotingiz 10 kun ichida yetkazib beriladi!!!',reply_markup=menu)
@dp.callback_query_handler(IsSuperAdmin(),text_startswith="refusal", state="*")
async def admin_refusal_product(call: types.CallbackQuery):
    infolist = call.data.split('|')
    await call.answer(cache_time=3)
    await bot.send_message(chat_id=infolist[1], text=f"{infolist[2]} <b>ID raqamli buyurtmangiz rad etildi...</b>")
    await call.message.edit_reply_markup(reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Rad etilgan buyurtma...",callback_data=f"0")))



# Inline query handler
@dp.inline_handler()
async def inline_query(query: types.InlineQuery):
    results = []
    try:
        search_product = db.is_product(order_id=query.query)
        print(search_product)
        for x in search_product:
            print(x)
            user_id = x[1]
            if user_id == query.from_user.id:
                tttt = x[3]
                ar = x[5]
                file_id = x[2]
                if ar == 'rejected':ar = 'Tasdiqlanmagan'
                title = f"Mening Buyurtmam: {tttt}"
                description = f"Buyurtma holati: {ar}"

                result_id = f"photo_{user_id}"
                results.append(
                    types.InlineQueryResultPhoto(
                        id=result_id,
                        title=title,
                        description=description,
                        photo_url=file_id,
                        thumb_url=file_id,
                        photo_width=1024,
                        photo_height=1024,
                        caption=f"{tttt}\n\n<b>Buyurtma holati:</b> {ar}",
                    )
                )

            await bot.answer_inline_query(query.id, results=results, cache_time=1)
        else:
            await query.answer(results, cache_time=5, switch_pm_parameter='start', switch_pm_text='Search Product ID 🔍')
    except:
        await query.answer([], cache_time=5, switch_pm_parameter='start', switch_pm_text='Search Product ID 🔍')

@dp.message_handler(text='💻Ijtimoiy tarmoqlar')
async def tarmoq(mess:types.Message):
    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Telegram', url='https://t.me/alim_market')
    but2 = types.InlineKeyboardButton('Instagram', url='https://instagram.com/alim_market.uz')
    but3 = types.InlineKeyboardButton('Facebook', url='https://facebook.com/alim_marketuz')

    keyboard.add(but1,but3,but2)
    await mess.answer("<b>Bizning Ijtimoiy tarmoqlar👇👇</b>",reply_markup=keyboard)


@dp.message_handler(text='☎Adminga bog`lanish')
async def ddd(mess:types.Message):
    keyboard = types.InlineKeyboardMarkup()
    # Create some inline keyboard buttons
    but = types.InlineKeyboardButton('Ali', url='https://t.me/alim_marketuz')
    but1 = types.InlineKeyboardButton('Rustamjon', url='https://t.me/vediboi')
    keyboard.add(but1,but)
    await mess.reply("<b>Telefon raqami : </b><pre>+998935579955</pre>\n<b>Telefon raqami :</b> <pre>+998913670106</pre>", reply_markup=keyboard)




if __name__ == '__main__':
    try:
        db.create_table_product()
        db.create_table_users()
    except:
        pass
    executor.start_polling(dp, skip_updates=True)
