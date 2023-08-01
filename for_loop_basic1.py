

# 1.Print all integers from 0 to 150.

for i in range(151):
        print(i)


#2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for i in range(5, 1001, 5):
        print(i)

# 3. Print integers from 1 to 100, replace multiples of 5 with "Coding" and multiples of 10 with "Coding Dojo"

for i in range(1, 101):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)


# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

minimum = 0
maximum = 500000
Oddsum = 0

for num in range(minimum, maximum+1):
    if(num % 2 != 0):
        print("{0}".format(num))
        Oddsum = Oddsum + num

print("The Odd Numbers from {0} to {1} = {2}".format(minimum, maximum, Oddsum))


# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.


def count_down():
    num = 2018
    while num > 0:
        print (num)
        num = num - 4
        
count_down()   

#6 Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

def flex_countdown(lowNum, highNum, mult):
    for num in range(lowNum, highNum)