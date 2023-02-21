import pytest

from service.movie import MovieService

class TestMovieService:
    @pytest.fixture(autouse=True)
    def __init__(self, movie_dao):
        self.movie_service = MovieService(movie_dao)


    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id == 1
        assert movie.title == "title1"
        assert movie.description == "description1"
        assert movie.trailer == "trailer1"
        assert movie.year == 2001
        assert movie.rating == 1.0
        assert movie.genre_id == 1
        assert movie.director_id == 1


    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert movies is not None
        assert len(movies) > 0


    def test_create(self):
        data = {
        'id': 4,
        'title': "title4",
        'description': "description4",
        'trailer': "trailer4",
        'year': 2004,
        'rating': 4.0,
        'genre_id': 4,
        'director_id': 4
        }
        movie = self.movie_service.create(data)
        assert movie.id == 4
        assert movie.title == "title4"
        assert movie.description == "description4"
        assert movie.trailer == "trailer4"
        assert movie.year == 2004
        assert movie.rating == 4.0
        assert movie.genre_id == 4
        assert movie.director_id == 4


    def test_update(self):
        data = {
            'id': 4,
            'title': "title4",
            'description': "description4",
            'trailer': "trailer4",
            'year': 2004,
            'rating': 4.0,
            'genre_id': 4,
            'director_id': 4
        }
        assert self.movie_service.update(data)


    def test_delete(self):
        assert self.movie_service.delete(1) is None