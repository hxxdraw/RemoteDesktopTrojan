from os import path, makedirs, remove


def is_exists(file_path):
    """
    Trying to find file. If founded >> ::return:: <True>, else <False>
    """
    if path.exists(file_path):
        return True
    else:
        return False


def make_dirs(d_path):
    """
    Creating dirs tree
    """
    makedirs(d_path)


def remove_dir(file_path):
    """
    Removing file by path
    return: String
    """
    try:
        remove(file_path)
        return f'"{file_path}" was removed.'
    except Exception as e:
        return e
