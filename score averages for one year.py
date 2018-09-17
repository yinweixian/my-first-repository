#matthew walker
#9/17/18
#averaging test scores
def TestAvarage():
    #assigning variables
    TimesRepeated = 0
    OverallScore = 0
    #creating while loop, loop repeates 10 times getting
    #a score form the user every time
    while TimesRepeated<10:
        #getting score
        score=input("what was your test score this time?")
        #converting to a float
        score=float(score)
        #adding each score to the overall score
        OverallScore=OverallScore+score
        #tracking how many times the loop has run
        TimesRepeated=TimesRepeated+1
    #finding the average score
    AverageScore=OverallScore/TimesRepeated
    #printing the average score
    print("your avarage score for the year is",AverageScore)
#running the program
TestAvarage()
input("press enter to end code")
