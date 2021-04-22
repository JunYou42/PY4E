# programm to promt the user for hours and rate per hour using
# input to compute gross pay

#get string type
hrs = input("Enter hours:")
rate = input("Enter rate per hour:")

#convert to floating points
hrs = float(hrs)
rate = float(rate)

print('Pay:',hrs*rate)
