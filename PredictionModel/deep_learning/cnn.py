# 필요 라이브러리 추가
import keras
from keras import models, layers
from keras import backend, datasets
import matplotlib.pyplot as plt

# CNN model


# 손실 그래프
def plot_loss(history):
    # 선 그리기
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    # 그래프 제목
    plt.title('Model Loss')
    # x,y축 이름 표시
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    # 각 라인 표식 표시
    plt.legend(['Train','Test'],loc=0)


# 정확도 그래프
def plot_acc(history):
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc=0)


class CNN(models.Sequential):
    # 상속한 부모 초기화
    def __init__(self, input_shape, num_classes):
        super().__init__()

        # 3*3 커널 32개, 활성 함수 relu,
        self.add(layers.Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=input_shape))
        self.add(layers.Conv2D(64, (3, 3), activation='relu'))
        # max_pooling 사용 : 2*2 셀을 묶어 가장 큰 값만 내보냄
        self.add(layers.MaxPooling2D(pool_size=(2, 2)))
        # dropout
        self.add(layers.Dropout(0.25))
        # 2차원을 1차원 벡터로 변형
        self.add(layers.Flatten())
        # fully connected layer(은닉계층, 출력계층으로 구성)
        # 은닉 계층
        self.add(layers.Dense(128, activation='relu'))
        self.add(layers.Dropout(0.5))
        # 출력 계층
        self.add(layers.Dense(num_classes, activation='softmax'))

        self.compile(loss=keras.losses.categorical_crossentropy, optimizer='rmsprop', metrics=['accuracy'])

# mnist 데이트 준비
class DATA():
    def __init__(self):

        num_classes = 10
        (x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()
        img_rows, img_cols = x_train.shape[1:]

        """
        DNN과의 차이
        1. 2차원 이미지를 1차원 벡터로 변환하지 않고 그대로 사용한다.
        2. 흑백 이미지에 대한 정보 처리를 위해서 추가적인 차원을 포함시켜야 한다.
        """
        # 이미지 배열의 앞 단에 추가해야하는 경우(channel_first) 반대(channel_last)
        if backend.image_data_format() == 'channels_first':
            # 이미지의 샘플수, 채널 수, 이미지의 가로 길이, 이미지의 세로 길이
            x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
            x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
            input_shape = (1, img_rows, img_cols)
        #
        else:
            x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
            x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
            input_shape = (img_rows, img_cols, 1)

        x_train = x_train.astype('float32')
        x_test = x_test.astype('float32')
        x_train /= 255
        x_test /= 255

        y_train = keras.utils.to_categorical(y_train, num_classes)
        y_test = keras.utils.to_categorical(y_test, num_classes)

        self.input_shape = input_shape
        self.num_classes = num_classes
        self.x_train, self.y_train = x_train, y_train
        self.x_test, self.y_test = x_test, y_test

# 그래프 그리는 함수 불러오기


def main():
    batch_size = 128
    epochs = 3

    data = DATA()
    model = CNN(data.input_shape, data.num_classes)

    history = model.fit(data.x_train, data.y_train, batch_size=batch_size, epochs=epochs, validation_split=0.2)

    score = model.evaluate(data.x_test, data.y_test)
    print()
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

    plot_acc(history)
    plt.show()
    plot_loss(history)
    plt.show()


if __name__ == '__main__':
    main()
