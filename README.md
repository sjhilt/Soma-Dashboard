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
   git clone https://github.com/yourusername/smart-blinds-controller.git
   cd smart-blinds-controller
