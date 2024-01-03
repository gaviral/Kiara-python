# PaperPy

Intelligent Assistant using voice commands. Coming soon: Context-awareness

## Features

### Voice Commands

- Google Search <!-- TODO: Context-aware Google Search -->
- Visual Studio Code Commands:
  - New file
  - Save file
- Custom-Mini-Scripts
  - say "leetCode 112" -> opens leetCode problem #: 112 in browser
  - say "reload" -> reload this project itself (helps in testing newly added features)
- Typing Mode (In-progress) <!-- TODO: Fix this recently broken feature -->
- Call someone (In-progress)
- Context-aware coding (TODO)

## Tech-Used

- Pure-Python
- Speech-to-Text: Google Speech to Text
- Text-to-Speech: playsound + Google Speech to Text
- keyboard simulation: pyAutoGUI
- clipboard controller: pyperclip

## Pre-Req

- Python 3.6 (PyAudio doesn't support 3.7)
- pip
- PyCharm EAP
- Visual Studio Build Tools (C++)

<!-- ## Project Structure


```ProjectStructure
.                       # Root
├── .vscode             # vscode config files
├── Infrastructure       # ARM template (Azure provisioning)
    └── logintemplate    # login/sign-up UI
├── Client
    ├── src              # main client code
    ├── api              # clients interface(s) to the servers API
    ├── auth             # client-side authentication
    ├── components       # app components
    ├── containers       # components rep
``` -->

## Installation

- Open project in PyCharm.
- Install the following Packages (`Alt-Enter` on errors in `main.py`):
    - `playsound`
    - `gtts`
    - `pyautogui`
- Run `install_cmds.sh` to install the following packages:
    - `speech_recognition`
    -  `pyaudio`
