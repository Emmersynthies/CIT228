class User:
    def __init__(self, first_name, last_name, username, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone = phone
        self.email = email
        self.login_attempts=0
        
    def describe_user(self):
        print(f"\nUser={self.first_name}, {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Phone: {self.phone}")
        print(f"  Email: {self.email}")
        

    def greet_user(self):
        print(f"\nWelcome, {self.username}. You got mail!")

    def increment_login_attempts(self):
       self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, username, phone, email, permissions):
        super().__init__(first_name, last_name, username, phone, email)
        self.privileges=Privileges(permissions)

class Privileges():
    def __init__(self, privileges):
        self.privileges=privileges

    def show_privileges(self,users):
        print("\nThe following was approved")
        for privilege in self.privileges:
            print(privilege)



jamie = User("jamie", "brady", 'jbrady', "(999)567-8888", 'Brady_j@example.com')
jamie.describe_user()


print("\nAdding items... :{privileges.show_privileges}")
jamie_privileges = [
    'can reset username',
    'can lead control',
    'can add accounts',
    ]


