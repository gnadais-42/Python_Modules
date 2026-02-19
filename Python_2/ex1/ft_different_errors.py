def garden_operations() -> None:
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError...")
        1 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    try:
        print("Testing FileNotFoundError...")
        c: str = "missing.txt"
        open(c, "r")
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{c}'\n")
    try:
        print("Testing KeyError...")
        e: dict = {"example key": "example value"}
        f: str = "missing_plant"
        e[f]
    except KeyError:
        print(f"Caught KeyError: '{f}'\n")
    try:
        print("Testing multiple errors together...")
        int("abc")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
