from controller.features import features_controller
from controller.modes import init_modes, modes_controller
from features.speech_to_text import get_text_from_speech

STOP_LISTENING_HOTWORDS = {'stop listening', 'bye'}


def init():
    init_modes()

    # starting with speech searches
    cmd_dispatcher("testing")


def cmd_dispatcher(sentence):
    if sentence in STOP_LISTENING_HOTWORDS:
        return True

    # setup
    sentence = str.lower(sentence)
    words = sentence.split(' ')

    modes_controller(words)
    features_controller(sentence, words)


def controller():
    init()

    while True:
        if cmd_dispatcher(get_text_from_speech()):
            break
