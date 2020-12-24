from is_user_in_group import is_user_in_group
from Group import Group
import unittest


# Unit test
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


class Testing(unittest.TestCase):
    def testCreateEmptyGroup(self):
        with self.assertRaises(Exception):
            p = Group('')

    def testAddEmptyGroup(self):
        with self.assertRaises(Exception):
            parent.add_group('')

    def testAddEmptyUser(self):
        with self.assertRaises(Exception):
            s = parent.add_user('')

    def testSuccessfullySearchUser(self):
        ans = is_user_in_group("sub_child_user", parent)
        self.assertEqual(ans, True)
        ans = is_user_in_group("abc", parent)
        self.assertEqual(ans, False)

    def testSearchInvalidUsername(self):
        with self.assertRaises(Exception):
            is_user_in_group("", parent)

    def testSearchInvalidGroup(self):
        with self.assertRaises(Exception):
            is_user_in_group("asdf", "")


if __name__ == "__main__":
    unittest.main()
