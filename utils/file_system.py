import os
import platform
import shutil

from pathlib import Path
from typing import Literal

Scope = Literal["project", "home", "system"]


class FileSystem:
    """
    Helper class for working with file system and create correct paths
    """

    @staticmethod
    def get_project_root() -> str:
        return Path(__file__).parent.parent.absolute().__str__()

    @staticmethod
    def get_home_root() -> str:
        return Path.home().__str__()

    @staticmethod
    def get_system_root() -> str:
        return os.path.abspath(os.sep)[:-1] if platform.system().lower() == 'windows' else ''

    @staticmethod
    def get_root(scope: Scope):
        """
        :param scope: "project" || "home" || "system"
            project: path from project root
            home: path from user folder root
            system: path from absolute system root
        """
        match scope:
            case 'project':
                return FileSystem.get_project_root()
            case 'home':
                return FileSystem.get_home_root()
            case 'system':
                return FileSystem.get_system_root()
            case _:
                raise ValueError(f'Wrong scope: "{scope}". Please, input "project" || "home" || "system"')

    @staticmethod
    def get_absolute_path(path: str | list, scope: Scope = 'project') -> str:
        path_list: list = [path] if isinstance(path, str) else path
        root = FileSystem.get_root(scope=scope)
        return os.sep.join([root] + path_list)

    @staticmethod
    def make_dir(path: str | list, scope: Scope = 'project'):
        path = FileSystem.get_absolute_path(path, scope=scope)
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def delete_dir(path: str | list, scope: Scope = 'project'):
        directory_to_delete_path = FileSystem.get_absolute_path(path, scope=scope)
        shutil.rmtree(directory_to_delete_path, ignore_errors=True)

    @staticmethod
    def delete_file(path: str | list, scope: Scope = 'project'):
        path = FileSystem.get_absolute_path(path, scope=scope)
        if os.path.isfile(path):
            os.remove(path)

    @staticmethod
    def rename_file(absolute_file_path_to_change: str, new_file_absolute_path: str):
        shutil.move(absolute_file_path_to_change, new_file_absolute_path)

    @staticmethod
    def get_newest_file_in_folder(path: str | list, scope: Scope = 'project') -> str:
        """
        :return: returns file name in folder by path, with the latest creation time
        """
        directory_path = FileSystem.get_absolute_path(path, scope=scope)
        return max([directory_path + os.sep + f for f in os.listdir(directory_path)], key=os.path.getctime)

