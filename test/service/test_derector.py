import pytest
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(None)

    test_derector1 = Director(id = 1, name="Иван Иванович")
    test_derector2 = Director(id = 2, name="Петр Петрович")
    test_derector3 = Director(id = 3, name="Тест Тестович")

    test_derectors =  {1: test_derector1, 2: test_derector2, 3: test_derector3}

    director_dao.get_one = MagicMock(return_value=test_derector1)
    director_dao.get_all = MagicMock(return_value=test_derectors.values())
    director_dao.create = MagicMock(return_value=Director(id=4, name="Семён Семёныч"))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao



class TestDerectorService:
    @pytest.fixture(autouse=True)
    def derector_service(self, director_dao):
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