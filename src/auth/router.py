from fastapi import APIRouter, HTTPException
from schemas import SignIn, SignInResponse, NonceResponse
from config import message_for_sign
from auth.utils import generate_nonce, validate_eth_signature, generate_jwt_token

auth_router = APIRouter('/auth')

@auth_router.get('/nonce')
def get_nonce() -> NonceResponse:
    return {'message': message_for_sign + str(generate_nonce())}
    

@auth_router.post('/sign-in')
def sign_in(dataSignIn: SignIn) -> SignInResponse:
    is_valid = validate_eth_signature(dataSignIn.signature, dataSignIn.public_key, dataSignIn.nonce)

    if not is_valid:
        raise HTTPException(status_code=401, detail='Invalid signature')
    
    return {'token': generate_jwt_token(dataSignIn.public_key)}

