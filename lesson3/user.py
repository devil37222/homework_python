class user:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.lastname = last_name
    def get_name(self):
        return self.name
    def get_last_name(self):
        return self.lastname
    def get_user_info(self):
        return f"User {self.name} {self.lastname}"
