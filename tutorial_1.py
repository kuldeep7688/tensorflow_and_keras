# tutorial 1 for tensorflow

import tensorflow as tf

if __name__ == "__main__":
    node1 = tf.constant(3.0, dtype=tf.float32)
    node2 = tf.constant(4.0)

    print node1, node2
    print "\n\n"

    sess = tf.Session()
    print sess.run([node1, node2])
    sess.close()
