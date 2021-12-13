from pydub import AudioSegment          # for manipulating sound files and applying effects to sound
from playsound import playsound         # for playing sound in the python program

dot = AudioSegment.from_mp3('dot.mp3')
line = AudioSegment.from_mp3('line.mp3')

# Silence segment for 1000 milliseconds
# AudioSegment.silent(1000)


MORSE_CODE_DICT = {
        'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
                   }

reversed_morse_code_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
print(reversed_morse_code_dict)

def input_text():
    text = input('Enter text to encrypt/decrypt: ').upper()
    return text


user_input = input_text()
print(user_input)


def encode_text(input_from_user):
    encoded_text_list = []
    encoded_audio = AudioSegment.silent(1)

    for char in input_from_user:
        if char == ' ':
            encoded_text_list.append('       ')
            encoded_audio = encoded_audio + AudioSegment.silent(490)
        elif char in MORSE_CODE_DICT:
            encoded_text_list.append(MORSE_CODE_DICT[char])
            encoded_text_list.append('   ')
            encoded_audio = encoded_audio + AudioSegment.silent(210)
            for morse in MORSE_CODE_DICT[char]:
                if morse == '.':
                    encoded_audio = encoded_audio + dot
                elif morse == '-':
                    encoded_audio = encoded_audio + line
                encoded_audio = encoded_audio + AudioSegment.silent(70)

    encoded_text = "".join(encoded_text_list)
    print(encoded_text)
    encoded_audio.export('encoded_audio.mp3')
    playsound('encoded_audio.mp3')
    return encoded_text


def decode_text(input_from_user):
    decoded_text_list = []
    words_list = input_from_user.split('       ')
    for word in words_list:
        letters_list = word.split('   ')
        for letter in letters_list:
            if letter in reversed_morse_code_dict:
                decoded_text_list.append(reversed_morse_code_dict[letter])
        decoded_text_list.append(' ')

    decoded_text = ''.join(decoded_text_list)

    return decoded_text


if user_input[0] in MORSE_CODE_DICT:
    print(encode_text(user_input))
elif user_input[0] in reversed_morse_code_dict:
    print(decode_text(user_input))

