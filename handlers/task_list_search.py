from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types.message import Message

from ..bot import dp
import bot.utils as bot_utils
from bot import message_texts
from ..states.task_search import GettingListOfTasks
from ..filters.filters import CheckAvailabilityOfTopic, CheckRangeCorrectness
from ..keyboards.inline import keyboards_inline


@dp.callback_query_handler(Text('task_list_search'))
async def start_searching_for_task_list(
        callback: CallbackQuery,
        state: FSMContext) -> None:
    """ Начинаем поиск списка задач """

    await state.set_state(GettingListOfTasks.enter_task_topic)
    await callback.message.answer(
        message_texts.TEXT_TO_ENTER_NAME_OF_TASK_TOPIC
    )


@dp.callback_query_handler(
    Text('confinue_searching_for_task_list'),
    state=GettingListOfTasks.task_list_search_is_completed
)
async def continue_searching_for_task_list(
        callback: CallbackQuery,
        state: FSMContext) -> None:
    """ Продолжаем поиск списка задач """

    await state.set_state(GettingListOfTasks.enter_complexity_of_tasks)
    await bot_utils.display_set_of_new_task(state, callback.message)
    await state.set_state(GettingListOfTasks.task_list_search_is_completed)


@dp.callback_query_handler(
    Text('search_by_other_parameters'),
    state=GettingListOfTasks.task_list_search_is_completed
)
async def search_for_tasks_by_other_parameters(
        callback: CallbackQuery,
        state: FSMContext) -> None:
    """ Ищем задачи только уже по другим параметрам """

    await state.set_state(GettingListOfTasks.enter_task_topic)
    await callback.message.answer(
        message_texts.TEXT_TO_ENTER_NAME_OF_TASK_TOPIC
    )


@dp.callback_query_handler(
    Text('exit_task_list_search'),
    state=GettingListOfTasks.task_list_search_is_completed
)
async def exit_task_list_search(
        callback: CallbackQuery,
        state: FSMContext) -> None:
    """ Выходим из поиска списка задач """

    await state.reset_state()
    await callback.message.answer(
        text=message_texts.TEXT_FOR_INITIAL_KEYBOARD,
        reply_markup=keyboards_inline.get_initial_keyboard()
    )


@dp.message_handler(
    CheckAvailabilityOfTopic(),
    state=GettingListOfTasks.enter_task_topic
)
async def process_task_topic(message: Message, state: FSMContext) -> None:
    """ Получаем тему задач """

    await state.update_data(task_topic=message.text)
    await state.set_state(GettingListOfTasks.enter_complexity_of_tasks)
    await message.answer(
        message_texts.TEXT_FOR_SELECTING_COMPLEXITY_OF_TASK_LIST
    )


@dp.message_handler(
    state=GettingListOfTasks.enter_task_topic
)
async def show_absence_of_chosen_topic(
        message: Message, state: FSMContext) -> None:
    """ Показываем отсутствие выбранной темы """

    text = message_texts.TEXT_FOR_THE_ABSENCE_OF_SELECTED_TOPIC.format(
        message.text
    )
    await message.answer(text=text)


@dp.message_handler(
    CheckRangeCorrectness(),
    state=GettingListOfTasks.enter_complexity_of_tasks
)
async def process_task_complexity(message: Message, state: FSMContext) -> None:
    """ Получаем сложность задач """

    await state.update_data(task_complexity=message.text)
    await state.set_state(GettingListOfTasks.getting_list_of_tasks)
    await bot_utils.display_set_of_new_task(state, message)
    await state.set_state(GettingListOfTasks.task_list_search_is_completed)


@dp.message_handler(
    state=GettingListOfTasks.enter_complexity_of_tasks
)
async def no_process_task_complexity(message: Message, state: FSMContext) -> None:
    """ Получаем сложность задач """

    await message.answer(
        message_texts.TEXT_FOR_NOTIFICATION_OF_INCORRECT_COMPLEXITY_OF_TASKS
    )
