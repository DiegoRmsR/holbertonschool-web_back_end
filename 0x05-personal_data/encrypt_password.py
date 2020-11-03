#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    User passwords should NEVER be stored in plain text in a database.
    """
    hashed = bcrypt.hashpw(password.encode(),
                           bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    function that expects 2 arguments and returns a boolean.
    """
    valid = False
    if bcrypt.checkpw(password.encode('utf-8'),
                      hashed_password):
        valid = True
    return valid
