from secrets import choice, token_urlsafe

def generate_secret(length: int = 50) -> str:
    """
    Generates a secret key for the application.
    """
    return secrets.token_urlsafe(length)

if __name__ == "__main__":
    print(generate_secret())
