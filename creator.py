import tensorflow as tf
tf.compat.v1.disable_eager_execution()
saver = tf.compat.v1.train.import_meta_graph('./calculate.meta', clear_devices=True)
graph = tf.compat.v1.get_default_graph()
input_graph_def = graph.as_graph_def()
sess = tf.compat.v1.Session()
saver.restore(sess, "./calculate") 
output_node_names="save/restore_all"
output_graph_def = tf.compat.v1.graph_util.convert_variables_to_constants(
            sess, # The session
            input_graph_def, # input_graph_def is useful for retrieving the nodes 
	    output_node_names.split(","),
	    variable_names_blacklist="Variable:0"
)
output_graph="./calculate.pb"
with tf.compat.v1.gfile.GFile(output_graph, "wb") as f:
    f.write(output_graph_def.SerializeToString())

sess.close()
