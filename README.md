# Kiara

Virtual Assistant using voice commands

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
- Run `install_cmds.sh` to install the following packages:
    - `speech_recognition`
    -  `pyaudio`
