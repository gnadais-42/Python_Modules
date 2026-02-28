import sys
import site
import os


def print_instructions() -> None:
    if os.name == "nt":
        print("Windows detected\n"
              "To enter the construct, run:\n"
              "python -m venv env_name\n"
              "env_name\\Scripts\\activate\n")
    else:
        print("Linux/MacOS detected\n"
              "To enter the construct, run:\n"
              "python3 -m venv env_name\n"
              "source env_name/bin/activate\n")
    print("Then run this program again")


def success_message() -> None:
    print("SUCCESS: You're in an isolated environment!\n"
          "Safe to install packages without affecting\n"
          "the global system\n")
    print("Package installation path:",
          site.getusersitepackages(),
          sep="\n")


def main() -> None:
    in_venv: bool = False
    venv_name: str | None = None
    venv_path: str | None = None

    print("MATRIX STATUS: ", end="")
    if sys.base_prefix != sys.prefix:
        print("Welcome to the construct\n")
        in_venv = True
        venv_path = sys.prefix
        venv_name = os.path.basename(venv_path)
    else:
        print("You're still plugged in!")
    print("Current Python:", sys.executable)
    print("Virtual Environment:", venv_name)
    if in_venv:
        print("Environment Path:", venv_path)
    print()
    success_message() if in_venv else print_instructions()


if __name__ == "__main__":
    main()
