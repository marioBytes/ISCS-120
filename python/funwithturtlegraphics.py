'''
Mario Martinez
6/14/18

This program prompts the user for an integer to draw each square.
After the intiger is entered a square is drawn.

Time spent: 5 hours

Honor Code: I pledge that this program represents my own
program code. I received help from no one in designing and debugging my program.
'''

import turtle


def mainOne():
    choice = int(input('Enter 1 for square one '))#propmt user

    if choice == 1:
        drawSquareOne()#call the first square funtion

def drawSquareOne():
    turtle.pendown()
    turtle.pensize(1)
    turtle.color("red")
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainOne()#call the first main function


def mainTwo():
    choice = int(input('Enter 2 for square two '))#prompt user

    if choice == 2:
        drawSquareTwo()#call the square function

def drawSquareTwo():
    turtle.rt(30)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainTwo()#call main function two


def mainThree():
    choice = int(input('Enter 3 for square three '))#prompt user

    if choice == 3:
        drawSquareThree()#call the square function

def drawSquareThree():
    turtle.rt(30)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainThree()#call main function three

def mainFour():
    choice = int(input('Enter 4 for square four '))#propmt user

    if choice == 4:
        drawSquareFour()#call the square function 

def drawSquareFour():
    turtle.rt(30)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainFour()#call main function four


def mainFive():
    choice = int(input('Enter 5 for square five '))#propmt user

    if choice == 5:
        drawSquareFive()#call the square function

def drawSquareFive():
    turtle.rt(30)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainFive()#call main function five


def mainSix():
    choice = int(input('Enter 6 for square six '))#propmt user

    if choice == 6:
        drawSquareSix()#call the square function

def drawSquareSix():
    turtle.rt(30)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainSix()#call main function six


def mainSeven():
    choice = int(input('Enter 7 for square seven '))#prompt user

    if choice == 7:
        drawSquareSeven()#call the square function

def drawSquareSeven():
    turtle.rt(10)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainSeven()#call main function seven


def mainEight():
    choice = int(input('Enter 8 for square eight '))#prompt user

    if choice == 8:
        drawSquareEight()#call the square function

def drawSquareEight():
    turtle.rt(10)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainEight()#call main function eight


def mainNine():
    choice = int(input('Enter 9 for square nine '))#propmt user

    if choice == 9:#call the sqaure function
        drawSquareNine()

def drawSquareNine():
    turtle.rt(10)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainNine()#call the main function nine


def mainTen():
    choice = int(input('Enter 10 for square ten '))#propmt user

    if choice == 10:
        drawSquareTen()#call square function

def drawSquareTen():
    turtle.rt(10)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainTen()#call the main function


def mainEleven():
    choice = int(input('Enter 11 for square eleven '))#propmt user

    if choice == 11:
        drawSquareEleven()#call square function

def drawSquareEleven():
    turtle.rt(10)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainEleven()#call the main function eleven


def mainTwelve():
    choice = int(input('Enter 12 for sqaure twelve '))#prompt user

    if choice == 12:
        drawSquareTwelve()#call square function

def drawSquareTwelve():
    turtle.rt(10)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainTwelve()#call the main function twelve


def mainThirteen():
    choice = int(input('Enter 13 for square thirteen '))#prompt user

    if choice == 13:
        drawSquareThirteen()#call sqaure function

def drawSquareThirteen():
    turtle.rt(40)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainThirteen()#call main function thirteen


def mainFourteen():
    choice = int(input('Enter 14 for square fourteen '))#prompt user

    if choice == 14:
        drawSquareFourteen()#call sqaure function

def drawSquareFourteen():
    turtle.rt(40)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainFourteen()#call main function fourteen


def mainFifteen():
    choice = int(input('Enter 15 for square fifteen '))#prompt user

    if choice == 15:
        drawSquareFifteen()#call sqaure function

def drawSquareFifteen():
    turtle.rt(40)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainFifteen()#call main function Fifteen


def mainSixteen():
    choice = int(input('Enter 16 for square Sixteen '))#prompt user

    if choice == 16:
        drawSquareThirteen()#call sqaure function

