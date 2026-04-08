# Problem: Decode Morse code into readable English text
# Approach:
# 1. Use dictionary mapping Morse → Alphabet
# 2. Split words and letters
# 3. Convert each symbol to character

morse_dict = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z"
}

def decode_morse(code):
    # Split words (3 spaces)
    words = code.strip().split("   ")
    decoded_message = []

    for word in words:
        letters = word.split()
        decoded_word = ""

        for letter in letters:
            decoded_word += morse_dict.get(letter, '?')

        decoded_message.append(decoded_word)

    return " ".join(decoded_message)


# 🔹 Example usage
if __name__ == "__main__":
    code = "... --- ..."
    print("Decoded Message:", decode_morse(code))


# 🔹 Next Step:
# Can extend to encode text → Morse (bidirectional system).
