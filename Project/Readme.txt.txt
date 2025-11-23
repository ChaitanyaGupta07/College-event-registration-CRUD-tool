This is a simple in-memory Python script designed for managing events and registrations through a command-line menu interface.

### Functionality Summary

The script uses two core Python lists: `events` (for event names) and `regs` (for registration records).

| Option | Action | Details |
| :---: |  :--- |     :--- |
| **1** | Add Event | Appends the event name to the `events` list. |
| **2** | Show Events | Displays all current events with their corresponding numerical index. |
| **3** | Delete Event | Removes an event based on the user-provided index. |
| **4** | Register | Takes a user's name and an event index. It creates a record formatted as "Name - Event Name" and adds it to the `regs` list. |
| **5** | Show Regs | Displays all recorded registrations with their index. |
| **6** | Delete Reg | Removes a registration based on the user-provided index. |
| **0** | Exit | Terminates the program loop. |

### Technical Note

The entire application runs in a `while True` loop and uses simple index-based logic (`enumerate`) for displaying and managing list items. Input validation is included to check if indices are numeric and within the list boundaries.

### Important Limitation

This is an **in-memory** script. All data (events and registrations) is **lost** when the program is closed or stopped.

To run: Save the code as a Python file (e.g., `manager.py`) and execute using `python manager.py` in your terminal.