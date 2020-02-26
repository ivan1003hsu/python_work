import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import matplotlib.pyplot as plt

def add_layer(input, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size,out_size]) )
    biases = tf.Variable(tf.zeros([1,out_size]) +0.1 )
    Wx_plus_b = tf.matmul(input,Weights) + biases
    if activation_function is None:
        output = Wx_plus_b
    else:
        output = activation_function(Wx_plus_b)
    return output

x_data = np.linspace(-1,1,300, dtype=np.float32)[:,np.newaxis]
noise = np.random.normal(0,0.05,x_data.shape).astype(np.float32)
y_data = np.square(x_data) - 0.5 + noise

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.scatter(x_data, y_data)
plt.ion()
plt.show()
print('ok')

#create tf structure
xs = tf.placeholder(tf.float32, [None,1])
ys = tf.placeholder(tf.float32, [None,1])

l1 = add_layer(xs, 1, 20, activation_function=tf.nn.relu)
l2 = add_layer(l1, 20, 1, activation_function=None)

predict = l2
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-predict), 
                                    reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print('ok2')
    for i in range(1000):
        sess.run(train_step, feed_dict={xs:x_data,ys:y_data})
        print('ok3')
        if i % 100 == 0 :
            try:
                ax.lines.remove(lines[0])
            except Exception:
                pass
            predict_value = sess.run(loss, feed_dict={xs:x_data,ys:y_data})
            lines = plt.plot(x_data,predict_value,'r-',lw=5)
            plt.pause(1)