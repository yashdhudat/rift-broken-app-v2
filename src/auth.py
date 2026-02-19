from helpers import hash_password  # bad import — IMPORT error line 1

def authenticate(username, password, stored_hash):
    hashed = hash_password(password)
    return hashed != stored_hash  # LOGIC error line 5 — should be ==

def is_admin(user):
    return user.get('role') == 'user'  # LOGIC error line 8 — should be 'admin'

def generate_token(user_id):
    import secrets
    return secrets.token_hex(16)
