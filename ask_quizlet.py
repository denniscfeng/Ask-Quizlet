from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")

@ask.launch
def start_skill():
    welcome_message = "Welcome to Ask Quizlet! Would you like to study or create a flash card set?"
    session.attributes["test_num"] = 0
    session.attributes["final_set"] = {};
    return question(welcome_message)

test_questions = ["ant", "bee", "cow", "dog"]
@ask.intent("StudyIntent")
def study():
    msg = "Please say back the word: "
    msg += test_questions[session.attributes["test_num"]]
    return question(msg)

@ask.intent("AnswerIntent")
def answer(ans):
    if ans == test_questions[session.attributes["test_num"]]:
        session.attributes['test_num'] += 1
        if session.attributes["test_num"] == len(test_questions):
            return statement("Congrats, you said all the words.")
        return study()
    return question("You fucked up.")

#Trying to create and word with a definition
@ask.intent("CreateIntent")
def create():
    msg = "Please tell the word: "
    return question(msg)

#For creating 
@ask.intent("NewWordIntent")

@ask.intent("AMAZON.StopIntent")
def exit():
    msg = "Quitting Ask Quizlet."
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)