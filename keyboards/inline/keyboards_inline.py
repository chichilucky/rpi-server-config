from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_initial_keyboard() -> InlineKeyboardMarkup:
    """ Получаем начальную клавиатуру """

    initial_keyboard = InlineKeyboardMarkup(row_width=1)

    task_search_button = InlineKeyboardButton(
        text='Поиск задачи',
        callback_data='task_search'
    )
    task_list_search_button = InlineKeyboardButton(
        text='Поиск списка задач',
        callback_data='task_list_search'
    )

    initial_keyboard.add(task_search_button, task_list_search_button)

    return initial_keyboard


def get_keyboard_task_found() -> InlineKeyboardMarkup:
    """ Получаем клавиатуру для найденой задачи """

    keyboard_for_task_found = InlineKeyboardMarkup(row_width=1)

    exit_task_search = InlineKeyboardButton(
        text='Вернуться',
        callback_data='exit_task_search'
    )

    keyboard_for_task_found.add(exit_task_search)

    return keyboard_for_task_found


def get_keyboard_fro_found_task_list() -> InlineKeyboardMarkup:
    """ Получаем клавиатуру для найденного списка задач """

    keyboard_fro_found_task_list = InlineKeyboardMarkup(row_width=1)

    continue_searching_for_task_list = InlineKeyboardButton(
        text='Следующие',
        callback_data='confinue_searching_for_task_list'
    )
    search_by_other_parameters = InlineKeyboardButton(
        text='Искать по другим параметрам',
        callback_data='search_by_other_parameters'
    )

    exit_task_list_search = InlineKeyboardButton(
        text='Вернуться',
        callback_data='exit_task_list_search'
    )

    keyboard_fro_found_task_list.add(
        continue_searching_for_task_list,
        search_by_other_parameters,
        exit_task_list_search
    )


    return keyboard_fro_found_task_list
