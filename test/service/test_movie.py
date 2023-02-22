from unittest.mock import MagicMock

import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


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
        director_id=2)

    test_movie3 = Movie(
        id=3,
        title="title3",
        description="description3",
        trailer="trailer3",
        year=2003,
        rating=3.0,
        genre_id=3,
        director_id=3)

    test_movies = {1: test_movie1, 2: test_movie2, 3: test_movie3}

    movie_dao.get_all = MagicMock(return_value=test_movies.values())
    movie_dao.get_one = MagicMock(return_value=test_movie1)
    movie_dao.create = MagicMock(return_value=Movie(
        id=4,
        title="title4",
        description="description4",
        trailer="trailer4",
        year=2004,
        rating=4.0,
        genre_id=4,
        director_id=4))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert movies is not None
        assert len(movies) > 0

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id == 1
        assert movie.title == "title1"
        assert movie.description == "description1"
        assert movie.trailer == "trailer1"
        assert movie.year == 2001
        assert movie.rating == 1.0
        assert movie.director_id == 1
        assert movie.genre_id == 1

    def test_create(self):
        data = {"id": 4,
                "title": "movie4",
                "description": "description4",
                "trailer": "trailer4",
                "year": 2004,
                "rating": 4.0,
                "genre_id": 4,
                "director_id": 4}

        movie = self.movie_service.create(data)
        assert movie is not None
        assert movie.id == 4
        assert movie.title == "title4"
        assert movie.description == "description4"
        assert movie.trailer == "trailer4"
        assert movie.year == 2004
        assert movie.rating == 4.0
        assert movie.director_id == 4
        assert movie.genre_id == 4

    def test_update(self):
        data = {"id": 4,
                "title": "movie4",
                "description": "description4",
                "trailer": "trailer4",
                "year": 2004,
                "rating": 4.0,
                "genre_id": 4,
                "director_id": 4}
        assert self.movie_service.update(data)

    def test_delete(self):
        assert self.movie_service.delete(1) is None
