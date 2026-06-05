questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 2],

    ["Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Mercury", 2],

    ["Who wrote the national anthem of India?", "Bankim Chandra Chatterjee", "Sarojini Naidu", "Rabindranath Tagore", "Jawaharlal Nehru", 3],

    ["Which is the largest ocean in the world?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4],

    ["Who invented the telephone?", "Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Isaac Newton", 1],

    ["Which country gifted the Statue of Liberty to the USA?", "Germany", "France", "Canada", "Spain", 2],

    ["What is the capital of Japan?", "Beijing", "Seoul", "Tokyo", "Bangkok", 3],
]

prizes = [1000.2000,5000,10000,100000,320000,1000000]

for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    # check where the answer is correct or not

    a = int(input("Enter your answer. \n1 for a \n2 for b\n3 for c\n4 for d\n"))
    if(question[5] == a):
        print("Correct Answer")
    else:
        print(f"Incorrect, the correct answer was {question[5]}")
        print("Better luck next time!")
        break