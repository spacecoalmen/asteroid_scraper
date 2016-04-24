from numpy import *

EARTH_ORBIT = {
    'ecce': 0.0167,  # orbital eccetricity
    'incl': 0,  # inclination to ecliptic da convertire in rad
    'Omega': deg2rad(0),  # longitude of Omega
    'omegap': deg2rad(102.416),
    'semiax': 1,  # semi-major axis
    'rp': 0,
}

MARS_ORBIT = {
    'ecce': 0.0934,
    'incl': deg2rad(1.850),
    'Omega': deg2rad(49.322),
    'omegap': deg2rad(335.497),
    'semiax': 1.524,
    'rp': 0,
}


def Qfunction(ob1, ob2=EARTH_ORBIT):
    # try:
    mu_S = 1.32712440018
    ob1['rp'] = ob1['semiax']*(1-ob1['ecce'])
    ob2['rp'] = ob2['semiax']*(1-ob2['ecce'])
    semilp = ob1['semiax']*(1-ob1['ecce']**2)
    hmom = sqrt(mu_S*semilp)

    #Penalty
    k = 0.1
    rpmin = 0.5
    Pen = exp(k*(1-ob1['rp']/rpmin))
    dist = []
    #distance
    dist.append(ob1['rp']-ob2['rp'])
    dist.append(ob1['ecce']-ob2['ecce'])
    dist.append(arccos(cos(ob1['incl']-ob2['incl'])))
    dist.append(arccos(cos(ob1['Omega']-ob2['Omega'])))
    dist.append(arccos(cos(ob1['omegap']-ob2['omegap'])))

    #Thrust
    # i need the Thrust value
    thr = 1

    der= []
    # semi major axis
    der.append(2*thr*sqrt((ob1['semiax']**3)*(1+ob1['ecce'])/mu_S/(1-ob1['ecce'])))
    # ecc
    der.append(2*semilp*thr/hmom)
    # inclination
    der.append(semilp*thr/hmom/(sqrt(1-ob1['ecce']**2*sin(ob1['omegap'])**2)-ob1['ecce']*absolute(sin(ob1['omegap']))))
    # line of nodes
    dum1 = (sqrt(1-(ob1['ecce']**2)*cos(ob1['omegap'])**2)-ob1['ecce']*absolute(sin(ob1['omegap'])))
    der.append(((semilp*thr/hmom)/sin(ob1['incl']))/dum1)
    # Arg of periapsis
    eccfun = (1-ob1['ecce']**2)/ob1['ecce']**3
    costhetaxx = (eccfun/float(2)+sqrt(1/float(4)*eccfun**2+1/float(27)))**(1/float(3))-(-eccfun/float(2)+sqrt(1/float(4)*eccfun**2+1/float(27)))**(1/float(3))-(1/ob1['ecce'])
    rxx=semilp/(1+exp(ob1['ecce']*costhetaxx))
    sinthetaxx2 = 1-costhetaxx**2
    omegapxxi = thr/ob1['ecce']/hmom*sqrt(((semilp*costhetaxx)**2)+((semilp+rxx)**2)*sinthetaxx2)
    omegapxx0 = der[3]*abs(cos(ob1['incl']))
    b = 0.01
    der.append((omegapxxi+b*omegapxx0)/(1+b))
    Q = 0
    # Weights
    Weights = [1, 1, 1, 1, 1]
    Weightp = 1
    #S
    m = 3
    n = 4
    r = 2
    S = [1, 1, 1, 1, 1]
    S[0] = (1+((ob1['semiax']-ob2['semiax'])/float(m)/float(ob2['semiax']))**n)**(1/float(r))

    num = range(0, 4)
    for i in num:
        Q = Q+(1+Weightp*Pen)*Weights[i]*S[i]*(dist[i]/der[i])**2

    return Q

