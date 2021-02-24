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





user = User("jamie", "brady", 'jbrady', "(999)567-8888", 'Brady_j@example.com')
user.describe_user()
user.greet_user()

print("\nMaking 5 login attempts...")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")

print("Resetting login attempts...")
user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}")
print("Your account is having an issue, try again later!")