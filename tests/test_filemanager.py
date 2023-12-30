import pytest

import wikipedia.fileManager


@pytest.fixture
def manager(tmp_path):
    return wikipedia.fileManager.FileManager(tmp_path)


def test_create_file_path(manager, tmp_path):
    path = tmp_path / "pages.pickle"
    assert manager.get_path() == str(path.absolute())


def test_save_without_file(manager):
    data = {
        "pages": ["Test Hello"],
        "apcontinue": "",
        "index_page": 0,
    }
    manager.save(data)
    data_new = manager.load()
    assert data_new == data


class TestFileSave:
    @staticmethod
    def test_load_file(manager):
        data = manager.load()
        assert "index_page" in data
        assert "apcontinue" in data
        assert "pages" in data

    @staticmethod
    def test_save_file(manager):
        data = manager.load()
        data["pages"].append("Test page")
        manager.save(data)
        data = manager.load()
        assert data["pages"] == ["Test page"]


__all__ = ()
