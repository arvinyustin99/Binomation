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
    
  def exportDF(self):
    temp_list = []
    for counter in self._data:
      temp_list.append([counter._true, counter._false])
    new_df = pd.DataFrame(temp_list, columns=['true', 'false'])
    return new_df
  
  def visualize(self):
    hist_bin = np.linspace(0, self._n, self._n)
    data_df = self.exportDF()
  
  def prepare_animation(bar_container):
    def animate(frame_number):
      data
  
success_rate = 0.95
n_length = 50
n_data = 10000

binoModel = binomation(success_rate, n_data, n_length)
binoModel.generateData()
binoModel.evaluateSuccessRate()
binoModel.printData(True)
temp_list = binoModel.exportDF()

HIST_BINS = np.linspace(0, n_length, n_length)
n, _ = np.histogram(temp_list[['true']], bins=n_length)
print(HIST_BINS)

print(temp_list)
fig, ax = plt.subplots()

_, _, bar_container = ax.hist(temp_list['true'],range=[i for i in (0, n_length)], bins=n_length, density=True)
plt.show()