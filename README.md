# JARVIS: Your Personal Voice Assistant

<!-- Repository Overview Badges -->
<div align="center">
    <img src="https://img.shields.io/github/stars/arpsn123/Voice-Activated-JARVIS?style=for-the-badge&logo=github&logoColor=white&color=ffca28" alt="GitHub Repo Stars">
    <img src="https://img.shields.io/github/forks/arpsn123/Voice-Activated-JARVIS?style=for-the-badge&logo=github&logoColor=white&color=00aaff" alt="GitHub Forks">
    <img src="https://img.shields.io/github/watchers/arpsn123/Voice-Activated-JARVIS?style=for-the-badge&logo=github&logoColor=white&color=00e676" alt="GitHub Watchers">
</div>

<!-- Issue & Pull Request Badges -->
<div align="center">
    <img src="https://img.shields.io/github/issues/arpsn123/Voice-Activated-JARVIS?style=for-the-badge&logo=github&logoColor=white&color=ea4335" alt="GitHub Issues">
    <img src="https://img.shields.io/github/issues-pr/arpsn123/Voice-Activated-JARVIS?style=for-the-badge&logo=github&logoColor=white&color=ff9100" alt="GitHub Pull Requests">
</div>

<!-- Repository Activity & Stats Badges -->
<div align="center">
    <img src="https://img.shields.io/github/last-commit/arpsn123/Voice-Activated-JARVIS?style=for-the-badge&logo=github&logoColor=white&color=673ab7" alt="GitHub Last Commit">
    <img src="https://img.shields.io/github/contributors/arpsn123/Voice-Activated-JARVIS?style=for-the-badge&logo=github&logoColor=white&color=388e3c" alt="GitHub Contributors">
    <img src="https://img.shields.io/github/repo-size/arpsn123/Voice-Activated-JARVIS?style=for-the-badge&logo=github&logoColor=white&color=303f9f" alt="GitHub Repo Size">
</div>

<!-- Language & Code Style Badges -->
<div align="center">
    <img src="https://img.shields.io/github/languages/count/arpsn123/Voice-Activated-JARVIS?style=for-the-badge&logo=github&logoColor=white&color=607d8b" alt="GitHub Language Count">
    <img src="https://img.shields.io/github/languages/top/arpsn123/Voice-Activated-JARVIS?style=for-the-badge&logo=github&logoColor=white&color=4caf50" alt="GitHub Top Language">
</div>

<!-- Maintenance Status Badge -->
<div align="center">
    <img src="https://img.shields.io/badge/Maintenance-%20Active-brightgreen?style=for-the-badge&logo=github&logoColor=white" alt="Maintenance Status">
</div>



## Description

JARVIS (Just A Rather Very Intelligent System) is a simple yet powerful voice assistant inspired by the character from the Iron Man series. This Python-based application uses speech recognition and text-to-speech technology to interact with users, execute commands, and provide information. It aims to automate various tasks such as searching Wikipedia, opening websites, playing music, and telling the current time.

## Features

- **Voice Activation**: JARVIS responds to voice commands for seamless interaction.
- **Dynamic Responses**: It greets users based on the time of day.
- **Web Browsing**: Open websites like Google, YouTube, and StackOverflow with simple voice commands.
- **Music Playback**: Play random music from a specified directory.
- **Wikipedia Search**: Retrieve information from Wikipedia and read it aloud.
- **Time Reporting**: Announce the current time upon request.
- **Security Protocol**: Requires a passcode to access JARVIS functionalities, ensuring user privacy and security.

## Tech Stack
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Speech Recognition](https://img.shields.io/badge/Speech%20Recognition-v3.8.1-orange.svg)
![Pyttsx3](https://img.shields.io/badge/Pyttsx3-v2.7.1-green.svg)
![Web Browser](https://img.shields.io/badge/Web%20Browser-v2.5.0-yellow.svg)
- **Python**: The primary programming language used for building the application.
- **Pyttsx3**: A text-to-speech conversion library in Python that works offline.
- **Speech Recognition**: A library that helps recognize speech and convert it into text.
- **Wikipedia API**: Used to fetch summaries from Wikipedia for various queries.
- **Web Browser**: For opening web pages directly from voice commands.

## Installation

To set up JARVIS on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/arpsn123/JARVIS-Virtual-Assistant.git
   cd JARVIS-Virtual-Assistant
   ```

2. **Install Required Libraries**:
   Use `pip` to install the necessary libraries:
   ```bash
   pip install pyttsx3 speech_recognition wikipedia
   ```

3. **Run the Application**:
   Once the installation is complete, you can run JARVIS:
   ```bash
   python jarvis.py
   ```

## How It Works

1. **Greeting**: Upon launching, JARVIS greets the user based on the current time of day (morning, afternoon, evening, or night).
2. **Security Check**: JARVIS requests a passcode to ensure secure access. Only users with the correct passcode can continue.
3. **Command Execution**: After authorization, users can issue commands to JARVIS. The assistant listens for specific phrases to perform tasks:
   - **Opening Websites**: Users can say "open google," "open youtube," or "open stackoverflow" to navigate to these sites.
   - **Playing Music**: By saying "play music," JARVIS selects a random song from the predefined music directory.
   - **Time Inquiry**: Saying "time" prompts JARVIS to announce the current time.
   - **Wikipedia Queries**: Users can ask JARVIS to search Wikipedia by saying "wikipedia," followed by their query.

## Future Enhancements

JARVIS is designed to evolve. Future updates may include:
- Integration with smart home devices for IoT control.
- Enhanced NLP capabilities for better understanding of complex queries.
- A graphical user interface (GUI) for a more interactive experience.
- Support for multiple languages to cater to a broader audience.

## Conclusion

JARVIS serves as a basic prototype of a voice-activated personal assistant, showcasing the potential of AI in daily life. Its capabilities will expand as more features are implemented and improved upon.


## Author

- **Arpan Nath**
