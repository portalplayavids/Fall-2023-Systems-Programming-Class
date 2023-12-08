
class FileIO:
    """
    This class provides methods for reading and writing files.
    """

    @staticmethod
    def read_file(file_path="to_read.txt") -> bytes:
        """
        Read the contents of a file and return as bytes.

        Args:
            file_path (str): The path of the file to read. Default is "to_read.txt".

        Returns:
            bytes: The contents of the file as bytes.
        """
        with open(file_path, "rb") as file:
            data = file.read()
        return data

    @staticmethod
    def write_file(data: bytes, file_path="to_write.txt"):
        """
        Write the given data to a file.

        Args:
            data (bytes): The data to write to the file.
            file_path (str): The path of the file to write. Default is "to_write.txt".
        """
        with open(file_path, "wb") as file:
            file.write(data)
