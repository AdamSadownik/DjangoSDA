import hashlib

def hash_password_without_salt(password: str) -> str:
    hash_pass = hashlib.sha256(password.encode("ascii")).hexdigest()
    return hash_pass

def verification_password_without_salt(password: str, hash_pass: str) -> bool:
    input_pass = hashlib.sha256(password.encode("ascii")).hexdigest()
    return input_pass == hash_pass
