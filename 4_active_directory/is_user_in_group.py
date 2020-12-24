from Group import Group


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if type(user) != str or len(user) <= 0:
        raise Exception("Provide a valid user to search")

    if not isinstance(group, Group):
        raise Exception("Provide a group object on second argument")

    # rewrite this solution based on feedback from reviewer
    return user in group.get_users() or any(is_user_in_group(user, sub_group) for sub_group in group.get_groups())
