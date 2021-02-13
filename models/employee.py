from pydantic import BaseModel, EmailStr, validator

class Add(BaseModel):
    username: str
    email: EmailStr
    password: str

    @validator('username')
    def username_lenght(cls, username):
        if len(username) < 4:
            raise ValueError('username must be > 4 character')

        if len(username) > 32:
            raise ValueError('username could not be more than 32 character')

        return username

    @validator('password')
    def password_lenght(cls, password):
        if len(password) < 8:
            raise ValueError('password must be > 8 character')

        if len(password) > 124:
            raise ValueError('password could not be more than 124 character')

        return password
