import time
b = 0
def func(num):
  if num == 0:
    print('Done!')
    return 1
  else:
    b = num * func(num-1)
    return b

ask = int(input('Enter the number: '))
time.sleep(1.5)
b = func(ask)
time.sleep(1.5)
print()
print(f'The factorial of {ask} is {b}')