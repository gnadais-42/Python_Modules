import sys


def main() -> None:
    arguments: list = sys.argv
    length: int = len(arguments)
    print("=== Command Quest ===")
    if length == 1:
        print("No arguments provided!")
    print(f"Program name: {arguments[0]}")
    if length > 1:
        print(f"Arguments received: {length - 1}")
        for i in range(1, length):
            print(f"Argument {i}: {arguments[i]}")
    print(f"Total arguments: {length}")


if __name__ == "__main__":
    main()
