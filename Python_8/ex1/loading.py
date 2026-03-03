from importlib import import_module


def main() -> None:
    required: list = [
        "numpy",
        "pandas",
        "matplotlib",
        "requests"
    ]

    missing: list = []
    for package in required:
        try:
            import_module(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print("Missing dependencies:", missing, end="\n\n")
        print("To install these dependencies you can "
              "install them manually using pip like:")
        print("python3 -m pip install ", end="")
        for package in missing:
            print(package + " ", end="")
        print("\n\nOr you can install everything in requirements.txt like:")
        print("python3 -m pip install -r requirements.txt\n")
        print("To install them using poetry you can do:\n"
              "poetry init\n"
              "Then follow the instructions or:\n"
              "poetry add ", end="")
        for package in missing:
            print(package + " ", end="")
        print("\nThen run it with:\n"
              "poetry run python3 loading.py\n")
        print("If you already have a valid pyproject.toml file you can just run it with poetry")
        print("Just make sure you're in a safe environment!")
        

        

if __name__ == "__main__":
    main()