from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types.message import Message

import db.utils as db_utils
from ..bot import dp
from bot import message_texts
from ..states.task_search import TaskSearch
from ..filters.filters import CheckAvailabilityOfTask
from ..keyboards.inline import keyboards_inline


@dp.callback_query_handler(Text('task_search'))
async def process_task_name(
        callback: CallbackQuery,
        state: FSMContext) -> None:
    """ Узнаем название задачи """

    await state.set_state(TaskSearch.enter_task_name)
    await callback.message.answer('Укажите точное название задачи')


@dp.message_handler(CheckAvailabilityOfTask(), state=TaskSearch.enter_task_name)
async def show_selected_task(message: Message, state: FSMContext) -> None:
    """ Показываем выбранную задачу """

    task = db_utils.DbUtils().get_full_information_on_task(
        fields={'name': message.text},
    )
    text = message_texts.TEXT_TO_DISPLAY_TASK.format(
        task['name'],
        task['id'],
        task['topics'],
        task['complexity'],
        task['number_of_solutions'],
        task['link'],
    )
    await message.answer(
        text=text,
        reply_markup=keyboards_inline.get_keyboard_task_found()
    )


@dp.message_handler(state=TaskSearch.enter_task_name)
async def show_absence_of_selected_task(
        message: Message, state: FSMContext) -> None:
    """ Оповещаем о том, что выбранной задачи нет """
 
    text = f'Задача "{message.text}" не найдена. Убедитесь в корректности названия и попробуйте еще раз.'
    await message.answer(text=text)


@dp.callback_query_handler(
        Text('exit_task_search'),
        state=TaskSearch.enter_task_name)
async def exit_task_search(
        callback: CallbackQuery,
        state: FSMContext) -> None:
    """ Выходим из поиска задач """

    await state.reset_state()
    await callback.message.answer(
        text=message_texts.TEXT_FOR_INITIAL_KEYBOARD,
        reply_markup=keyboards_inline.get_initial_keyboard()
    )
