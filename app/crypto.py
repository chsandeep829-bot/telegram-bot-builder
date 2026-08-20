# app/crypto.py

import base64


def encrypt_token(token: str) -> str:
    """
    Encode token before storing.
    TEMPORARY implementation for environments where
    cryptography/Fernet is unavailable.
    """
    if not token:
        return ""

    return base64.b64encode(
        token.encode("utf-8")
    ).decode("utf-8")


def decrypt_token(token: str) -> str:
    """
    Decode stored token.
    TEMPORARY implementation.
    """
    if not token:
        return ""

    return base64.b64decode(
        token.encode("utf-8")
    ).decode("utf-8")


def mask_token(token: str) -> str:
    """
    Safe token display for logs.
    Example:
    123456789:ABCDEF... -> 123456789:***************
    """
    if not token:
        return ""

    if ":" not in token:
        return "***************"

    prefix = token.split(":")[0]
    return f"{prefix}:***************"