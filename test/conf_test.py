import pytest
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)
    test_derector1 = Director(id=1, name='Иван Иванович')
    test_derector2 = Director(id=2, name='Петр Петрович')
    test_derector3 = Director(id=3, name='Тест Тестович')

    test_derectors =  {1: test_derector1, 2: test_derector2, 3: test_derector3}

    director_dao.get_one = MagicMock(return_value=test_derector1)
    director_dao.get_all = MagicMock(return_value=test_derectors.values())
    director_dao.create = MagicMock(return_value=Director(id=4, name='Семён Семёныч'))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    test_genre1 = Genre(id=1, name='комедия')
    test_genre2 = Genre(id=2, name='трилер')
    test_genre3 = Genre(id=3, name='фэнтэзи')

    test_genres = {1: test_genre1, 2: test_genre2, 3:test_genre3}

    genre_dao.get_one = MagicMock(return_value=test_genre1)
    genre_dao.get_all = MagicMock(return_value=test_genres.values())
    genre_dao.create = MagicMock(return_value=Director(id=4, name='фантастика'))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    test_movie1 = Movie(
        id=1,
        title="title1",
        description="description1",
        trailer="trailer1",
        year=2001,
        rating=1.0,
        genre_id=1,
        director_id=1
    )

    test_movie2 = Movie(
        id=2,
        title="title2",
        description="description2",
        trailer="trailer2",
        year=2002,
        rating=2.0,
        genre_id=2,
        director_id=2
    )

    test_movie3 = Movie(
        id=3,
        title="title3",
        description="description3",
        trailer="trailer3",
        year=2003,
        rating=3.0,
        genre_id=3,
        director_id=3
    )

    test_movies = {1: test_movie1, 2: test_movie2, 3: test_movie3}

    movie_dao.get_one = MagicMock(return_value=test_movie1)
    movie_dao.get_all = MagicMock(return_value=test_movies.values())
    movie_dao.create = MagicMock(return_value=Movie(
        id=4,
        title="title4",
        description="description4",
        trailer="trailer4",
        year=2004,
        rating=4.0,
        genre_id=4,
        director_id=4
    ))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao