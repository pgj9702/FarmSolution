import tensorflow as tf
from keras import layers, models

# 784개 입력, 은닉 노드 100, 50
Nin = 784
Nh_l = [100, 50]
number_of_class = 10
Nout = number_of_class

# 분류 DNN 모델 구현 ########################


class DNN(models.Sequential):
    def __init__(self, Nin, Nh_l, Nout):
        super().__init__()
        # 첫 번째 은닉층 : 784 in, 100 out & relu(sigmoid 사용시 역전파시 성능 저하)
        self.add(layers.Dense(Nh_l[0], activation='relu', input_shape=(Nin,), name='Hidden-1'))
        # 두 번쨰 은닉층 : 100 in, 50 out & relu
        self.add(layers.Dense(Nh_l[1], activation='relu', name='Hidden-2'))
        # softmax를 사용하여 출력 값들의 합이 1이 되도록 만들어 준다.
        self.add(layers.Dense(Nout, activation='softmax'))
        # 손실함수 : 교차 엔트로
        self.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])


# 데이터 입력
from keras import datasets
from keras.utils import np_utils

(X_train, y_train), (X_test, y_test) = datasets.mnist.load_data()

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

L, W, H = X_train.shape
X_train = X_train.reshape(-1, W * H)
X_test = X_test.reshape(-1, W * H)

X_train = X_train / 255.0
X_test = X_test / 255.0

# DNN 을 사용하여 학습을 한다.
model = DNN(Nin, Nh_l, Nout)
history = model.fit(X_train, y_train, epochs=15, batch_size=100, validation_split=0.2)
performance_test = model.evaluate(X_test, y_test, batch_size=100)
print('Test Loss and Accuracy ->', performance_test)

