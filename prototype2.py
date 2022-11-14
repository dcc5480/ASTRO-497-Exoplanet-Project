import sys
import os
import numpy as np
from astroquery.mast import Observations
from astropy.io import fits
import matplotlib.pyplot as plt
import astropy.units as u
from scipy.signal import savgol_filter
from astropy.timeseries import BoxLeastSquares
normalstdout=sys.stdout

#It is necessary to set "mainpath" to an appropriate location on any given machine.
def Analyze(keplername=None,mainpath="/Users/suoenallecsim/Documents/PrimeNumbers",silent=True,savedata=True):
  #Gathering options for given keplername
  if keplername==None:
    mainpath=input(f"Choose an existing filepath for data to be saved under\n")
    if not mainpath:return
    keplername=input(f"Choose a Kepler ID (Kepler-10 for example)\n")

  print(f"Gathering obs_id for {keplername}")
  obs=Observations.query_criteria(obs_collection=["Kepler"],objectname=keplername,radius=0)

  obsrow=int(input(f"Choose an obs_id row:\n{obs['obs_id']}\n"))
  print(f"Gathering Products for Row {obsrow}")
  products=Observations.get_product_list(obs[obsrow])
  product=Observations.filter_products(products,description=input(f"Choose a description:\n{products['description']}\n"))

  #Collecting and combining data for chosen observation
  time,flux,err=np.array([],np.float32),np.array([],np.float32),np.array([],np.float32)
  for i in range(len(product)):
    filepath=f"/mastDownload/{product['obs_collection'][i]}/{product['obs_id'][i]}/{product['productFilename'][i]}"
    if savedata and (not os.path.exists(f"{mainpath}{filepath}")):
      f=open(os.devnull,'w')
      print("Downloading Data...")
      print("(This may take a while)")
      if silent==True:sys.stdout=f
      Observations.download_products(product)
      f.close();sys.stdout=normalstdout
    temp=fits.open(f"{mainpath}{filepath}")[1].data
    time,flux,err=np.append(time,temp["TIME"]),np.append(flux,temp["SAP_FLUX"]),np.append(err,temp["SAP_FLUX_ERR"])
  if len(time)<50:
    print("Warning: data contains <50 entries")

  #Plotting raw data
  plt.errorbar(time,flux,err,fmt=',')
  plt.show()
  print("Plotting Cleaned Data...")
  
  #Clean the data
  #Remove NaN
  t1=(~np.isnan(time))&(~np.isnan(flux))
  time=time[t1]
  flux=flux[t1]
  err=err[t1]
  #Flatten data
  filt=savgol_filter(flux,101,2)
  flux=flux/filt
  err=err/filt
  #Remove outliers
  t1=np.abs(1-flux)<2*np.std(flux)
  time=time[t1]
  flux=flux[t1]
  err=err[t1]
  plt.errorbar(time,flux,err,fmt=',')
  plt.show()
  print("Plotting Periodogram...")

  #Create box least squares model
  model=BoxLeastSquares(time,flux)
  periodogram=model.autopower(0.2)
  plt.plot(periodogram.period,periodogram.power)
  plt.show()
  #Analyze model
  max_power=np.argmax(periodogram.power)
  period=periodogram.period[max_power]
  print(f"\nTransit period in days appears to be: {period}\n")
  stats=model.compute_stats(periodogram.period[max_power],periodogram.duration[max_power],periodogram.transit_time[max_power])
  print("Plotting Folded Data...")
  #Folded data
  timefold=(time-max_power)%period
  plt.plot(timefold,flux,'.k',ms=3)
  plt.show()
  

#Suggested test objects: "Kepler-2b" "Kepler-3c" "Kepler-10"
#Lightcurve long cadence is faster, though both short and long should work.

Analyze()
