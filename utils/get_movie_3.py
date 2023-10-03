import requests
from loader import headers


def get_movie_3(name, page=1, limit=1):
    """ Функция получает информацию о ближайшем похожем по названию фильме или сериале """
    response = requests.get(
        'https://api.kinopoisk.dev/v1.3/movie',
        params={
            "name": name,
            "limit": limit,
            "page": page,
        },
        headers=headers
    )
    movies = response.json()
    return movies["docs"]


# search = 'Аватар'
# data = get_movie_3(search)
# print(data)


# [{'externalId': {'kpHD': '4127663ed234fa8584aeb969ceb02cd8', 'imdb': 'tt1675434', 'tmdb': 77338},
#   'rating': {'kp': 8.808, 'imdb': 8.5, 'filmCritics': 6.8, 'russianFilmCritics': 100, 'await': None},
#   'votes': {'kp': 1603737, 'imdb': 884938, 'filmCritics': 130, 'russianFilmCritics': 12, 'await': 15},
#   'movieLength': 112,
#   'id': 535341,
#   'type': 'movie',
#   'name': '1+1',
#   'description': 'Пострадав в результате несчастного случая, богатый аристократ Филипп нанимает в помощники человека, который менее всего подходит для этой работы, – молодого жителя предместья Дрисса, только что освободившегося из тюрьмы. Несмотря на то, что Филипп прикован к инвалидному креслу, Дриссу удается привнести в размеренную жизнь аристократа дух приключений.',
#   'year': 2011,
#   'poster': {'url': 'https://st.kp.yandex.net/images/film_big/535341.jpg', 'previewUrl': 'https://st.kp.yandex.net/images/film_iphone/iphone360_535341.jpg'},
#   'genres': [{'name': 'драма'}, {'name': 'комедия'}, {'name': 'биография'}],
#   'countries': [{'name': 'Франция'}],
#   'alternativeName': 'Intouchables',
#   'enName': None,
#   'names': [{'name': '1+1'}, {'name': 'Intouchables'}, {'name': '不可触碰', 'language': 'CN', 'type': None}, {'name': '最佳拍档', 'language': 'CN', 'type': None}, {'name': '无法触碰', 'language': 'CN', 'type': None}, {'name': 'Untouchable', 'language': 'GB', 'type': None}, {'name': '不可触摸', 'language': 'CN', 'type': None}, {'name': 'Неприкасаемые', 'language': 'RU', 'type': 'Literal'}, {'name': '1+1 [Intouchables]', 'language': 'RU', 'type': None}, {'name': 'Saikyô no futari', 'language': 'JP', 'type': None}, {'name': 'Amigos', 'language': 'CL', 'type': None}, {'name': "Mehubarim la'hayim", 'language': 'IL', 'type': 'Hebrew title'}, {'name': 'Amigos para siempre', 'language': 'VE', 'type': None}, {'name': 'Prijatelja', 'language': 'SI', 'type': None}, {'name': 'En oväntad vänskap', 'language': 'SE', 'type': None}, {'name': 'Intocáveis', 'language': 'BR', 'type': None}, {'name': 'Intouchables – Ziemlich beste Freunde', 'language': 'DE', 'type': None}, {'name': '언터처블 1%의 우정', 'language': 'KR', 'type': None}, {'name': 'De Uroerlige', 'language': 'DK', 'type': None}],
#   'shortDescription': 'Аристократ на коляске нанимает в сиделки бывшего заключенного. Искрометная французская комедия с Омаром Си',
#   'logo': {'url': 'https://avatars.mds.yandex.net/get-ott/1531675/2a0000017f0262661cde61dc260cb86f7830/orig'},
#   'watchability': {'items': [{'name': 'Okko', 'logo': {'url': 'https://avatars.mds.yandex.net/get-ott/239697/7713e586-17d1-42d1-ac62-53e9ef1e70c3/orig'}, 'url': 'https://okko.tv/movie/intouchables?utm_medium=referral&utm_source=yandex_search&utm_campaign=new_search_feed'}, {'name': 'Иви', 'logo': {'url': 'https://avatars.mds.yandex.net/get-ott/2419418/0dfd1724-848f-4725-9160-abc571f41c11/orig'}, 'url': 'https://www.ivi.ru/watch/109726?utm_source=yandex&utm_medium=wizard'}, {'name': 'START', 'logo': {'url': 'https://avatars.mds.yandex.net/get-ott/239697/1a632675-0d99-4268-bd5e-d5f3dd800174/orig'}, 'url': 'https://start.ru/watch/1-1?utm_source=kinopoisk&utm_medium=feed_watch&utm_campaign=1-1'}, {'name': 'Kinopoisk HD', 'logo': {'url': 'https://yastatic.net/s3/kinopoisk-frontend/hd-www/release/apple-touch-icon-180x180.png'}, 'url': 'https://hd.kinopoisk.ru/?rt=4127663ed234fa8584aeb969ceb02cd8'}, {'name': 'Kinopoisk HD', 'logo': {'url': 'https://yastatic.net/s3/kinopoisk-frontend/hd-www/release/apple-touch-icon-180x180.png'}, 'url': 'https://hd.kinopoisk.ru/?rt=4127663ed234fa8584aeb969ceb02cd8'}]}}]

