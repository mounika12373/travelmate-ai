import base64
import hashlib
import hmac
import json
import time

import streamlit as st

SECRET_KEY = "travelmate_super_secret_key_12345"


def hash_password(password: str) -> str:
    """Hashes a password using SHA-256 with a static salt for database storage."""
    salt = "travelmate_salt_6789"
    keyed = password + salt
    return hashlib.sha256(keyed.encode("utf-8")).hexdigest()


def verify_password(password: str, hashed: str) -> bool:
    """Verifies that a password matches its hashed form."""
    return hash_password(password) == hashed


def base64url_encode(payload) -> str:
    """Helper to base64url encode payloads or headers."""
    if isinstance(payload, dict):
        payload = json.dumps(payload).encode("utf-8")
    elif isinstance(payload, str):
        payload = payload.encode("utf-8")
    return base64.urlsafe_b64encode(payload).replace(b"=", b"").decode("utf-8")


def base64url_decode(s: str) -> bytes:
    """Helper to base64url decode strings."""
    padding = "=" * (4 - len(s) % 4)
    return base64.urlsafe_b64decode(s + padding)


def encode_jwt(payload: dict, expiry_seconds: int = 86400) -> str:
    """Generates a secure signed JWT-like token (HMAC-SHA256) for user sessions."""
    header = {"alg": "HS256", "typ": "JWT"}
    payload = payload.copy()
    payload["exp"] = int(time.time()) + expiry_seconds

    header_b64 = base64url_encode(header)
    payload_b64 = base64url_encode(payload)

    signature_input = f"{header_b64}.{payload_b64}".encode("utf-8")
    signature = hmac.new(SECRET_KEY.encode("utf-8"), signature_input, hashlib.sha256).digest()
    signature_b64 = base64.urlsafe_b64encode(signature).replace(b"=", b"").decode("utf-8")

    return f"{header_b64}.{payload_b64}.{signature_b64}"


def decode_jwt(token: str) -> dict:
    """Decodes and verifies a JWT-like token. Returns payload dict or None if invalid/expired."""
    if not token:
        return None
    try:
        parts = token.split(".")
        if len(parts) != 3:
            return None
        header_b64, payload_b64, signature_b64 = parts

        # Verify signature
        signature_input = f"{header_b64}.{payload_b64}".encode("utf-8")
        expected_signature = hmac.new(SECRET_KEY.encode("utf-8"), signature_input, hashlib.sha256).digest()
        expected_signature_b64 = base64.urlsafe_b64encode(expected_signature).replace(b"=", b"").decode("utf-8")

        if not hmac.compare_digest(signature_b64, expected_signature_b64):
            return None

        payload = json.loads(base64url_decode(payload_b64).decode("utf-8"))
        if payload.get("exp", 0) < time.time():
            return None  # Expired

        return payload
    except Exception:
        return None


def login_user(user_data: dict, remember_me: bool = False):
    """Sets the user session state and optionally a remember-me token."""
    # Strip sensitive data before putting user in session state
    session_user = {
        "id": user_data["id"],
        "full_name": user_data["full_name"],
        "email": user_data["email"],
        "phone": user_data.get("phone", ""),
        "country": user_data.get("country", ""),
        "city": user_data.get("city", ""),
        "profile_pic": user_data.get("profile_pic", ""),
        "preferences": user_data.get("preferences", "[]"),
    }
    st.session_state.user = session_user
    token = encode_jwt(session_user, expiry_seconds=86400 * 30 if remember_me else 86400)
    st.session_state.auth_token = token
    if remember_me:
        # Mocking remember me by storing it in local storage / query params
        # In streamlit, we can also use query params or cookie mock in session state
        st.session_state.remember_me_token = token


def logout_user():
    """Logs the user out by clearing the session state."""
    st.session_state.user = None
    st.session_state.auth_token = None
    if "remember_me_token" in st.session_state:
        del st.session_state.remember_me_token
    # Clear chat history and other session states specific to user
    if "messages" in st.session_state:
        st.session_state.messages = []