def drawSquareSixteen():
    turtle.rt(40)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainSixteen()#call main function sixteen


def mainSeventeen():
    choice = int(input('Enter 17 for square seventeen '))#prompt user

    if choice == 17:
        drawSquareSeventeen()#call sqaure function

def drawSquareSeventeen():
    turtle.rt(40)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainSeventeen()#call main function seventeen


def mainEighteen():
    choice = int(input('Enter 18 for square eighteen '))#prompt user

    if choice == 18:
        drawSquareEighteen()#call sqaure function

def drawSquareEighteen():
    turtle.rt(40)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainEighteen()#call main function Eighteen


def mainNineteen():
    choice = int(input('Enter 19 for square nineteen '))#prompt user

    if choice == 19:
        drawSquareNineteen()#call sqaure function

def drawSquareNineteen():
    turtle.rt(50)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainNineteen()#call main function nineteen


def mainTwenty():
    choice = int(input('Enter 20 for square twenty '))#prompt user

    if choice == 20:
        drawSquareTwenty()#call sqaure function

def drawSquareTwenty():
    turtle.rt(50)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainTwenty()#call main function twenty


def mainTwentyOne():
    choice = int(input('Enter 21 for square twenty-one '))#prompt user

    if choice == 21:
        drawSquareTwentyOne()#call sqaure function

def drawSquareTwentyOne():
    turtle.rt(50)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainTwentyOne()#call main function twenty-one


def mainTwentyTwo():
    choice = int(input('Enter 22 for square twenty-two '))#prompt user

    if choice == 22:
        drawSquareTwentyTwo()#call sqaure function

def drawSquareTwentyTwo():
    turtle.rt(50)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainTwentyTwo()#call main function twenty-two


def mainTwentyThree():
    choice = int(input('Enter 23 for square twenty-three '))#prompt user

    if choice == 23:
        drawSquareTwentyThree()#call sqaure function

def drawSquareTwentyThree():
    turtle.rt(50)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainTwentyThree()#call main function twenty-three


def mainTwentyFour():
    choice = int(input('Enter 24 for square twenty-four '))#prompt user

    if choice == 24:
        drawSquareTwentyFour()#call sqaure function

def drawSquareTwentyFour():
    turtle.rt(50)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainTwentyFour()#call main function twenty-four


def mainTwentyFive():
    choice = int(input('Enter 25 for square twenty-five '))#prompt user

    if choice == 25:
        drawSquareTwentyFive()#call sqaure function

def drawSquareTwentyFive():
    turtle.rt(50)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainTwentyFive()#call main function twenty-five


def mainTwentySix():
    choice = int(input('Enter 26 for square twenty-six '))#prompt user

    if choice == 26:
        drawSquareTwentySix()#call sqaure function

def drawSquareTwentySix():
    turtle.rt(70)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainTwentySix()#call main function twenty-six


def mainTwentySeven():
    choice = int(input('Enter 27 for square twenty-seven '))#prompt user

    if choice == 27:
        drawSquareTwentySeven()#call sqaure function

def drawSquareTwentySeven():
    turtle.rt(70)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainTwentySeven()#call main function twenty-seven


def mainTwentyEight():
    choice = int(input('Enter 28 for square twenty-eight '))#prompt user

    if choice == 28:
        drawSquareTwentyEight()#call sqaure function

def drawSquareTwentyEight():
    turtle.rt(70)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainTwentyEight()#call main function twenty-eight


def mainTwentyNine():
    choice = int(input('Enter 29 for square twenty-nine '))#prompt user

    if choice == 29:
        drawSquareTwentyNine()#call sqaure function

def drawSquareTwentyNine():
    turtle.rt(70)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainTwentyNine()#call main function twenty-nine


def mainThirty():
    choice = int(input('Enter 30 for square thirty '))#prompt user

    if choice == 30:
        drawSquareThirty()#call sqaure function

def drawSquareThirty():
    turtle.rt(70)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainThirty()#call main function thirty


def mainThirtyOne():
    choice = int(input('Enter 31 for square thirty-one '))#prompt user

    if choice == 31:
        drawSquareThirtyOne()#call sqaure function

