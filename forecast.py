import tensorflow as tf
import numpy as np
import array
import math
#goal - add 2 numbers 
#inputs must be on the same line this model is run from 

tf.compat.v1.disable_eager_execution()
#euler1 = e^(-2x), euler2 = e^(-x), euler3 = e^(-x/5), exponential1 = x^(-2), exponential2 = x^(-1.5),exponential3 = x^(-1.1), constant = 1, fractional = 1/(x+1) 

max_size = 1000


beginsonwinter = 0
beginsonsummer = 0
beginsonfall = 0
beginsonspring = 0

class period:
  
  def _init_(self, name):
    self.name = name
    self.model = ""

  def set_model(self, newmodel):
    self.model = newmodel

  def calculatealpha(self, time, totaltransactionsinperiod):
    if (self.model == 'euler1'):
      numerator = exp(-2*time)
      denominator = 1
      for i in range(1,totaltransactionsinperiod+1):
        denominator = denominator + exp(-2*i)
      return numerator/denominator
    if (self.model == 'euler2'):
      numerator = exp(-time)
      denominator = 1
      for i in range(1,totaltransactionsinperiod+1):
        denominator = denominator + exp(-i)
      return numerator/denominator
    if (self.model == 'euler3'):
      numerator = exp(-time/5)
      denominator = 1
      for i in range(1,totaltransactionsinperiod+1):
        denominator = denominator + exp(-i/5)
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
          value = (inputarray[i][1])*(exp(-2*(counter)))
          weighedaverage = weighedaverage + value
          counter += 1
        counter+=1
        for i in range(1, counter):
          divisor = divisor + exp(-2*i)
        return (weighedaverage/divisor)
      if (self.model == 'euler2'):
        for i in range(sizeofarray-1, start-1, -1):
          value = (inputarray[i][1])*(exp(-(counter)))
          weighedaverage = weighedaverage + value
          counter += 1
        counter+=1
        for i in range(1, counter):
          divisor = divisor + exp(-i)
        return (weighedaverage/divisor)
      if (self.model == 'euler3'):
        for i in range(sizeofarray-1, start-1, -1):
          value = (inputarray[i][1])*(exp(-(counter)/5))
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
  trainingsize = math.floor(3/4*(sizeofarray))
  testingsize = sizeofarray - trainingsize
  testingav = 0
  euler1av = inputarray[trainingsize-1]
  euler2av = inputarray[trainingsize-1]
  euler3av = inputarray[trainingsize-1]
  exponential1av = inputarray[trainingsize-1]
  exponential2av = inputarray[trainingsize-1]
  exponential3av = inputarray[trainingsize-1]
  constantav = inputarray[trainingsize-1]
  fractionalav = inputarray[trainingsize-1]
  testingaverages = []
  counter = 1
  for i in range(trainingsize, sizeofarray-1):
    value = (inputarray[i][1])
    testingav = testingav + value
  counter = 1;
  for i in range(trainingsize-2, -1, -1):
    value = (inputarray[i][1])*(exp(-2(counter)))
    euler1av = euler1av + value
    counter += 1
  divisor = 1
  for i in range (1, counter+1):
    divisor = divisor + (exp(-2(i)))
  euler1av = euler1av/divisor
  testingaverages.append(euler1av)
  counter = 1
  divisor = 1
  for i in range(trainingsize-2, -1, -1):
    value = (inputarray[i][1])*(exp(-(counter)))
    euler2av = euler2av + value
    counter += 1
  for i in range (1, counter+1):
    divisor = divisor + (exp(-(i)))
  euler2av = euler2av/divisor
  testingaverages.append(euler2av)
  counter = 1
  divisor = 1
  for i in range(trainingsize-2, -1, -1):
    value = (inputarray[i][1])*(exp(-(counter)/5))
    euler3av = euler3av + value
    counter += 1
  for i in range (1, counter+1):
    divisor = divisor + (exp(-(i/5)))
  euler3av = euler3av/divisor
  testingaverages.append(euler3av)
  counter = 1
  divisor = 1
  for i in range(trainingsize-2, -1, -1):
    value = (inputarray[i][1])*((counter)**(-2))
    exponential1av = exponential1av + value
    counter += 1
  for i in range (1, counter+1):
    divisor = divisor + (i**(-2))
  exponential1av = exponentialav/divisor
  testingaverages.append(exponential1av)
  counter = 1;
  divisor = 1
  for i in range(trainingsize-2, -1, -1):
    value = (inputarray[i][1])*((counter)**-1.5)
    exponential2av = exponential2av + value
    counter += 1
  for i in range (1, counter+1):
    divisor = divisor + (i**(-1.5))
  exponential2av = exponentia2av/divisor
  testingaverages.append(exponential2av)
  counter = 1
  divisor = 1
  for i in range(trainingsize-2, -1, -1):
    value = (inputarray[i][1])*((counter)**-1.1)
    exponential3av = exponential3av + value
    counter += 1
  for i in range (1, counter+1):
    divisor = divisor + (i**(-1.1))
  exponential3av = exponential3av/divisor
  testingaverages.append(exponential3av)
  counter = 1
  divisor = 1
  for i in range(trainingsize-2, -1, -1):
    value = (inputarray[i][1])
    constantav = constantav + value
  testingaverages.append(constantav)
  counter = 1
  divisor = 1
  for i in range(trainingsize-2, -1, -1):
    value = (inputarray[i][1])*(1/((counter)+1))
    fractionalav = fractionalav + value
    counter += 1
  for i in range (1, counter+1):
    divisor = divisor + (1/(i+1))
  fractionalv = fractionalav/divisor
  testingaverages.append(fractionalav)
  testingarray = numpy.array(testingaverages)
  minimumdiff = abs(testingarray[0] - testingav)
  closestvalue = testingarray[0]
  indexofchoice = 0
  for i in range(1,7):
    if (abs(testingarray[i] - testingav) < minimumdiff):
      minimumdiff = abs(testingarray[i] - testingav)
      indexofchoice = i
    if ((abs(testingarray[i] - testingav) == minimumdiff) and (testingarray[i] > closestvalue)):
      closestvalue = testingarray[i]
      indexofchoice = i
  if (i == 0):
    period.set_model('euler1')
  if (i == 1):
    period.set_model('euler2')
  if (i == 2):
    period.set_model('euler3')
  if (i == 3):
    period.set_model('exponential1')
  if (i == 4):
    period.set_model('exponential2')
  if (i == 5):
    period.set_model('exponential3')
  if (i == 6):
    period.set_model('constant')
  if (i == 7):
    period.set_model('fractional')


    



  

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
with tf.compat.v1.Session() as sess:
  y_data = [5, 9, 10, 14, 18, 20, -1]
  x_data = [10, 20, 30, 40, 50, 70, -1]
  result = sess.run(y, feed_dict={y: y_data})
  dayindexes = result

