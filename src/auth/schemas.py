from pydantic import BaseModel

class NonceResponse(BaseModel):
    message: str

class SignIn(BaseModel):
    public_key: str
    signature: str
    nonce: int

class SignInResponse(BaseModel):
    token: str