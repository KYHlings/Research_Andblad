import requests
import random
def get_quizz():
    url = requests.get('https://mqif4s7obg.execute-api.eu-central-1.amazonaws.com/olofs_lambda')
    content = url.json()['questions']
    return content


def slump():
    content = get_quizz()
    random.shuffle(content)
    return content

def get_quiz():
    content = slump()
    #print(F"Nu ska vi svara på 10 frågor, svara med sifferalternativen.")
    qNum = 0
    score = 0
    wrong_answer_and_question = []
    for q in content[:1]:
        qNum += 1
        lista = []
        #lista.append(q['rightAnswer'])
        #for wA in q['wrongAnswers']:
            #lista.append(wA)
        random.shuffle(lista)
        #print(f"Fråga {qNum}: {q['prompt']}")
        for A in lista:
            pass
            #print(f"{lista.index(A) + 1}:{A}")
        return q['prompt'],q['rightAnswer'],q['wrongAnswers']
       ## try:
           # if int(sv) == (lista.index(q['rightAnswer']) + 1):
               # print("Rätt!")
                #score = score + 1
            #else:
                #score += 1
                #print(f"Fel, rätt svar är {lista.index(q['rightAnswer']) + 1}: {q['rightAnswer']}")
                #t = q['prompt'],q['rightAnswer']
                #wrong_answer_and_question.append(t)
        #except ValueError:
            #print("---")
            #print(f"Svara med en siffra mellan 1 och {len(lista)}.")
            #print(f"Rätt svar är {lista.index(q['rightAnswer']) + 1}: {q['rightAnswer']}")
            #print("Försök på nästa fråga")
            #print("---")
            #t = q['prompt'],q['rightAnswer']
            #wrong_answer_and_question.append(t)

    #print("***Resultat***")
    #print(f"Du fick {score} rätt")

    #if len(wrong_answer_and_question) > 0 :
        #print(f"Följande fågor var fel.")
        #for wa in wrong_answer_and_question:
            #print(f"Frågan: {wa[0]}. Rätt svar: {wa[1]}")

        #return q['rightAnswer'],q['prompt'],q['wrongAnswer']

print(get_quiz())