print(dayindexes)

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
h = tf.placeholder(tf.float32, name="initialstate")
secondindex = 1
if (soldonfirstday == 0)
	secondindex = 1
if (soldonfirstday == 1)
	secondindex = 0
h = [soldonfirstday, secondindex]
fallcount = 0
wintercount = 0
springcount = 0
fallcount = 0
fallperiod = [[]]
winterperiod = [[]]
springperiod = [[]]
summerperiod = [[]]
for i in range(0,totaltransactions):
	currentday = y[:, i, :]
	if (((currentday%366) <= 78) or ((currentday%366) > 356)):
		winterperiod.append(currentday, x[:, i, :])
    if (i == 0):
      beginsonwinter = 1
		wintercount+=1
	if (((currentday%366) > 78) and ((currentday%366) <= 171)) :
		springperiod.append(currentday, x[:, i, :])
    if (i == 0):
      beginsonspring = 1
		springcount+=1
	if (((currentday%366) > 171) and ((currentday%366) <= 265)) :
		summerperiod.append(currentday, x[:, i, :])
    if (i == 0):
      beginsonsummer = 1
		summercount+=1
	if (((currentday%366) > 265) and ((currentday%366) <= 356)):
		fallperiod.append(currentday, x[:, i, :])
    if (i == 0):
      beginsonfall = 1
		fallcount+=1
	continue
