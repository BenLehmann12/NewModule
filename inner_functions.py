'''
Author: Ben Lehmann
Date Modified: 10/4/20
Function: Methods to calculate the area and perimeter of list and then put those into a new function
'''
def measurements(a_list):
    perim = perimeter(a_list)
    areas = area(a_list)
    statement = "Perimeter = " + str(perim) + " Area = " + str(areas)
    return statement
def area(a_list):
    if len(a_list) == 1:        #If the list has 1 item, multiply by itself
        areas = a_list[0] * a_list[0]
    elif len(a_list) == 2:      #If the list has 2 items, multiply first item by second item
        areas = a_list[0] * a_list[1]
    else:
        areas = 0
    return areas

def perimeter(a_list):
    if len(a_list) == 1:    #If the list has 1 item, multiply by 4
        perim = a_list[0]*4
    elif len(a_list) == 2:
        perim = 2*(a_list[0] + a_list[1])    #If the list has 2 items, add them together and multiply by 2
    else:
        perim = 0 #If nothing, return 0
    return perim

if __name__ == "__main__":
    print(measurements([2.1,3.4]))   #Test
