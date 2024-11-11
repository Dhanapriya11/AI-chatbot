import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
from gtts import gTTS  # Google Text-to-Speech for output
import os

# Function to recognize speech
def recognize_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening... (Speak in Tamil)")
        audio = recognizer.listen(source)
    
    try:
        # Recognize speech using Google Speech Recognition for Tamil
        text = recognizer.recognize_google(audio, language='ta-IN')
        print(f"Recognized: {text}")
        output_text.insert(tk.END, f"நான் சொல்கிறேன்: {text}\n")
        process_command(text)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
        output_text.insert(tk.END, "மன்னிக்கவும், புரியவில்லை.\n")
        
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        output_text.insert(tk.END, "போர்க்கப்படவில்லை; இணைய இணைப்பு இல்லை.\n")

# Function to process commands based on recognized text
def process_command(text):
    # Example: Add your logic here based on recognized commands
    if 'வணக்கம்' in text:
        speak_text("வணக்கம்! நீங்கள் எப்படி உதவ முடியும்?")
    elif 'எப்படி இருக்கிறீர்கள்' in text:
        speak_text("நான் நன்கு இருக்கிறேன்! நீங்கள் எப்படி இருக்கிறீர்கள்?")
    # Add more command processing logic as needed

# Function to convert text to speech (Tamil)
def speak_text(text):
    tts = gTTS(text=text, lang='ta')
    tts.save("output.mp3")
    os.system("start output.mp3")

# Create the main Tkinter window
root = tk.Tk()
root.title("Tamil AI Assistant")
root.geometry("500x400")

# Create a text area for output
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15)
output_text.pack(padx=10, pady=10)

# Create a button to start speech recognition
button_recognize = tk.Button(root, text="உச்சரிக்க", command=recognize_speech)
button_recognize.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
