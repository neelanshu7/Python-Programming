# A. Create a Python funcMon that performs the following tasks:
'''
b. Computes the area to be whitewashed using the function
whitewashing_Area().
'''
def whitewashing_Area(l,b,h):
    ww_area=(2*b*h)+(2*l*h)+(l*b)
    return ww_area
'''
c. Calculates the cost of whitewashing at a rate of Rs.15/- per sq.m using the
function whitewashing_Cost().
'''
def whitewashing_Cost(ww_area):
    ww_cost=ww_area*15
    return ww_cost
'''
d. Computes the cost of flooring at different rates: Rs.100/- per sq.m for mosaic
flooring and
e. Rs.55/- per sq.m for cement flooring using the function flooring_Cost().
'''
def flooring_Cost(floor,typ):
    if typ==1:
        cost=100
    elif typ==2:
        cost=55
    else:
        print("Invalid Input")

    f_cost=cost*floor
    return f_cost
'''
f. The function should display the calculated costs for whitewashing and
flooring.
'''
def total_cost(ww_cost,f_cost):
    t_cost=ww_cost+f_cost
    
def main():
    '''
    a. Accepts three parameters: length, width, and height representing the dimensions of room.
    '''
    print("Enter the Dimensions of room in meters: ")
    l=float(input("Enter Length : "))
    b=float(input("Enter Bredth : "))
    h=float(input("Enter Height : "))
    print("Enter  1. Mosaic \t\t  2. Cement")
    typ=int(input("Enter your Choice of flooring  "))
    floor=l*b

    ww_area=whitewashing_Area(l,b,h)
    ww_cost=whitewashing_Cost(ww_area)
    f_cost=flooring_Cost(floor,typ)

    print("White Washing Area : ",ww_area," sq. m\n")
    print("White Washing Cost  :  ",ww_cost,"\n")
    print("Flooring Cost :  ",f_cost,"\n")

    total_cost=ww_cost+f_cost
    print("Total Cost : ",total_cost)
main()
