import tensorflow as tf

# LSTM model


def lstm(x, y):
    model = tf.keras.Sequential([tf.keras.layers.LSTM(units=30, return_sequences=True, input_shape=[100, 2]),
                                 tf.keras.layers.LSTM(units=30), tf.keras.layers.Dense(1)])
    model.compile(optimizer='adam', loss='mse')
    history = model.fit(x, y, epochs=100, verbose=0)
    return history
