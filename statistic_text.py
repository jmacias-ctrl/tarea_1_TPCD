def wpc_total(content):
    text_paragraphs = [x for x in content.splitlines() if x]
    count = 0
    total_char = 0
    total_char_b = 0
    set_words = set()
    for string in text:
        words = string.split()
        total_char += len(string)
        total_char_b += sum(map(len,string.split()))
        count += len(words)
        set_words.update(words)
    return len(text), count, len(set_words), total_char, total_char_b
    