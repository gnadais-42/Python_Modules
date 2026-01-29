print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
storage = "new_discovery.txt"
print("Initializing new storage unit:", storage)
f = open(storage, 'w')
print("Storage unit created successfully...\n")

f.write("[ENTRY 001] New quantum algorithm discovered\n")
f.write("[ENTRY 002] Efficiency increased by 347%\n")
f.write("[ENTRY 003] Archived by Data Archivist trainee\n")
f.close()

f = open(storage, 'r')
print("Inscribing preservation data...")
print(f.read())
f.close()

print("Data inscription complete. Storage unit sealed.")
print(f"Archive \'{storage}\' ready for long-term preservation.")
