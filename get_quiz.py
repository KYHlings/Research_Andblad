import requests

def get_quiz():
    url = requests.get('https://mqif4s7obg.execute-api.eu-central-1.amazonaws.com/olofs_lambda')
    content = url.json()['questions']

    questions = []
    right_answer = []
    wrong_answers = []
    for i in content:
        questions.append(i['prompt'])
        right_answer.append(i['rightAnswer'])
        wrong_answers.append(i['wrongAnswers'])


    return questions,right_answer,wrong_answers


print(get_quiz())