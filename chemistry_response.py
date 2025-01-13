import csv
def elements(given):
    given=given.capitalize()
    answers=''
    with open('Periodic Table of Elements.csv') as elements:
        read_file=csv.reader(elements)
        x=0
        for i in read_file:
         if x==0:
          first=i
          x+=1
         else:
          break
        index=0
        unkown=0
        for row in read_file:
            if given==row[1] or given==row[2]:
                for i in range(len(row)):
                    answers=answers+'\n'+first[i]+': '+row[i]
            else:
                unkown+=1
            index+=1
        if answers!='':
            return answers
        else:
            return 'There is no such element'

def concentration(pH):
    pass
def pH():
    pass
def molecularFormula():
    pass
