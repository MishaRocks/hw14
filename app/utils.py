import sqlite3

from flask import json


def movie_by_title(user_title):
    """Поиск фильма по названию"""
    with sqlite3.connect("app/netflix.db") as db:
        cursor = db.cursor()
        query = f"""
                SELECT title, country, release_year, listed_in, description
                FROM netflix
                WHERE title = '{user_title}'
                ORDER by release_year DESC
                LIMIT 1
                """

        cursor.execute(query)
        movie = cursor.fetchall()
        show_movie = {
                "title": movie[0][0],
                "country": movie[0][1],
                "release_year": movie[0][2],
                "genre": movie[0][3],
                "description": movie[0][4]
        }
        return show_movie


def between_years(first_year, last_year):
    with sqlite3.connect("app/netflix.db") as db:
        cursor = db.cursor()
        query = """
                SELECT title, release_year
                FROM netflix
                WHERE release_year BETWEEN ? AND ?
                ORDER BY release_year DESC
                LIMIT 1000
                """

        cursor.execute(query, (first_year, last_year))
        movie = cursor.fetchall()
        show_movie = []
        for film in movie:
            show_movie.append({"title": film[0], "release_year": film[1]})
        return show_movie


def rating_search(rating):
    with sqlite3.connect("app/netflix.db") as db:
        sql = db.cursor()
        if rating == 'children':
            r_1, r_2, r_3 = 'G', 'G', 'G'
        elif rating == 'family':
            r_1, r_2, r_3 = 'G', 'PG', 'PG-13'
        elif rating == 'adult':
            r_1, r_2, r_3 = 'R', 'NC-17', 'NC-17'

        movies = f"""
                SELECT title, rating, description
                FROM netflix
                WHERE rating = "{r_1}"
                OR rating = "{r_2}"
                OR rating = "{r_3}"
                LIMIT 100
        """

        sql.execute(movies)

        show_result = []
        for film in sql.fetchall():
            show_result.append({"title": film[0], "rating": film[1], "description": film[2]})

        return show_result


def genre_search(genre):
    with sqlite3.connect("app/netflix.db") as data:
        sql = data.cursor()
        movies = f"""
                SELECT title, description, release_year
                FROM netflix
                WHERE listed_in = "{genre}"
                ORDER BY release_year DESC
                LIMIT 10
        """
        sql.execute(movies)
        movies_list = sql.fetchall()

        result = []
        for item in movies_list:
            result.append({"title": item[0], "description": item[1]})

        return result


def two_actors(a_1, a_2):
    with sqlite3.connect("netflix.db") as data:
        sql = data.cursor()
        actors = f"""
                SELECT "cast"
                FROM netflix
                WHERE "cast" LIKE "%{a_1}%"
                AND "cast" LIKE "%{a_2}%"
        """
        sql.execute(actors)
        actors_base = sql.fetchall()
        all_actors = ""
        for a in actors_base:
            actor = ','.join(a)
            all_actors += actor
        result = []
        for actor in all_actors.split(', '):
            if all_actors.count(actor) > 2 and actor != a_1 and actor != a_2:
                result.append(actor)

        return result


def tyj_movie(type, year, jenre):
    with sqlite3.connect("netflix.db") as data:
        sql = data.cursor()
        movies = f"""
                SELECT title, description
                FROM netflix
                WHERE type = "{type}"
                AND release_year = "{year}"
                AND listed_in LIKE "%{jenre}%"
        """
        sql.execute(movies)
        movies_base = sql.fetchall()

    return json.dumps(movies_base)

