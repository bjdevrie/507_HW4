def add_questions():
    pass


while True:
    usr_input = str(input("\nWhat is your question?\n"))
    if usr_input.lower() == 'quit':
        break
    if usr_input.endswith('?') == True:
        pass  #random print statement from "add questions" go here
    else:
        print ("I'm sorry, I can only answer questions.")
