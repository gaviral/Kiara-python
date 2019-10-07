from pyperclip import paste, copy

from features.google_search import search
from features.text_to_speech import say
from model.mode import get_lang_mode

SEARCH_HOTWORDS = {'search', 'versus', 'difference', 'when', 'why', 'how', 'Which', 'what', 'who', 'where', 'whether',
                   'is',
                   'does', 'do'}


def search_ctrlr(_words, _sentence):
    # TODO: secondary search (continuous search) window
    # TODO: primary search (in HOTWORDS search) window
    if any(word in SEARCH_HOTWORDS for word in _words):
        searched_txt = search(f'{get_lang_mode()} {_sentence}')
        say(f'[SEARCHED]: "{searched_txt}"')


TYPE_HOTWORDS = {'type', 'add'}


def type_ctrlr(_first_word, _sentence):
    if _first_word in TYPE_HOTWORDS:
        copy(_sentence)
        paste()


def features_controller(sentence, words):
    search_ctrlr(words, sentence)
    type_ctrlr(words[0], sentence)
