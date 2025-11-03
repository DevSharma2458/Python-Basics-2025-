import sys

def count_lines(filename):
    with open(filename) as f:
        return len(f.readlines())
    

if __name__ == "__main__":
    filename = sys.argv[1]
    num_lines = count_lines(filename)
    print(f"There are {num_lines} lines in {filename}")

    # In terminal cd to current folder which Command Line 
    # then in terminal paste this 
    # python count_lines.py dev.txt