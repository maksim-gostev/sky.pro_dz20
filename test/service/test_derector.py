import pytest

from service.director import DirectorService


class TestDerectorService:
    @pytest.fixture(autouse=True)
    def __init__(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id == 1
        assert director.name == 'Иван Иванович'


    def test_get_all(self):
        directors = self.director_service.get_all()
        assert directors is not None
        assert len(directors) > 0


    def test_create(self):
        data = {'id': 4, 'name': 'Семён Семёныч'}
        director = self.director_service.create(data)
        assert director is not None
        assert director.id == 4
        assert director.name == 'Семён Семёныч'


    def test_update(self):
        data = {'id': 4, 'name': 'Семён Семёныч'}
        assert self.director_service.update(data)


    def test_delete(self):
        assert self.director_service.delete(1) is None