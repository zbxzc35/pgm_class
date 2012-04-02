from __future__ import division

Ppresident = [0.99, 0.01]
Paccident = [0.9, 0.1]

# P[p,a] = P(traffic=1|president=p,accident=a)
Ptraffic = {}
Ptraffic[0,0] = 0.1
Ptraffic[0,1] = 0.5
Ptraffic[1,0] = 0.6
Ptraffic[1,1] = 0.9

def margin(president, accident):
    return sum([Ptraffic[(p,a)]*Ppresident[p]*Paccident[a] 
         for p in president
         for a in accident])

# P(accident=1,traffic=1)
Pat = Paccident[1] * sum([Ptraffic[p,1]*Ppresident[p] for p in (0,1)])
Pat = margin(president=[0,1], accident=[1])

# P(traffic=1)
Pt = sum([Ptraffic[(p,a)]*Ppresident[p]*Paccident[a] for a in (0,1) for p in (0,1)])
Pt = margin(president=[0,1], accident=[0,1])

# P(accident=1 | traffic=1) = P(accident=1,traffic=1)/P(traffic=1) 
Pa_t = Pat/Pt

print 'Pat  = %f' % Pat
print 'Pt   = %f' % Pt
print 'Pa_t = %f' % Pa_t
print '-' * 80

#Patp = P(Accident=1, Traffic=1, President=1)
Patp = margin(president=[1], accident=[1])

#Ptp = P(Traffic=1, President=1)
Ptp = margin(president=[1], accident=[0,1])

# P(Accident=1 | Traffic=1, President=1)
# = P(Accident=1, Traffic=1, President=1) / P(Traffic=1, President=1)
Pa_tp = Patp/Ptp

print 'Patp  = %f' % Patp
print 'Ptp   = %f' % Ptp
print 'Pa_tp = %f' % Pa_tp
print '-' * 80