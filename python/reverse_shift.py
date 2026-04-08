# Problem: Reverse a string and apply simple encoding
# Approach:
# 1. Reverse the string
# 2. Shift each character by +1 (ASCII)

def reverse_encode(text):
    reversed_text = text[::-1]
    encoded_text = ""

    for ch in reversed_text:
        encoded_text += chr(ord(ch) + 1)

    return encoded_text


# 🔹 Example usage
if __name__ == "__main__":
    text = "mars"
    print("Encoded Output:", reverse_encode(text))


# 🔹 Next Step:
# This can be extended into encryption algorithms (Caesar cipher / hashing).
