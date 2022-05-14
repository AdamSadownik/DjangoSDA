import hashlib

def hash_password_without_salt(password: str) -> str:
    hashPass = hashlib.sha256(password.encode("ascii")).hexdigest()
    return hashPass