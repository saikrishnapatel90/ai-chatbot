import google.generativeai as genai  # pip install google-generativeai
import tkinter as tk  # pip install tk
from tkinter import scrolledtext
api_data = "AIzaSyDcrZUeqWqCU11WJitp63qErnJNgt06C50"

# Configure API key
genai.configure(api_key=api_data)

# Initialize Gemini model once
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

# GUI-based chatbot without voice input/output
def generate_response(query):
    try:
        response = gemini_model.generate_content(query, generation_config=genai.GenerationConfig(
            max_output_tokens=75,
            temperature=0.1,
        ))
        return response.text
    except Exception as e:
        return f"Sorry, I encountered an error: {e}"

def send_query():
    query = user_input.get()
    if not query.strip():
        return

    conversation_area.insert(tk.END, f"You: {query}\n", "user")
    user_input.delete(0, tk.END)

    response = generate_response(query)
    conversation_area.insert(tk.END, f"Jarvis: {response}\n", "bot")
    conversation_area.see(tk.END)

# Set up GUI
root = tk.Tk()
root.title("J-A-R-V-I-S Chatbot")
root.configure(bg="black")

conversation_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12), bg="black", fg="white")
conversation_area.pack(padx=10, pady=10)
conversation_area.tag_config("user", foreground="yellow")
conversation_area.tag_config("bot", foreground="green")

input_frame = tk.Frame(root, bg="black")
input_frame.pack(pady=5)

user_input = tk.Entry(input_frame, font=("Arial", 12), width=40)
user_input.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(input_frame, text="Send", font=("Arial", 12), bg="gray", command=send_query)
send_button.pack(side=tk.LEFT)

root.mainloop()
