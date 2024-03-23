import random


def split_sentence_randomly(sentence):
    """
    Split a sentence into words and then randomly divide each word into two parts.
    Combine these parts into two separate sentences.
    """
    first_word, second_word = sentence.split()[:2]

    # Split the sentence into words
    words = sentence.split()

    sentence1_parts, sentence2_parts = [], []

    for word in words:
        # For words longer than 1 character, choose a random split point
        if len(word) > 1:
            split_point = random.randint(1, len(word) - 1)
            part1, part2 = word[:split_point], word[split_point:]
        else:
            # Single-character words can't be split; add the whole word to the first part, and use a space for the second
            part1, part2 = word, ' '
        sentence1_parts.append(part1)
        sentence2_parts.append(part2)
        # Append a comma to each part for separation
        sentence1_parts.append(',')
        sentence2_parts.append(',')

    # Remove the last comma from each part list
    sentence1_parts = sentence1_parts[:-1]
    sentence2_parts = sentence2_parts[:-1]

    # Join the parts without spaces (as per original code) and enclose in brackets
    sentence1 = f"[{''.join(sentence1_parts)}]"
    sentence2 = f"[{''.join(sentence2_parts)}]"

    return sentence1, sentence2, first_word, second_word

