import os


def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.join(working_directory, file_path)
        working_dir_abs = os.path.abspath(working_directory)
        full_path_abs = os.path.abspath(full_path)

        if (
            not full_path_abs.startswith(working_dir_abs + os.sep)
            and full_path_abs != working_dir_abs
        ):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        with open(full_path_abs, "w", encoding="utf-8") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: {e}"
