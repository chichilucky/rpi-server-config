from .keyboards.inline import keyboards_inline
import db.utils as db_utils
from . import message_texts


async def display_set_of_new_task(state, message) -> None:
    """ Отображаем набор новых задач """

    def get_list_of_tasks_in_form_text(list_of_tasks) -> str:
        """ Получаем список задач для отображения """

        final_text = ''

        for task in list_of_tasks:
            text = message_texts.TEXT_TO_DISPLAY_TASK.format(
                task['name'],
                task['number'],
                task['topics'],
                task['complexity'],
                task['number_of_solutions'],
                task['link'],
            ) + '\n'
            final_text += text

        return final_text


    # ВЫШЕ ОПРЕДЕЛЕНИЕ ФУНКЦИЙ

    if not 'id_of_last_tasks' in await state.get_data():
        await state.update_data(id_of_last_tasks='')

    user_data =  await state.get_data()
    id_of_new_tasks, new_set_of_tasks = db_utils.DbUtils().get_set_of_new_tasks(
        user_data
    )

    if new_set_of_tasks:
        text_for_message = get_list_of_tasks_in_form_text(new_set_of_tasks)
    else:
        text_for_message = message_texts.TEXT_FOR_NOTIFICATION_OF_ABSENCE_OF_TASKS

    await state.update_data(id_of_last_tasks=id_of_new_tasks)
    await message.answer(
        text=text_for_message,
        reply_markup=keyboards_inline.get_keyboard_fro_found_task_list()
    )
