class UserNotFoundError(Exception):
    message = "No user found"

    def __str__(self):
        return UserNotFoundError.message
    
class UserUnauthorizedError(Exception):
    message = "Email or password incorrect."

    def __str__(self):
        return UserUnauthorizedError.message
    
class EmailAlreadyExistError(Exception):
    message = "Email already exists"

    def __str__(self):
        return EmailAlreadyExistError.message
    