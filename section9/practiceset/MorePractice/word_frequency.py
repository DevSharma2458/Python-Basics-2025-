import sys

def word_frequency(filename):
    with open(filename) as f:
        text = f.read().lower() # read entire file and make lowercase
        words = text.split() # split into list of words 

        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1

        for word, count in freq.items():
            print(f"{word}: {count}")

if __name__ == "__main__":
    filename = sys.argv[1]
    word_frequency(filename)



'''
Explanation:

1 - .read().lower() → makes all words lowercase (so “Apple” == “apple”).

2 - .split() → breaks text by spaces into a list.

3 - .get(word, 0) → safely gets old count or 0 if new.

4 - .items() → prints key-value pairs.

'''

# use this command in terminal to run this code but before that to your current directory
# python word_frequency.py dev.txt
