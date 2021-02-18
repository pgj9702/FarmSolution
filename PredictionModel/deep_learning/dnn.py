import tensorflow as tf

hello = tf.constant("Hello T")
sess = tf.Session()
print(sess.run(hello))
hello.