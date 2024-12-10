# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
filehandle = open("question.txt", "r")

print("Quiz")

while True:
    question = filehandle.readline().strip()
    if not question:
        break
    a = filehandle.readline().strip()
    b = filehandle.readline().strip()
    c = filehandle.readline().strip()
    d = filehandle.readline().strip()
    x = filehandle.readline().strip()

    print(question)
    print("a.", a)
    print("b.", b)
    print("c.", c)
    print("d.", d)

    y = input("Enter your answer: ")
    if y == x:
        print("You are right")
    else:
        print("You are wrong. The correct answer was:", x)

filehandle.close()

print("Good Job :)")