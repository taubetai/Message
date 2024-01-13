import tkinter as tk
from tkinter import scrolledtext, messagebox

class ChatGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Game")

        self.chat_history = scrolledtext.ScrolledText(root, width=40, height=10, wrap=tk.WORD)
        self.chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.message_entry = tk.Entry(root, width=30)
        self.message_entry.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.chat_history.insert(tk.END, f"You: {message}\n")
            # You can add logic here to handle responses from other users
            self.message_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a message.")

if __name__ == "__main__":
    root = tk.Tk()
    chat_game = ChatGame(root)
    root.mainloop()