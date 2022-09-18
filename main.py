morse_alp = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--.."
}
morse_alp_rev = {}
for key, value in morse_alp.items():
    morse_alp_rev[value] = key
running = True

while running:
    choice = input("Would you like to translate English text to Morse Code (Enter 'e') or "
                   "Morse Code to English text (Enter 'm')? ").lower()

    code_list = []
    if choice == "e":
        text_input = input("Enter text to be converted to Morse Code: ").lower()
        text_lower = text_input

        for letter in text_lower:
            if letter != ' ':
                morse_let = morse_alp[letter]
                code_list.append(morse_let)

        morse_code = ' '.join(str(m) for m in code_list)

        print(f"Your text converted to Morse Code successfully!\nMorse Code for {text_input} is: {morse_code}")
    else:
        morse_input = input("Enter Morse Code to be converted to English text: ").split(' ')

        for letter in morse_input:
            eng_let = morse_alp_rev[letter]
            code_list.append(eng_let)

        eng_letters = ''.join(str(e) for e in code_list)

        print(f"Your Morse Code converted to English text successfully! (no spaces)\nMorse Code for {morse_input} is: {eng_letters}")
    cont = input("Would you like to keep translating? Y or N ").lower()
    if cont == "y":
        if choice == "e":
            keep = input("Would you like to translate this Morse Code back? Y or N  ").lower()
            if keep == "y":
                code_list = []
                morse_input = morse_code.split(' ')

                for letter in morse_input:
                    eng_let = morse_alp_rev[letter]
                    code_list.append(eng_let)

                eng_letters = ''.join(str(e) for e in code_list)

                print(f"Your Morse Code converted to English text successfully! (no spaces) \nMorse Code for {morse_input} is: {eng_letters}")

    else:
        running = False
