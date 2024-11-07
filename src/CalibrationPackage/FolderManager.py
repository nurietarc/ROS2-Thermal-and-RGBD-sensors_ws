import os
import shutil
from datetime import datetime
from colorama import Fore, Style

"""
Nuria Rodríguez Calderón
    Manages the creation and deletion of folders within a specified base path for image calibration.
    This class allows users to:
    - Create specified base folders (e.g., for storing calibration and homography files).
    - Generate timestamped subfolders within each base folder based on existing subdirectories in the images folder.
    - Delete all or only subfolders within each base folder as needed.
    - Obtain and print the names of subfolders within the specified images folder.
"""

class FolderManager:
    def __init__(self, base_path, images_base_path, folders_names):
        """
        Initializes the FolderManager with base paths and folder names.
        
        Parameters:
        - base_path: The base directory where folders will be created.
        - images_base_path: The path to the folder containing images for calibration.
        - folders_names: List of names for the base folders to be managed.
        """
        self.base_path = base_path
        self.images_base_path = images_base_path
        self.folders_names = folders_names
        self.current_datetime = datetime.now().strftime('%Y-%m-%d___%H-%M-%S')

        # Set up dictionary with paths for the specified name folders
        self.folders_path = {folder: os.path.join(self.base_path, folder) for folder in folders_names}

        # Check if the images folder exists
        if not os.path.isdir(self.images_base_path):
            print(f"The '{images_base_path}' folder is not found. Please create a folder named '{images_base_path}' with subfolders containing images for calibration.")

    def obtain_name_of_image_folders(self):
        """ 
        Obtains a list of the names of all subfolders inside images_base_path. 
        """
        self.folders_images_names = [f for f in os.listdir(self.images_base_path) 
                              if os.path.isdir(os.path.join(self.images_base_path, f))]

    def create_folders(self):
        """ 
        Creates the base folders where plots and .txt/.json files will be stored. 
        """
        for path in self.folders_path.values():
            if not os.path.exists(path):
                os.makedirs(path)
                print(Fore.LIGHTBLACK_EX + f"Folder created: {path}" + Style.RESET_ALL)

    def create_subfolders(self, specific_folder=None, suffix=''):
        """
        Create timestamped subfolders within each base folder.
        
        Parameters:
        - specific_folder: If provided, only a subfolder for this specific folder will be created.
        - suffix: A suffix to be added to the subfolder name.
        """
        self.obtain_name_of_image_folders()
        current_datetime = datetime.now().strftime('%Y-%m-%d___%H-%M-%S')
        
        for folder_type in self.folders_path:
            folder_path = self.folders_path[folder_type]

            # Skip folders that do not match specific_folder if specified
            if specific_folder:
                subfolder_name = f"{specific_folder}_{current_datetime}{suffix}"
                subfolder_path = os.path.join(folder_path, subfolder_name)
                
                # Create the subfolder if it does not exist
                os.makedirs(subfolder_path, exist_ok=True)
                print(Fore.LIGHTBLACK_EX + f"Subfolder created: {subfolder_path}" + Style.RESET_ALL)

            else:
                # Create subfolders based on names from self.folders_images_names
                for subfolder in self.folders_images_names:
                    # Create the subfolder name with type, date, and suffix
                    subfolder_name = f"{subfolder}_{current_datetime}{suffix}"
                    subfolder_path = os.path.join(folder_path, subfolder_name)
                    
                    # Create the subfolder if it does not exist
                    os.makedirs(subfolder_path, exist_ok=True)
                    print(Fore.LIGHTBLACK_EX + f"Subfolder created: {subfolder_path}" + Style.RESET_ALL)

    def create_combined_subfolder(self, folder1, folder2):
        """
        Create a combined subfolder for HomographyFiles and HomographyPlots with folder1, folder2 names, and timestamp.
        
        Parameters:
        - folder1, folder2: Names of the folders to be combined in the subfolder name.
        
        Returns:
        - Dictionary containing paths for files and plots.
        """
        timestamp = datetime.now().strftime('%Y-%m-%d___%H-%M-%S')
        subfolder_name = f"{folder1}{folder2}_{timestamp}"
        files_path = os.path.join(self.base_path, self.folders_names[1], subfolder_name)
        plots_path = os.path.join(self.base_path, self.folders_names[0], subfolder_name)

        os.makedirs(files_path, exist_ok=True)
        os.makedirs(plots_path, exist_ok=True)

        return {"files_path": files_path, "plots_path": plots_path}
    
    def create_all_folders(self):
        """ 
        Creates both the base folders and their timestamped subfolders. 
        """
        self.obtain_name_of_image_folders()
        self.create_folders()
        self.create_subfolders()

    def delete_folders(self):
        """ 
        Deletes the base folders if they exist. 
        """
        for path in self.folders_path.values():
            if os.path.exists(path):
                shutil.rmtree(path)
                print(Fore.LIGHTBLACK_EX + f"Folder deleted: {path}" + Style.RESET_ALL)

    def delete_subfolders(self):
        """ 
        Deletes all subfolders within each base folder but keeps the base folders. 
        """
        self.obtain_name_of_image_folders()
        for folder_path in self.folders_path.values():
            if os.path.exists(folder_path):
                for subfolder in os.listdir(folder_path):
                    subfolder_path = os.path.join(folder_path, subfolder)
                    if os.path.isdir(subfolder_path):
                        shutil.rmtree(subfolder_path)
                        print(Fore.LIGHTBLACK_EX + f"Subfolder deleted: {subfolder_path}" + Style.RESET_ALL)

    def delete_all_folders(self):
        """ 
        Deletes both the base folders and all subfolders within them. 
        """
        self.obtain_name_of_image_folders()
        self.delete_subfolders()  
        self.delete_folders() 

    def get_latest_subfolder_with_prefix_and_suffix(self, folder_name, prefix, suffix="_intersection"):
        """
        Get the latest subfolder in a specified folder that starts with a given prefix and ends with a given suffix.
        
        Parameters:
        - folder_name: The base folder where subfolders are searched.
        - prefix: Prefix of the subfolder name to match.
        - suffix: Suffix of the subfolder name to match (default is "_intersection").
        
        Returns:
        - The path to the latest matching subfolder, or None if no match is found.
        """
        folder_path = os.path.join(self.base_path, folder_name)
        
        # Filter subfolders that start with the prefix and end with the suffix
        subfolders = [os.path.join(folder_path, d) for d in os.listdir(folder_path)
                    if os.path.isdir(os.path.join(folder_path, d)) and 
                    d.startswith(prefix) and d.endswith(suffix)]

        # Sort subfolders by modification date (latest first)
        if subfolders:
            latest_subfolder = max(subfolders, key=os.path.getmtime)
            return latest_subfolder
        else:
            print(Fore.RED + f"No subfolders with prefix '{prefix}' and suffix '{suffix}' found in '{folder_path}'" + Style.RESET_ALL)
            return None
