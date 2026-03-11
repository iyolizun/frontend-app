
import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def calculate_total(items: list) -> float:
    return sum(item.get('price', 0) * item.get('quantity', 1) for item in items)

