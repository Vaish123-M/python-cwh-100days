"""
# Day 40: Exercise 4 - Secret Code Language

Build an encoder and decoder for a secret language.  For words with at least
three characters, move the first character to the end and surround the word
with three-character markers.  Short words are left unchanged.

The fixed markers make this solution deterministic and allow the decoder to
reverse exactly the transformation performed by the encoder.
"""

PREFIX = "xyz"
SUFFIX = "abc"


def encode_word(word):
    """Encode one word according to the exercise rules."""
    if len(word) < 3:
        return word
    return PREFIX + word[1:] + word[0] + SUFFIX


def decode_word(word):
    """Decode one word produced by encode_word()."""
    if len(word) < 3:
        return word
    if not (word.startswith(PREFIX) and word.endswith(SUFFIX)):
        raise ValueError("encoded word has invalid markers")
    body = word[len(PREFIX) : -len(SUFFIX)]
    if not body:
        raise ValueError("encoded word has no original content")
    return body[-1] + body[:-1]


def encode_message(message):
    """Encode every whitespace-separated word in a message."""
    return " ".join(encode_word(word) for word in message.split())


def decode_message(message):
    """Decode every whitespace-separated word in a message."""
    return " ".join(decode_word(word) for word in message.split())


message = "this is a secret"
encoded = encode_message(message)
print("Encoded:", encoded)
print("Decoded:", decode_message(encoded))

# Words shorter than three characters pass through unchanged.
print("Short word:", encode_word("to"))
