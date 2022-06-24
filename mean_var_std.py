import numpy as np

def calculate(list):
  
  if len(list) == 9 :
    # list as 3x3 array
    list_arr = np.array(list).reshape(3,3)
    # keys
    cal_keys = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    
    # get mean, var, sd, max, min, and sum along all axes
    # add to list of values
    cal_vals = []
    stats = [np.mean, np.var, np.std, np.max, np.min, np.sum]

    [cal_vals.append(calc_attribute(stat, list_arr)) for stat in stats]

    calculations = dict(zip(cal_keys, cal_vals))
    return calculations
  else :
    raise ValueError('List must contain nine numbers.')
  

# calls given numpy statistic function on given array along two axes and flattened array
# returns results as list
def calc_attribute (stat, arr) :
  # results list
  lstats = []
  # axes to calculate along
  axes = [0,1,None]

  [lstats.append(stat(arr, axis=a)) for a in axes]

  # covert arrays to lists (first two items)
  for i in [0,1] :
    lstats[i] = lstats[i].tolist()
  
  return lstats