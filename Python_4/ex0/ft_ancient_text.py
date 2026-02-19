def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    vault: str = "ancient_fragment.txt"
    print("Accessing Storage vault:", vault)
    try:
        f = open(vault, 'r')
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    else:
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(f.read())
        print()
        f.close()
        print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
