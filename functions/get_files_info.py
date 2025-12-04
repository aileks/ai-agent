import os


def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory, directory)
        working_dir_abs = os.path.abspath(working_directory)
        full_path_abs = os.path.abspath(full_path)

        if not full_path_abs.startswith(working_dir_abs + os.sep) and full_path_abs != working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(full_path_abs):
            return f'Error: "{directory}" is not a directory'

        return list_dir_contents(full_path_abs)
    except Exception as e:
        return f"Error: {e}"


def list_dir_contents(full_path):
    items = os.listdir(full_path)
    lines = []

    for item in items:
        item_path = os.path.join(full_path, item)
        file_size = os.path.getsize(item_path)
        is_dir = os.path.isdir(item_path)

        line = f"- {item}: file_size={file_size} bytes, is_dir={is_dir}"
        lines.append(line)

    return "\n".join(lines)
