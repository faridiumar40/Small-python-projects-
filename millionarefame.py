questions = [
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
    ["Who invented the light bulb?", "Thomas Edison", "Albert Einstein", "Isaac Newton", "Nikola Tesla", 1],
    ["What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", 2],
    ["Which gas do plants absorb from the atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Helium", 3],
    ["What is the currency of Japan?", "Yen", "Won", "Dollar", "Euro", 1],
    ["Who painted the Mona Lisa?", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", "Claude Monet", 2],
    ["What is the boiling point of water at sea level (in °C)?", "90", "95", "100", "110", 3],
    ["Which is the fastest land animal?", "Cheetah", "Leopard", "Tiger", "Lion", 1],
    ["Who is known as the 'Father of Computers'?", "Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs", 1],
    ["Which ocean is the largest?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4]
]

prizes = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

i = 0

for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    
    a = input("Enter your answer. 1 for a , 1 for b , 3 for c , 4 for d\n")
    if str(question[5]) == a:
        print("You are correct")
        print(f"You won {prizes[i]}")
        i += 1
    else:
        print("You are wrong!")
        print(f"The correct answer is: {question[question[5]-1]}")
        break