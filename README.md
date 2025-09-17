# IP-Scope-Manager

The IP Scope Manager is a command-line utility designed to help cybersecurity professionals manage IP address scopes efficiently. It allows users to add or remove IP ranges from a working set, validates input using Python’s ipaddress module, and provides clear feedback on invalid entries and operation results.
Key Features:
- Validates and normalizes IP ranges using ipaddress.ip_network()
- Supports dynamic addition and removal of IP ranges
- Tracks duplicates and missing entries for transparency
- Summarizes changes and displays the updated scope
- Looping interface for continuous use

Ideal for vulnerability management workflows, especially when defining or refining scan scopes. This script helps ensure clean, validated input and reduces human error when managing large sets of IPs.

