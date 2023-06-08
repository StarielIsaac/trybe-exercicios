from src.importer import import_from_json
import pytest


def test_import_from_json_not_found():
    with pytest.raises(
      FileNotFoundError, match="Arquivo inexistente: fake_file.json"):
        import_from_json("fake_file.json")