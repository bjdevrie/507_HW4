# Adding random module
import random

usr_input = input("What is your question? \n")

def magic_eight_ball():
	usr_input = input("What is your question? \n")
	response = usr_input

    # List of possible answers
	possible_answers = ["It is certain.", "It is decidedly so.", "Without a doubt.",
	"Yes, definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.",
	"Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.",
	"Ask again later.", "Better not tell you now.", "Cannot predict now.",
	"Concentrate and ask again.", "Don't count on it.", "My reply is no.",
	"My sources say no.", "Outlook not so good.", "Very unlikely."]

    # Using random module to select string from list
    print(random.choice(possible_answers))

magic_eight_ball()
