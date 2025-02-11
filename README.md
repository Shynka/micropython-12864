# MicroPython Display Driver with Software SPI

This script initializes and controls a monochrome display using software SPI on a MicroPython-compatible board.

## Dependencies
- `machine` module (for Pin and SPI)
- `time` module

## Font Data
A predefined font set is stored as a list of byte patterns to represent ASCII characters.

## Pin Configuration
- **Clock (SCK):** GPIO 16
- **Data (MOSI):** GPIO 17
- **Chip Select (CS):** GPIO 18
- **Reset:** GPIO 19
- **MISO (not used):** GPIO 15

## SPI Initialization
Software SPI is initialized with:
```python
spi = SoftSPI(baudrate=1000000, polarity=0, phase=0, sck=clock, mosi=data, miso=miso)
```
Most of this script was made using Chat-GPT so probly most of it is copied from somewhere else
