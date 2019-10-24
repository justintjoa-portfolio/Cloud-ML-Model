import tensorflow as tf
import numpy as np
#print(tf._version_)

tf.compat.v1.disable_eager_execution()

with tf.compat.v1.Session() as sess:
  new_saver = tf.compat.v1.train.import_meta_graph('calculate.meta')
  new_saver.restore(sess, tf.compat.v1.train.latest_checkpoint('./'))
  # Now, let's access and create placeholders variables and
  # create feed-dict to feed new data
 
  graph = tf.compat.v1.get_default_graph()
  z = graph.get_tensor_by_name("Variable:0")
  x = graph.get_tensor_by_name("Placeholder:0")
  y = graph.get_tensor_by_name("Placeholder_1:0")
  h = graph.get_tensor_by_name("mul_1:0")
  print(z)
  feed_dict ={x:13.0,y:17.0}
  #Now, access the op that you want to run. 
  result = sess.run(h,feed_dict)
  print(result)
  z_value = result
  #This will print 60 which is calculated 
  #using new values of w1 and w2 and saved value of b1. 
  sess.close()


