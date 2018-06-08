from nltk.tokenize import sent_tokenize


def question_asked():
    try:
        with open('questions.txt') as q:
            questions = q.read()
            a = sent_tokenize(questions)
            return a
    except FileNotFoundError:
        pass
