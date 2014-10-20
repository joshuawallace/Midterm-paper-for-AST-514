import matplotlib.pyplot as pp
import numpy as np
from scipy.interpolate import interp1d as intp

lambda_ = [16300., 16200., 16100., 16000., 15750., 15500., 15250., 15000., 14750., 14500., 14250., 14000., 13750., 13500., 13250., 13000., 12750., 12500., 12250., 12000., 11750., 11500., 11250., 11000., 10750., 10500., 10250., 10000., 9750., 9500., 9250., 9000., 8750., 8500., 8250., 8000., 7750., 7500., 7250., 7000., 6750., 6500., 6250., 6000., 5750., 5500., 5250., 5000., 4750., 4500., 4250., 4000., 3750., 3500., 3250., 3000., 2750., 2500., 2250., 2000., 1750., 1500., 1250.]

cross_section = [0.1989, 0.4974, 0.8697, 1.302, 2.575, 4.052, 5.677, 7.407, 9.211, 11.07, 12.95, 14.85, 16.74, 18.62, 20.46, 22.26, 24.02, 25.71, 27.33, 28.87, 30.34, 31.72, 33.01, 34.19, 35.28, 36.25, 37.13, 37.89, 38.53, 39.06, 39.48, 39.77, 39.95, 40.01, 39.95, 39.77, 39.48, 39.07, 38.54, 37.91, 37.17, 36.32, 35.37, 34.32, 33.17, 31.94, 30.62, 29.23, 27.77, 26.24, 24.65, 23.02, 21.35, 19.65, 17.92, 16.19, 14.46, 12.75, 11.08, 9.453, 7.918, 6.512, 5.431]

lambda_.reverse()
cross_section.reverse()

#print len(lambda_)
#print len(cross_section)

fit = intp(lambda_,cross_section,kind='cubic')


lambdasmaller = np.linspace(1250.01,16299.99,1200)
#lambdasmaller = np.linspace(16299.99,1250.011200)
#print lambdasmaller

pp.plot(lambdasmaller,fit(lambdasmaller))
pp.scatter(lambda_,cross_section, marker='o')
pp.ylim(0,45)
pp.xlim(1250,16300)
pp.rc('text',usetex=True)
pp.xlabel(r"Wavelength (\AA)")
pp.ylabel(r"$\sigma$ (10^{-18}~cm$^{2}$)")


pp.savefig("boundfree.crosssection.png")

#pp.show()
