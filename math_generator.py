import random 
import time

operand = ["+","-","*"]
min_operand = 2
max_operand = 17
total_questions = 5

def genarate_problem():
    left = random.randint(min_operand,max_operand)    
    right = random.randint(min_operand,max_operand)
    operation = random.choice(operand)

    expration= str(left) +" "+  operation +" "+ str(right) 
    # print("Question : " , expration )
    solution = eval(expration)
    solution=str(solution)
    return expration , solution
counter =0
print("Cant leave untill you answer ")

wrong =0 
input("are you ready ,press enter to start ")
print("------------------------------------")
start_time= time.time() 
for i in range(total_questions) :
    question , answer =  genarate_problem()
    while True:
        guess = input("problem no: " + str(i+1)  + ":  "+ question + ":"  )
        guess = str(guess)
        if guess != answer:
            wrong+=1
        break
        

end_time= time.time()
total_time= end_time - start_time
print("you complited the task in time " , round(total_time , 2) , "seconds and total mistakes you made ", wrong , "out of " , total_questions ) 
