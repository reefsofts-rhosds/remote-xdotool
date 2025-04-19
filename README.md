# Remote XDoTool
Ever wanted something overcomplicated to control your computer remotely? Remote XDoTool is here to help! It is basically an easy way to create an API, for XDoTool, with Python and Flask.
### Requirements
- Python 3.5 or more
- Flask
- Suprocess

### Use the complete Flaskapp
To use the complete Flaskapp, simply type
```
 python3 full.py
```
in a terminal.

Then, try cURLing http://computer.ip.adress.123:5000/key_ID, where computer.ip.adress.123 is the IP adress of the host and key_ID is the xdotool key ID. Here you go!

### Some examples of config
In the repo, the presentation.py file is an example of how you might use this to remotely control a presentation (here it was created by me to control a lesson i gave with a pi and a Stream Deck)
### Make your own config
#### First method: Create your own Flask app
To make your own config, take a blank python file and copy-paste the following inside:

```python
from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

def run_xdotool(command):
    try:
        subprocess.run(f"xdotool {command}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to execute command: {e}"}
    return {"message": "Command executed successfully"}
```
Then, you can add Keypoints (keypress API endpoints), following this template:
```python
@app.route('/your_route', methods=['GET'])
def your_route():
    # Maybe a short description?
    return run_xdotool("key Key_ID")
```
where 'your_route' is the endpoint you wish to call to press the 'Key_ID' key. If you want to, replace Maybe a short description? with a short one-line description.

At the very end of the file, add these lines of code:
```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```
##### Run your Flask App and use it
To run the program, simply type
```
python3 file.py
```
in a terminal, where file.py is your config file.

Then, try cURLing http://computer.ip.adress.123:5000/your_route, where computer.ip.adress.123 is the IP adress of the host and your_route is the keypoint. Here you go!
#### Second method: use the auto-generating Flask app
This is a bit simpler, because you will only have to fill a list. In the agfinal.py file, locate this line:
```python
keys = [Key("Up"), Key("Down")]
```
If you want to add anything, add a comma at 'Key("Down")' to indicate Python to add something.
To add a Keypoint (keypress API endpoints), simply add 'Key("key_id"),' where key_id is the Key ID for standard xdotool. For a final element, do not forget to remove the comma. 
##### Run the Auto-generating Flask app and use it
To run the auto-generating Flask app, simply type
```
python3 agfinal.py
```
in a terminal.

Then, try cURLing http://computer.ip.adress.123:5000/key_ID, where computer.ip.adress.123 is the IP adress of the host and key_ID is the xdotool key ID. Here you go!

