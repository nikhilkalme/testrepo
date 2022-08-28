'''
Name : Nikhil Santosh Kalme
Batch : F3
Roll no. : 663
'''

#Problem 1 : To accept an object mass in kilograms and velocity in meters per second and display its momentum and energy. Momentum=mc, Energy=mc2 where m is the mass of the object and c is its velocity.

#Here we are taking input from the end user using input() function
#   '#' is used for dingle line comment and for multi line comment we use '''.....'''

#if we have to declare the value which we are declering is int then put 'int' before the input()  function

M = int(input('Enter the mass : '))
print("Mass of body is ", M, "kg\n")

V = int(input('Enter the velocity : '))
print("Velocity of body is ", V, "m/sec\n")

# momentum = mass * velocity
print("Momentum of the body is ", M*V,"kg m/sec\n")
# **is index oprator
#energy = mass*(velocity)^2
print("Energy of the body is ", M*(V**2), "joule")


'''
OUTPUT

Enter the mass : 3
Mass of body is  3 kg

Enter the velocity : 2
Velocity of body is  2 m/sec

Momentum of the body is  6 kg m/sec

Energy of the body is  12 joule

'''


print('______________________________________')
#Problem 2 : Calculate heat generated in a conductor of resistance 200 ohm if current is flowing for User input time and value of current flowing for user input amps.

R = 200 
print("\nResistance of the resistor is ", R, "ohm")

I = int(input("Enter the current : "))
print("The current flowing through resistor is  ", I, "A\n")

T = int(input("Enter the time : "))
print("The current flows for ", T, "sec\n")

print("The heat generated in the resistor is ", (I**2)*R*T, "J")
#Heat generated= (I^2)RT
#I is current ,R is resistance ,T is time
'''
OUTPUT

______________________________________

Resistance of the resistor is  200 ohm
Enter the current : 2
The current flowing through resistor is   2 A

Enter the time : 10
The current flows for  10 sec

The heat generated in the resistor is  8000 J

'''


print('______________________________________\n')
#Problem 3 : A Crash Test is being conducted. Enter the Car detail using input function. Also Calculate the initial speed, acceleration of the car if the final velocity is zero in time 10s and distance of track is 20 m.

T=10
Acce = (40)/(T*T)
print("The deceleration of the car is : ",Acce)
# as final velocity is zero and the initial velocity is nonzero so the acceleration is negative i.e.deceleration
Initialvelo = Acce*T
print("The initial velocity of the car is : ",Initialvelo)


'''
OUTPUT
______________________________________

The deceleration of the car is :  0.4
The initial velocity of the car is :  4.0

'''

print('______________________________________\n')
#Problem 3 : Find the area of plots to build housing society . take input from user is length and breadth of the site in Meter. and area is in meter square.

len=int(input("Enter the length of plot : "))
print("Length of the plot is : ",len," m\n")

brea=int(input("Enter the breadth of plot : "))
print("Breadth of plot is : ",brea," m\n")
temp =input("Press ENTER key to calculate area of plot")
print("\nThe area of the plot is ",len*brea, " sq. m\n")

'''
OUTPUT
______________________________________

Enter the length of plot : 13
Length of the plot is :  13  m

Enter the breadth of plot : 15
Breadth of plot is :  15  m

Press ENTER key to calculate area of plot

The area of the plot is  195  sq. m
'''