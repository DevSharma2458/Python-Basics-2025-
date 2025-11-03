import sys

def reverse_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        for line in reversed(lines):
            print(line.strip())

if __name__ == "__main__":
    filename = sys.argv[1]
    reverse_file(filename)

# now in terminal run this command
'''
python reverse_file.py dev.txt

'''
'''
Explanation:

sys.argv[1] → takes the filename from command line.

f.readlines() → reads all lines into a list.

reversed(lines) → gives them in reverse order.

line.strip() → removes \n so print looks clean.

'''