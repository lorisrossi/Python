from __future__ import division
from math import sqrt


def mean(args):
    """Return the mean, the variance, the standard deviation and
    the semi-width of confidence interval (95% accuracy) of args."""
    N = len(args)
    mean = sum(args) / N
    variance = sum((x-mean)**2 for x in args) / N
    st_deviation = sqrt(variance)
    cf_interval = 1.96 * st_deviation / sqrt(N) # 1.96 corresponds to 95%
    print """            Mean: %19.4f
            Variance: %15.4f
            St.Deviation: %11.4f
            Cf.Interval:  %11.4f""" % (mean,
            variance, st_deviation, cf_interval)


raw_numbers = raw_input('Write your numbers: ')
numbers = list(float(x) for x in raw_numbers.split())
mean(numbers)
print
