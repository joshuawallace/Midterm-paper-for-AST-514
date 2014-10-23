species = ["H", "Li", "Na", "K", "Rb", "He"]
A = [12.0, 1.10, 6.33, 5.12, 2.60, 10.93]
chi = [13.598,5.392,5.139,4.341,4.177,24.587]

#         atom abun chi [gi+1/gi]
bigun = [ ["H",12.0,13.598,.5],
          ["Li",1.10,5.392,.5],
          ["Na",6.33,5.139,.5],
          ["Mg",8.151,7.046,2.],
          ["Al",6.47,5.986,0.16666666],
          ["K",5.12,4.341,.5],
          ["Ca",6.36,6.113,2.],
          ["Rb",2.60,4.177,.5],
          ["Sc",3.17,6.54,.1],
          ["Ti",5.02,6.82,.2],
          ["Sr",2.97,5.695,2.],
          ["Ba",2.13,5.212,2.],
          ["He",10.93,24.587,2.]]

print len(bigun)
          

import numpy as np

T = 5778. #if this is changed the prefactor will need to be chaged as well. Maybe

"""for i in range(len(species)):
    relativeabundance = np.exp(A[i] - 12.0)
    sahaionization = 2.413e15 * (T)**(1.5) * 2. * 1./2. * np.exp(-1*chi[i] / (8.6173324e-5 * T))
    string = "Relative abundance is " + str(relativeabundance)
    print string
    string = """

rel=[]

normalization = 1.20324462038e+14#1.0#82374.5901884

for i in range(len(bigun)):
    relativeabundance = np.exp(bigun[i][1] - 12.0)
    sahaionization = 2.413e15 * (T)**(1.5) * 2. * bigun[i][3] * np.exp(-1*bigun[i][2] / (8.6173324e-5 * T))
    print bigun[i][0] + ":"
#    string = "Relative abundance is " 
#    print relativeabundance
#    print string
    print "Fraction of particles ionized is "
    print sahaionization
    r = relativeabundance * sahaionization
#    if i==0:
#        normalization = r
    r = r/normalization
    print "Relative number of electrons contributed is "
    print r
    print "\n"
    rel.append(r)

sum_ = sum(rel)
ne = sum_ * .734 * 1.4 * 6.02214129e23 #mass fraction of hydrogen, average density of sun, N_A

#Go back and recalculate the actual fraction for h-

hoverhminus = 2.413e15 / ne * (T)**(1.5) * 2. * 2. * np.exp(-0.754 / (8.6173324e-5 * T))

hminusoverh = 1./hoverhminus


print str(hminusoverh)
