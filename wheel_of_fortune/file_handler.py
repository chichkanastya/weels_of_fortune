import linecache
import random

# def get_random_word(filename):
#     used_words = set()
#     # Подсчитываем количество строк в файле
#     with open(filename, 'r', encoding='utf-8') as f:
#         total_lines = sum(1 for _ in f)
#     random_line = random.randint(1, total_lines)
#     while random_line in used_words:
#         random_line = random.randint(1, total_lines)
#     line = linecache.getline(filename, random_line)
#     if len(used_words) == 15:
#         used_words.clear()
#     used_words.add(random_line)
#     return line.strip()
    
used_words = set()

def get_random_word(filename):
    global used_words
    
    # Подсчитываем количество строк в файле
    with open(filename, 'r', encoding='utf-8') as f:
        total_lines = sum(1 for _ in f)
    
    random_line = random.randint(1, total_lines)
    while random_line in used_words:
        random_line = random.randint(1, total_lines)
    
    line = linecache.getline(filename, random_line)
    
    if len(used_words) >= 15:
        used_words.clear()
    
    used_words.add(random_line)
    return line.strip()