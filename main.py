import tkinter as tk
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

class Timer:
    def __init__(self, root):
        self.root = root
        self.time_left = 0
        self.is_running = False
        self.paused = False
        self.alarm_sound = "alarm.wav" 

        # Create label
        self.label = tk.Label(root, text="00:00", font=("Helvetica", 48))
        self.label.pack()

        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack()

        # Display for minutes
        self.entry_minutes = tk.Entry(self.entry_frame, width=3, font=("Helvetica", 24))
        self.entry_minutes.insert(0, "00")
        self.entry_minutes.pack(side="left")

        # Display for seconds
        self.entry_seconds = tk.Entry(self.entry_frame, width=3, font=("Helvetica", 24))
        self.entry_seconds.insert(0, "00")
        self.entry_seconds.pack(side="left")

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        # Start button
        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_timer, font=("Helvetica", 14))
        self.start_button.pack(side="left")

        # Pause button
        self.pause_button = tk.Button(self.button_frame, text="Pause", command=self.pause_timer, font=("Helvetica", 14))
        self.pause_button.pack(side="left")

        # Reset button
        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset_timer, font=("Helvetica", 14))
        self.reset_button.pack(side="left")

    def start_timer(self):
        if not self.is_running:
            try:
                self.time_left = int(self.entry_minutes.get()) * 60 + int(self.entry_seconds.get())
                self.is_running = True
                self.update_timer()
            except ValueError:
                self.label.config(text="Invalid input")

    def pause_timer(self):
        # Pause
        if self.is_running:
            self.paused = not self.paused
            # Unpause
            if not self.paused:
                self.update_timer()

    def reset_timer(self):
        self.is_running = False
        self.time_left = 0
        self.label.config(text="00:00")

    def update_timer(self):
        if self.is_running and not self.paused:
            if self.time_left > 0:
                mins, secs = divmod(self.time_left, 60)
                self.label.config(text=f"{mins:02}:{secs:02}")
                self.time_left -= 1
                self.root.after(1000, self.update_timer)
            else:
                self.is_running = False
                self.label.config(text="00:00")
                pygame.mixer.music.load(self.alarm_sound)
                pygame.mixer.music.play()

if __name__ == "__main__":
    root = tk.Tk()
    timer = Timer(root)
    root.mainloop()
