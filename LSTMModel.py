import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM, BatchNormalization
import numpy as np
from sklearn.metrics import f1_score, accuracy_score


class LSTMModel:
    def __init__(self, x_train):
        self.model = self.buildModel(x_train)

    def buildModel(self, x_train):
        model = Sequential()
        x = len(x_train[0])

        model.add(LSTM(256, input_shape=((1, x)), return_sequences=True, activation="relu"))
        model.add(Dropout(0.2))
        model.add(BatchNormalization())

        model.add(LSTM(128, input_shape=((1, x)), return_sequences=True, activation="relu"))
        model.add(Dropout(0.2))
        model.add(BatchNormalization())

        model.add(LSTM(128, input_shape=((1, x)), activation="relu"))
        model.add(Dropout(0.2))
        model.add(BatchNormalization())

        model.add(Dense(32, activation="relu"))
        model.add(Dropout(0.2))

        model.add(Dense(2, activation="softmax"))
        optimizer = tf.keras.optimizers.Adam(lr=0.001, decay=1e-6)
        model.compile(loss="sparse_categorical_crossentropy", optimizer=optimizer)

        return model

    def train(self, x_train, y_train, batch_size, epochs):
        x_train = x_train.reshape(-1, 1, len(x_train[0]))
        print(">>> Training Model...")
        self.model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs)

    def evaluate(self, x_test, y_test):
        print(">>> Evaluating Model...")
        predictions = self.predict(x_test)

        expected_increase, found_increase, expected_decrease, found_decrease = 0

        for i in range(0, len(predictions)):
            if y_test[i] == 0:
                expected_decrease += 1
                if predictions[i] == y_test[i]:
                    found_decrease += 1
            else:
                expected_increase += 1
                if predictions[i] == y_test[i]:
                    found_increase += 1

        accuracy = accuracy_score(y_test, predictions)
        print(">>>>>> Accuracy: {}".format(accuracy))
        print(">>>>>> Increase Accuracy: {}%".format((found_increase*100)/expected_increase))
        print(">>>>>> Decrease Accuracy: {}%".format((found_decrease*100)/expected_decrease))
        loss = self.model.evaluate(x_test, y_test)
        print(">>>>>> Lost: {}".format(loss))

    def predict(self, sample):
        sample = sample.reshape(-1,1,len(sample[0]))
        prediction = np.array(tf.argmax(self.model.predict(sample), 1))[0]

        return prediction

