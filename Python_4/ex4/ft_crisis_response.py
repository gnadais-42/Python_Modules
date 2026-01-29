def open_and_read(archive, mode):
    if mode == "crisis":
        print("CRISIS ALERT: ", end="")
    elif mode == "routine":
        print("ROUTINE ACCESS: ", end="")
    else:
        print("Invalid mode", mode)
        print("Usage: open_and_read(archive, mode), "
              "mode is \'crisis\' or \'routine\'")
        return
    print(f"Attempting access to \'{archive}\'...")
    try:
        with open(archive, 'r') as f:
            print(f"SUCCESS: Archive recovered - ``{f.read()}\'\'")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as e:
        print("ERROR:", e)


print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
open_and_read("lost_archive.txt", "crisis")
open_and_read("classified_vault.txt", "crisis")
open_and_read("standard_archive.txt", "routine")
print("All crisis scenarios handles successfully. Archives secure.")
