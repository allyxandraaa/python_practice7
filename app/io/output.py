def user_output(prompt):
    """
    Display data to the console.

    This function provides a standardized way to print various data types
    to the console with appropriate formatting.

    Args:
        prompt (Any): Data to be displayed. Can be string, list, dict,
        or pandas DataFrame.

    Returns:
        None: Outputs directly to console
    """
    print(prompt)
    return None


def file_output(file_name, data):
    """
    Write data to a text file.

    This function appends data to a specified file using a context manager.
    Then it appends a new line character. The file is automatically closed
    after reading.

    Args:
        file_name (str): Path to the output file.
        data (str): Content to be written to the file. Non-string data will be
                    automatically converted to string during writing.

    Returns:
        None: This function doesn't return useful data. Indicates successful
              completion of the file write operation.
    """
    with open(file_name, "a") as f:
        f.write(data)
        f.write("\n")
    return None
