from numpy import *
import scipy.linalg


# def fTiss(eltsPlanet,eltsSC):
#     rpPl=eltsPlanet(1)
#TERRA
earth = dict(
    eccPl= 0.0167,  #orbital eccetricity
    aincPl= 0, #inclination to ecliptic da convertire in rad
    OmegaPl= 0, #longitude of Omega
    omegapPl= deg2rad(102.416),
    semiaPl= 1, #semi-major axis
)
#MARTE
mars = dict(
    # rpSC=eltsSC(1)
    eccSC= 0.0934,
    aincSC= deg2rad(1.850),
    OmegaSC= deg2rad(49.322),
    omegapSC= deg2rad(335.497),
    semiaSC=1.524,
)

cosisc_ga=0.5*cos(earth['aincPl']+mars['aincSC'])*(cos(earth['omegapPl']-mars['omegapSC'])+1)+0.5*cos(earth['aincPl']-mars['aincSC'])*(-cos(earth['omegapPl']-mars['omegapSC'])+1)
isc_ga=arccos(cosisc_ga)


Tiss=earth['semiaPl']/mars['semiaSC']+2*cosisc_ga*sqrt(mars['semiaSC']/earth['semiaPl']*(1-power(mars['eccSC'],2)))
print Tiss
