import os

import playsound
from gtts import gTTS

ON = 1
OFF = 0
STOP_TALKING_HOTWORDS = {'stop talking', 'pause'}
START_TALKING_HOTWORDS = {'start talking', 'you can talk now', 'play'}

talk_mode = OFF


def handle_talk_mode(cmd_str):
    global talk_mode

    if cmd_str in STOP_TALKING_HOTWORDS:
        say("ok! I'll stop talking")
        talk_mode = OFF

    elif cmd_str in START_TALKING_HOTWORDS:
        talk_mode = ON
        say("Alright, I'll talk now")


def say(words, file='tts.mp3'):
    """
    Makes Kiara say the `words`
    :param words:
    :param file:
    """

    def play_mp3(mp3_file):
        playsound.playsound(mp3_file, True)

    def create_mp3(t, f):
        gTTS(text=t, lang='en', slow=False).save(f)

    def remove_mp3(f):
        os.remove(f)

    print(f'Kiara: {words}')
    if talk_mode:
        create_mp3(words, file)
        play_mp3(file)
        remove_mp3(file)
