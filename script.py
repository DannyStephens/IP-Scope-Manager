import ipaddress

def get_ip_ranges(prompt):
    ranges = input(f"{prompt} (space-separated IP ranges): ").split()
    valid_ranges = []
    for r in ranges:
        try:
            net = ipaddress.ip_network(r, strict=False)
            valid_ranges.append(str(net))
        except ValueError:
            print("=== INVALID IP FOUND ===")
            print(f"Invalid IP skipped: {r}")
    return valid_ranges

def main():
    print("\n=== IP Scope Manager ===")

    scope = get_ip_ranges("Enter the current IP scope")
    scope_set = set(scope)

    while True:
        action = input("Do you want to ADD or REMOVE IP ranges? (add/remove): ").strip().lower()
        if action in ['add', 'remove']:
            break
        else:
            print(" Invalid input. Please enter 'add' or 'remove'.")

    new_ranges = get_ip_ranges(f"Enter the IP ranges to {action}")

    already_present = []
    not_found = []
    added = []
    removed = []

    if action == 'add':
        for r in new_ranges:
            if r in scope_set:
                already_present.append(r)
            else:
                scope_set.add(r)
                added.append(r)
    elif action == 'remove':
        for r in new_ranges:
            if r in scope_set:
                scope_set.remove(r)
                removed.append(r)
            else:
                not_found.append(r)

    print("\n=== Operation Summary ===")
    if action == 'add':
        print(f"Added {len(added)} new IP ranges.")
        if already_present:
            print(f"{len(already_present)} ranges were already in the scope:")
            for r in already_present:
                print(f" - {r}")
    elif action == 'remove':
        print(f"Removed {len(removed)} IP ranges.")
        for r in removed:
            print(f" - {r}")
        if not_found:
            print(f"{len(not_found)} ranges were not found in the scope:")
            for r in not_found:
                print(f" - {r}")

    print("\n=== Updated Scope ===")
    print(f"The current scope has {len(scope_set)} targets")
    for r in sorted(scope_set):
        print(r)

if __name__ == "__main__":
  looping=1
  while looping==1:
        main()