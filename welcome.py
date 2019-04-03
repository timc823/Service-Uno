'''this program hasnt prevent user input the wrong information yet.'''
import time
sdelay = 0.2
ldelay = 1.0
time.sleep(sdelay)
def welcome():
    print('.......................................................................'
          '...................................')
    print('........................................WELCOME TO........................................................')
    print('..........................................................................................................')
    time.sleep(ldelay)
    print(' .d8888b.                               d8b                       888        888 888b     888  .d888888b.')
    time.sleep(sdelay)
    print('d88P  Y88b                              Y8P                       888        888 8888b    888 d88P"  "Y88b')
    time.sleep(sdelay)
    print('Y88b.                                                             888        888 88888b   888 888      888')
    time.sleep(sdelay)
    print('   "Y888b.    .d88b.  888d888 888  888  888  .d8888b  .d88b.      888        888 888Y88b  888 888      888')
    time.sleep(sdelay)
    print('     "Y88b.  d8P  Y8b 888P"   888  888  888 d88P"    d8P  Y8b     888        888 888  Y88b888 888      888')
    time.sleep(sdelay)
    print('       "888  88888888 888     Y88  88P  888 88       88888888     888        888 888   Y88888 888      888')
    time.sleep(sdelay)
    print('Y88b   d88P  Y8b.     888      Y8bd8P   888 Y88b     Y8b.          Y88b. .d88P   888    Y8888 Y88b.  .d88P')
    time.sleep(sdelay)
    print(' "Y8888P"     "Y8888  888       Y88P    888  "Y8888P  "Y8888        "Y88888P"    888     Y888  "Y888888P"')
    time.sleep(ldelay)
    print('...........................................................................................................')
    print('...........................................................................................................')
    print('...........................................................................................................')
    # print('')
    # print('')
welcome()
# def yes_no():
#
#         L = input('Please input [yes/no] refer to the question:')
#         if L == 'yes':
#             return 10
#         elif L =='no':
#             return 5
#
# def calculatescore():
#     a = 0
#     rank = []
#     print('Have you been seated?')
#     q1 = yes_no()
#     a += q1
#     print('Did your server greet you?')
#     q2 = yes_no()
#     a += q2
#     print('Did you order?')
#     q3 = yes_no()
#     a += q3
#     print('Did server bring you drinks?')
#     q4 = yes_no()
#     a += q4
#     print('Did server bring you appetizers')
#     q5 = yes_no()
#     a += q5
#     print('Did server bring you food?')
#     q6 = yes_no()
#     a += q6
#     print('Did server clean the table for you?')
#     q7 = yes_no()
#     a += q7
#
#     r1 = int(input('From 1-10, please provide a score for how satisified were you for the service: '))
#     a += r1
#     r2 = int(input('From 1-10, please provide a score for how friendly your server was: '))
#     a += r2
#     r3 = int(input('From 1-10, please provide a overall score for your server: '))
#     a += r3
#     # answer = yes_no(L)
#
#     return a
#
# score = calculatescore()
# scale = score / 100
# bill = eval(input('Please input the bill amount: '))
# TipPercent = 0
# if scale >= 0.95:
#     TipPercent = 0.35
# elif scale >= 0.9 and scale <0.95:
#     TipPercent = 0.3
# elif scale >= 0.75 and scale <0.89:
#     TipPercent = 0.2
# elif scale >= 0.6 and scale <0.75:
#     TipPercent = 0.15
# elif scale >= 0.3 and scale <0.6:
#     TipPercent = 0.1
# else:
#     TipPercent = 0.05
#
# Tips = bill*TipPercent
# print('Base on your bill amount and the service you have today, we think amount of ', Tips,
#       'is the valuable amount to tip your server.')