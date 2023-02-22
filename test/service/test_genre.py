from unittest.mock import MagicMock

import pytest

from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService

@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    test_genre1 = Genre(id=1, name='комедия')
    test_genre2 = Genre(id=2, name='трилер')
    test_genre3 = Genre(id=3, name='фэнтэзи')

    test_genres = {1: test_genre1, 2: test_genre2, 3:test_genre3}

    genre_dao.get_one = MagicMock(return_value=test_genre1)
    genre_dao.get_all = MagicMock(return_value=test_genres.values())
    genre_dao.create = MagicMock(return_value=Genre(id=4, name='фантастика'))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id == 1
        assert genre.name == 'комедия'


    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert genres is not None
        assert len(genres) > 0


    def test_create(self):
        data = {'id': 4, 'name': 'фантастика'}
        genre = self.genre_service.create(data)
        assert genre is not None
        assert genre.id == 4
        assert genre.name == 'фантастика'


    def test_update(self):
        data = {'id': 4, 'name': 'Семён Семёныч'}
        assert self.genre_service.update(data)


    def test_delete(self):
        assert self.genre_service.delete(1) is None