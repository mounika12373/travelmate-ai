import time
from utils import auth_utils as auth

def describe_auth_module():
    def it_hashes_and_verifies_passwords():
        password = "mySecretPassword123"
        hashed = auth.hash_password(password)
        
        assert hashed != password
        assert len(hashed) == 64  # SHA256 length is 64 hex characters
        assert auth.verify_password(password, hashed) is True
        assert auth.verify_password("wrongPassword", hashed) is False

    def it_encodes_and_decodes_jwt_tokens():
        payload = {"id": 42, "full_name": "Alice Smith", "email": "alice@example.com"}
        token = auth.encode_jwt(payload, expiry_seconds=10)
        
        assert token is not None
        assert len(token.split('.')) == 3
        
        decoded = auth.decode_jwt(token)
        assert decoded is not None
        assert decoded["id"] == 42
        assert decoded["full_name"] == "Alice Smith"
        assert decoded["email"] == "alice@example.com"
        assert "exp" in decoded

    def it_returns_none_for_expired_jwt_tokens():
        payload = {"id": 1, "name": "Bob"}
        # Generate token with negative expiry (already expired)
        token = auth.encode_jwt(payload, expiry_seconds=-10)
        
        decoded = auth.decode_jwt(token)
        assert decoded is None

    def it_returns_none_for_tampered_jwt_tokens():
        payload = {"id": 1, "name": "Charlie"}
        token = auth.encode_jwt(payload, expiry_seconds=3600)
        
        # Tamper the token payload
        parts = token.split('.')
        tampered_token = f"{parts[0]}.eyJpZCI6IDEsICJuYW1lIjogIk1hbGljb3VzIn0.{parts[2]}"
        
        decoded = auth.decode_jwt(tampered_token)
        assert decoded is None
