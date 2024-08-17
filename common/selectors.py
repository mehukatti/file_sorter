from common.exceptions import NotImplemented
import common.tools as tools

import json

class FileExtensionSelector:
    """Determine the file extensions to look for when sorting"""
    def __init__(self, file_type:str):
        self.file_type = file_type
        self.extension_dict = tools.read_json("common\\supported_file_extensions.json")
        self.file_extensions = self._select_file_extensions()
        
    def _select_file_extensions(self):
        """Select the correct file extensions for files to sort."""
        print(f"Given file type: {self.file_type}")

        if self.file_type.lower() not in self.extension_dict.keys():
            raise NotImplemented("The file sorter supports only image types at the moment.")
        # NOTE: To add support for more file extensions, edit the json. You may need to edit code too.
        file_extensions = self.extension_dict[self.file_type.lower()]
        
        print(f"Got the file type: {self.file_type}. file extensions for this: {', '.join(file_extensions)}")
        return file_extensions