import json


def import_from_json(file_path: str):
    try:
        with open(file_path) as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {file_path}")
    except Exception:
        raise FileNotFoundError(f"Algo deu errado: {file_path}")