def drawSquareThirtyOne():
    turtle.rt(70)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainThirtyOne()#call main function thirty-one


def mainThirtyTwo():
    choice = int(input('Enter 32 for square thirty-two '))#prompt user

    if choice == 32:
        drawSquareThirtyTwo()#call sqaure function

def drawSquareThirtyTwo():
    turtle.rt(70)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainThirtyTwo()#call main function thirty-two


def mainThirtyThree():
    choice = int(input('Enter 33 for square thirty-three '))#prompt user

    if choice == 33:
        drawSquareThirtyThree()#call sqaure function

def drawSquareThirtyThree():
    turtle.rt(70)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainThirtyThree()#call main function thirty-three


def mainThirtyFour():
    choice = int(input('Enter 34 for square thirty-four '))#prompt user

    if choice == 34:
        drawSquareThirtyFour()#call sqaure function

def drawSquareThirtyFour():
    turtle.rt(70)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainThirtyFour()#call main function thirty-four


def mainThirtyFive():
    choice = int(input('Enter 35 for square thirty-five '))#prompt user

    if choice == 35:
        drawSquareThirtyFive()#call sqaure function

def drawSquareThirtyFive():
    turtle.rt(70)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainThirtyFive()#call main function thirty-five


def mainThirtySix():
    choice = int(input('Enter 36 for square thirty-six '))#prompt user

    if choice == 36:
        drawSquareThirtySix()#call sqaure function

def drawSquareThirtySix():
    turtle.rt(70)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainThirtySix()#call main function thirty-six


def mainThirtySeven():
    choice = int(input('Enter 37 for square thirty-seven '))#prompt user

    if choice == 37:
        drawSquareThirtySeven()#call sqaure function

def drawSquareThirtySeven():
    turtle.rt(70)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainThirtySeven()#call main function thirty-seven


def mainThirtyEight():
    choice = int(input('Enter 38 for square thirty-eight '))#prompt user

    if choice == 38:
        drawSquareThirtyEight()#call sqaure function

def drawSquareThirtyEight():
    turtle.rt(70)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainThirtyEight()#call main function thirty-eight


def mainThirtyNine():
    choice = int(input('Enter 39 for square thirty-nine '))#prompt user

    if choice == 39:
        drawSquareThirtyNine()#call sqaure function

def drawSquareThirtyNine():
    turtle.rt(70)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainThirtyNine()#call main function thirty-nine


def mainFourty():
    choice = int(input('Enter 40 for square fourty '))#prompt user

    if choice == 40:
        drawSquareThirty()#call sqaure function

def drawSquareFourty():
    turtle.rt(70)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainFourty()#call main function fourty


def mainFourtyOne():
    choice = int(input('Enter 41 for square fourty-one '))#prompt user

    if choice == 41:
        drawSquareThirty()#call sqaure function

def drawSquareFourtyOne():
    turtle.rt(70)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)

mainFourtyOne()#call main function fourty-one



def mainOne():
    choice = int(input('Enter 1 for square one '))#propmt user

    if choice == 1:
        drawSquareOne()#call the first square funtion

def drawSquareOne():
    turtle.home()
    turtle.pendown()
    turtle.pensize(1)
    turtle.color("red")
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainOne()#call the first main function


def mainTwo():
    choice = int(input('Enter 2 for square two '))#prompt user

    if choice == 2:
        drawSquareTwo()#call the square function

def drawSquareTwo():
    turtle.rt(30)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainTwo()#call main function two


def mainThree():
    choice = int(input('Enter 3 for square three '))#prompt user

    if choice == 3:
        drawSquareThree()#call the square function

def drawSquareThree():
    turtle.rt(30)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainThree()#call main function three

def mainFour():
    choice = int(input('Enter 4 for square four '))#propmt user

    if choice == 4:
        drawSquareFour()#call the square function 

def drawSquareFour():
    turtle.rt(30)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainFour()#call main function four


def mainFive():
    choice = int(input('Enter 5 for square five '))#propmt user

    if choice == 5:
        drawSquareFive()#call the square function

def drawSquareFive():
    turtle.rt(30)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainFive()#call main function five


