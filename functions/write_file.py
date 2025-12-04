import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes a file to the given directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The directory to write the file, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write into the file.",
            ),
        },
    ),
)


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
