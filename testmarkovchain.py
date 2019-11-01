import tensorflow as tf
import numpy as np
import array
import math
#goal - add 2 numbers 
#inputs must be on the same line this model is run from 

tf.compat.v1.disable_eager_execution()
#tf.compat.v1.enable_eager_execution()
#euler1 = e^(-2x), euler2 = e^(-x), euler3 = e^(-x/5), exponential1 = x^(-2), exponential2 = x^(-1.5),exponential3 = x^(-1.1), constant = 1, fractional = 1/(x+1) 

max_size = 1000

class period:
  
  def __init__(self, name):
    self.name = name
    self.model = ""

  def set_model(self, newmodel):
    self.model = newmodel

  def print_model(self):
    print(self.model)

  def calculatealpha(self, time, totaltransactionsinperiod):
    if (self.model == 'euler1'):
      numerator = math.exp(-2*time)
      denominator = 1
      for i in range(1,totaltransactionsinperiod+1):
        denominator = denominator + math.exp(-2*i)
      return numerator/denominator
    if (self.model == 'euler2'):
      numerator = math.exp(-time)
      denominator = 1
      for i in range(1,totaltransactionsinperiod+1):
        denominator = denominator + math.exp(-i)
      return numerator/denominator
    if (self.model == 'euler3'):
      numerator = exp(-time/5)
      denominator = 1
      for i in range(1,totaltransactionsinperiod+1):
        denominator = denominator + math.exp(-i/5)
      return numerator/denominator
    if (self.model == 'exponential1'):
      numerator = (time)**(-2)
      denominator = 1
      for i in range(1,totaltransactionsinperiod+1):
        denominator = denominator + (i**(-2))
      return numerator/denominator
    if (self.model == 'exponential2'):
      numerator = time**(-1.5)
      denominator = 1
      for i in range(1,totaltransactionsinperiod+1):
        denominator = denominator + (i**(-1.5))
      return numerator/denominator
    if (self.model == 'exponential3'):
      numerator = time**(-1.1)
      denominator = 1
      for i in range(1,totaltransactionsinperiod+1):
        denominator = denominator + (i**(-1.1))
      return numerator/denominator
    if (self.model == 'exponential3'):
      numerator = time
      denominator = 1
      for i in range(1,totaltransactionsinperiod+1):
        denominator = denominator + (i**(-1.1))
      return numerator/denominator
    if (self.model == 'constant'):
      numerator = time
      return numerator/(sizeofarray-start)
    if (self.model == 'fractional'):
      numerator = 1/(time+1)
      denominator = 1
      for i in range(1,totaltransactionsinperiod+1):
        denominator = denominator + (1/(i+1))
      return numerator/denominator


  def calculateweighedaverage(self, inputarray, start, sizeofarray): #left off on october 1 6:38
      counter = 1
      weighedaverage = inputarray[sizeofarray]
      divisor = 1
      if (self.model == 'euler1'):
        for i in range(sizeofarray-1, start-1, -1):
          value = (inputarray[i][1])*(math.exp(-2*(counter)))
          weighedaverage = weighedaverage + value
          counter += 1
        counter+=1
        for i in range(1, counter):
          divisor = divisor + exp(-2*i)
        return (weighedaverage/divisor)
      if (self.model == 'euler2'):
        for i in range(sizeofarray-1, start-1, -1):
          value = (inputarray[i][1])*(math.exp(-(counter)))
          weighedaverage = weighedaverage + value
          counter += 1
        counter+=1
        for i in range(1, counter):
          divisor = divisor + exp(-i)
        return (weighedaverage/divisor)
      if (self.model == 'euler3'):
        for i in range(sizeofarray-1, start-1, -1):
          value = (inputarray[i][1])*(math.exp(-(counter)/5))
          weighedaverage = weighedaverage + value
          counter += 1
        counter+=1
        for i in range(1, counter):
          divisor = divisor + exp(-i/5)
        return (weighedaverage/divisor)
      if (self.model == 'exponential1'):
        for i in range(sizeofarray-1, start-1, -1):
          value = (inputarray[i][1])*((counter)**-2)
          counter += 1
          weighedaverage = weighedaverage + value
        counter+=1
        for i in range(1, counter):
          divisor = divisor + (i**(-2))
        return (weighedaverage/divisor)
      if (self.model == 'exponential2'):
        for i in range(sizeofarray-1, start-1, -1):
          value = (inputarray[i][1])*((counter)**-1.5)
          weighedaverage = weighedaverage + value
          counter += 1
        counter+=1
        for i in range(1, counter):
          divisor = divisor + (i**(-1.5))
        return (weighedaverage/divisor)
      if (self.model == 'exponential3'):
        for i in range(sizeofarray-1, start-1, -1):
          value = (inputarray[i][1])*((counter)**-1.1)
          weighedaverage = weighedaverage + value
          counter += 1
        counter+=1
        for i in range(1, counter):
          divisor = divisor + (i**(-1.1))
        return (weighedaverage/divisor)
      if (self.model == 'constant'):
        for i in range(sizeofarray-1, start-1, -1):
          value = (inputarray[i][1])
          weighedaverage = weighedaverage + value
        return weighedaverage/(sizeofarray-start)
      if (self.model == 'fractional'):
        for i in range(sizeofarray-1, start-1, -1):
          value = (inputarray[i][1])*(1/((counter)+1))
          weighedaverage = weighedaverage + value
          counter += 1
        counter+=1
        for i in range(1, counter+1):
          divisor = divisor + (1/(i+1))
        return (weighedaverage/divisor)




