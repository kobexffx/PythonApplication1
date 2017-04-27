from pyhdf.SD import *
 # import Numeric Python package -- Numpy
from numpy import *

 data = array(((1, 2, 3),
(4, 5, 6)), int16)

 # Create an HDF file
 sd = SD("hello.hdf", SDC.WRITE | SDC.CREATE)

 # Create a dataset
 sds = sd.create("sds1", SDC.INT16, (2, 3))

 # Fill the dataset with a fill value
 sds.setfillvalue(0)

 # Set dimension names
 dim1 = sds.dim(0)
 dim1.setname("row")
 dim2 = sds.dim(1)
 dim2.setname("col")

 # Assign an attribute to the dataset
 sds.units = "miles"

 # Write data
 sds[:] = data

 # Close the dataset
 sds.endaccess()

 # Flush and close the HDF file
 sd.end() 
