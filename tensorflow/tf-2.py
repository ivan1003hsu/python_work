import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

m1 = tf.constant([[1,2]])
m2 = tf.constant([[2],
                [2]])

product = tf.matmul(m1,m2)

sess = tf.Session()
#print(sess.run(product))
sess.close()

with tf.Session() as sess:
    result = sess.run(product)
    #print(result)


state = tf.Variable(0,name='counter')
#print(state.name)
step = tf.constant(1)
new_state = tf.add(state, step)
update = tf.assign(state, new_state)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(5):
        result = sess.run(update)
        print(result)
        print(sess.run(state))
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(state))