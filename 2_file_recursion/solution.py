import os
import unittest


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
    answer = []

    def recursive_find(suffix, path):
        children_paths = os.listdir(path)
        for child_path in children_paths:
            next_path = path + '/' + child_path

            # if path is not a file, run find_files(path)
            if not os.path.isfile(next_path):
                recursive_find(suffix, next_path)
            elif next_path.endswith(suffix):
                answer.append(next_path)

    recursive_find(suffix, path)
    if len(answer) == 0:
        return None
    else:
        return answer


class Testing(unittest.TestCase):

    def testFindEmptyFile(self):
        answer = 10  # there are 10 files
        files = find_files('', './testdir')
        self.assertEqual(answer, len(files))

    def testFindCfile(self):
        answer = 4  # there are 4 files end with .c
        files = find_files('.c', './testdir')
        self.assertEqual(answer, len(files))

    def testsearchEmptyPathWillRaiseException(self):
        answer = 4  # there are 4 files end with .c
        with self.assertRaises(FileNotFoundError):
            files = find_files('.c', '')


if __name__ == "__main__":
    unittest.main()
