from loader import bot
from .get_person_by_name import get_person_by_name
import database.api_db as db # noqa


def send_person_info(search):
    r_inf = db.get_cached_data(search.text)

    if r_inf:
        data_person = eval(r_inf)
        print(search.text, 'inf person on cache')
    else:
        data_person = get_person_by_name(search.text)
        db.cache_data(str(search.text), str(data_person))
        print(search.text, 'inf person on api')

    bot.send_photo(search.chat.id, data_person[0]['photo'],
                   caption=f"Имя: {data_person[0]['name']}\n"
                           f"Англ. имя: {data_person[0]['enName']}\n"
                           f"Пол: {data_person[0]['sex']}\n"
                           f"Возраст: {data_person[0]['age']}\n"
                           f"Профессия: {', '.join(data_person[0]['profession'])}\n"
                           f"Место рождения: {', '.join(data_person[0]['birthPlace'])}\n"
                           f"Дата рождения: {data_person[0]['birthday'][:10]}\n"
                           f"Дата смерти: {data_person[0]['death'][:10]}\n"
                           f"Место упокоения: {', '.join(data_person[0]['deathPlace'])}")