fallarray = numpy.array(fallperiod)
winterarray = numpy.array(winterperiod)
springarray = numpy.array(springperiod)
summerarray = numpy.array(summerperiod)
fall = period('fall')
winter = period('winter')
spring = period('spring')
summer = period('summer')
decidemodel(fall, fallarray, fallcount)
decidemodel(winter, winterarray, wintercount)
decidemodel(spring, springarray, springcount)
decidemodel(summer, summerarray, summercount)

initialtrend = 0
marker = 0
endofyear = 0
averagewavlist = [] #average weighed average per year
averagewav = 0
falllastindex = fallcount-1
winterlastindex = wintercount-1
springlastindex = springcount-1
summerlastindex = summercount-1
addfall = 1
addwinter = 1
addspring = 1
addsummer = 1

while (marker < totalnumberyears):
  if (addfall == 1):
    for i in reversed(xrange(fallcount+1)):
      if (math.ceiling((fallarray[i][0])/365)>marker):
        averagewavarray = averagewavarray + fall.calculate_weighedaverage(fallarray, falllastindex, i)
        endofyear+=1
        falllastindex = i
        addfall = 0
        break
      else:
        continue
  if (addwinter == 1):
    for i in reversed(xrange(wintercount+1)):
      if (math.ceiling((winterarray[i][0])/365)>marker):
        averagewavarray = averagewavarray + winter.calculate_weighedaverage(winterarray, winterlastindex, i)
        endofyear+=1
        winterlastindex = i
        addwinter = 0
        break
      else:
        continue
  if (addspring ==1)
    for i in reversed(xrange(springcount+1)):
      if (math.ceiling((springarray[i][0])/365)>marker)
        averagewavarray = averagewavarray + spring.calculate_weighedaverage(springarray, springlastindex, i)
        endofyear+=1
        springlastindex = i
        addspring = 0
        break
      else
        continue
  if (addsummer == 1)
    for i in reversed(xrange(summercount+1)):
      if(math.ceiling((summerarray[i][0])/365)>marker)
        averagewavarray = averagewavarray + summer.calculate_weighedaverage(summerarray, summerlastindex, i)
        endofyear+=1
        summerlastindex = i
        addsummer = 0
      else
        continue
  if (endofyear == 4)
    marker+=1
    averagewav = Double(averagewavarray/4)
    averagewavlist.append(averagewav)
    averagewav = 0
    endofyear = 0
    addfall = 1
    addwinter = 1
    addspring = 1
    addsummer = 1

averagewavarray = numpy.array(averagwavlist)
fallinitialindex = 0
winterinitialindex = 0
springinitialindex = 0
summerinitialindex = 0
falllastindex = 0
winterlastindex = 0
springlastindex = 0
summerlastindex = 0
marker = 0
temporarysum = 0
firstfallweighedaverage = 0
secondfallweighedaverage = 0
firstwinterweighedaverage = 0
secondwinterweighedaverage = 0
first springweighedaverage = 0
second springweighedaverage = 0
first summerweighedaverage = 0
second summerweighedaverage = 0
while (marker < totalnumberyears)
  for i in range(0, fallcount):
    if (math.ceiling((fallarray[i][1])/365)>marker)
      temporarysum = temporarysum + fall.calculate_weighedaverage(fallarray, falllastindex, i)
      if (marker == 0)
        firstfallweighedaverage = temporarysum
      if (marker == 1)
        secondfallweighedaverage = temporarysum
      falllastindex = i
      temporarysum = temporarysum/(averagwavarray[marker])
      fallinitialindex = fallinitialindex + temporarysum
      temporarysum = 0
      marker+=1
      continue