def mainSix():
    choice = int(input('Enter 6 for square six '))#propmt user

    if choice == 6:
        drawSquareSix()#call the square function

def drawSquareSix():
    turtle.rt(30)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainSix()#call main function six


def mainSeven():
    choice = int(input('Enter 7 for square seven '))#prompt user

    if choice == 7:
        drawSquareSeven()#call the square function

def drawSquareSeven():
    turtle.rt(10)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainSeven()#call main function seven


def mainEight():
    choice = int(input('Enter 8 for square eight '))#prompt user

    if choice == 8:
        drawSquareEight()#call the square function

def drawSquareEight():
    turtle.rt(10)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainEight()#call main function eight


def mainNine():
    choice = int(input('Enter 9 for square nine '))#propmt user

    if choice == 9:#call the sqaure function
        drawSquareNine()

def drawSquareNine():
    turtle.rt(10)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainNine()#call the main function nine


def mainTen():
    choice = int(input('Enter 10 for square ten '))#propmt user

    if choice == 10:
        drawSquareTen()#call square function

def drawSquareTen():
    turtle.rt(10)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainTen()#call the main function


def mainEleven():
    choice = int(input('Enter 11 for square eleven '))#propmt user

    if choice == 11:
        drawSquareEleven()#call square function

def drawSquareEleven():
    turtle.rt(10)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainEleven()#call the main function eleven


def mainTwelve():
    choice = int(input('Enter 12 for sqaure twelve '))#prompt user

    if choice == 12:
        drawSquareTwelve()#call square function

def drawSquareTwelve():
    turtle.rt(10)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainTwelve()#call the main function twelve


def mainThirteen():
    choice = int(input('Enter 13 for square thirteen '))#prompt user

    if choice == 13:
        drawSquareThirteen()#call sqaure function

def drawSquareThirteen():
    turtle.rt(40)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainThirteen()#call main function thirteen


def mainFourteen():
    choice = int(input('Enter 14 for square fourteen '))#prompt user

    if choice == 14:
        drawSquareFourteen()#call sqaure function

def drawSquareFourteen():
    turtle.rt(40)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainFourteen()#call main function fourteen


def mainFifteen():
    choice = int(input('Enter 15 for square fifteen '))#prompt user

    if choice == 15:
        drawSquareFifteen()#call sqaure function

def drawSquareFifteen():
    turtle.rt(40)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
mainFifteen()#call main function Fifteen


def mainSixteen():
    choice = int(input('Enter 16 for square Sixteen '))#prompt user

    if choice == 16:
        drawSquareThirteen()#call sqaure function

def drawSquareSixteen():
    turtle.rt(40)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainSixteen()#call main function sixteen


def mainSeventeen():
    choice = int(input('Enter 17 for square seventeen '))#prompt user

    if choice == 17:
        drawSquareSeventeen()#call sqaure function

def drawSquareSeventeen():
    turtle.rt(40)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainSeventeen()#call main function seventeen


def mainEighteen():
    choice = int(input('Enter 18 for square eighteen '))#prompt user

    if choice == 18:
        drawSquareEighteen()#call sqaure function

def drawSquareEighteen():
    turtle.rt(40)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainEighteen()#call main function Eighteen


def mainNineteen():
    choice = int(input('Enter 19 for square nineteen '))#prompt user

    if choice == 19:
        drawSquareNineteen()#call sqaure function

def drawSquareNineteen():
    turtle.rt(50)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainNineteen()#call main function nineteen


def mainTwenty():
    choice = int(input('Enter 20 for square twenty '))#prompt user

    if choice == 20:
        drawSquareTwenty()#call sqaure function

def drawSquareTwenty():
    turtle.rt(50)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainTwenty()#call main function twenty


def mainTwentyOne():
    choice = int(input('Enter 21 for square twenty-one '))#prompt user

    if choice == 21:
        drawSquareTwentyOne()#call sqaure function

def drawSquareTwentyOne():
    turtle.rt(50)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainTwentyOne()#call main function twenty-one


def mainTwentyTwo():
    choice = int(input('Enter 22 for square twenty-two '))#prompt user

    if choice == 22:
        drawSquareTwentyTwo()#call sqaure function

