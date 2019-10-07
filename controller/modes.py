from features.speech_to_text import get_voice_input
from features.text_to_speech import say
from model.mode import set_lang_mode, NORMAL, get_lang_mode, OFF, set_talk_mode


# Initializations #############################################
def init_modes() -> None:
    set_talk_mode(OFF)
    set_lang_mode(NORMAL)


# Kiara's talk_mode ###########################################
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
def lang_mode_ctrlr(_first_word, _second_word):
    if _second_word == "mode":
        if _first_word != "normal":
            set_lang_mode(NORMAL)
        else:
            set_lang_mode(_first_word)

        say(f'Language Mode: {get_lang_mode()}')


# feeling_lucky_mode ###########################################
feeling_lucky_mode: bool


def is_feeling_lucky():
    say("Are you feeling lucky?")
    return True if get_voice_input(bool_answer=True) == "y" else False


# Main ########################################################
def modes_controller(words):
    talk_mode_ctrlr(words)
    if len(words) == 2:
        lang_mode_ctrlr(words[0], words[1])
