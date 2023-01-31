import numpy as np
from scipy.stats import pearsonr

def read_bits(filename):
  """ Read bits from the raw file.  """
  bytes_data = np.fromfile(filename, dtype="uint8") # read bytes
  bits_data = np.unpackbits(bytes_data, axis=None, count=None, bitorder='little') # unpack to bits
  bits_data = bits_data.reshape((-1,32))[:,::-1].ravel() # reverse bits order in blocks of 32
  return bits_data


def autocorr(x,lag):
  """ Estimate autocorrelation function at a given lag """
  return pearsonr(x[lag:],x[:-lag]).statistic