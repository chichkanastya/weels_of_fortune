import random
import linecache

def random_word_generator(filename):
    used_lines = set()
    with open(filename, 'r', encoding='utf-8') as f:
        total_lines = sum(1 for _ in f)
    while len(used_lines) < total_lines:
        random_line = random.randint(1, total_lines)
        if random_line not in used_lines:
            word = linecache.getline(filename, random_line).strip()
            if word:
                yield word
            used_lines.add(random_line)
    linecache.clearcache()