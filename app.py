import time
import os

def clear_screen():
    # Clear command for Windows or Unix systems
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_clock():
    dial = [
        "        12        ",
        "     11    1      ",
        "   10        2    ",
        "  9    GR     3   ",
        "   8         4    ",
        "     7    5       ",
        "        6         ",
    ]
    for line in dial:
        print(line)

def start_clock():
    while True:
        clear_screen()
        print("======= GR CLOCK =======\n")
        draw_clock()
        current_time = time.strftime('%H:%M:%S')
        print(f"\n     Time: {current_time}")
        time.sleep(1)

if __name__ == "__main__":
    start_clock()
