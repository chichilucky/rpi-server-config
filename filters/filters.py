import re

from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter

import db.utils as db_utils
import db.models as db_models
 

class CheckAvailabilityOfTask(BoundFilter):
    """ Проверяем наличие задачи """

    async def check(self, message: Message):
        is_entry_availability = db_utils.DbUtils().check_for_entry(
            field=db_models.Task.name,
            value=message.text
        )
        return is_entry_availability


class CheckAvailabilityOfTopic(BoundFilter):
    """ Проверяем наличие темы """

    async def check(self, message: Message):
        is_entry_availability = db_utils.DbUtils().check_for_entry(
            field=db_models.Topic.name,
            value=message.text
        )
        return is_entry_availability


class CheckRangeCorrectness(BoundFilter):
    """ Провремя корректность диапазона сложности задач """

    async def check(self, message: Message) -> bool:

        text = message.text
        if re.search('[a-zA-Zа-яА-Я]', text): return

        pattern0 = re.compile('\d+')
        pattern1 = re.compile('\d+-\d+')
        patterns = [pattern0, pattern1]

        for pattern in patterns:
            try:
                pattern.search(text).group(0)
                return True
            except AttributeError:
                return False
