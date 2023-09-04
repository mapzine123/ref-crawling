import re

patterns_to_remove = []
# remove_patterns에 저장된 패턴을 읽어와 해당 패턴이면 번역하지 않음
def remove_word(text):
    with open('static/remove_patterns.txt', 'r') as file:
        for line in file:
            patterns_to_remove.append(line.strip())

    for pattern in patterns_to_remove:
        text = re.sub(pattern, '', text)

    return text