# [{'externalId': {'kpHD': '4ae8f7b627a55093b7a4f634dd2f9cc5', 'imdb': 'tt0499549', 'tmdb': 19995},
# 'rating': {'kp': 7.971, 'imdb': 7.9, 'filmCritics': 7.4, 'russianFilmCritics': 75, 'await': None},
# 'votes': {'kp': 985831, 'imdb': 1349279, 'filmCritics': 335, 'russianFilmCritics': 12, 'await': 38689},
# 'movieLength': 162,
# 'id': 251733,
# 'type': 'movie',
# 'name': 'Аватар',
# 'description': 'Бывший морпех Джейк Салли прикован к\xa0инвалидному креслу. Несмотря на\xa0немощное тело, Джейк в\xa0душе по-прежнему остается воином. Он\xa0получает задание совершить путешествие в\xa0несколько световых лет\xa0к базе землян на\xa0планете Пандора, где\xa0корпорации добывают редкий минерал, имеющий огромное значение для\xa0выхода Земли из\xa0энергетического кризиса.',
# 'year': 2009,
# 'poster': {'url': 'https://st.kp.yandex.net/images/film_big/251733.jpg', 'previewUrl': 'https://st.kp.yandex.net/images/film_iphone/iphone360_251733.jpg'},
# 'genres': [{'name': 'фантастика'}, {'name': 'боевик'}, {'name': 'драма'}, {'name': 'приключения'}],
# 'countries': [{'name': 'США'}],
# 'alternativeName': 'Avatar', 'enName': None, 'names': [{'name': 'Аватар'}, {'name': 'Avatar'}, {'name': 'Project 880465wtgsdtg', 'language': 'US', 'type': 'working title'}, {'name': 'Avatar Edicion Coleccionista', 'language': 'ES', 'type': None}, {'name': 'Avatar: Extended Version', 'language': 'US', 'type': 'extended version'}, {'name': "Avatar - Collector's Extended Edition", 'language': 'GB', 'type': None}, {'name': 'Avatar - Edição Estendida de Colecionador', 'language': 'BR', 'type': None}, {'name': 'Avatar 3D', 'language': 'US', 'type': '3D version'}, {'name': 'Avatar: An IMAX 3D Experience', 'language': 'US', 'type': 'IMAX version'}, {'name': "James Cameron's Avatar", 'language': 'US', 'type': 'promotional title'}, {'name': 'Avatar: Special Edition', 'language': 'US', 'type': 'longer version'}, {'name': '아바타', 'language': 'KR', 'type': None}, {'name': 'Аватар 3D', 'language': 'RU', 'type': None}, {'name': 'Avatar - Wersja Specjalna', 'language': 'PL', 'type': None}, {'name': 'Avatar - Wersja Rozszerzona', 'language': 'PL', 'type': None}, {'name': "Avatar - Collector's Edition", 'language': 'DE', 'type': None}, {'name': "Avatar - Extended Collector's Edition", 'language': 'US', 'type': 'box set'}, {'name': 'અવતાર', 'language': 'IN', 'type': 'Gujarati'}, {'name': 'अवतार', 'language': 'IN', 'type': 'Hindi'}, {'name': 'অবতার', 'language': 'IN', 'type': 'Bengali'}, {'name': 'Avatar 1 - Aufbruch nach Pandora', 'language': 'DE', 'type': None}],
# 'shortDescription': 'Парализованный морпех становится мессией для жителей Пандоры. Самый кассовый фильм в истории кино\n',
# 'logo': {'url': 'https://avatars.mds.yandex.net/get-ott/2385704/2a00000176f1bb64212c9df414a8909c8f44/orig'},
# 'watchability': {'items': []}}]
