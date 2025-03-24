import os
import re 
from collections import Counter


def count_rebecca(text):
    return len(re.findall(r'\bRebecca\b', text))

def top_frequent_words(text, min_length=4, top_n=5):
    words = re.findall(r'\b[a-zA-Z]{%d,}\b' %min_length, text.lower())
    return Counter(words).most_common(top_n)


if __name__ == "__main__":
    cur_dir = os.path.dirname(__file__)
    with open(os.path.join(cur_dir, "example.txt"), "r", encoding="utf-8") as f:
        text = f.read()
    
    print(count_rebecca(text))
    print(top_frequent_words(text))
    
    