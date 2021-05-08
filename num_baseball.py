#coding=utf-8
import random
import string
# 원하는 자리수를 입력하면 해당 자리수의 숫자를 랜덤하게 반환
def set_answer(size):
    return str(random.randint(pow(10,size-1),pow(10,size)-1))

# 숫자 추리에 성공했는지 알려줌
def is_over(answer, guess):
    if answer==guess:
        return True
    else:
        return False

# 제대로 된 입력이 들어왔는지 확인함
def is_right_input(size, my_answer):
    right_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(my_answer)):
        if my_answer[i] not in right_char:
            return False
    if len(my_answer)!=size:
        return False
    else:
        return True

# user에게서 입력을 받아옴
def set_guess(size):
    guess = input("Enter the numbers: ")
    while not is_right_input(size, guess):
        guess=input("Wrong input, Enter the numbers again: ")
    return guess

# 추리 결과를 프린트 함
def print_score(answer, guess):
    s = 0
    b = 0
    fscore = ""
    for i in range(3):
        if guess[i] == answer[i]:
            s += 1
        else:
            if answer[i] in guess:
                b += 1
    fscore = str(s) + "S" + str(b) + "B"
    print(fscore)

# main
size = 3
answer = set_answer(size)
attempt = 0
guess = ""

is_end = False
while not is_end:
    attempt += 1
    guess = set_guess(size)
    if is_over(answer, guess):
        print("NICE GUESS! THE ANSWER WAS %s" %answer)
        print("YOUR ATTEMPT: %d" %attempt)
        is_end = True
    else:
        print_score(answer, guess)
