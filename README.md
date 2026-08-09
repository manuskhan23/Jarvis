# 🤖 Jarvis — AI Voice Assistant

Jarvis is a versatile, voice-activated AI assistant built with Python. Inspired by Iron Man's JARVIS, this project brings voice-controlled automation to your desktop — handling tasks like opening websites, playing music, fetching live news, and answering questions with the power of Groq AI (LLaMA 3.3 70B).

## ⚡ Features

- **Voice Activation** — Wake word detection ("Jarvis") triggers listening mode
- **Natural Language Processing** — Understands and responds to user queries via Groq AI
- **Speech Synthesis** — Speaks responses aloud using gTTS (Google Text-to-Speech)
- **Web Navigation** — Open Google, YouTube, Facebook, LinkedIn, Fiverr with voice commands
- **Music Playback** — Play songs from a music library with voice control
- **Live News** — Fetch and read top headlines via NewsAPI
- **Exit Commands** — Natural phrases to shut down ("goodbye", "bye", "exit", "quit")
- **Continuous Listening** — Stays active for multiple commands until dismissed

## 🧰 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.x |
| Speech Recognition | `speech_recognition` (Google Web Speech API) |
| Text-to-Speech | `gTTS` (Google TTS) |
| Audio Playback | `pygame` mixer |
| AI / LLM | Groq API (LLaMA 3.3 70B Versatile) |
| News | NewsAPI |
| Environment | `python-dotenv` |

## 📁 Project Structure

```
Jarvis/
├── main.py           # Core assistant logic & voice loop
├── client.py         # Alternative client script
└── musicLibrary.py   # Song-to-URL mapping for music playback
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A working microphone
- Groq API key ([console.groq.com](https://console.groq.com))
- NewsAPI key ([newsapi.org](https://newsapi.org))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/manuskhan23/Jarvis.git
cd Jarvis
```

2. Install dependencies:
```bash
pip install speechrecognition gTTS pygame groq python-dotenv requests
```

3. Create a `.env` file with your API keys:
```env
GROQ_API_KEY=your_groq_api_key
NEWS_API_KEY=your_news_api_key
```

4. Run Jarvis:
```bash
python main.py
```

### Usage

1. Say **"Jarvis"** to wake the assistant
2. Give a command like:
   - "Open YouTube"
   - "Play [song name]"
   - "What's the news today?"
   - "Tell me a joke"
3. Say **"Goodbye"** or **"Exit"** to shut down

## 📸 Preview

> Coming soon

## 🔮 Future Enhancements

- [ ] Replace gTTS with ElevenLabs for more natural speech
- [ ] Add system control commands (volume, brightness, etc.)
- [ ] Integrate with smart home devices
- [ ] Add a GUI interface
- [ ] Support for multiple wake words
- [ ] Conversation history and memory

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center"><sub>Built with ❤️ by <a href="https://github.com/manuskhan23">Muhammad Anus Khan</a></sub></p>
