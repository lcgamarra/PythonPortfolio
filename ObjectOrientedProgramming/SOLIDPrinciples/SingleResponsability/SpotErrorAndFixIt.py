class Authenticator:
    def login(self, username, password):
        if username == "admin" and password == "123":
            self.send_login_email(username)
            return True
        return False

    def send_login_email(self, username):
        print(f"Sending login email to {username}")


class Notifier:
    @staticmethod
    def notify(message):
        print(f"Sending notification: {message}")

class FixedAuthenticator:
    def login(self, username, password):
        if username == "admin" and password == "123":
            Notifier.notify(f"Sending login email {username}")
            return True
        return False

if __name__ == "__main__":
    authenticator = FixedAuthenticator()
    authenticator.login("admin", "123")