from pyperclip import paste

SEARCH_HOTWORDS = {'search', 'versus', 'difference', 'when', 'why', 'how', 'Which', 'what', 'who', 'where', 'whether',
                   'is',
                   'does', 'do'}


def search_ctrlr(_str: str):
    # TODO: secondary search (continuous search) window
    # TODO: primary search (in HOTWORDS search) window
    if any(word in SEARCH_HOTWORDS for word in words):  # TODO: (experimental) list search in set
        searched_txt = search(f'{get_lang_mode()} {sentence}')
        say(f'[SEARCHED]: "{searched_txt}"')


TYPE_HOTWORDS = {'type', 'add'}


def type_ctrlr(_first_word, _sentence):
    if _first_word in TYPE_HOTWORDS:
        paste(_sentence)


def features_controller(sentence, words):
    search_ctrlr(sentence)
    type_ctrlr(words[0], sentence)
