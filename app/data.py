import json


class Data:
    data = None

    @staticmethod
    def load_config(filename: json) -> dict:
        with open(filename, "r") as file:
            info = json.load(file)
            return info
