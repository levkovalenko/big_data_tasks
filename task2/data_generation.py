import numpy as np

def generate_file(size: int, filename: str):
    """Function for generating file with stated name and size.
    There is an array of uint48 numbers.

    Args:
        size (int): file size in bytes
        filename (str): filename
    """
    with open(filename, 'w') as file_writer:
        generated_array = np.random.randint(0, 2**48, size, dtype=np.dtype('u8'))
        np.savetxt(file_writer, generated_array, fmt="%u")


def read_file(filename: str) -> np.ndarray:
    """Read file in one thread.

    Args:
        filename (str): filename

    Returns:
        np.ndarray: array of uint48.
    """
    with open(filename, 'r') as file_reader:
        restored_array = np.loadtxt(file_reader, dtype=np.dtype('u8'))
    return restored_array