def decidemodel(period, inputarray, sizeofarray):
  print("welcome")
  trainingsize = math.floor(3/4*(sizeofarray))
  testingsize = sizeofarray - trainingsize
  testingav = 0
  euler1av = inputarray[trainingsize-1][1]
  euler2av = inputarray[trainingsize-1][1]
  euler3av = inputarray[trainingsize-1][1]
  exponential1av = inputarray[trainingsize-1][1]
  exponential2av = inputarray[trainingsize-1][1]
  exponential3av = inputarray[trainingsize-1][1]
  constantav = inputarray[trainingsize-1][1]
  fractionalav = inputarray[trainingsize-1][1]
  testingaverages = []
  counter = 1
  for i in range(trainingsize, sizeofarray):
    value = (inputarray[i][1])
    testingav = testingav + value
  print(testingav)
  counter = 1;
  for i in range(trainingsize-2, -1, -1):
    value = (inputarray[i][1])*(math.exp(-2*(counter)))
    euler1av = euler1av + value
    counter += 1
  divisor = 1
  for i in range (1, counter):
    divisor = divisor + (math.exp(-2*(i)))
  euler1av = euler1av/divisor
  testingaverages.append(euler1av)
  counter = 1
  divisor = 1
  for i in range(trainingsize-2, -1, -1):
    value = (inputarray[i][1])*(math.exp(-(counter)))
    euler2av = euler2av + value
    counter += 1
  for i in range (1, counter):
    divisor = divisor + (math.exp(-(i)))
  euler2av = euler2av/divisor
  testingaverages.append(euler2av)
  counter = 1
  divisor = 1
  for i in range(trainingsize-2, -1, -1):
    value = (inputarray[i][1])*(math.exp(-(counter)/5))
    euler3av = euler3av + value
    counter += 1
  for i in range (1, counter):
    divisor = divisor + (math.exp(-(i/5)))
  euler3av = euler3av/divisor
  testingaverages.append(euler3av)
  counter = 1
  divisor = 1
  for i in range(trainingsize-2, -1, -1):
    value = (inputarray[i][1])*((counter)**(-2))
    exponential1av = exponential1av + value
    counter += 1
  for i in range (1, counter):
    divisor = divisor + (i**(-2))
  exponential1av = exponential1av/divisor
  testingaverages.append(exponential1av)
  counter = 1;
  divisor = 1
  for i in range(trainingsize-2, -1, -1):
    value = (inputarray[i][1])*((counter)**-1.5)
    exponential2av = exponential2av + value
    counter += 1
  for i in range (1, counter):
    divisor = divisor + (i**(-1.5))
  exponential2av = exponential2av/divisor
  testingaverages.append(exponential2av)
  counter = 1
  divisor = 1
  for i in range(trainingsize-2, -1, -1):
    value = (inputarray[i][1])*((counter)**-1.1)
    exponential3av = exponential3av + value
    counter += 1
  for i in range (1, counter):
    divisor = divisor + (i**(-1.1))
  exponential3av = exponential3av/divisor
  testingaverages.append(exponential3av)
  counter = 1
  divisor = 1
  for i in range(trainingsize-2, -1, -1):
    value = (inputarray[i][1])
    constantav = constantav + value
    counter+=1
  constantav = constantav/(counter)
  testingaverages.append(constantav)
  counter = 1
  divisor = 1
  for i in range(trainingsize-2, -1, -1):
    value = (inputarray[i][1])*(1/((counter)+1))
    fractionalav = fractionalav + value
    counter += 1
  for i in range (1, counter):
    divisor = divisor + (1/(i+1))
  fractionalav = fractionalav/divisor
  testingaverages.append(fractionalav)
  testingarray = np.array(testingaverages)
  minimumdiff = abs(testingarray[0] - testingav)
  closestvalue = testingarray[0]
  indexofchoice = 0
  for i in range(0,8):
    print('res')
    print(testingarray[i]-testingav)
    if ((abs(testingarray[i] - testingav)) < minimumdiff):
      minimumdiff = abs(testingarray[i] - testingav)
      indexofchoice = i
      continue
    if ((abs(testingarray[i] - testingav) == minimumdiff) and (testingarray[i] > closestvalue)):
      closestvalue = testingarray[i]
      indexofchoice = i
      continue
  if (indexofchoice == 0):
    period.set_model('euler1')
  if (indexofchoice == 1):
    period.set_model('euler2')
  if (indexofchoice == 2):
    period.set_model('euler3')
  if (indexofchoice == 3):
    period.set_model('exponential1')
  if (indexofchoice == 4):
    period.set_model('exponential2')
  if (indexofchoice == 5):
    period.set_model('exponential3')
  if (indexofchoice == 6):
    period.set_model('constant')
  if (indexofchoice == 7):
    period.set_model('fractional')

  

