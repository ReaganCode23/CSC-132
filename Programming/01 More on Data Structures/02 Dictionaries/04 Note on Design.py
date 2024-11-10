user = {
    "username": "coriell"
}


#or do a class
class User:

    def __init__(self, username:str, email: str):
        self.username = username
        self.email = email

    
    def __str__(self):
        return f"{self.username} -- {self.email}"