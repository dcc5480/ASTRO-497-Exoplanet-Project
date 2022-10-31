import sys
import os
import numpy as np
from astroquery.mast import Observations
from astropy.io import fits
import matplotlib.pyplot as plt
normalstdout=sys.stdout

#It is necessary to set "mainpath" to an appropriate location on any given machine.
def getData(keplername,mainpath="/Users/suoenallecsim/Documents/PrimeNumbers",silent=True):
  #Gathering options for given keplername
  obs=Observations.query_criteria(obs_collection=["Kepler"],objectname=keplername,radius=0)
  obsrow=int(input(f"Choose an obs_id row:\n{obs['obs_id']}\n"))
  products=Observations.get_product_list(obs[obsrow])
  product=Observations.filter_products(products,description=input(f"Choose a description:\n{products['description']}\n"))

  #Collecting and combining data for chosen observation
  time,flux,err=np.array([],np.float32),np.array([],np.float32),np.array([],np.float32)
  for i in range(len(product)):
    filepath=f"/mastDownload/{product['obs_collection'][i]}/{product['obs_id'][i]}/{product['productFilename'][i]}"
    if not os.path.exists(f"{mainpath}{filepath}"):
      f=open(os.devnull,'w')
      print("Downloading...")
      print("(This may take a while)")
      if silent==True:sys.stdout=f
      Observations.download_products(product)
      f.close();sys.stdout=normalstdout
    temp=fits.open(f"{mainpath}{filepath}")[1].data
    time,flux,err=np.append(time,temp["TIME"]),np.append(flux,temp["SAP_FLUX"]),np.append(err,temp["SAP_FLUX_ERR"])
  if len(time)<50:
    print("Warning: data contains <50 entries")

  #Plotting raw data
  plt.errorbar(time,flux,err)
  plt.show()
  return obs,obsrow,products,product,filepath,time,flux,err

#Suggested test objects: "Kepler-2 b" "Kepler-3 c"
#Lightcurve long cadence is faster, though both short and long should work.
