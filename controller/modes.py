from features.speech_to_text import get_voice_input
from features.text_to_speech import say
from model.mode import set_lang_mode, NORMAL, get_lang_mode, OFF, set_talk_mode, ON, set_feeling_lucky_mode, \
    get_feeling_lucky_mode


# Initializations #############################################


def init_modes() -> None:
    set_talk_mode(ON)
    set_lang_mode(NORMAL)
    set_feeling_lucky_mode(OFF)
    print(get_feeling_lucky_mode())


# Kiara's talk_mode ###########################################
# TODO: not working
START_TALKING_HOTWORDS = {'start talking', 'you can talk now'}
STOP_TALKING_HOTWORDS = {'stop talking'}


def talk_mode_ctrlr(_words):
    # if _words in START_TALKING_HOTWORDS:
    #     set_talk_mode(ON)
    #     say("I'll be talking now.")
    # elif _words in STOP_TALKING_HOTWORDS:
    #     say("ok! I'll stop talking.")
    #     set_talk_mode(OFF)
    return


# Kiara's lang_mode ###########################################
# TODO: not working
def lang_mode_ctrlr(_first_word, _second_word):
    if _second_word == "mode":
        if _first_word != "normal":
            set_lang_mode(NORMAL)
        else:
            set_lang_mode(_first_word)

        say(f'Language Mode: {get_lang_mode()}')


# feeling_lucky_mode ###########################################
def feeling_lucky_mode_ctrlr():
    say("Are you feeling lucky?")
    _bool = True \
        if get_voice_input(bool_answer=True) == "y" \
        else False

    set_feeling_lucky_mode(_bool)
    print(get_feeling_lucky_mode())


# Main ########################################################
def modes_controller(words):
    talk_mode_ctrlr(words)
    if len(words) == 2:
        lang_mode_ctrlr(words[0], words[1])
