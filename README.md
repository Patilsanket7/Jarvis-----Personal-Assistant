# 🤖 Jarvis - AI-Powered Personal Assistant

A smart virtual assistant inspired by Iron Man's Jarvis, built using **Python** for backend logic and **HTML/CSS/JavaScript with Bootstrap** for a responsive front-end interface. Jarvis interacts via voice commands and performs real-time automation and information retrieval.

---

## 🚀 Features

- 🎙️ **Voice Recognition**: Accepts natural language voice commands
- 🧠 **ChatGPT Integration**: Uses OpenAI API for smart, conversational responses
- 💻 **System Automation**: Opens applications, manages files, executes commands
- 🌐 **Web Search**: Performs Google and YouTube searches
- 🌦️ **Real-Time Info**: Provides weather updates, date & time, and news
- 🖥️ **GUI**: Responsive frontend with HTML, CSS, JS & Bootstrap
- 📦 **Docker Support** *(optional)*: Containerized for deployment ease

---

## 🛠️ Technologies Used

- **Backend**: Python, OpenAI API, SpeechRecognition, pyttsx3, requests, os
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **APIs**: OpenAI, Weather API, YouTube Search API
- **Others**: Tkinter (optional GUI), Docker (optional)

---

## 📁 Project Structure
Jarvis/
├── engine/
│   ├── __init__.py
│   ├── auth.py              # Facial authentication
│   ├── command.py           # Text-to-speech and command responses
│   ├── features.py          # Assistant features (e.g., hotword detection)
│   ├── image_gen.py         # AI image generation
│   ├── config.py            # Assistant settings and constants
│   └── __pycache__/         # Cached Python files (ignored)
│
├── www/
│   ├── index.html           # Frontend UI
│   ├── style.css            # Styling with CSS
│   ├── script.js            # JS interactions
│   └── bootstrap/           # Bootstrap assets (if locally added)
│
├── .env                     # API keys (e.g., OpenAI)
├── .gitignore               # Git ignore rules
├── #Core Functionality.py   # Main functionality module (utility/misc)
├── contacts.csv             # (ignored) possibly for contact handling
├── device.bat               # Batch script for device actions
├── jarvis.db                # SQLite database file
├── main.py                  # Main GUI logic with Eel
├── run.py                   # Runs Jarvis + hotword detection in parallel
├── requirements.txt         # Python dependencies
└── README.md                # Project overview (to be added)
