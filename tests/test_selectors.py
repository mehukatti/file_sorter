from common.selectors import FileExtensionSelector

import json

def test_file_extension_selector():
    extension_selector = FileExtensionSelector("image")
    extension_selector.file_extensions

def test():
    with open("common\\supported_file_extensions.json") as f:
        extension_dict = json.load(f)