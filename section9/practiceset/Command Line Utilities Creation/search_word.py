import sys  # this helps read command-line arguments

# sys.argv is a list of values you pass when running the program
# Example: python count_lines.py tasks.txt
# sys.argv[0] -> "count_lines.py"
# sys.argv[1] -> "tasks.txt"

def search_word(word, string):
    return string.count(word)

if __name__ == "__main__":
    filename = sys.argv[1]
    word = sys.argv[2]
    with open(filename) as f:
        string = f.read()
        n = search_word(word, string)
        print(f"There are {n} occurences of {word} in the {filename}")

# in terminal type and must cd to Command Line folder
# python search_word.py dev.txt apple
