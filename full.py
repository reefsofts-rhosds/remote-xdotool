from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

def run_xdotool(command):
    try:
        subprocess.run(f"xdotool {command}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to execute command: {e}"}
    return {"message": "Command executed successfully"}

class Key:
    def __init__(self, name):
        self.name = name

keys = [
    Key("0"), Key("1"), Key("2"), Key("3"), Key("4"),
    Key("5"), Key("6"), Key("7"), Key("8"), Key("9"),
    Key("A"), Key("B"), Key("C"), Key("D"), Key("E"),
    Key("F"), Key("G"), Key("H"), Key("I"), Key("J"),
    Key("K"), Key("L"), Key("M"), Key("N"), Key("O"),
    Key("P"), Key("Q"), Key("R"), Key("S"), Key("T"),
    Key("U"), Key("V"), Key("W"), Key("X"), Key("Y"),
    Key("Z"),
    Key("F1"), Key("F2"), Key("F3"), Key("F4"), Key("F5"),
    Key("F6"), Key("F7"), Key("F8"), Key("F9"), Key("F10"),
    Key("F11"), Key("F12"),
    Key("Shift"), Key("Control"), Key("Ctrl"), Key("Alt"),
    Key("AltGr"), Key("Meta"), Key("Windows"), Key("Caps Lock"),
    Key("Num Lock"), Key("Scroll Lock"),
    Key("Arrow Up"), Key("Arrow Down"), Key("Arrow Left"),
    Key("Arrow Right"), Key("Home"), Key("End"),
    Key("Page Up"), Key("Page Down"), Key("Insert"),
    Key("Delete"), Key("Space"), Key("Enter"), Key("Tab"),
    Key("Backspace"), Key("Escape"), Key("Esc"),
    Key("Print Screen"), Key("Pause"), Key("Break"),
    Key("Numpad 0"), Key("Numpad 1"), Key("Numpad 2"),
    Key("Numpad 3"), Key("Numpad 4"), Key("Numpad 5"),
    Key("Numpad 6"), Key("Numpad 7"), Key("Numpad 8"),
    Key("Numpad 9"), Key("Numpad +"), Key("Numpad -"),
    Key("Numpad *"), Key("Numpad /"), Key("Numpad ."),
    Key("Application"), Key("Volume Up"), Key("Volume Down"),
    Key("Mute"), Key("Media Play/Pause"), Key("Media Stop"),
    Key("Media Next"), Key("Media Previous")
]


for key in keys:
    # Create a unique endpoint name for each key
    @app.route(f'/{key.name}', methods=['GET'], endpoint=f'key_action_{key.name}')
    def key_action(key=key):  # Use a default argument to capture the current key
        # Simulate pressing the '{key.name}' key
        return jsonify(run_xdotool(f"key {key.name}"))

if __name__ == '__main__':
    app.run(debug=True)

