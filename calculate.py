import tensorflow as tf
import numpy as np
#goal - add 2 numbers 
#inputs must be on the same line this model is run from 

tf.compat.v1.disable_eager_execution()

x = tf.compat.v1.placeholder(tf.compat.v1.float32, None)
y = tf.compat.v1.placeholder(tf.compat.v1.float32, None)
h = tf.compat.v1.placeholder(tf.compat.v1.float32, None)
i = tf.compat.v1.placeholder(tf.compat.v1.float32, None)
z = tf.compat.v1.Variable([0.], tf.float32)
i = x*y
h = (y + x)*i
init = tf.compat.v1.global_variables_initializer()
saver = tf.compat.v1.train.Saver([z])

with tf.compat.v1.Session() as sess:
        sess.run(init)
        x_data = [1]
        y_data = [3]
        print(x)
        print(y)
        print(h)
        result = sess.run(h, feed_dict={x: x_data, y: y_data})
        print(result)
        z_value = result
        saver.save(sess, './calculate')
        sess.close()