def drawSquareTwentyTwo():
    turtle.rt(50)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainTwentyTwo()#call main function twenty-two


def mainTwentyThree():
    choice = int(input('Enter 23 for square twenty-three '))#prompt user

    if choice == 23:
        drawSquareTwentyThree()#call sqaure function

def drawSquareTwentyThree():
    turtle.rt(50)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainTwentyThree()#call main function twenty-three


def mainTwentyFour():
    choice = int(input('Enter 24 for square twenty-four '))#prompt user

    if choice == 24:
        drawSquareTwentyFour()#call sqaure function

def drawSquareTwentyFour():
    turtle.rt(50)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainTwentyFour()#call main function twenty-four


def mainTwentyFive():
    choice = int(input('Enter 25 for square twenty-five '))#prompt user

    if choice == 25:
        drawSquareTwentyFive()#call sqaure function

def drawSquareTwentyFive():
    turtle.rt(50)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
mainTwentyFive()#call main function twenty-five


def mainTwentySix():
    choice = int(input('Enter 26 for square twenty-six '))#prompt user

    if choice == 26:
        drawSquareTwentySix()#call sqaure function

def drawSquareTwentySix():
    turtle.rt(70)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainTwentySix()#call main function twenty-six


def mainTwentySeven():
    choice = int(input('Enter 27 for square twenty-seven '))#prompt user

    if choice == 27:
        drawSquareTwentySeven()#call sqaure function

def drawSquareTwentySeven():
    turtle.rt(70)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainTwentySeven()#call main function twenty-seven


def mainTwentyEight():
    choice = int(input('Enter 28 for square twenty-eight '))#prompt user

    if choice == 28:
        drawSquareTwentyEight()#call sqaure function

def drawSquareTwentyEight():
    turtle.rt(70)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainTwentyEight()#call main function twenty-eight


def mainTwentyNine():
    choice = int(input('Enter 29 for square twenty-nine '))#prompt user

    if choice == 29:
        drawSquareTwentyNine()#call sqaure function

def drawSquareTwentyNine():
    turtle.rt(70)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainTwentyNine()#call main function twenty-nine


def mainThirty():
    choice = int(input('Enter 30 for square thirty '))#prompt user

    if choice == 30:
        drawSquareThirty()#call sqaure function

def drawSquareThirty():
    turtle.rt(70)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainThirty()#call main function thirty


def mainThirtyOne():
    choice = int(input('Enter 31 for square thirty-one '))#prompt user

    if choice == 31:
        drawSquareThirtyOne()#call sqaure function

def drawSquareThirtyOne():
    turtle.rt(70)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainThirtyOne()#call main function thirty-one


def mainThirtyTwo():
    choice = int(input('Enter 32 for square thirty-two '))#prompt user

    if choice == 32:
        drawSquareThirtyTwo()#call sqaure function

def drawSquareThirtyTwo():
    turtle.rt(70)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
mainThirtyTwo()#call main function thirty-two


def mainThirtyThree():
    choice = int(input('Enter 33 for square thirty-three '))#prompt user

    if choice == 33:
        drawSquareThirtyThree()#call sqaure function

def drawSquareThirtyThree():
    turtle.rt(70)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainThirtyThree()#call main function thirty-three


def mainThirtyFour():
    choice = int(input('Enter 34 for square thirty-four '))#prompt user

    if choice == 34:
        drawSquareThirtyFour()#call sqaure function

def drawSquareThirtyFour():
    turtle.rt(70)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainThirtyFour()#call main function thirty-four


def mainThirtyFive():
    choice = int(input('Enter 35 for square thirty-five '))#prompt user

    if choice == 35:
        drawSquareThirtyFive()#call sqaure function

def drawSquareThirtyFive():
    turtle.rt(70)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainThirtyFive()#call main function thirty-five


def mainThirtySix():
    choice = int(input('Enter 36 for square thirty-six '))#prompt user

    if choice == 36:
        drawSquareThirtySix()#call sqaure function

def drawSquareThirtySix():
    turtle.rt(70)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainThirtySix()#call main function thirty-six


def mainThirtySeven():
    choice = int(input('Enter 37 for square thirty-seven '))#prompt user

    if choice == 37:
        drawSquareThirtySeven()#call sqaure function

