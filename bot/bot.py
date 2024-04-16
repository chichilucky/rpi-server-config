import os

from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot

from .filters import filters


dotenv_path = os.path.abspath(
    os.path.join(os.path.dirname( __file__ ), '.env')
)

load_dotenv(dotenv_path)

bot = Bot(os.getenv('TOKEN_BOT'), parse_mode='HTML')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.filters_factory.bind(filters.CheckAvailabilityOfTask)
