from .User import User

class Folder:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def create(self):
        import os
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def delete(self):
        import shutil
        if os.path.exists(self.path):
            shutil.rmtree(self.path)
    
    def add_user(self, user_name: str):
        if len(user_name) > 32:
            raise ValueError("Der Nutzername darf maximal 32 Zeichen lang sein.")
        self.users.append(User(user_name))

    def remove_user(self, user_name: str):
        self.users = [user for user in self.users if user.name != user_name]

    def list_files(self):
        import os
        if os.path.exists(self.path):
            return os.listdir(self.path)
        return []