def drawSquareThirtySeven():
    turtle.rt(70)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainThirtySeven()#call main function thirty-seven


def mainThirtyEight():
    choice = int(input('Enter 38 for square thirty-eight '))#prompt user

    if choice == 38:
        drawSquareThirtyEight()#call sqaure function

def drawSquareThirtyEight():
    turtle.rt(70)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainThirtyEight()#call main function thirty-eight


def mainThirtyNine():
    choice = int(input('Enter 39 for square thirty-nine '))#prompt user

    if choice == 39:
        drawSquareThirtyNine()#call sqaure function

def drawSquareThirtyNine():
    turtle.rt(70)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainThirtyNine()#call main function thirty-nine


def mainFourty():
    choice = int(input('Enter 40 for square fourty '))#prompt user

    if choice == 40:
        drawSquareThirty()#call sqaure function

def drawSquareFourty():
    turtle.rt(70)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
mainFourty()#call main function fourty


def mainFourtyOne():
    choice = int(input('Enter 41 for square fourty-one '))#prompt user

    if choice == 41:
        drawSquareThirty()#call sqaure function

def drawSquareFourtyOne():
    turtle.rt(70)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)
    turtle.rt(90)
    turtle.fd(125)

mainFourtyOne()#call main function fourty-one


##########################################################

def mainOne():
    choice = int(input('Enter 1 for square one '))#propmt user

    if choice == 1:
        drawSquareOne()#call the first square funtion

def drawSquareOne():
    turtle.home()
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainOne()#call the first main function


def mainTwo():
    choice = int(input('Enter 2 for square two '))#prompt user

    if choice == 2:
        drawSquareTwo()#call the square function

def drawSquareTwo():
    turtle.rt(30)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainTwo()#call main function two


def mainThree():
    choice = int(input('Enter 3 for square three '))#prompt user

    if choice == 3:
        drawSquareThree()#call the square function

def drawSquareThree():
    turtle.rt(30)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainThree()#call main function three

def mainFour():
    choice = int(input('Enter 4 for square four '))#propmt user

    if choice == 4:
        drawSquareFour()#call the square function 

def drawSquareFour():
    turtle.rt(30)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainFour()#call main function four


def mainFive():
    choice = int(input('Enter 5 for square five '))#propmt user

    if choice == 5:
        drawSquareFive()#call the square function

def drawSquareFive():
    turtle.rt(30)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainFive()#call main function five


def mainSix():
    choice = int(input('Enter 6 for square six '))#propmt user

    if choice == 6:
        drawSquareSix()#call the square function

def drawSquareSix():
    turtle.rt(30)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainSix()#call main function six


def mainSeven():
    choice = int(input('Enter 7 for square seven '))#prompt user

    if choice == 7:
        drawSquareSeven()#call the square function

def drawSquareSeven():
    turtle.rt(10)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainSeven()#call main function seven


def mainEight():
    choice = int(input('Enter 8 for square eight '))#prompt user

    if choice == 8:
        drawSquareEight()#call the square function

def drawSquareEight():
    turtle.rt(10)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainEight()#call main function eight


def mainNine():
    choice = int(input('Enter 9 for square nine '))#propmt user

    if choice == 9:#call the sqaure function
        drawSquareNine()

def drawSquareNine():
    turtle.rt(10)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainNine()#call the main function nine


def mainTen():
    choice = int(input('Enter 10 for square ten '))#propmt user

    if choice == 10:
        drawSquareTen()#call square function

def drawSquareTen():
    turtle.rt(10)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainTen()#call the main function


def mainEleven():
    choice = int(input('Enter 11 for square eleven '))#propmt user

    if choice == 11:
        drawSquareEleven()#call square function

def drawSquareEleven():
    turtle.rt(10)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainEleven()#call the main function eleven


def mainTwelve():
    choice = int(input('Enter 12 for sqaure twelve '))#prompt user

    if choice == 12:
        drawSquareTwelve()#call square function

def drawSquareTwelve():
    turtle.rt(10)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainTwelve()#call the main function twelve


