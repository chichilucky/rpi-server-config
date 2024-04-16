from aiogram.dispatcher.filters.state import StatesGroup, State


class TaskSearch(StatesGroup):
    """ Алгоритм для поиска задачи """

    enter_task_name = State()


class GettingListOfTasks(StatesGroup):
    """ Алгоритм получения списка задач """

    start_searching_for_task_list = State()
    enter_task_topic = State()
    enter_complexity_of_tasks = State()
    getting_list_of_tasks = State()
    task_list_search_is_completed = State()
