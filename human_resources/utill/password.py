import hashlib

salt = 'dummy_salt'


def pass_gen(password: str) -> str:
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()
