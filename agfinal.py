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

keys = [Key("Up"), Key("Down")]


for key in keys:
    # Create a unique endpoint name for each key
    @app.route(f'/{key.name}', methods=['GET'], endpoint=f'key_action_{key.name}')
    def key_action(key=key):  # Use a default argument to capture the current key
        # Simulate pressing the '{key.name}' key
        return jsonify(run_xdotool(f"key {key.name}"))

if __name__ == '__main__':
    app.run(debug=True)

