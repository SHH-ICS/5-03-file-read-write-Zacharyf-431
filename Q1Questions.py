# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.

filehandle=open("question.txt","w")
m = str(input("please enter a question:  "))
a = str(input("Please enter option a:  "))
b = str(input("Please enter option b:  "))
c = str(input("Please enter option c:  "))
d = str(input("Please enter option d:  "))
x = str(input("Please enter the correct answer:  "))
filehandle.write(f"{m}\n{a}\n{b}\n{c}\n{d}\n{x}\n")
filehandle.close()
