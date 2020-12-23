def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    answer = False
    answer = loopSearch(user, group)
    return answer


def loopSearch(user, group):
    # check if user is inside group.user
    if user in group.get_users():
        return True
    # if group has no sub_groups, return False
    elif len(group.get_groups()) == 0:
        return False
    else:
       # walk through all the groups
        for g in group.get_groups():
            return loopSearch(user, g)
