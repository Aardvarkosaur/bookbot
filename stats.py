def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_character_counts(character_counts):
    char_list = []
    for char, count in character_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    char_list.sort(key=lambda item: item['num'], reverse=True)
    return char_list