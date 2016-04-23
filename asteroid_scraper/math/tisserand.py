from numpy.core.umath import deg2rad, sqrt
from numpy.ma import cos, power

earth = {
    'ecce': 0.0167,  #orbital eccetricity
    'incl': 0, #inclination to ecliptic da convertire in rad
    'Omega': 0, #longitude of Omega
    'omegap': deg2rad(102.416),
    'semiax': 1, #semi-major axis
}
#MARTE
mars = {
    'ecce': 0.0934,
    'incl': deg2rad(1.850),
    'Omega': deg2rad(49.322),
    'omegap': deg2rad(335.497),
    'semiax': 1.524,
}


def tisserand(ob1, ob2):
    try:
        cosisc_ga = 0.5*cos(ob1['incl']+ob2['incl'])*(cos(ob1['omegap']-ob2['omegap'])+1)+0.5*cos(ob1['incl']-ob2['incl'])*(-cos(ob1['omegap']-ob2['omegap'])+1)

        Tiss=ob1['semiax']/ob2['semiax']+2*cosisc_ga*sqrt(ob2['semiax']/ob1['semiax']*(1-power(ob2['ecce'],2)))
    except TypeError:
        print 'Error on tisserand', ob1, ob2
        return 999
    return Tiss
