import pyttsx3
import pyjokes
import tkinter as tk

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

def tell_joke():
    joke = pyjokes.get_joke()
    joke_label.config(text=joke)
    engine.say(joke)
    engine.runAndWait()

# GUI setup
root = tk.Tk()
root.title("Voice Joke Teller")
root.geometry("400x300")
root.config(bg="lightblue")

# Joke Display Label
joke_label = tk.Label(root, text="", wraplength=350, bg="lightblue", font=("Arial", 12))
joke_label.pack(pady=50)

# Button to Get Joke
joke_button = tk.Button(root, text="Tell me a Joke", command=tell_joke, font=("Arial", 14), bg="green", fg="white")
joke_button.pack()

# Run GUI
root.mainloop()
