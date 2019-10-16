import os

import playsound
from gtts import gTTS

from model.mode import get_talk_mode


def say(words, file='tts.mp3'):
    """
    Makes Kiara say the `words`
    :param words:
    :param file:
    """

    def create_mp3(t, f):
        gTTS(text=t, lang='en', slow=False).save(f)

    def play_mp3(mp3_file):
        playsound.playsound(mp3_file, True)

    def remove_mp3(f):
        os.remove(f)

    print(f'Kiara {words}')
    if get_talk_mode():
        create_mp3(words, file)
        play_mp3(file)
        remove_mp3(file)
