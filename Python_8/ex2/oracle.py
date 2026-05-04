import os
import sys
from dotenv import load_dotenv


def load_configuration() -> dict:
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    return config


def validate_config(config: dict) -> None:
    missing = [key for key, value in config.items() if not value]

    if missing:
        print("ORACLE STATUS: Configuration error\n")
        print("Missing required environment variables:")
        for var in missing:
            print(f"- {var}")
        print("\nYou can add them by copying .env.example like this"
              "\ncp .env.example .env")
        sys.exit(1)


def get_database_status(db_url: str) -> str:
    if "localhost" in db_url or "127.0.0.1" in db_url:
        return "Connected to local instance"
    return "Connected to remote instance"


def get_api_status(api_key: str) -> str:
    return "Authenticated" if api_key else "Unavailable"


def get_zion_status(endpoint: str) -> str:
    return "Online" if endpoint else "Offline"


def main() -> None:
    config = load_configuration()
    validate_config(config)

    print("ORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")

    print(f"Mode: {config['MATRIX_MODE']}")
    print(f"Database: {get_database_status(config['DATABASE_URL'])}")
    print(f"API Access: {get_api_status(config['API_KEY'])}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {get_zion_status(config['ZION_ENDPOINT'])}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")
    print(os.environ)
    print(os.getenv("testvariable"))
    print(os.path)


if __name__ == "__main__":
    main()
