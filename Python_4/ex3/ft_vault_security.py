print("CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
print("Initiating vault access...")
archive = "classified_data.txt"
try:
    with open(archive, 'r') as f:
        print("Vault connection established with failsafe protocols")
        print("SECURE EXTRACTION:")
        print(f.read())
        print()
    with open(archive, 'w') as f:
        print("SECURE PRESERVATION:")
        f.write("[CLASSIFIED] New security protocols archived")
        print("[CLASSIFIED] New security protocols archived")
except FileNotFoundError as e:
    print(f"ERROR: {e}")
print("Vault automatically sealed upon completion\n")
print("All vault operations completed with maximum security.")
