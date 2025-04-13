# This is a program says hello and ask for your name

print('Hello, world!')
print('What is your name?')  # ask for customer name
customerName = input()

print('Glad to meet you, ' + customerName)
print('The length of your name is:')
print(len(customerName))
print('What is your age?')
customerAge = input()

print('You will be ' + str(int(customerAge) + 1) + ' in a year.')
