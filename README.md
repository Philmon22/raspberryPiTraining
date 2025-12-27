# LED Toggle Script

A Python script that toggles an LED on pin 8 every second for 5 seconds.

## Requirements

- Python 3.x
- Raspberry Pi with GPIO support
- RPi.GPIO library

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install RPi.GPIO==0.7.0
```

## Usage

Run the script with sudo (GPIO access requires root privileges):

```bash
sudo python led_toggle.py
```

## How it works

1. Sets up GPIO pin 8 as an output (BOARD mode)
2. Toggles the LED ON/OFF every second
3. Runs for 5 complete cycles (10 seconds total: 5 seconds ON, 5 seconds OFF)
4. Cleans up GPIO resources on completion

## Hardware Connection

Connect your LED to:
- **GPIO Pin 8** (as configured)
- Include a current-limiting resistor (~220Ω for standard LED)
- Connect to ground

## Notes

- Requires root/sudo privileges to access GPIO
- Use BOARD pin numbering (physical pin numbers)
