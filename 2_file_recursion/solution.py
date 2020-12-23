import os

answer = []


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    children_paths = os.listdir(path)
    for child_path in children_paths:
        next_path = path + '/' + child_path

        # if path is not a file, run find_files(path)
        if not os.path.isfile(next_path):
            find_files(suffix, next_path)
        elif next_path.endswith(suffix):
            answer.append(next_path)
    return None


# sample test code
find_files('', "./testdir")
print(answer)
