import app.io.input as inputs
import app.io.output as outputs


def main():

    print("=" * 10, "Getting inputs", "=" * 10)

    user_input = inputs.user_input()  # 4.1.1
    print(user_input)

    file_to_read = "data/input_file.txt"
    file_input = inputs.file_input(file_to_read)  # 4.1.2
    print(file_input)

    data_to_read = "data/data_pandas.csv"
    pandas_input = inputs.pandas_input(data_to_read)  # 4.1.3
    print(pandas_input)

    file_to_write = "data/output_file.txt"
    # truncate the file if it's not empty before writing
    with open(file_to_write, "rb+") as f:
        first_char = f.read(1)
        if first_char:
            f.seek(0)
            f.truncate()
    print("=" * 10, f"Writing to {file_to_write}", "=" * 10)

    outputs.file_output(file_to_write, user_input)
    outputs.file_output(file_to_write, file_input)
    outputs.file_output(file_to_write, pandas_input)


if __name__ == "__main__":
    main()
