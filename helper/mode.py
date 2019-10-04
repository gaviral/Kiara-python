from helper.features.tts import say


def set_language_mode(words):
    global lang_mode
    if "normal" in words:
        lang_mode = NO_LANG
    else:
        lang_mode = words[0]
    say(f'Language Mode: {lang_mode}')


NO_LANG = ""
lang_mode = NO_LANG
