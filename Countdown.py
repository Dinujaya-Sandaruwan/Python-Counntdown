import tkinter as tk
import time

# Create a window
window = tk.Tk()

# Set window size
window.geometry("700x150")
window.attributes('-topmost', True)

# Make window not resizable
# window.resizable(0, 0)
window.resizable(True, True)

# Set window background
window.configure(background='black')

# Set window always on top
window.attributes('-topmost', True)

# Hide default minimize, maximize and close buttons
window.overrideredirect(True)

# Create a count down label
label = tk.Label(window, font=('Helvetica', 20), fg='white', bg='black')
label.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Create a close button
close_button = tk.Button(window, text='Close', font=('Helvetica', 12), bg='red', fg='white', width=10, command=window.destroy)
close_button.pack(pady=20)

# Set window move using mouse pointer
window.bind('<Button-1>', lambda event: window.focus_set())
window.bind('<B1-Motion>', lambda event: window.geometry('+{0}+{1}'.format(event.x_root, event.y_root)))

# Function to calculate time
def countdown(end_time):
    seconds = end_time - int(time.time())
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    # Format the output
    output = f"{days} Days, {hours:02d} Hours, {minutes:02d} Minutes and {seconds:02d} Seconds"
    # Show the output
    label.configure(text=output)
    # Re-run the function every second
    window.after(1000, countdown, end_time)

# Set the end time
end_time = int(time.mktime(time.strptime("22/01/2023", "%d/%m/%Y")))

# Run the function
countdown(end_time)

# Run the window
window.mainloop()