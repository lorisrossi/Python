from __future__ import division
from math import sqrt

def coefficient(xnum, ynum):
    "B is the gradient, A is the intercept, R is the correlation coefficient."
    xmean = sum(x for x in xnum) / len(xnum)
    ymean = sum(y for y in ynum) / len(ynum)
    pairs = zip(xnum, ynum)
    numerator = sum((pair[0] - xmean)*(pair[1] - ymean)
                for pair in pairs)
    xsquared = sum((x - xmean)**2 for x in xnum)
    ysquared = sum((y - ymean)**2 for y in ynum)
    B = numerator / xsquared
    A = ymean - B*xmean
    R = numerator / sqrt(xsquared * ysquared)
    return B, A, R

x = [float(n) for n in raw_input('X numbers: ').split()]
y = [float(n) for n in raw_input('Y numbers: ').split()]

print
print '%.5fx + %.5f\nCorrelation coeff : %.4f' % (coefficient(x, y))
