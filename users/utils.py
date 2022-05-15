import hashlib
import os


def hash_password_without_salt(password: str) -> str:
    hash_pass = hashlib.sha256(password.encode("ascii")).hexdigest()
    return hash_pass

def verification_password_without_salt(password: str, hash_pass: str) -> bool:
    input_pass = hashlib.sha256(password.encode("ascii")).hexdigest()
    return input_pass == hash_pass

def hash_password_with_salt(password: str) -> str:
    # creating salt
    random_size = 30
    salt = os.urandom(random_size)
    hashed_salt = hashlib.sha256(salt).hexdigest()

    # hashing_password
    new_password = password + hashed_salt
    hashed_password = hashlib.sha256(new_password.encode('ascii')).hexdigest()

    combined_salt_and_password = ''.join([hashed_password, hashed_salt])

    return combined_salt_and_password

def verify_password_with_salt(password: str, hashed_password: str) -> bool:
    hashed_salt = hashed_password[-64:]
    new_password = password + hashed_salt
    password_to_check = hashlib.sha256(new_password.encode('ascii')).hexdigest()

    combined_salt_and_password = ''.join([password_to_check, hashed_salt])

    return combined_salt_and_password == hashed_password

'2d6f7756a01805472ff1e206f32ce4d317aa86e7b08c3573a862cc45954ac916df23e2c4b31f185e97b2390a4eceb0b4d309ceca570c6953381e0b11697d2e17'