def mainThirteen():
    choice = int(input('Enter 13 for square thirteen '))#prompt user

    if choice == 13:
        drawSquareThirteen()#call sqaure function

def drawSquareThirteen():
    turtle.rt(40)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainThirteen()#call main function thirteen


def mainFourteen():
    choice = int(input('Enter 14 for square fourteen '))#prompt user

    if choice == 14:
        drawSquareFourteen()#call sqaure function

def drawSquareFourteen():
    turtle.rt(40)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainFourteen()#call main function fourteen


def mainFifteen():
    choice = int(input('Enter 15 for square fifteen '))#prompt user

    if choice == 15:
        drawSquareFifteen()#call sqaure function

def drawSquareFifteen():
    turtle.rt(40)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainFifteen()#call main function Fifteen


def mainSixteen():
    choice = int(input('Enter 16 for square Sixteen '))#prompt user

    if choice == 16:
        drawSquareThirteen()#call sqaure function

def drawSquareSixteen():
    turtle.rt(40)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainSixteen()#call main function sixteen


def mainSeventeen():
    choice = int(input('Enter 17 for square seventeen '))#prompt user

    if choice == 17:
        drawSquareSeventeen()#call sqaure function

def drawSquareSeventeen():
    turtle.rt(40)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainSeventeen()#call main function seventeen


def mainEighteen():
    choice = int(input('Enter 18 for square eighteen '))#prompt user

    if choice == 18:
        drawSquareEighteen()#call sqaure function

def drawSquareEighteen():
    turtle.rt(40)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainEighteen()#call main function Eighteen


def mainNineteen():
    choice = int(input('Enter 19 for square nineteen '))#prompt user

    if choice == 19:
        drawSquareNineteen()#call sqaure function

def drawSquareNineteen():
    turtle.rt(50)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainNineteen()#call main function nineteen


def mainTwenty():
    choice = int(input('Enter 20 for square twenty '))#prompt user

    if choice == 20:
        drawSquareTwenty()#call sqaure function

def drawSquareTwenty():
    turtle.rt(50)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainTwenty()#call main function twenty


def mainTwentyOne():
    choice = int(input('Enter 21 for square twenty-one '))#prompt user

    if choice == 21:
        drawSquareTwentyOne()#call sqaure function

def drawSquareTwentyOne():
    turtle.rt(50)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainTwentyOne()#call main function twenty-one


def mainTwentyTwo():
    choice = int(input('Enter 22 for square twenty-two '))#prompt user

    if choice == 22:
        drawSquareTwentyTwo()#call sqaure function

def drawSquareTwentyTwo():
    turtle.rt(50)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainTwentyTwo()#call main function twenty-two


def mainTwentyThree():
    choice = int(input('Enter 23 for square twenty-three '))#prompt user

    if choice == 23:
        drawSquareTwentyThree()#call sqaure function

def drawSquareTwentyThree():
    turtle.rt(50)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainTwentyThree()#call main function twenty-three


def mainTwentyFour():
    choice = int(input('Enter 24 for square twenty-four '))#prompt user

    if choice == 24:
        drawSquareTwentyFour()#call sqaure function

def drawSquareTwentyFour():
    turtle.rt(50)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainTwentyFour()#call main function twenty-four


def mainTwentyFive():
    choice = int(input('Enter 25 for square twenty-five '))#prompt user

    if choice == 25:
        drawSquareTwentyFive()#call sqaure function

def drawSquareTwentyFive():
    turtle.rt(50)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainTwentyFive()#call main function twenty-five


def mainTwentySix():
    choice = int(input('Enter 26 for square twenty-six '))#prompt user

    if choice == 26:
        drawSquareTwentySix()#call sqaure function

def drawSquareTwentySix():
    turtle.rt(70)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainTwentySix()#call main function twenty-six


def mainTwentySeven():
    choice = int(input('Enter 27 for square twenty-seven '))#prompt user

    if choice == 27:
        drawSquareTwentySeven()#call sqaure function

def drawSquareTwentySeven():
    turtle.rt(70)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainTwentySeven()#call main function twenty-seven


def mainTwentyEight():
    choice = int(input('Enter 28 for square twenty-eight '))#prompt user

    if choice == 28:
        drawSquareTwentyEight()#call sqaure function

