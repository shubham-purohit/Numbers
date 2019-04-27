import tensorflow as tf
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()


plt.imshow(x_train[0], plt.cm.binary)
plt.show()

x_train = tf.keras.utils.normalize(x_train, axis=1, order=1)
x_test = tf.keras.utils.normalize(x_test, axis=1, order=1)

plt.imshow(x_train[0], plt.cm.binary)
plt.show()
