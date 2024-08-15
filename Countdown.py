import tkinter as tk
from tkinter import messagebox


class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.time_left = 0
        self.running = False
        self.paused = False

        # Title label
        self.label_title = tk.Label(
            root,
            text="Countdown Timer",
            font=("Helvetica", 16),
            bg="#4CAF50",
            fg="white",
        )
        self.label_title.pack(pady=10, fill=tk.X)

        # Time input frame
        self.frame_input = tk.Frame(root, bg="#f1f1f1")
        self.frame_input.pack(pady=5)

        self.label_minutes = tk.Label(
            self.frame_input, text="Minutes:", font=("Helvetica", 12), bg="#f1f1f1"
        )
        self.label_minutes.pack(side=tk.LEFT)

        self.entry_minutes = tk.Entry(self.frame_input, width=5, font=("Helvetica", 12))
        self.entry_minutes.pack(side=tk.LEFT, padx=10)

        self.label_seconds = tk.Label(
            self.frame_input, text="Seconds:", font=("Helvetica", 12), bg="#f1f1f1"
        )
        self.label_seconds.pack(side=tk.LEFT)

        self.entry_seconds = tk.Entry(self.frame_input, width=5, font=("Helvetica", 12))
        self.entry_seconds.pack(side=tk.LEFT, padx=10)

        # Display frame
        self.frame_display = tk.Frame(root, bg="#f1f1f1")
        self.frame_display.pack(pady=10)

        self.label_display = tk.Label(
            self.frame_display, text="00:00", font=("Helvetica", 24), bg="#f1f1f1"
        )
        self.label_display.pack()

        # Control buttons frame
        self.frame_buttons = tk.Frame(root, bg="#f1f1f1")
        self.frame_buttons.pack(pady=10)

        self.button_start = tk.Button(
            self.frame_buttons,
            text="Start",
            command=self.start_timer,
            font=("Helvetica", 12),
            bg="#4CAF50",
            fg="white",
        )
        self.button_start.pack(side=tk.LEFT, padx=10)

        self.button_pause = tk.Button(
            self.frame_buttons,
            text="Pause",
            command=self.pause_timer,
            font=("Helvetica", 12),
            bg="#FFC107",
            fg="black",
        )
        self.button_pause.pack(side=tk.LEFT, padx=10)

        self.button_resume = tk.Button(
            self.frame_buttons,
            text="Resume",
            command=self.resume_timer,
            font=("Helvetica", 12),
            bg="#FFC107",
            fg="black",
        )
        self.button_resume.pack(side=tk.LEFT, padx=10)

        self.button_clear = tk.Button(
            self.frame_buttons,
            text="Clear",
            command=self.clear_timer,
            font=("Helvetica", 12),
            bg="#FF5722",
            fg="white",
        )
        self.button_clear.pack(side=tk.LEFT, padx=10)

        self.button_quit = tk.Button(
            self.frame_buttons,
            text="Quit",
            command=self.root.quit,
            font=("Helvetica", 12),
            bg="#607D8B",
            fg="white",
        )
        self.button_quit.pack(side=tk.LEFT, padx=10)

    def start_timer(self):
        try:
            if not self.paused:
                minutes = int(self.entry_minutes.get())
                seconds = int(self.entry_seconds.get())
                self.time_left = minutes * 60 + seconds
            if self.time_left > 0:
                self.running = True
                self.paused = False
                self.update_timer()
            else:
                messagebox.showerror("Error", "Please enter a valid time.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    def pause_timer(self):
        if self.running:
            self.running = False
            self.paused = True

    def resume_timer(self):
        if self.paused:
            self.running = True
            self.paused = False
            self.update_timer()

    def stop_timer(self):
        self.running = False
        self.paused = False

    def clear_timer(self):
        self.stop_timer()
        self.entry_minutes.delete(0, tk.END)
        self.entry_seconds.delete(0, tk.END)
        self.label_display.config(text="00:00")

    def update_timer(self):
        if self.running and self.time_left > 0:
            minutes, seconds = divmod(self.time_left, 60)
            self.label_display.config(text=f"{minutes:02d}:{seconds:02d}")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        elif self.time_left <= 0:
            self.label_display.config(text="00:00")
            messagebox.showinfo("Time's up!", "The countdown has finished.")
            self.running = False


if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