fallinitialindex = fallinitialindex/totalnumberyears

#now caclulate the index for winter
marker = 0
while (marker < totalnumberyears)
  for i in range(0, wintercount):
  if (math.ceiling((winterarray[i][1])/365)>marker)
      temporarysum = temporarysum + winter.calculate_weighedaverage(winterarray, winterlastindex, i)
      if (marker == 0)
        firstwinterweighedaverage = temporarysum
      if (marker == 1)
        secondwinterweighedaverage = temporarysum
      winterlastindex = i
      temporarysum = temporarysum/(averagwavarray[marker])
      winterinitialindex = winterinitialindex + temporarysum
      temporarysum = 0
      marker+=1
      continue

winterinitialindex = winterinitialindex/totalnumberyears

marker = 0
while (marker < totalnumberyears)
  for i in range(0, springcount):
  if (math.ceiling((springarray[i][1])/365)>marker)
      temporarysum = temporarysum + spring.calculate_weighedaverage(springarray, springlastindex, i)
      if (marker == 0)
        firstspringweighedaverage = temporarysum
      if (marker == 1)
        secondspringweighedaverage = temporarysum
      springlastindex = i
      temporarysum = temporarysum/(averagwavarray[marker])
      springinitialindex = springinitialindex + temporarysum
      temporarysum = 0
      marker+=1
      continue

springinitialindex = springinitialindex/totalnumberyears

marker = 0
while (marker < totalnumberyears)
  for i in range(0, summercount):
  if (math.ceiling((summerarray[i][1])/365)>marker)
      temporarysum = temporarysum + summer.calculate_weighedaverage(summerarray, summerlastindex, i)
      if (marker == 0)
        firstsummerweighedaverage = temporarysum
      if (marker == 1)
        secondsummerweighedaverage = temporarysum
      summerlastindex = i
      temporarysum = temporarysum/(averagwavarray[marker])
      summerinitialindex = summerinitialindex + temporarysum
      temporarysum = 0
      marker++
      continue

summerinitialindex = summerinitialindex/totalnumberyears

if (totalnumberyears >= 2)
  fallweighedaveragediff = secondfallweighedaverage - firstfallweighedaverage
  winterweighedaveragediff = secondwinterweighedaverage - firstwinterweighedaverage
  springweighedaveragediff = secondspringweighedaverage - firstspringweighedaverage
  summerweighedaveragediff = secondsummerweighedaverage - firstsummerweighedaverage
  initialtrend = (1/4)*((fallweighedaveragediff/4) + (winterweighedaveragediff/4) + (springweighedaveragediff/4) + (summerweighedaveragediff/4)) 

for i in range(1, fallcount+1)
  fallarray[i] = fall.calculateweighedaverage(fallarray,0,i)

for i in range(1, wintercount+1)
  winterarray[i] = winter.calculateweighedaverage(winterarray,0,i)

for i in range(1, springcount+1)
  springarray[i] = spring.calculateweighedaverage(springarray,0,i)

for i in range(1, summercount+1)
  summerarray[i] = summer.calculateweighedaverage(summerarray,0,i)

fs = tf.placeholder(tf.float32, name="falltospringweighedserialaverage")
finalarray = np.concatenate((fallarray, winterarray, springarray, summerarray))
fs = torch.from_numpy(finalarray)



init = tf.compat.v1.global_variables_initializer()
saver = tf.compat.v1.train.Saver([z])

with tf.compat.v1.Session() as sess:
  sess.run(init)
  x_data = [1, 2, 9, 20, 240, 338, 500, 800]
  y_data = [10, 15, 20, 25, 9, 100, 400, 700]
  print(x)
  print(y)
  result = sess.run(fs, feed_dict={x: x_data, y: y_data})
  print(result)
  z_value = result
  saver.save(sess, './forecast')
  sess.close()


















  

