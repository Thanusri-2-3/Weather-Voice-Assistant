import os
import uuid
import requests
import speech_recognition as sr
from gtts import gTTS
import playsound
import threading
import time
import re

# --- CONFIGURATION --- #
API_KEY_OPENWEATHER = "YOUR_WEATHER_API_HERE"  # Replace with your real API key

# --- SPEAK FUNCTION --- #
def speak(text):
    print(f"Assistant: {text}")
    tts = gTTS(text=text, lang='en')
    filename = f"voice_{uuid.uuid4().hex}.mp3"
    tts.save(filename)
    try:
        playsound.playsound(filename)
    finally:
        if os.path.exists(filename):
            os.remove(filename)

# --- WEATHER FUNCTION --- #
def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY_OPENWEATHER}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return f"Sorry, I couldn't find the weather for '{city}'."

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        return (
            f"The weather in {city.title()} is {weather} with a temperature of {temp}°C, "
            f"feels like {feels_like}°C, and humidity is {humidity}%."
        )
    except Exception:
        return "There was an error getting the weather."

# --- CITY EXTRACTION FROM USER QUERY --- #
def extract_city(prompt):
    match = re.search(r"weather in ([a-zA-Z\s]+)", prompt)
    if match:
        return match.group(1).strip()
    return None

# --- MAIN RESPONSE FUNCTION --- #
def respond_to_query(query):
    query = query.lower()
    if "weather in" in query:
        city = extract_city(query)
        if city:
            return get_weather(city)
        else:
            return "Please specify a city."
    return "I can only provide weather updates for now."

# --- CONTINUOUS LISTENING --- #
def listen_loop():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        speak("I'm listening. Ask about the weather in any city.")

    while True:
        with mic as source:
            try:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
                query = recognizer.recognize_google(audio)
                print(f"You said: {query}")
                response = respond_to_query(query)
                speak(response)

                if query.lower() in ["exit", "quit", "stop"]:
                    speak("Goodbye!")
                    break

            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                speak("Sorry, I didn't catch that.")
            except Exception as e:
                speak(f"Error: {str(e)}")

# --- START LISTENING THREAD --- #
if __name__ == "__main__":
    listen_thread = threading.Thread(target=listen_loop)
    listen_thread.start()
    while listen_thread.is_alive():
        time.sleep(1)