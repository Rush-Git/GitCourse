# def hello_world_printer():
#     print("Hello World")
#
# hello_world_printer()
#
# def name_printer(num):
#     print(num)
#
# name_printer(2)
#
# name = input("What is your name?")
#
#
# name_printer(name)
#
#
# Length = int(input("Length"))
# Width = int(input("Width"))
# Height = int(input("Height"))
#
# def volume_cal(Length, Width, Height):
#     return Length * Width * Height
#
# volume_cal(Length, Width, Height)
#
# print("The volume of the rectangular prism is" + " " + str(volume_cal(Length, Width, Height)) + " " + "cubic feet.")

Temp = int(input("Enter the Celsius temperature"))

def Fah_temperature(Temp):
    return (18 * Temp +320)/10

Fah_temperature(Temp)
print("The Fahrenheit equivalent of" + " " + str(Temp) + " " + "degree celsius is" + " " + str(Fah_temperature(Temp)))











