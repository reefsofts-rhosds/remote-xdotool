from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

def run_xdotool(command):
    try:
        subprocess.run(f"xdotool {command}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to execute command: {e}"}
    return {"message": "Command executed successfully"}

@app.route('/playpause', methods=['GET'])
def playpause():
    # Simulate pressing the 'space' key to play/pause the video
    return run_xdotool("key space")

@app.route('/stop', methods=['GET'])
def stop():
    # Simulate pressing the 's' key to stop the video
    return run_xdotool("key s")

@app.route('/next', methods=['GET'])
def next():
    # Simulate pressing the 'Right' arrow key to go to the next video
    return run_xdotool("key Right")

@app.route('/previous', methods=['GET'])
def previous():
    # Simulate pressing the 'Left' arrow key to go to the previous video
    return run_xdotool("key Left")

@app.route('/fullscreen', methods=['GET'])
def fullscreen():
    # Simulate pressing the 'f' key to toggle fullscreen
    return run_xdotool("key f")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

