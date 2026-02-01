#Magic8Ball.py
#Name:Carter Guthrie
#Date:2/1/2025
#Assignment:Lab 2
#Purpose: Create A Random Response Generator
#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  responses = ["Yes, definitely", "No, not a chance", "Ask again later", "It is certain", "Outlook not so good"]
  print("Magic 8 Ball")
  #Prompt the user for their question.
  input("Ask the Magic 8 Ball a question: ")
  #Answer question randomly with one of the options from your earlier list.
  answer = random.choice(responses)
  print(answer)

if __name__ == '__main__':
  main()
