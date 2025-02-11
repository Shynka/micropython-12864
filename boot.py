from machine import Pin, SoftSPI
import time
font = [[0x00,0x00,0x00,0x00,0x00],[0x00,0x00,0x5f,0x00,0x00],[0x00,0x07,0x00,0x07,0x00],[0x14,0x7f,0x14,0x7f,0x14],[0x24,0x2a,0x6b,0x2a,0x12],[0x63,0x13,0x08,0x64,0x63],[0x36,0x49,0x56,0x20,0x50],[0x00,0x00,0x07,0x00,0x00],[0x00,0x3c,0x42,0x81,0x00],[0x00,0x81,0x42,0x3c,0x00],[0x14,0x08,0x3e,0x08,0x14],[0x08,0x08,0x3e,0x08,0x08],[0x00,0x80,0x60,0x00,0x00],[0x08,0x08,0x08,0x08,0x08],[0x00,0x00,0x60,0x00,0x00],[0xc0,0x30,0x0c,0x03,0x00],[0x3e,0x51,0x49,0x45,0x3e],[0x00,0x42,0x7f,0x40,0x00],[0x62,0x51,0x49,0x49,0x46],[0x22,0x41,0x49,0x49,0x36],[0x18,0x14,0x12,0x7f,0x10],[0x27,0x45,0x45,0x45,0x39],[0x3c,0x4a,0x49,0x49,0x30],[0x01,0x71,0x09,0x05,0x03],[0x36,0x49,0x49,0x49,0x36],[0x06,0x49,0x49,0x29,0x1e],[0x00,0x00,0x6c,0x00,0x00],[0x00,0x80,0x6c,0x00,0x00],[0x08,0x14,0x22,0x41,0x00],[0x24,0x24,0x24,0x24,0x24],[0x00,0x41,0x22,0x14,0x08],[0x02,0x01,0x51,0x09,0x06],[0x3e,0x41,0x5d,0x55,0x1e],[0x7c,0x12,0x11,0x12,0x7c],[0x7f,0x49,0x49,0x49,0x36],[0x3e,0x41,0x41,0x41,0x22],[0x7f,0x41,0x41,0x41,0x3e],[0x7f,0x49,0x49,0x49,0x41],[0x7f,0x09,0x09,0x09,0x01],[0x3e,0x41,0x49,0x49,0x7a],[0x7f,0x08,0x08,0x08,0x7f],[0x00,0x41,0x7f,0x41,0x00],[0x20,0x40,0x40,0x40,0x3f],[0x7f,0x08,0x14,0x22,0x41],[0x7f,0x40,0x40,0x40,0x40],[0x7f,0x02,0x0c,0x02,0x7f],[0x7f,0x04,0x08,0x10,0x7f],[0x3e,0x41,0x41,0x41,0x3e],[0x7f,0x09,0x09,0x09,0x06],[0x3e,0x41,0x51,0x21,0x5e],[0x7f,0x09,0x19,0x29,0x46],[0x26,0x49,0x49,0x49,0x32],[0x01,0x01,0x7f,0x01,0x01],[0x3f,0x40,0x40,0x40,0x3f],[0x1f,0x20,0x40,0x20,0x1f],[0x1f,0x60,0x18,0x60,0x1f],[0x63,0x14,0x08,0x14,0x63],[0x03,0x04,0x78,0x04,0x03],[0x61,0x51,0x49,0x45,0x43],[0x00,0xff,0x81,0x81,0x00],[0x03,0x0c,0x30,0xc0,0x00],[0x00,0x81,0x81,0xff,0x00],[0x04,0x02,0x01,0x02,0x04],[0x80,0x80,0x80,0x80,0x80],[0x06,0x09,0x09,0x06,0x00],[0x20,0x54,0x54,0x54,0x78],[0x7f,0x48,0x48,0x48,0x30],[0x38,0x44,0x44,0x44,0x00],[0x30,0x48,0x48,0x48,0x7f],[0x38,0x54,0x54,0x54,0x08],[0x08,0x7e,0x09,0x09,0x00],[0x18,0xa4,0xa4,0xa4,0x7c],[0x7f,0x08,0x08,0x70,0x00],[0x00,0x00,0x7d,0x40,0x00],[0x40,0x80,0x84,0x7d,0x00],[0x7f,0x10,0x28,0x44,0x00],[0x00,0x00,0x7f,0x40,0x00],[0x7c,0x04,0x18,0x04,0x78],[0x7c,0x04,0x04,0x78,0x00],[0x38,0x44,0x44,0x44,0x38],[0xfc,0x24,0x24,0x24,0x18],[0x18,0x24,0x24,0x24,0xfc],[0x7c,0x08,0x04,0x04,0x00],[0x08,0x54,0x54,0x54,0x20],[0x04,0x3e,0x44,0x44,0x00],[0x3c,0x40,0x40,0x20,0x7c],[0x1c,0x20,0x40,0x20,0x1c],[0x3c,0x60,0x30,0x60,0x3c],[0x6c,0x10,0x10,0x6c,0x00],[0x9c,0xa0,0x60,0x3c,0x00],[0x64,0x54,0x54,0x4c,0x00],[0x00,0x08,0x76,0x81,0x81],[0x00,0x00,0xff,0x00,0x00],[0x81,0x81,0x76,0x08,0x00],[0x4c,0x72,0x02,0x72,0x4c],[0x55,0x2a,0x55,0x2a,0x55]]
font_size = [[0,2],[2,1],[1,3],[0,5],[0,5],[0,5],[0,5],[2,1],[1,3],[1,3],[0,5],[0,5],[1,2],[0,5],[2,1],[0,4],[0,5],[1,3],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[2,1],[1,2],[0,4],[0,5],[1,4],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[1,3],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[0,5],[1,3],[0,4],[1,3],[0,5],[0,5],[0,4],[0,5],[0,5],[0,4],[0,5],[0,5],[0,4],[0,5],[0,4],[2,2],[0,4],[0,4],[2,2],[0,5],[0,4],[0,5],[0,5],[0,5],[0,4],[0,5],[0,4],[0,5],[0,5],[0,5],[0,4],[0,4],[0,4],[1,4],[2,1],[0,4],[0,5],[0,5]]
# Pin definitions for software SPI
clock = Pin(16)    # Clock pin
data = Pin(17)     # Data (MOSI) pin
cs = Pin(18)       # Chip Select pin
reset = Pin(19)    # Reset pin
miso = Pin(15)     # Placeholder MISO pin (not used)

