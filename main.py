import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pandas as pd

class data:
  def __init__(self):
    self._true = 0
    self._false = 0
    self._tabData = []
    
  def evaluateTrueness(self, _succ_rate):
    self._true = 0
    for i in self._tabData:
      if (i < _succ_rate):
        self._true += 1
    self._false = len(self._tabData) - self._true

class binomation:
  def __init__(self, succ_rate, _m, _n):
    self._succ_rate = succ_rate
    self._m = _m
    self._n = _n
    self._data = []

  def evaluateSuccessRate(self):
    for each_obj in self._data:
      each_obj.evaluateTrueness(self._succ_rate)
    
  def generateData(self):
    self._data = []
    for counter in range(0, self._m + 1):
      self._data.append(self.__generateSingleData(self._n))

# this will create an array with N length containing the value [0..1]
  def __generateSingleData(self, n):
    temp_list = []
    if (n < 1):
      raise TypeError("Array can not be created with length less than 1")

    new_data = data()
    for counter in range(0, n ):
      new_data._tabData.append(round(np.random.uniform(), 3))
    
    return new_data
  
  def printData(self, showTrue = False):
    if (len(self._data) < 1):
      raise ValueError("Data is not defined yet")
    for ptr_1 in self._data:
      if (showTrue):
        print("True ", ptr_1._true)
      else:
        for ptr_2 in ptr_1._tabData:
          print(ptr_2, end=" ")
      print()
    
  def exportDF(self, useDF=False):
    temp_list = np.asarray([])
    for counter in self._data:
      temp_list = np.insert(temp_list, 0, counter._true)
    if useDF:
      return pd.DataFrame(temp_list, columns=['true'])
    else:
      return temp_list
  
  def visualize(self):
    hist_bin = np.linspace(0, self._n, self._n)
    data_df = self.exportDF()
  
  def exportXY(self):
    temp_list = [0 for i in range(self._n + 1)]

    for counter in self._data:
      temp_list[counter._true] += 1
    return temp_list


# Define this Parameter
success_rate = 0.6
n_length = 50
n_data = 1000

binoModel = binomation(success_rate, n_data, n_length)
binoModel.generateData()
binoModel.evaluateSuccessRate()
conv_list = binoModel.exportXY()
arr_data = binoModel.exportDF(False)
hist_bins = [x for x in range(n_length + 1)]

def init():
  plt.hist(arr_data[:1], bins=hist_bins)
  plt.text(0.1, 2.8, "Frame: 0")

def updateData(frame):
  if (frame >= 1):
    plt.cla()
    plt.hist(arr_data[:frame], density=True, bins=hist_bins, alpha=0.5)
    ax = plt.gca()
    ax.set_xlabel("Frame: " + str(frame))

fig = plt.figure()
simulation = animation.FuncAnimation(fig, updateData, interval=2, frames=n_data, init_func=init, repeat=False)

plt.show()
