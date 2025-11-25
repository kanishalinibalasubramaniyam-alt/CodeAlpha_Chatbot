import tkinter as tk
from tkinter import scrolledtext
import random

# --- Chatbot logic ---
responses = {
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "how are you": ["I'm fine, thanks!", "Doing great!", "All good!"],
    "bye": ["Goodbye!", "See you later!", "Bye! "],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"]
}

def get_reply(user_input):
    user_input = user_input.lower()

    # Check for matching key
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "I don't understand "

# --- GUI setup ---
class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Chatbot")
        self.root.geometry("400x500")
        self.root.configure(bg="#f5f5f5")

        # Chat display
        self.chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Arial", 12))
        self.chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Entry field
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(padx=10, pady=(0,10), fill=tk.X)
        self.entry.bind("<Return>", lambda event: self.send_message())

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message, bg="#007AFF", fg="white", font=("Arial", 12))
        self.send_button.pack(padx=10, pady=(0,10))

        self.add_message("Bot", "Hello! Type 'bye' to exit.")

    # Display messages
    def add_message(self, sender, message):
        self.chat_box.config(state='normal')
        self.chat_box.insert(tk.END, f"{sender}: {message}\n")
        self.chat_box.see(tk.END)
        self.chat_box.config(state='disabled')

    # Send message
    def send_message(self):
        user_msg = self.entry.get().strip()
        if not user_msg:
            return
        self.add_message("You", user_msg)
        self.entry.delete(0, tk.END)

        # Get bot reply
        reply = get_reply(user_msg)
        self.add_message("Bot", reply)

        if "bye" in user_msg.lower():
            self.add_message("Bot", "Chat ended. Close the window to exit.")


# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()
