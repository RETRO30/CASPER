from eth_account import Account
from auth.config import message_for_sign, secret_jwt_key
import random
from datetime import datetime, timedelta
import jwt

def validate_eth_signature(signature: str, address: str, nonce: int):
    message_bytes = (message_for_sign + nonce).encode('utf-8')
    public_key = Account.recover_message(message_bytes, signature=signature)
    recovered_address = Account.from_key(public_key).address
    return recovered_address.lower() == address.lower()

def generate_nonce() -> int:
    return random.randint(100000, 999999)

def generate_jwt_token(address: str) -> str:
    payload = {
        'address': address,
        'exp': datetime.utcnow() + timedelta(seconds=10800)
    }
    token = jwt.encode(payload, secret_jwt_key, algorithm='HS256')
    return token.decode('utf-8')

