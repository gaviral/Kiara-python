# Kiara

Virtual Assistant

## Pre-Req

- Python 3.6 (PyAudio doesn't support 3.7)
- pip
- PyCharm EAP
- Visual Studio Build Tools (C++)

## Installation

- Open project in PyCharm.
- Install the following Packages (`Alt-Enter` on errors in `main.py`):
    - `playsound`
    - `gtts`
- Run `install_cmds.sh` to install the following packages:
    - `speech_recognition`
    -  `pyaudio`
- For "I'm feeling lucky" feature:
    - install `cjs 2` chrome extension
    - Add `JQuery3` as a resource
    - Add following code for `google.com`:
    
```javascript

$(document).ready(function(){
  if($("*:contains(Redirect Notice)").length>1){
    const newLink = document.getElementsByTagName('a')[0].href.css("background-color", "yellow");
    window.location.replace(newLink);
  }
});
```