import argparse
from aiogram.utils import executor

from .bot import dp
from .bot import bot
from .handlers import handlers, task_display, task_list_search
from .keyboards.inline import keyboards_inline

import settings


def run_bot(list_of_passed_arguments: argparse.Namespace) -> None:
    """ Запускаем бота """

    executor.start_polling(dp)
