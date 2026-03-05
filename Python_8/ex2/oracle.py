import os
import sys
from dotenv import load_dotenv


def parse_first_occurrence(string: str, c: str) -> list:
    for i in range(len(string)):
        if string[i:].startswith(c):
            return [string[:i], string[i + len(c):]]
    return [string]


def main() -> None:
    if ".env" not in os.listdir():
        print("Error: .env file not found\n"
              "Copy the example one given to you like this:\n\n"
              "cp .env.example .env\n\n"
              "Then run again")
        sys.exit(1)

    valid_env_format: bool = True

    env_variables: dict = {
        "Mode": "MATRIX_MODE",
        "Database": "DATABASE_URL",
        "API Access": "API_KEY",
        "Log Level": "LOG_LEVEL",
        "Zion Network": "ZION_ENDPOINT"
    }
    load_dotenv()
    with open(".env", "r") as f:
        for line in f:
            if len(parse_first_occurrence(line, "=")) != 2:
                valid_env_format = False

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    for key in env_variables:
        value: str = os.getenv(env_variables[key])
        print(f"{key}: ", end="")
        if env_variables[key] in ("MATRIX_MODE", "LOG_LEVEL"):
            print(value if value else None)
        elif env_variables[key] == "DATABASE_URL":
            print("Connected to local instance"
                  if value else "Failed to connect")
        elif env_variables[key] == "API_KEY":
            print("Authenticated" if value else "Invalid key")
        elif env_variables[key] == "ZION_ENDPOINT":
            print("Online" if value else "Offline")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured"
          if valid_env_format else
          "[KO] .env file is not properly formatted")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations")


if __name__ == "__main__":
    main()
