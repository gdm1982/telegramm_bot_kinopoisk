from loader import bot
from .get_movies_by_name import get_movie_by_name
import database.api_db as db # noqa


def send_movie_info(search):
    r_inf = db.get_cached_data(search.text)

    if r_inf:
        data_movie = eval(r_inf)
        print(search.text, 'inf movie on cache')
    else:
        data_movie = get_movie_by_name(search.text)
        db.cache_data(str(search.text), str(data_movie))
        print(search.text, 'inf movie on api')

    f_poster = data_movie[0]['poster']
    f_name = data_movie[0]['name']
    f_a_name = data_movie[0]['alternativeName']
    f_type = data_movie[0]['type']
    f_date = data_movie[0]['year']
    f_descr = data_movie[0]['shortDescription']
    f_rate = data_movie[0]['rating']
    f_genres = ', '.join(data_movie[0]['genres'])
    f_con = ', '.join(data_movie[0]['countries'])

    bot.send_photo(search.chat.id, f_poster,
                   caption=f"Название фильма: {f_name}\n"
                           f"Оригинальное название: {f_a_name}\n"
                           f"Тип: {f_type}\n"
                           f"Год выпуска: {f_date}\n"
                           f"Краткое описание: {f_descr}\n"
                           f"Рейтинг на Кинопоиске: {f_rate}\n"
                           f"Жанр: {f_genres}\n"
                           f"Страна: {f_con}")