# Initialize software SPI
spi = SoftSPI(baudrate=1000000, polarity=0, phase=0, sck=clock, mosi=data, miso=miso)

# Initialize pins
cs.init(Pin.OUT, value=1)
reset.init(Pin.OUT, value=1)

def reset_display():
    reset.value(0)
    time.sleep_ms(10)
    reset.value(1)
    time.sleep_ms(10)

reset_display()

def send_command(command):
    cs.value(0)
    spi.write(bytearray([0xF8, (command & 0xF0), ((command << 4) & 0xF0)]))
    cs.value(1)

def send_data(data):
    cs.value(0)
    spi.write(bytearray([0xFA, (data & 0xF0), ((data << 4) & 0xF0)]))
    cs.value(1)

def initialize_display():
    send_command(0x30)
    time.sleep_ms(1)
    send_command(0x30)
    time.sleep_ms(1)
    send_command(0x0C)
    time.sleep_ms(1)
    send_command(0x01)
    time.sleep_ms(2)
    send_command(0x36)

initialize_display()

def clear_screen():
    # Iterate over all rows (0 to 63 for a 64-pixel height)
    for y in range(64):
        # Set Y address for each row
        if y < 32:
            y_address = 0x80 | y  # Y address for top half
            x_offset = 0x80
        else:
            y_address = 0x80 | (y - 32)  # Y address for bottom half
            x_offset = 0x88
        send_command(y_address)  # Set the Y address
        # Set X address and clear each byte in the row
        send_command(x_offset)
        for x in range(16):  # 16 bytes per row for a 128-pixel width (128 / 8 = 16)
            send_data(0x00)  # Send 0x00 to clear 8 pixels at a time

clear_screen()
def draw_point(x, y):
    if 0 <= x < 128 and 0 <= y < 64:  # Ensure x is under 128 and y is under 64
        byte_column = x // 8
        bit_position = 7 - (x % 8)  # Always use left-to-right bit order
        display_buffer[y][byte_column] |= (1 << bit_position)

    
display_buffer = [[0x00] * 16 for _ in range(64)]
def flush_display():
    # Iterate over the buffer and send each byte to the display
    for y in range(64):
        # Set the Y address (top half or bottom half of the screen)
        if y < 32:
            send_command(0x80 | y)  # Y address for top half
            x_offset = 0x80
        else:
            send_command(0x80 | (y - 32))  # Y address for bottom half
            x_offset = 0x88
        # Set the X address and send each byte in the row
        send_command(x_offset)
        for byte in display_buffer[y]:
            send_data(byte)
    # Clear the display buffer by setting each byte to 0
    for row in display_buffer:
        for i in range(len(row)):
            row[i] = 0x00

def draw_line(x0, y0, x1, y1):
    # Bresenham's line algorithm
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        draw_point(x0, y0)  # Draw each point on the line
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

def custom_ascii_code(char):
    if ' ' <= char <= '~':  # Space (32) to tilde (126) in ASCII
        return ord(char) - ord(' ')
def draw_text(text, x, y):
    for char in text:
        code = custom_ascii_code(char)
        if ord(char) ==10:
            x =0
            y+=8
            continue
        if x <= 123:
            draw_symbol(font[code], x - font_size[code][0], y)
            x += font_size[code][1] + 1
def draw_symbol(pattern,x,y):
    for col, byte in enumerate(pattern):
        for row in range(8):  # Each byte has 8 bits
            # Check if the specific bit is set (1) in the byte
            if byte & (1 << row):
                # Draw the point, adjusting y to render right-side up
                draw_point(x + col, y + row)

draw_text("loading...",0,0)
flush_display()
