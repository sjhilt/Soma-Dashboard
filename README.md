# Smart Blinds Controller

A Flask-based web application to control and monitor SOMA smart blinds via the SOMA Connect HTTP API. This application provides a dashboard to view the current state of blinds, battery levels, and allows users to open, close, stop, or set specific positions for the blinds.

---

## Features
- **Dashboard**: Displays all connected blinds with their name, MAC address, state (Open/Closed), and battery percentage.
- **Controls**: Provides buttons to:
  - Open blinds
  - Close blinds
  - Stop blinds immediately
  - Set blinds to a specific position (0–100)
- **Real-time Updates**: Fetches the latest status of blinds and logs API interactions in the console.

---

## Installation

### Prerequisites
- Python 3.7+
- SOMA Connect device on the same network as the application
- Flask and other required Python libraries (see below)

### Steps
1. **Clone the repository**:
  ```bash
   git clone https://github.com/sjhilt/soma-dashboard.git
   cd soma-dashboard
   ```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```


3. **Configure the IP address**:
- Open app.py.
- Replace 192.168.0.123 with the IP address of your SOMA Connect device:

``` config 
DEVICE_IP = "172.18.32.54"
```
4. **Run the application**:

```bash 
python -m app
```


5. **Access the application:
- Open a browser and navigate to http://127.0.0.1:5000/.

## Usage

### Dashboard Overview

Name: The name of the shade as set in the SOMA app.
- MAC Address: Unique hardware identifier for the shade.
- State: Indicates if the shade is “Open” (position ≠ 100) or “Closed” (position = 100).
- Battery Percentage: Displays the current battery level of the shade.

### Controls

1.	**Open: Fully opens the shade.**
2.	**Close: Fully closes the shade.**
3.	**Stop: Stops the shade movement immediately.**
4.	**Set Position: Allows setting a custom position between 0 (fully closed) and 100 (fully open).**

## API Reference

- The application interacts with the SOMA Connect device using the following endpoints:

|Endpoint | Description |
| --- | -- | 
|/list_devices | Fetches a list of all shades detected by the SOMA Connect.|
|/get_shade_state?mac=<MAC>	| Retrieves the current state of a shade, including its position and direction.|
|/get_battery_level?mac=<MAC>	| Fetches the battery level and percentage for the given shade.|
|/set_shade_position?mac=<MAC>	| Moves the shade to a specific position (0–100).|
|/open_shade?mac=<MAC>	| Fully opens the shade.|
|/close_shade?mac=<MAC>	| Fully closes the shade.|
|/stop_shade?mac=<MAC>	| Stops the shade immediately.|




## Requirements

- Flask
- Requests

## Install dependencies with:

``` bash
pip install -r requirements.txt
```

## Contributions

- Contributions are welcome! Feel free to fork the repository, make improvements, and open a pull request.

## License

This project is licensed under the MIT License.

## Troubleshooting
- Issue: Blinds not appearing on the dashboard.
- Solution: Check the SOMA Connect device IP address and ensure it’s reachable on your network.
- Issue: Buttons not working.
- Solution: Check the console logs for API errors or inspect the network requests in your browser’s developer tools.

