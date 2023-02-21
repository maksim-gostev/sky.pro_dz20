import pytest

from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def __init__(self, genre_dao):
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