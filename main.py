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
    
    
