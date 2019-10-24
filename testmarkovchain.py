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
print(z)
#z should now have relevant markov chain state


