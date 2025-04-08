import tkinter as tk
import time
import math

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)  # Update every second

def draw_dial():
    canvas.create_oval(50, 50, 250, 250, width=2, outline='black')  # Outer circle

    # Draw hour numbers
    for i in range(12):
        angle_deg = i * 30
        angle_rad = math.radians(angle_deg)
        x = 150 + 80 * math.sin(angle_rad)
        y = 150 - 80 * math.cos(angle_rad)
        canvas.create_text(x, y, text=str(i+1), font=('Helvetica', 12, 'bold'))

    # Add 'GR' label at the center
    canvas.create_text(150, 150, text='GR', font=('Helvetica', 16, 'bold'), fill='darkblue')

# Create main window
window = tk.Tk()
window.title("GR Clock")

# Digital clock label
clock_label = tk.Label(window, text="", font=('Helvetica', 36), bg='black', fg='white')
clock_label.pack(pady=10)

# Clock dial canvas
canvas = tk.Canvas(window, width=300, height=300, bg='white', highlightthickness=0)
canvas.pack()

draw_dial()
update_clock()

window.mainloop()
