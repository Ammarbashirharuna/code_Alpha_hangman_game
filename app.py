import tkinter as tk

class HangmanGame:
    def __init__(self,master):
        self.master = master
        self.master.title("HangmanGame")
        self.master.geometry = ("900x600")
def initilalize_gui(self):
     self.hangman_canvas = tk.canvas(self.master, width=300, height=300, bg="white")
     self.hangman_canvas.pack(pady=20)
     self.word_display = tk.Label(self.master, text="_ " * len(self.secret_word), font=("Helvetica", 30))
     self.word_display.pack(pady=(40, 20))
     self.buttons_frame = tk.Frame(self.master)
     self.buttons_frame.pack(pady=20)
     self.setup_alphabet_buttons()

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
if __name__ == "__main__":
    main()
