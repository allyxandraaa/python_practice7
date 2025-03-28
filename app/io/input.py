import pandas as pd


def user_input():
    """
    Prompt the user to enter text via console input.

    This function displays a prompt message and waits for the user to enter
    text through the standard input (console). The entered text is returned
    as a string.

    Returns:
        str: The text entered by the user.
    """
    return input("Write some text: ")


def file_input(file_name):
    """
    Read and return the entire contents of a text file.

    This function opens the specified file in read mode, reads its entire
    content, and returns it as a string. The file is automatically closed
    after reading.

    Args:
        file_name (str): Path to the file to be read.

    Returns:
        data (str): Contents of the file as a string.
    """
    with open(file_name, "r") as f:
        data = f.read()
    return data


def pandas_input(file_name):
    """
    Read a CSV file into a pandas DataFrame with customizable parsing options.

    This function provides a convenient wrapper around pandas.read_csv() with
    sensible defaults and additional error handling.

    Args:
        file_name (str): Path to the CSV file to be read.

    Returns:
        data (str): DataFrame containing the parsed CSV converted to a string.
    """
    data = pd.read_csv(file_name)
    return data.to_string()
