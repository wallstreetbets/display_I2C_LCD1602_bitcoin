# Raspberry Pi BTC Price Display

A Python-based project that uses Binance's WebSocket API to fetch real-time Bitcoin (BTC/USDT) prices and display them on an LCD screen connected to a Raspberry Pi. This project leverages the Binance API, LCD1602 library, and Raspberry Pi hardware for a live cryptocurrency price tracker.

---

# Raspberry Pi BTC Price Display

Here’s a snapshot of the project in action:

<img src="https://github.com/wallstreetbets/display_I2C_LCD1602_bitcoin/blob/master/20180108_132036.jpg" alt="Alt text" width="500"/>


## Features
- **Real-time Price Updates:** Fetches live BTC/USDT prices using Binance's WebSocket API.
- **LCD Display Integration:** Displays the price and timestamp on a 16x2 LCD screen.
- **Lightweight and Efficient:** Optimized for continuous streaming and display updates.
- **User-Friendly Setup:** Minimal setup with Raspberry Pi and Python libraries.

---

## Prerequisites

### Hardware Requirements
- Raspberry Pi (any model with I2C support)
- LCD1602 Display Module with I2C interface
- I2C Connection (wires and breadboard if necessary)

### Software Requirements
- Python 3.x
- Required Python Libraries:
  - `python-binance`
  - `LCD1602`
  - `datetime`

---

## Setup and Installation

### Step 1: Clone the Repository

git clone https://github.com/yourusername/raspberry-pi-btc-display.git
cd raspberry-pi-btc-display

### Step 2: Set Up Environment

python3 -m venv env

source env/bin/activate

pip install python-binance

### Step 3: Configure Binance API Keys
- Create an account on Binance.
- Generate your API keys (Public and Private).
- Store the keys in a .env file in the project directory:

  BINANCE_PUBLIC_API_KEY=your_public_key
  BINANCE_PRIVATE_API_KEY=your_private_key

### Step 4: Enable I2C on Raspberry Pi
Enable the I2C interface:

- Run sudo raspi-config.
- Navigate to Interfacing Options > I2C and enable it.
- Reboot your Raspberry Pi.

### Usage
Running the Application
1. Connect the LCD1602 module to the Raspberry Pi using I2C.

2. Start the application:
python3 app.py

3. The LCD will display the current BTC price and timestamp.

Stopping the Application
Press Ctrl + C to stop the application safely.

### Project Structure

├── app.py            # Main application file

├── README.md         # Documentation

├── .env              # API keys (not included in the repository)

└── requirements.txt  # Python dependencies


###  Troubleshooting
Common Issues
LCD Not Displaying Properly:

Ensure correct wiring and I2C address configuration.
Verify that the LCD is initialized in the app.py file with the correct address.
WebSocket Errors:

Check your Binance API key permissions.
Verify internet connectivity.
Dependency Errors:

Run pip install -r requirements.txt to install missing dependencies.
License
This project is licensed under the MIT License.

Acknowledgments
Binance API: For providing real-time cryptocurrency data.
LCD1602 Library: For Raspberry Pi and I2C LCD integration.

### Author
Python Legion Soft | Developer & Technology Enthusiast
