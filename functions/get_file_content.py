import os
from functions.config import MAX_FILE_CONTENT_LENGTH


def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        working_dir_abs = os.path.abspath(working_directory)
        full_path_abs = os.path.abspath(full_path)

        if (
            not full_path_abs.startswith(working_dir_abs + os.sep)
            and full_path_abs != working_dir_abs
        ):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_path_abs, "r", encoding="utf-8") as f:
            content = f.read()

        if len(content) > MAX_FILE_CONTENT_LENGTH:
            content = content[:MAX_FILE_CONTENT_LENGTH]
            content += f'\n[...File "{file_path}" truncated at {MAX_FILE_CONTENT_LENGTH} characters]'

        return content
    except Exception as e:
        return f"Error: {e}"
