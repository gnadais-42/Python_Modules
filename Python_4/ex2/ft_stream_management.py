import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

id = input("Input Stream active. Enter archivist ID: ")
report = input("Input Stream active. Enter status report: ")
print()
print("[STANDARD] Archive status from "
      f"{id}: {report}", file=sys.stdout)
print("[ALERT] System diagnostic: "
      "Communication channels verified", file=sys.stderr)
print("[STANDARD] Data transmission complete\n", file=sys.stdout)
print("Three-channel communication test successful.")
