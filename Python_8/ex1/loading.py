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
              "install them manually like:")
        print("python3 -m pip install ", end="")
        for package in missing:
            print(package + " ", end="")
        print("\n\n Or you can install everything in requirements.txt like:")
        print("python3 -m pip install -r requirements.txt")

        

if __name__ == "__main__":
    main()