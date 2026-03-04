#ITERATIVE NUMERICAL METHOD 'eulers' method for estimation of first order differential equation solutions

#the iterative formula 
#y_new = y_prev + step(dy_prev/dx_prev)

#an equation for the derivative is always given 
#STEPS
#Define the differential equation in the diff(x,y) function so it returns the desired output
#Then run the program
import math

def diff(x,y):
    # return (math.exp(x)+2*math.exp(y))**0.5 # example differential equation for dy/dx = sqrt(e^x + 2e^y)
    return (math.log(x) + 3*y)
    


def iteration(start_x=2.5,start_y=0,step= 0.1, final_x=3):
    iters = int((final_x-start_x)/step)
    x = start_x
    # y_next = y_prev + step(diff(x_prev, y_prev))
    y_next = start_y + step*(diff(start_x,start_y))
    
    x_next = start_x + step
    print(y_next)
    print("(x,y)")
    print(f"({start_x:2f},{start_y:2f})")
    print(f"({x_next:2f},{y_next:2f})")
    for i in range(1,iters):
        y_prev = y_next
        x_prev = start_x + i * step
        y_next = y_prev + step*(diff(x_prev, y_prev))
        x_next = x_prev + step
        
        print(f"({x_next:1f},{y_next :2f})")
        
        
    
start_x = float(input("Enter starting x value: "))
start_y = float(input("Enter starting y value: "))
step = float(input("Enter the step: "))
final_x = float(input("Enter final x value: "))

iteration(start_x,start_y,step, final_x)