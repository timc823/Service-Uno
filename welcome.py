'''this program hasn't prevent user input the wrong information yet.'''
import time
sdelay = 0.2
ldelay = 1.0
time.sleep(sdelay)


print('Welcome come to use ....')
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
print('rating program')

def yes_no():

        L = input('Please input [yes/no] refer to the question:')
        if L == 'yes':
            return 'yes'
        elif L =='no':
            return 'no'
        # else:
        #     time.sleep(sdelay)
        #     print('you enter something not related to the question, please enter again')
        #     time.sleep(sdelay)
        #     yes_no()


answer = []
rank = []
print('Have you been sat?')
q1 = yes_no()
answer.append(q1)
print('Did your server greet you?')
q2 = yes_no()
answer.append(q2)
print('Did you order?')
q3 = yes_no()
answer.append(q3)
print('Did server bring you drinks?')
q4 = yes_no()
answer.append(q4)
print('Did server bring you appetizers')
q5 = yes_no()
answer.append(q5)
print('Did server bring you food?')
q6 = yes_no()
answer.append(q6)
print('Did server clean the table for you?')
q7 = yes_no()
answer.append(q7)

print('Are you satisfied with the service from server?')
k = input('From 1-5,please rank how satisfy are you?')
rank.append(k)
#answer = yes_no(L)
print(answer)
print(rank)
