import os
import json

class ConfigReader:
    _config = None

    @classmethod
    def load_config(cls, file_path):
        if ConfigReader._config is None:
            Config_path = os.path.join(os.path.dirname(__file__), file_path)