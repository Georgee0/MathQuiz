# Passing a custom validation input function: inputCustom()
'''
import pyinputplus as pyip
from pyinputplus import inputCustom
print('Enter number to add to 10')
#response = pyip.inputCustom(addTenNum) 
def addTenNum(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10 not %s' %(sum(numbersList))) 
    return int(numbers)           
response = pyip.inputCustom(addTenNum)
print(response)    
'''
# How to keep am idiot busy 
'''
import pyinputplus as pyip
while True:
    prompt = 'Want to know how to keep an idiot busy for quite a long time?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'yes':
        continue
    elif response == 'no':
        break
print('Thank you for you for your time')
'''
# Multiplication Quiz
import pyinputplus as pyip
import random, time
NumberOfQuestion = 10
CorrectAnswer = 0
for QuestionNumber in range(NumberOfQuestion):
                    # Pick two random numbers
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt ='Q:%s . %s x %s = ' %(QuestionNumber,num1,num2)
    try:
        # Right answers are handled by allowRegexes
        # wrong answers are handled by blockRegexes, with na custom message
        pyip.inputStr(prompt,allowRegexes=['^%s$'%(num1*num2)], blockRegexes=['.*', 'Incorrect!'],
         timeout=8,limit=3)
    except pyip.TimeoutException:
        print('Out of time!')     
    except pyip.RetryLimitException:
        print('Out of tries!')    
    else:
        # This block runs if no exception were raised in the try block
        print('Correct!')    
        CorrectAnswer += 1  
    time.sleep(4)   # Brief pause to let user see the result.
    print('score %s / %s' %(CorrectAnswer, NumberOfQuestion))    
    
    