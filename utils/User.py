class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"
    
    
    def get_info(self):
        print(self)
        
if __name__ == "__main__":
    user = User("john_doe", "me@me.com")
    print(user)