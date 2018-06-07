from data import questions, answers

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

    position = 0
    for i in count:
        if i == max_num:
            return position
        position += 1




wrong_answers = []

while True:
    print("Добрый день! Чем я могу помочь?")
    req = input()
    possible_answer = guess_ask(req, questions)
    print(answers[possible_answer])
    print('Помогло? Если да, то ответье да.')
    is_done = input()
    if (is_done == "да"):
        print('Спасибо, всего доброго!')
        break 
        





#print(guess_ask('Мигает связи', questions))





