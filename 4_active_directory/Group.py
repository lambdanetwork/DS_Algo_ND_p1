class Group(object):
    def __init__(self, _name):
        if type(_name) != str or len(_name) <= 0:
            raise Exception("Provide a valid name for group")
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        if not isinstance(group, Group):
            raise Exception("Provide a group object")

        self.groups.append(group)

    def add_user(self, user):
        if type(user) != str or len(user) <= 0:
            raise Exception("Provide a valid name for user")

        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
