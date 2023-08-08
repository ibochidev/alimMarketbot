from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
import logging
from sql import database 

ADMINS = ['6041962881']
BOT_TOKEN = '6489036760:AAHdm1c-06ExF8n2FmA_dzWs9mWtyUcTDqE'

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = database(path_to_db="main.db")
logging.basicConfig(level=logging.INFO)
