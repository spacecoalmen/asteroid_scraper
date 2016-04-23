
from numpy.core.umath import deg2rad, power, sqrt, exp, cos, arccos, sin, absolute

earth = dict(
    ecc= 0.0167,  #orbital eccetricity
    incl= 0, #inclination to ecliptic da convertire in rad
    Omega= 0, #longitude of Omega
    omegap= deg2rad(102.416),
    semiax= 1, #semi-major axis
    rp=0,
)

mars = dict(
    ecc= 0.0934,
    incl= deg2rad(1.850),
    Omega= deg2rad(49.322),
    omegap= deg2rad(335.497),
    semiax=1.524,
    rp=0,
)

def Qfunction(ob1, ob2):
    try:
        mu_S=1.32712440018
        ob1['rp']=ob1['semiax']*(1-ob1['ecc'])
        
        
        semilp=ob1['semiax']*(1-power(ob1['ecc'],2))
        hmom=sqrt(mu_S*semilp)
        
        #Penalty
        k=0.1
        rpmin=0.5
        Pen=exp(k*(1-ob1['rp']/rpmin))
        
        dist=[0,0,0,0,0]
        #distance
        dist[0]=ob1['rp']-ob2['rp']
        dist[1]=ob1['ecc']-ob2['ecc']
        dist[2]=ob1['incl']-ob2['incl']
        dist[3]=cos(arccos(ob1['Omega']-ob2['Omega']))
        dist[4]=cos(arccos(ob1['omegap']-ob2['omegap']))
        #Thrust
        # i need the Thrust value
        thr=1
        der=[0,0,0,0,0]
        #semi major axis
        der[0]=2*thr*sqrt(power(ob1['semiax'],3)*(1+ob1['ecc'])/mu_S/(1-ob1['ecc']))
        
        #ecc
        der[1]=2*semilp*thr/hmom
        
        #inclination
        der[2]=semilp*thr/hmom/(sqrt(1-power(ob1['ecc'],2)*power(sin(ob1['omegap']),2))-ob1['ecc']*absolute(sin(ob1['omegap'])))
        
        #line of nodes
        dum1=(sqrt(1-(ob1['ecc']**2)*cos(ob1['omegap'])**2)-ob1['ecc']*absolute(sin(ob1['omegap'])))
        der[3]=semilp*thr/hmom/sin(ob1['incl'])/dum1
        
        # Arg of periapsis
        eccfun=(1-power(ob1['ecc'],2))/power(ob1['ecc'],3)
        costhetaxx=(eccfun/2+sqrt(1/4*power(eccfun,2)+1/27))**(1/3)-(-eccfun/2+sqrt(1/4*eccfun**2+1/27))**(1/3)-1/ob1['ecc']
        rxx=semilp/(1+ob1['ecc']*costhetaxx)
        sinthetaxx2=1-power(costhetaxx,2)
        omegapxxi=thr/ob1['ecc']/hmom*sqrt((semilp*costhetaxx)**2+((semilp+rxx)**2)*sinthetaxx2)
        omegapxx0=der[4]*abs(cos(ob1['incl']))
        b=0.01
        der[4]=(omegapxxi+b*omegapxx0)/(1+b)
        
        Q=0
        #Weights
        Weights=[0,0,0,0,0]
        Weightp=1
        #S
        m=3
        n=4
        r=2
        S=[1,1,1,1,1]
        S[0]=(1+((ob1['semiax']-ob2['semiax'])/m/ob2['semiax'])**n)**(1/r)
        num=range(0,4)
        for i in num:
            Weights[i]=1
            Q=Q+(1+Weightp*Pen)*Weights[i]*S[i]*(dist[i]/der[i])**2
    except TypeError:
        print 'Error on Qfunction', ob1, ob2
        return 999
    return Q