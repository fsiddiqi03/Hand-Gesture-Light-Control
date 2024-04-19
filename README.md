# Hand Gesture Light Control

This project utilizes Google's MediaPipe hand tracking model to control Philips HUE smart lights via hand gestures. Users can adjust brightness by changing the distance between their index finger and thumb, turn the lights on by showing an open hand, and turn them off by making a fist. The system calculates the brightness level based on the distance between the index and thumb using the distance formula.

## Description

The application integrates real-time hand gesture recognition with a network-enabled lighting system. It's designed to run on a local machine with a webcam, processing video input to detect hand gestures which then translate into control commands for the lights. The project showcases the practical use of computer vision and IoT control in a home automation scenario.

## Setup

### Requirements

- Python 3.8 or newer
- MediaPipe
- OpenCV
- Requests library

### Installation

Install the required Python libraries:

```bash
pip install mediapipe opencv-python requests
```

### Obtaining HUE bridge ip:

Refer to HUE api documentation to get your bridge IP and Light ID
Use HUE API v2
[HUE API Doc](https://developers.meethue.com/develop/hue-api-v2/)

Running the Application
To run the application, you need to set up the configuration file `config.py` with your Philips HUE bridge IP, light ID, and username (API key). Here’s a template for `config.py`:

```python
BRIDGE_IP = 'your_bridge_ip'
LIGHT_ID = 'your_light_id'
USERNAME = 'your_username'
```

To Run: 
```bash
python main.py
```
