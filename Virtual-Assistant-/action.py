# action.py

import datetime
import speak
import webbrowser
import weather
import os

def Action(send):
    if send is None:
        return "No input received"

    data_btn = send.lower()

    # English responses
    if "what is your name" in data_btn:
        speak.speak("my name is virtual Assistant")
        return "my name is virtual Assistant"

    elif "hello" in data_btn or "hi" in data_btn:
        speak.speak("Hey sir/mam, How can I help you!")
        return "Hey sir, How can I help you!"

    elif "how are you" in data_btn:
        speak.speak("I am doing great these days sir/mam")
        return "I am doing great these days sir/mam"

    elif "thank you" in data_btn or "thanks" in data_btn:
        speak.speak("It's my pleasure sir to assist you")
        return "It's my pleasure sir to assist you"

    elif "good morning" in data_btn:
        speak.speak("Good morning sir, I think you might need some help")
        return "Good morning sir, I think you might need some help"

    elif "time now" in data_btn:
        current_time = datetime.datetime.now()
        Time = str(current_time.hour) + " Hour : " + str(current_time.minute) + " Minute"
        speak.speak(Time)
        return Time

    elif "shutdown" in data_btn or "quit" in data_btn:
        speak.speak("ok sir")
        return "ok sir"

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")
        speak.speak("gaana.com is now ready for you, enjoy your music")
        return "gaana.com is now ready for you, enjoy your music"

    elif 'open google' in data_btn or 'google' in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open")
        return "YouTube open"

    elif 'weather' in data_btn:
        ans = weather.Weather()
        speak.speak(ans)
        return ans

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music'
        songs = os.listdir(url)
        if songs:
            os.startfile(os.path.join(url, songs[0]))
            speak.speak("songs playing...")
            return "songs playing..."
        else:
            return "No music found on your laptop"

    elif 'gmail' in data_btn:
        url = "https://mail.google.com/mail/u/0/"
        webbrowser.get().open(url)
        speak.speak("Gmail open")
        return "Gmail open"

    elif 'news' in data_btn:
        url = "https://www.youtube.com/watch?v=maeJfPcpUy8"
        webbrowser.get().open(url)
        speak.speak("news open")
        return "News open"

    else:
        speak.speak("I'm sorry, I didn't understand that!")
        return "I'm sorry, I didn't understand that!"
