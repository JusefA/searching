from jikanpy import Jikan
jikan = Jikan()

while True:

    mushishi = jikan.anime(457)
    mushishi_with_eps = jikan.anime(457, extension='episodes')

    search_result = jikan.search('anime', 'Mushishi', page=2)

    winter_2018_anime = jikan.season(year=2018, season='winter')

    archive = jikan.season_archive()

    print(search_result)
