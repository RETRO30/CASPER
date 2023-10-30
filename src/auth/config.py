import os

message_for_sign = 'You are signing in to the application with the following nonce: '
secret_jwt_key = os.environ.get('SECRET_JWT_KEY')
