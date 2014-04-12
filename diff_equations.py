#Kyle Golden
# Euler and Taylor Functions
#Written in Python to make my math homework less painfull

import math

#----------------------------------------------------------
#Euler's Method Function
#	@Parameters	
#	f  		= function(x, y)
#	x0 		= initial x value
#	y0 		= initial y value
#	x1 		= x value of target y approx.
#	steps 	= desired steps *mo tha betta*
#----------------------------------------------------------
def Euler(f, x0, y0, x1, steps):
	x,y = x0,y0
	h = (x1 - x0)/steps
	print "\nXn\t| Yn\t\t| F(Xn, Yn)\n"
	for i in range(x0, steps+1):
		print "{0:.2f}\t| {1:.4f}\t| {2:.4f}\n".format(x,y, y+(h*f(x,y)))
		temp=y+(f(x, y)* h)
		x+=h
		y=temp

#----------------------------------------------------------
#Taylor Polynomial Function
#	@Parameters	
#	f1  	= 1st derivative - anon lambda func
#	f2		= 2nd derivative - anon lambda func
#	x0		= initial x value
#	y0		= initial y value
#	steps	= number of steps
#----------------------------------------------------------	
def Taylor(f1, f2, x0, y0, x1,steps):
	x,y = x0,y0
	h = (x1-x0)/steps
	print "\nXn\t| Yn\t\t| F(Xn, Yn)\n"
	while x <= x1+h:
		z = y + (f1(x,y))*(.1) + (f2(x,y)*((.1**2)/2))
		print "{0:.2f}\t| {1:.3f}\t\t| {2:.3f}\n".format(x,y,z)
		temp = y+(f1(x,y))*(.1)+(f2(x,y)*((.1**2)/2))
		x+=h
		y=temp
		
#---------------------------------------------------------
# Main Func. 
# example of how to run
#---------------------------------------------------------
if __name__ == "__main__":

    Euler(lambda x,y: math.exp(-y), 0, 0, .5, 10)
	Taylor(lambda x,y: (x+(y**2)), lambda x,y: (1+(2*x*y)+(2*(y**3))), 1, 2, 1.3, 3)
	
	