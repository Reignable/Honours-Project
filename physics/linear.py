import numpy as np
import scipy.stats as stats
import pylab
import sys

pressures = []
movements = []

with open(sys.argv[1], 'r') as csv:
    for line in csv:
        pressure, movement = line.split(', ')
        pressures.append(float(pressure))
        movements.append(float(movement))
y=np.array(pressures)
x=np.array(movements)

#print x
#print y

slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
#print "slope = "+ str(slope)
#print "r_value = "+ str(r_value)
#print "r_squared = " + str(r_value**2)
#print "p_value = "+str(p_value)
# Calculate some additional outputs
predict_y = intercept + slope * x
#print predict_y
pred_error = y - predict_y
degrees_of_freedom = len(x) - 2
residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)

# Plotting
pylab.title('y={s}x+{i}'.format(s=slope, i=intercept))
pylab.xlabel('movement(mm)')
pylab.ylabel('pressure(psi)')
pylab.plot(x, y, 'o')
pylab.plot(x, predict_y, 'k-')
pylab.show()
