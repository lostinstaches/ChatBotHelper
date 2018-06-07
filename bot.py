from data import questions, answers
from heapq import nlargest

def guess_ask(str, questions):
    str = str.lower()
    words_apart = str.split()
    count = []

    for sentence in questions:
        occurrences = 0
        sentence = sentence.lower()
        for i in range(len(words_apart)):
            if len(words_apart[i]) > 4:
                word = words_apart[i]
                short_form = word [:4]
                occurrences += sentence.count(short_form)
            else:
                occurrences += sentence.count(words_apart[i])
        count.append(occurrences)

    max_num = max(count)
    # maxnumbers = nlargest(3, count)
    # positions = []
    #position = 0
    # for i in maxnumbers:
    #     positions.append(count.index(i))
    return count.index(max_num)
    # for i in count:
    #     if i == max_num:
    #         return position
    #     position += 1




#wrong_answers = []
tempanswers = answers
tempquestions = questions
while True:
    print("Добрый день! Чем я могу помочь?")
    req = input()
    possible_answer = guess_ask(req, tempquestions)
    print(tempanswers[possible_answer])
    print('Помогло? Если да, то ответье да.')
    is_done = input()
    if (is_done == "да"):
        print('Спасибо, всего доброго!')
        break 
    del tempquestions[possible_answer]
    del tempanswers[possible_answer]
        





#print(guess_ask('Мигает связи', questions))





