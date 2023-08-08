from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
import logging
import sql 

ADMINS = ['6041962881']
BOT_TOKEN = '6489036760:AAFCnWx_keKdEVi7Zcl3GlVfs_OqxXWW9Zc'

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = sql.Database(path_to_db="main.db")
logging.basicConfig(level=logging.INFO)
