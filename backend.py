from imdb import IMDb
ia = IMDb()


def Get_Tags(films):
    movies = []
    keywords = []
    for movie in films:
        movies.append(ia.search_movie(movie)[0])
    for movie_obj in movies:
        ia.update(movie_obj, info=['keywords'])
        keywords.append(movie_obj['keywords'])
    return keywords


def Film_Filter(good_lst, bad_lst):
    films = []
    best_films = []
    best_films_by_tag = []
    movie_dic = {}
    rating_dic = {}
    best_keywords = set(good_lst).difference_update(set(bad_lst))
    for keyword in list(best_keywords):
        films.append(ia.get_keyword(keyword))
    while len(films) > 0:
        film = films[0]
        if films.count(film) not in movie_dic:
            movie_dic[films.count(film)] = []
        movie_dic[films.count(film)].append(film)
        films.remove(film)
    while len(best_films_by_tag) < 3:
        number = max(movie_dic.keys())
        best_films_by_tag.extend(movie_dic[number])
    for film in best_films_by_tag:
        rating = film['rating']
        if rating not in rating_dic:
            movie_dic[rating] = []
        movie_dic[rating].append(film)
    while len(best_films) < 3:
        number = max(movie_dic.keys())
        best_films.extend(movie_dic[number])
    return best_films


def Get_Best_Films(best_films, bad_films):
    good_tags = Get_Tags(best_films)
    bad_tags = Get_Tags(bad_films)
    best_films = [str(i) for i in Film_Filter(good_tags, bad_tags)]
    return best_films
