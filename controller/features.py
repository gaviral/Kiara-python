import sys

from pyperclip import paste, copy

from features.google_speech_search import google_speech_search
from features.text_to_speech import say

SEARCH_HOTWORDS = {'search', 'versus', 'difference', 'when', 'why', 'how', 'Which', 'what', 'who', 'where', 'whether',
                   'is',
                   'does', 'do'}

attempt = 0


def search_ctrlr(_first_word):
    if _first_word == "search":
        try:
            google_speech_search()
        except:
            e = sys.exc_info()[0]
            say(e)


TYPE_HOTWORDS = {'type', 'add'}


def type_ctrlr(_first_word, _sentence):
    if _first_word in TYPE_HOTWORDS:
        copy(_sentence)
        paste()


def features_controller(sentence, words):
    search_ctrlr(words[0])
    type_ctrlr(words[0], sentence)
