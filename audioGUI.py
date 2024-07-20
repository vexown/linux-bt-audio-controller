import tkinter as tk
import subprocess

def set_volume(volume):
    """Set system volume to the given level (0-100)."""
    subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{volume}%"])

def send_command(command):
    """Send a command to the media player script."""
    subprocess.run(["./btDriver", command])

def create_gui():
    root = tk.Tk()
    root.geometry("1024x600")  # Set the window size to 1024x600

    # Configure the grid layout
    root.grid_rowconfigure(0, weight=1)  # Row for empty space above the volume slider
    root.grid_rowconfigure(1, weight=1)  # Row for volume slider
    root.grid_rowconfigure(2, weight=0)  # Row for control buttons
    root.grid_rowconfigure(3, weight=0)  # Row for close button
    root.grid_columnconfigure(0, weight=1)  # Column will expand horizontally

    # Frame for volume slider, centered in the window
    volume_frame = tk.Frame(root)
    volume_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # Volume slider
    volume_slider = tk.Scale(volume_frame, from_=0, to=100, orient=tk.HORIZONTAL, label="Volume", length=900, width=150, command=set_volume)
    volume_slider.set(30)  # Set initial volume
    volume_slider.pack(pady=20)  # Add padding around slider

    # Frame for control buttons at the bottom
    button_frame = tk.Frame(root)
    button_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    # Define button dimensions
    button_width = 25
    button_height = 5

    # Play button
    play_button = tk.Button(button_frame, text="Play", command=lambda: send_command("play"), width=button_width, height=button_height)
    play_button.grid(row=2, column=0, padx=10, pady=10)

    # Pause button
    pause_button = tk.Button(button_frame, text="Pause", command=lambda: send_command("pause"), width=button_width, height=button_height)
    pause_button.grid(row=2, column=1, padx=10, pady=10)

    # Next button
    next_button = tk.Button(button_frame, text="Next", command=lambda: send_command("next"), width=button_width, height=button_height)
    next_button.grid(row=3, column=0, padx=10, pady=10)

    # Previous button
    prev_button = tk.Button(button_frame, text="Previous", command=lambda: send_command("previous"), width=button_width, height=button_height)
    prev_button.grid(row=3, column=1, padx=10, pady=10)

    # Close button
    close_button = tk.Button(root, text="Close", command=root.quit, width=button_width, height=button_height)
    close_button.grid(row=3, column=0, sticky="se", padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
