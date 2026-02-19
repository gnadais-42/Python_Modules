import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    id: str = input("Input Stream active. Enter archivist ID: ")
    report: str = input("Input Stream active. Enter status report: ")
    print()
    print("[STANDARD] Archive status from "
          f"{id}: {report}", file=sys.stdout)
    print("[ALERT] System diagnostic: "
          "Communication channels verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete\n", file=sys.stdout)
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
