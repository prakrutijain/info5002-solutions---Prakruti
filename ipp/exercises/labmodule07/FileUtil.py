import os
import json

from typing import Dict, List, Optional, Union

class FileUtil:
    """
    Utility class for common file operations such as reading, writing,
    and checking existence of files and directories.
    """

    def __init__(self):
        pass

    @classmethod
    def readTextFile(cls, fileName: str, encoding: str = 'utf-8') -> Optional[str]:
        """
        Reads the contents of a text file and returns it as a string.
        
        Parameters:
            fileName (str): The full path to the file to read.
            encoding (str): The character encoding to use. Defaults to 'utf-8'.
        
        Returns:
            str: The contents of the file, or None if an error occurred.
        """
        try:
            if FileUtil.fileExists(fileName):
                with open(fileName, 'r', encoding=encoding) as f:
                    return f.read()
            else:
                print(f"Can't read text file. File doesn't exist: {fileName}")

        except FileNotFoundError:
            print(f"Error: File '{fileName}' not found")
            return None
        except PermissionError:
            print(f"Error: Permission denied for '{fileName}'")
            return None
        except UnicodeDecodeError:
            print(f"Error: Unable to decode '{fileName}' with encoding '{encoding}'")
            return None
        except Exception as e:
            print(f"Error reading file '{fileName}': {e}")
            return None

    @classmethod
    def writeTextFile(cls, fileName: str, content: str, encoding: str = 'utf-8', mode: str = 'w') -> bool:
        """
        Writes a string of content to a text file.
        
        Parameters:
            fileName (str): The full path to the file to write.
            content (str): The text content to write into the file.
            encoding (str): The character encoding to use. Defaults to 'utf-8'.
            mode (str): The write mode - 'w' to overwrite, 'a' to append. Defaults to 'w'.
        
        Returns:
            bool: True if the file was written successfully, False otherwise.
        """
        try:
            with open(fileName, mode, encoding = encoding) as f:
                f.write(content)
            return True
        except PermissionError:
            print(f"Error: Permission denied for '{fileName}'")
            return False
        except IOError as e:
            print(f"Error writing to file '{fileName}': {e}")
            return False
        except Exception as e:
            print(f"Unexpected error writing file '{fileName}': {e}")
            return False

    @classmethod
    def fileExists(cls, fileName: str) -> bool:
        """
        Checks whether a file exists at the given path.
        
        Parameters:
            fileName (str): The full path to the file to check.
        
        Returns:
            bool: True if the file exists, False otherwise.
        """
        return os.path.isfile(fileName)

    @classmethod
    def directoryExists(cls, dirName: str) -> bool:
        """
        Checks whether a directory exists at the given path.
        
        Parameters:
            dirName (str): The full path to the directory to check.
        
        Returns:
            bool: True if the directory exists, False otherwise.
        """
        return os.path.isdir(dirName)