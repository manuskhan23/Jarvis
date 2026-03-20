import speech_recognition as sr
import webbrowser
import musicLibrary
import requests
from groq import Groq
from gtts import gTTS
import os
from dotenv import load_dotenv
import time
import pygame
import sys

load_dotenv()

# pip install pocketsphinx

recognizer = sr.Recognizer()
newsapi = os.getenv("NEWS_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

if not newsapi or not groq_api_key:
    raise RuntimeError("Missing NEWS_API_KEY or GROQ_API_KEY in environment. Please set them in .env")

def speak(text):
     # Replace special characters (except hyphens in proper nouns)
     text = text.replace("*", "star")
     text = text.replace("_", "underscore")
     text = text.replace("@", "at")
     text = text.replace("#", "hash")
     text = text.replace("$", "dollar")
     text = text.replace("%", "percent")
     text = text.replace("&", "and")
     text = text.replace("+", "plus")
     text = text.replace("=", "equals")
     
     print(f"[SPEAK] Speaking: {text[:60]}...")
     
     try:
         pygame.mixer.init()
         
         # Split into chunks (max 300 words)
         words = text.split()
         chunks = []
         current_chunk = []
         
         for word in words:
             current_chunk.append(word)
             if len(current_chunk) >= 300:
                 chunks.append(" ".join(current_chunk))
                 current_chunk = []
         
         if current_chunk:
             chunks.append(" ".join(current_chunk))
         
         # Speak each chunk using gTTS (You can replace with ElevenLabs later)
         for i, chunk in enumerate(chunks):
             print(f"[SPEAK] Chunk {i+1}/{len(chunks)}: Generating audio...")
             
             # Generate MP3 from gTTS
             tts = gTTS(chunk, lang='en', slow=False)
             tts.save('temp.mp3')
             
             print(f"[SPEAK] Playing chunk {i+1}...")
             
             # Play using pygame
             pygame.mixer.music.load('temp.mp3')
             pygame.mixer.music.play()
             
             # Wait for playback to finish
             while pygame.mixer.music.get_busy():
                 time.sleep(0.1)
             
             pygame.mixer.music.unload()
             time.sleep(0.3)
         
         # Clean up
         if os.path.exists('temp.mp3'):
             os.remove('temp.mp3')
         
         print("[SPEAK] Completed")
     except Exception as e:
         print(f"[SPEAK] Error: {type(e).__name__}: {e}")

def aiProcess(command):
    client = Groq(api_key=groq_api_key)

    completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open fiver" in c.lower():
        webbrowser.open("https://fiverr.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
    else:
        try:
            # Let Groq handle the request
            print(f"Processing with Groq: {c}")
            output = aiProcess(c)
            print(f"Groq response: {output}")
            speak(output)
        except Exception as e:
            print(f"Error in aiProcess: {type(e).__name__}: {e}") 





if __name__ == "__main__":
     speak("Initializing Jarvis....")
     while True:
         # Listen for the wake word "Jarvis"
         r = sr.Recognizer()
         r.energy_threshold = 4000
          
         print("recognizing...")
         try:
             with sr.Microphone() as source:
                 print("Listening...")
                 audio = r.listen(source, timeout=2, phrase_time_limit=3)
             word = r.recognize_google(audio)
             print(f"You said: {word}")
             if(word.lower() == "jarvis"):
                 speak("Ya")
                 time.sleep(1)
                 # Stay in listening mode for commands until user exits
                 while True:
                     try:
                         with sr.Microphone() as source:
                             print("Jarvis Active... Waiting for command...")
                             audio = r.listen(source, timeout=10, phrase_time_limit=5)
                             command = r.recognize_google(audio)
                             print(f"Command: {command}")
                             
                             # Check for exit commands (more variations)
                             exit_keywords = ["exit", "bye", "goodbye", "quit", "stop jarvis", "bye bye", "see you"]
                             command_lower = command.lower()
                             
                             if command_lower == "bye" or command_lower == "goodbye" or any(word in command_lower for word in exit_keywords):
                                 speak("Goodbye!")
                                 time.sleep(1)
                                 print("\n[EXIT] Closing Jarvis...")
                                 sys.exit(0)  # Kill the program
                             
                             processCommand(command)
                             time.sleep(0.5)
                     except sr.UnknownValueError:
                         print("Could not understand. Say your command again.")
                         time.sleep(0.5)
                     except sr.RequestError as e:
                         print(f"API Error: {e}")
                         time.sleep(0.5)
                     except Exception as e:
                         print(f"Error in command listening: {type(e).__name__}: {e}")
                         time.sleep(0.5)

         except Exception as e:
             print(f"Error: {type(e).__name__}: {e}")
             time.sleep(0.5)



