# 🛡️ Keylogger Simulation & Risk Analysis
### Arc Technology Internship — Task 2

## ⚠️ Ethical Notice
This project is for educational use only on a personal host machine. No real passwords or sensitive data were captured. No data was transmitted outside the machine.

## Overview
Simulated a basic keylogger in Python using `pynput` to understand keystroke logging, then analyzed risks and defensive detection methods.

## Environment
- Windows Host (OS)
- Python 3.x
- pynput library

## What It Does
- Listens to keyboard events in user space.
- Logs each keypress to `keystrokes.log` with timestamps.
- Stops cleanly on ESC.
- No persistence or network transmission.

## Detection & Defense
- **Process Monitoring:** Unusual `python.exe` processes visible in Task Manager or via `tasklist`.
- **File Monitoring:** Unexpected `.log` files created in user directories.
- **Mitigation:** Use standard user accounts, keep AV updated, monitor auto-start entries.

## Skills Demonstrated
- Python scripting with `pynput`
- Threat modeling and risk analysis
- Defensive detection (Process monitoring)

## Disclaimer
All activity was performed on a personal machine. No unauthorized systems were accessed.
