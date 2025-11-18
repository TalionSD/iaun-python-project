def trim_spaces(text):
    start = 0
    end = len(text) - 1

    while start <= end and text[start] == " ":
        start += 1

    while end >= start and text[end] == " ":
        end -= 1

    return text[start:end+1]
