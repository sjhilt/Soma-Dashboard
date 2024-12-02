from flask import Flask, render_template, jsonify, request
import requests
import logging

# Flask application instance
app = Flask(__name__)

# Replace with the IP address of your SOMA Connect device
DEVICE_IP = "192.168.0.123"
BASE_URL = f"http://{DEVICE_IP}:3000"

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def list_devices():
    """
    Fetch a list of all devices connected to the SOMA Connect.

    Returns:
        dict: A dictionary containing the device list or an error message.
    """
    try:
        url = f"{BASE_URL}/list_devices"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logging.debug(f"Devices API response: {data}")
        return data
    except requests.RequestException as e:
        logging.error(f"Failed to fetch devices: {e}")
        return {"error": str(e)}

def get_shade_state(mac):
    """
    Get the current state (position and close direction) of a specific shade.

    Args:
        mac (str): The MAC address of the shade.

    Returns:
        dict: A dictionary containing the shade state or an error message.
    """
    try:
        url = f"{BASE_URL}/get_shade_state?mac={mac}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logging.debug(f"Current State API response for {mac}: {data}")
        return data
    except requests.RequestException as e:
        logging.error(f"Failed to fetch current state for {mac}: {e}")
        return {"error": str(e)}

def get_battery_level(mac):
    """
    Get the battery level and percentage of a specific shade.

    Args:
        mac (str): The MAC address of the shade.

    Returns:
        dict: A dictionary containing the battery level or an error message.
    """
    try:
        url = f"{BASE_URL}/get_battery_level?mac={mac}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logging.debug(f"Battery Level API response for {mac}: {data}")
        return data
    except requests.RequestException as e:
        logging.error(f"Failed to fetch battery level for {mac}: {e}")
        return {"error": str(e)}

def control_shade(mac, action, position=None):
    """
    Send a command to control the shade (open, close, stop, or set position).

    Args:
        mac (str): The MAC address of the shade.
        action (str): The action to perform ('open', 'close', 'stop', 'set_position').
        position (int, optional): The position to set the shade to (0-100).

    Returns:
        dict: A dictionary containing the result of the command or an error message.
    """
    try:
        if action == "set_position" and position is not None:
            url = f"{BASE_URL}/set_shade_position?mac={mac}&pos={position}"
        elif action in ["open", "close", "stop"]:
            url = f"{BASE_URL}/{action}_shade?mac={mac}"
        else:
            return {"error": "Invalid action or missing position"}
        
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logging.debug(f"Control Shade API response for {mac} with action '{action}': {data}")
        return data
    except requests.RequestException as e:
        logging.error(f"Failed to execute '{action}' action for {mac}: {e}")
        return {"error": str(e)}

@app.route("/")
def home():
    """
    The main route that displays the dashboard with shades and their statuses.

    Returns:
        str: Rendered HTML template with the list of shades and their details.
    """
    devices = list_devices()
    if "error" in devices:
        return render_template("error.html", error=devices["error"])

    shades_info = []
    for device in devices.get("shades", []):
        mac = device.get("mac", "Unknown")
        shade_state = get_shade_state(mac)
        battery_info = get_battery_level(mac)

        # Determine the state based on the position
        position = shade_state.get("position", "Unknown")
        state = "Closed" if position == 100 else "Open"

        shades_info.append({
            "name": device.get("name", "Unknown"),
            "mac": mac,
            "state": state,  # "Closed" or "Open" based on position
            "battery_percentage": battery_info.get("battery_percentage", "Unknown"),
        })

    return render_template("index.html", shades=shades_info)

@app.route("/control", methods=["POST"])
def control():
    """
    API route to handle control commands for shades (open, close, stop, set position).

    Returns:
        Response: JSON response with the result of the action or an error message.
    """
    data = request.json
    mac = data.get("mac")
    action = data.get("action")
    position = data.get("position", None)

    if not mac or not action:
        return jsonify({"error": "Missing MAC address or action"}), 400

    result = control_shade(mac, action, position)
    return jsonify(result)

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)