from helper.features.google_search import google_search
from helper.mode import set_language_mode, lang_mode
from helper.features.stt import stt
from helper.features.tts import say, handle_talk_mode

SEARCH_HOTWORDS = {'versus', 'difference', 'when', 'why', 'how', 'Which', 'what', 'who', 'where', 'whether', 'is',
                   'does', 'do'}
STOP_LISTENING_HOTWORDS = {'stop listening', 'bye'}


def handle_command(sentence):
    if sentence in STOP_LISTENING_HOTWORDS:
        exit(0)

    elif sentence == '':
        pass

    else:
        # SETUP
        sentence = str.lower(sentence)
        words = sentence.split(' ', 1)

        # COMMANDS

        # cmd - 1
        handle_talk_mode(sentence)

        if len(words) > 1:

            # cmd - 2
            if words[0] in SEARCH_HOTWORDS:
                google_search(f'{lang_mode} {sentence}')

            # cmd - 3
            elif "mode" == words[1]:
                set_language_mode(words)

        else:
            say(f'Sorry, I don\'t understand this command: {words}')


if __name__ == '__main__':
    while True:
        handle_command(stt())
