""" 
    THIS PROGRAM CALCULATES THE BODY MASS INDEX OF INDIVIDUALS 
    
"""


if __name__ == '__main__':

    #COLLECT HEIGHT IN CENTIMETERS
    heights = int(input("Enter Height in Centimers: ")) 

    #CONVERT HEIGHT TO METERS
    convert_diff = float(0.01)
    meters = heights * convert_diff 

    #GET THE SQUARE OF HEIGHT
    square_height = float(meters * meters)

    #COLLECT THE WEIGHT IN KILOGRAMS
    weights = int(input("Enter Weight in Kilograms: "))

    #CALCULATE THE BMI == WEIGHT / SQAURE HEIGHT 
    bmi = float(weights / square_height)

    #AND THE PROBLEM HAS BEEN SOLVED 
    print("Your Body Mass Index is: {:.2f}".format(bmi))