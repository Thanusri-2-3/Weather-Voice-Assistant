# Weather-Voice-Assistant
A weather voice assistant project is a voice-activated program that provides users with real-time weather information. The assistant uses speech recognition to understand user commands, retrieves weather data from an API (like OpenWeatherMap), and then relays that information back to the user through text-to-speech or by displaying it on a screen.

# 🌤️ Weather Voice Assistant - Nova

This is a Python-based **Voice Assistant** named **Nova** that listens to your voice queries and replies with the current weather conditions of any city using real-time data from the OpenWeatherMap API.

It uses:
- 🎤 Voice recognition (`SpeechRecognition`)
- 🔊 Text-to-speech using Google (`gTTS`)
- 🌍 Live weather data (`OpenWeatherMap API`)

---

## 🎯 Features

- Responds to voice commands like:
  - “What’s the weather in Hyderabad?”
  - “Tell me the weather in New York.”
- Gives spoken feedback using text-to-speech.
- Handles multiple cities.
- Gracefully handles errors like invalid cities or no internet.

---

## 🖥️ Demo

```bash
You: What's the weather in Visakhapatnam?
Nova: The weather in Visakhapatnam is light rain with a temperature of 27°C, feels like 28°C, and humidity is 88%.
```

---

## ⚙️ Requirements

Make sure you have Python 3.8+ installed.

### Python Packages

Install required packages:

```bash
pip install -r requirements.txt
```

`requirements.txt`:
```
gtts
playsound==1.2.2
requests
SpeechRecognition
pyaudio
```

> Note: `playsound==1.2.2` works best on Windows.

### Fix PyAudio Installation (if needed)

If `pyaudio` fails to install via pip:

1. Download appropriate `.whl` file from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio  
2. Then install it manually:

```bash
pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl
```

---

## 🔑 OpenWeatherMap API Setup

1. Sign up at: [https://openweathermap.org/api](https://openweathermap.org/api)
2. Go to your [API Keys](https://home.openweathermap.org/api_keys)
3. Copy your key and replace it inside the Python file:

```python
API_KEY_OPENWEATHER = "your_actual_api_key"
```

---

## 🚀 How to Run

1. Make sure your microphone is connected and working.
2. Run the script:

```bash
python weather_voice_assist.py
```

3. Speak your query when prompted, like:

```
What's the weather in Mumbai?
```

---

## 🧠 How It Works

- Listens to your voice using `SpeechRecognition`.
- Extracts the city name from your query.
- Calls OpenWeatherMap API to fetch real-time weather.
- Uses `gTTS` to speak the response.
- Deletes the audio file after playback.

---

## 📂 Project Structure

```
weather_voice_assist/
│
├── weather_voice_assist.py     # Main script
├── requirements.txt            # Dependencies
└── README.md                   # This file
```

---

## 🛑 Voice Commands to Exit

Say:
- “stop”
- “exit”
- “quit”

The assistant will shut down gracefully.

---

## 🙋‍♀️ Credits

**Developed by**: Thanusri Reddy  
**Assistant Name**: Nova

---

## 📄 License

This project is licensed under the MIT License. Feel free to use, modify, and share!
