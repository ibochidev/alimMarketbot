from rHLDS import Console
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

BOT_TOKEN = "6154626712:AAFE-fFyNLgY5QTUl4uQZV11Kb0pkFxblio"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):

    await message.answer("Assalomu aleykum botga buyruq bering")
@dp.message_handler(content_types=["text"])
async def cmd_start(message: types.Message):
    aa = message.text
    srv = Console(host='83.69.139.184', port=27015, password='qweasdzxc1')
    srv.connect()
    await message.answer(srv.execute(aa))
    srv.disconnect()




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
