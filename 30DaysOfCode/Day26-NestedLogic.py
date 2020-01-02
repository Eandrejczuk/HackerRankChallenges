
# https://www.hackerrank.com/challenges/30-nested-logic/problem

def calculateFine(dayR, monthR, yearR, dayDue, monthDue, yearDue):
    if yearR < yearDue:
        return 0
    if yearR == yearDue:
        if monthR <= monthDue:
            if dayR <= dayDue:
                return 0
            else:
                return 15*(dayR-dayDue)
        else:
            return 500*(monthR-monthDue)

    else:
        return 10000


dayR, monthR, yearR = 9, 6, 2015
dayDue, monthDue, yearDue = 6, 6, 2015

print(calculateFine(dayR, monthR, yearR, dayDue, monthDue, yearDue))