def drawSquareTwentyEight():
    turtle.rt(70)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainTwentyEight()#call main function twenty-eight


def mainTwentyNine():
    choice = int(input('Enter 29 for square twenty-nine '))#prompt user

    if choice == 29:
        drawSquareTwentyNine()#call sqaure function

def drawSquareTwentyNine():
    turtle.rt(70)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainTwentyNine()#call main function twenty-nine


def mainThirty():
    choice = int(input('Enter 30 for square thirty '))#prompt user

    if choice == 30:
        drawSquareThirty()#call sqaure function

def drawSquareThirty():
    turtle.rt(70)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainThirty()#call main function thirty


def mainThirtyOne():
    choice = int(input('Enter 31 for square thirty-one '))#prompt user

    if choice == 31:
        drawSquareThirtyOne()#call sqaure function

def drawSquareThirtyOne():
    turtle.rt(70)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainThirtyOne()#call main function thirty-one


def mainThirtyTwo():
    choice = int(input('Enter 32 for square thirty-two '))#prompt user

    if choice == 32:
        drawSquareThirtyTwo()#call sqaure function

def drawSquareThirtyTwo():
    turtle.rt(70)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainThirtyTwo()#call main function thirty-two


def mainThirtyThree():
    choice = int(input('Enter 33 for square thirty-three '))#prompt user

    if choice == 33:
        drawSquareThirtyThree()#call sqaure function

def drawSquareThirtyThree():
    turtle.rt(70)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainThirtyThree()#call main function thirty-three


def mainThirtyFour():
    choice = int(input('Enter 34 for square thirty-four '))#prompt user

    if choice == 34:
        drawSquareThirtyFour()#call sqaure function

def drawSquareThirtyFour():
    turtle.rt(70)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainThirtyFour()#call main function thirty-four


def mainThirtyFive():
    choice = int(input('Enter 35 for square thirty-five '))#prompt user

    if choice == 35:
        drawSquareThirtyFive()#call sqaure function

def drawSquareThirtyFive():
    turtle.rt(70)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainThirtyFive()#call main function thirty-five


def mainThirtySix():
    choice = int(input('Enter 36 for square thirty-six '))#prompt user

    if choice == 36:
        drawSquareThirtySix()#call sqaure function

def drawSquareThirtySix():
    turtle.rt(70)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainThirtySix()#call main function thirty-six


def mainThirtySeven():
    choice = int(input('Enter 37 for square thirty-seven '))#prompt user

    if choice == 37:
        drawSquareThirtySeven()#call sqaure function

def drawSquareThirtySeven():
    turtle.rt(70)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainThirtySeven()#call main function thirty-seven


def mainThirtyEight():
    choice = int(input('Enter 38 for square thirty-eight '))#prompt user

    if choice == 38:
        drawSquareThirtyEight()#call sqaure function

def drawSquareThirtyEight():
    turtle.rt(70)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainThirtyEight()#call main function thirty-eight


def mainThirtyNine():
    choice = int(input('Enter 39 for square thirty-nine '))#prompt user

    if choice == 39:
        drawSquareThirtyNine()#call sqaure function

def drawSquareThirtyNine():
    turtle.rt(70)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainThirtyNine()#call main function thirty-nine


def mainFourty():
    choice = int(input('Enter 40 for square fourty '))#prompt user

    if choice == 40:
        drawSquareThirty()#call sqaure function

def drawSquareFourty():
    turtle.rt(70)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainFourty()#call main function fourty


def mainFourtyOne():
    choice = int(input('Enter 41 for square fourty-one '))#prompt user

    if choice == 41:
        drawSquareThirty()#call sqaure function

def drawSquareFourtyOne():
    turtle.rt(70)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(150)

mainFourtyOne()#call main function fourty-one

'''
turtle.home()
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(30)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(30)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(30)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(30)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(30)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(10)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(10)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(10)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(10)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(10)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(10)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(40)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(40)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(40)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(40)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(40)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(40)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(50)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(50)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(50)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(50)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(50)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(50)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)


turtle.rt(70)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(150)
'''
