from imdb import IMDb
ia = IMDb()


def Get_Tags(films):
    movies = []
    keywords = []
    for movie in films:
        movies.append(ia.search_movie(movie)[0])
    for movie_obj in movies:
        ia.update(movie_obj, info=['keywords'])
        keywords.extend(movie_obj['keywords'])
    for each in keywords:
        if keywords.count(each) < 3:
            keywords.remove(each)
    return keywords


def Film_Filter(good_lst, bad_lst):
    films = []
    best_films = set()
    best_films_by_tag = []
    movie_dic = {}
    best_keywords = set(good_lst[::40]) - set(bad_lst)
    for keyword in best_keywords:
        films.extend(ia.get_keyword(keyword))
    while len(films) > 0:
        film = films[0]
        if films.count(film) not in movie_dic:
            movie_dic[films.count(film)] = []
        movie_dic[films.count(film)].append(film)
        films.remove(film)
    while len(best_films_by_tag) < 3:
        number = max(movie_dic.keys())
        best_films_by_tag.extend(movie_dic.pop(number))
    for each in best_films_by_tag:
        best_films.add(each['title'])
    return best_films


def Get_Best_Films(best_films, bad_films):
    good_tags = Get_Tags(best_films)
    bad_tags = Get_Tags(bad_films)
    best_films = Film_Filter(good_tags, bad_tags)
    return best_films