beginsonwinter = 0
beginsonsummer = 0
beginsonfall = 0
beginsonspring = 0






  

x = tf.compat.v1.placeholder(tf.float32, name="amounts_by_day")
y = tf.compat.v1.placeholder(tf.float32, name="dayindexes")
soldonfirstday = 1
yestoyes = 0
notoyes = 0
currentday = 0
previousday = 0
ytynumberdays = 0
ntynumberdays = 0
totaltransactions = 0
dayindexes = []
moneyindexes = []
with tf.compat.v1.Session() as sess:
  y_data = [5, 9, 10, 14, 18, 20, 80, 130, 180, 220, 270, 310, 350, 500, -1]
  x_data = [10, 20, 30, 40, 50, 70, 20, 150, 170, 230, 250, 40, 5, 2, -1]
  result = sess.run(y, feed_dict={y: y_data})
  dayindexes = result
  result = sess.run(x, feed_dict={x: x_data})
  moneyindexes = result

print(dayindexes)
print(moneyindexes)
for i in range(0, max_size):
    currentday = dayindexes[i]
    if (currentday < 0):
      break
    totaltransactions+=1
    if (i == 0):
      previousday = currentday
      ntynumberdays = previousday - 1
      if (ntynumberdays > 0):
        notoyes+=1
        soldonfirstday = 0
      continue
    difference = currentday - previousday
    ytynumberdays+=1
    if (difference == 1):
      yestoyes+=1
      previousday = currentday
      continue
    ntynumberdays = ntynumberdays + (difference - 1)
    if (difference > 1):
      notoyes+=1
      previousday = currentday
      continue

totalnumberyears = math.floor((dayindexes[(totaltransactions-1)])/365)
z = tf.compat.v1.placeholder(tf.float32, name="markovchain")
z = [[yestoyes/ytynumberdays, notoyes/ntynumberdays],[(1-yestoyes/ytynumberdays), (1-notoyes/ntynumberdays)]]
secondindex = 1
soldonfirstday = 0
if (dayindexes[0] == 1):
  soldonfirstday = 1
  secondindex = 0
if (dayindexes[0] != 1):
  secondindex = 1
h = [soldonfirstday, secondindex]
fallcount = 0
wintercount = 0
springcount = 0
summercount = 0
fallperiod = [[]]
winterperiod = [[]]
springperiod = [[]]
summerperiod = [[]]
for i in range(0,totaltransactions):
  currentday = dayindexes[i]
  if (((currentday%366) <= 78) or ((currentday%366) > 356)):
    winterperiod[-1].append(currentday)
    winterperiod[-1].append(moneyindexes[i])
    winterperiod.append([])
    if (i == 0):
      beginsonwinter = 1
    wintercount+=1
  if (((currentday%366) > 78) and ((currentday%366) <= 171)):
    springperiod[-1].append(currentday)
    springperiod[-1].append(moneyindexes[i])
    springperiod.append([])
    if (i == 0):
      beginsonspring = 1
    springcount+=1
  if (((currentday%366) > 171) and ((currentday%366) <= 265)) :
    summerperiod[-1].append(currentday)
    summerperiod[-1].append(moneyindexes[i])
    summerperiod.append([])
    if (i == 0):
      beginsonsummer = 1
    summercount+=1
  if (((currentday%366) > 265) and ((currentday%366) <= 356)):
    fallperiod[-1].append(currentday)
    fallperiod[-1].append(moneyindexes[i])
    fallperiod.append([])
    if (i == 0):
      beginsonfall = 1
    fallcount+=1
  continue
del fallperiod[-1]
del winterperiod[-1]
del springperiod[-1]
del summerperiod[-1]
fallarray = np.array(fallperiod)
winterarray = np.array(winterperiod)
springarray = np.array(springperiod)
summerarray = np.array(summerperiod)
print("fall")
print(fallarray)
print("winter")
print(winterarray)
print("spring")
print(springarray)
print("summer")
print(summerarray)
print('initial')
print(summerarray[0])
fall = period('fall')
winter = period('winter')
spring = period('spring')
summer = period('summer')
decidemodel(fall, fallarray, fallcount)
decidemodel(winter, winterarray, wintercount)
decidemodel(spring, springarray, springcount)
decidemodel(summer, summerarray, summercount)
fall.print_model()
winter.print_model()
spring.print_model()
summer.print_model()
#z should now have relevant markov chain state


