from matplotlib.pyplot import *
from numpy import *

t = arange(1,3,0.02)
T = 6*log(t)-7*exp(0.2*t)

plot(t,T)

xlabel('Time (min)')
ylabel('Temp (C)')
suptitle('Myers-plot')

print 'Hello World! I just wrote my first Python program. Yayyyyyy'
print 'Dylan Myers'

show()
