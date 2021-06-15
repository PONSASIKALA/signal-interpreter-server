import json


class JsonParser:
    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        with open(file_path, "r") as json_file:
            self.data = json.load(json_file)

    def get_signal_title(self, identifier):
        for service in self.data["services"]:
            if service["id"] == identifier:
                return service["title"]
		return None
