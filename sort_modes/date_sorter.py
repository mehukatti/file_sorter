import os
import pathlib
import datetime
import shutil
import time

from common.selectors import FileExtensionSelector
import common.tools as tools

class DateSorter:
    def __init__(self, root_folder:str, new_root_folder: str, file_type:str, test_mode=True):
        self.root_folder = self._check_root_folder_format(root_folder)
        self.new_root_folder = self._check_root_folder_format(new_root_folder)
        self.file_type = file_type
        self.test_mode = test_mode # NOTE Does not create anything.
        self.file_extensions = self._file_extension()
        self.iter_images()
        self._create_report()
    
    def _check_root_folder_format(self, folder):
        if not folder.endswith("\\"):
            folder = folder = "\\"
        return folder

    def _file_extension(self):
        extension_selector = FileExtensionSelector(self.file_type)
        return extension_selector.file_extensions
    
    def _get_modification_date(self, file_path):
        timestamp = os.path.getmtime(file_path)
        datestamp = datetime.datetime.fromtimestamp(timestamp)
        print(f"Modified Date/Time: {datestamp}. File {file_path}")
        return datestamp

    def _check_root_folders(self):
        if not os.path.exists(self.root_folder):
            raise Exception(f"The target root folder does not exist: {self.root_folder}")
        
        # Check if new root folder exist
        if os.path.exists(self.new_root_folder):
            raise Exception(f"The new root folder already exists. Cannot continue as this process may overwrite something you do not wish to be overwritten.")
        os.makedirs(self.new_root_folder)
        print(f"New root folder created: {self.new_root_folder}")

    def iter_images(self):
        """Iterate the files in root folder and copy them by date to a new folder"""
        self._check_root_folders()

        # Start iteration
        test_limit = 10
        self.counter = 0
        self.skipped_files = []

        files = os.listdir(self.root_folder)
        for file in files:
            if self.test_mode and self.counter > test_limit:
                print("In test mode and exceeds limit. Stopping.")
                self._remove_subfolders_in_test()
                return
            
            # Check if file extension is correct
            if pathlib.Path(file).suffix not in self.file_extensions:
                self.skipped_files.append(file)
                continue

            # Check the modification date of the file
            file_path = f"{self.root_folder}{file}"
            datestamp = self._get_modification_date(file_path)
            # Select subfolder inside the new root folder
            subfolder = f"{self.new_root_folder}{datetime.datetime.strftime(datestamp, '%Y%m')}"
            if not os.path.exists(subfolder):
                os.mkdir(subfolder)
            
            print(f"Copying the file {file} to {subfolder}")
            if not self.test_mode:
                # copy the image to the new folder
                shutil.copy2(file_path, f"{subfolder}\\{file}")
            self.counter += 1
            
    def _remove_subfolders_in_test(self):
        """Remove the subfolders that were created."""

        # First remove empty subfolders
        for path in os.listdir(self.new_root_folder):
            complete_path = f"{self.new_root_folder}{path}"
            if os.path.isdir(complete_path):
                os.rmdir(complete_path)
                print(f"removing the path {path}")
        
        # Lastly remove the new, empty root folder
        time.sleep(2) # To avoid permissiondenied
        print(f"Removing the new root folder: {self.new_root_folder}")
        os.rmdir(self.new_root_folder)
    
    def _create_report(self):
        """Create a report of the process into a txt file"""
        content = f"Sorted {self.counter} files.\nSkipped these files:\n"
        if self.skipped_files:
            content = content + "\n".join(self.skipped_files)
        else:
            content = content + "No files were skipped."
        
        tools.create_report(content)
