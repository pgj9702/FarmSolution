import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# model = keras.Sequential()
# Add an Embedding layer expecting input vocab of size 1000, and
# output embedding dimension of size 64.
# model.add(layers.Embedding(input_dim=1000, output_dim=64))

# Add a LSTM layer with 128 internal units.
# model.add(layers.LSTM(128))

# Add a Dense layer with 10 units.
# model.add(layers.Dense(10))

# model.summary()


def rnn(x, y):
    model = tf.keras.Sequential([tf.keras.layers.SimpleRNN(units=10, return_sequences=False, input_shape=[4, 1]),
                                 tf.keras.layers.Dense(1)])
    model.compile(optimizer='adam', loss='mse')
    history = model.fit(x, y, epochs=100, verbose=0)
    return history
