import numpy as np
import mmap
from typing import  Tuple

def generate_file(size: int, filename: str) -> Tuple[int, int, int]:
    """Function for generating file with stated name and size.
    There is an array of uint32 numbers written in big endian.

    Args:
        size (int): file size in bytes
        filename (str): filename

    Returns:
        Tuple[int, int, int]: sum of numbers, min and max number in array
    """
    with open(filename, 'wb') as file_writer:
        generated_array = np.random.randint(0, 2**32, size//4, dtype=np.dtype('uint32')).newbyteorder()
        file_writer.write(generated_array.data)
    return np.sum(generated_array), np.min(generated_array), np.max(generated_array)

def read_file(filename: str) -> np.ndarray:
    """Read file in one thread.

    Args:
        filename (str): filename

    Returns:
        np.ndarray: array of uint32 numbers written in big endian.
    """
    with open(filename, 'rb') as file_reader:
        restored_array = np.frombuffer(file_reader.read(), dtype=np.dtype('uint32').newbyteorder('>'))
    return restored_array

def read_mmap_file(size: int, filename: str) -> np.ndarray:
    """read array with mmap files

    Args:
        size (int): length of file
        filename (str): filename

    Returns:
        np.ndarray: array of uint32 numbers written in big endian.
    """
    with open(filename, 'rb') as file_reader:
        mm_buf = mmap.mmap(file_reader .fileno(), length=size, offset=0, access=mmap.ACCESS_READ)
        restored_array = np.frombuffer(mm_buf, dtype=np.dtype('uint32').newbyteorder('>'))
    return restored_array
