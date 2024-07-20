import subprocess
import tkinter as tk

def send_command(command):
    subprocess.run(["./btDriver", command])

def create_gui():
    root = tk.Tk()
    root.geometry("600x400")
    root.title("Bluetooth Media Player Control")

    # Button to play
    play_button = tk.Button(root, text="Play", command=lambda: send_command("play"))
    play_button.pack(pady=10)

    # Button to pause
    pause_button = tk.Button(root, text="Pause", command=lambda: send_command("pause"))
    pause_button.pack(pady=10)

    # Button to play next
    next_button = tk.Button(root, text="Next", command=lambda: send_command("next"))
    next_button.pack(pady=10)

    # Button to play previous
    prev_button = tk.Button(root, text="Previous", command=lambda: send_command("previous"))
    prev_button.pack(pady=10)

    # Close button
    close_button = tk.Button(root, text="Close", command=root.quit)
    close_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
