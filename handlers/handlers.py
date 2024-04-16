from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.types.message import Message
from aiogram.dispatcher.filters.builtin import CommandStart

from bot.bot import dp
from bot import message_texts
from bot.keyboards.inline import keyboards_inline


@dp.message_handler(CommandStart())
async def start(message: Message) -> None:
    """ Начинаем """

    text = 'Выберите необходимое действие'
    await message.answer(
        text=text,
        reply_markup=keyboards_inline.get_initial_keyboard()
    )


@dp.callback_query_handler(Text('show_initial_keyboard'))
async def show_initial_keyboard(callback: CallbackQuery) -> None:
    """ Показываем начальную клавиатуру """

    await callback.message.answer(
        text=message_texts.TEXT_FOR_INITIAL_KEYBOARD,
        reply_markup=keyboards_inline.get_initial_keyboard()
    )


