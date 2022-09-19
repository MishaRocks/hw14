from flask import Blueprint, jsonify
from app.utils import *

view_blueprint = Blueprint('posts_blueprint', __name__)


@view_blueprint.route('/movie/<title>')
def search_movie_by_title(title):
    data = movie_by_title(title)
    return jsonify(data)


@view_blueprint.route('/movie/<int:first_year>/to/<int:last_year>')
def search_movie_between_years(first_year, last_year):
    data = between_years(first_year, last_year)
    return jsonify(data)


@view_blueprint.route('/rating/<rating>')
def search_rating(rating):
    data = rating_search(rating)
    return jsonify(data)


@view_blueprint.route('/genre/<genre>')
def genre_search_10(genre):
    data = genre_search(genre)
    return jsonify(data)
