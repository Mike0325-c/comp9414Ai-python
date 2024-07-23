# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 13:51:04 2023

@author: Maryam Hashemi
"""
############################### 5.1 Exercise #####################################

############################ 5.1.2 ####################################


# import tensorflow_datasets as tfds
from tensorflow.keras.utils import to_categorical
import tensorflow as tf
import datetime
import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import EarlyStopping
# import cv2



## Loading MNIST dataset
(train_ds, train_labels), (test_ds, test_labels) = tf.keras.datasets.mnist.load_data()


## MNIST dataset images are 28*28, and they are between 0-255. 
#Preprocessing part 1 
train_ds = train_ds / 255.0
test_ds = test_ds / 255.0

## Transforming labels
train_labels = to_categorical(train_labels, num_classes=10)
test_labels = to_categorical(test_labels, num_classes=10)



############################ 5.1.3 ####################################

from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input

## Loading VGG16 model
base_model = VGG16(weights="imagenet", include_top=False, input_shape=(32, 32, 3))
base_model.trainable = False ## Not trainable weights


## Preprocessing part 2
train_ds = tf.image.grayscale_to_rgb(tf.expand_dims(train_ds, -1))
train_ds = tf.image.resize(train_ds, (32, 32))
train_ds = preprocess_input(train_ds)

test_ds = tf.image.grayscale_to_rgb(tf.expand_dims(test_ds, -1))
test_ds = tf.image.resize(test_ds, (32, 32))
test_ds = preprocess_input(test_ds)



############################ 5.1.4 ####################################

base_model.summary()



############################ 5.1.5 ####################################

from tensorflow.keras import layers, models

flatten_layer = layers.Flatten()
dense_layer_1 = layers.Dense(50, activation='relu')
dense_layer_2 = layers.Dense(20, activation='relu')
prediction_layer = layers.Dense(10, activation='softmax')

model = models.Sequential([
    base_model,
    flatten_layer,
    dense_layer_1,
    dense_layer_2,
    prediction_layer
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'],
)

es = EarlyStopping(monitor='val_accuracy', mode='max', patience=5, restore_best_weights=True)

start = datetime.datetime.now()

history = model.fit(train_ds, train_labels, epochs=5, validation_split=0.2, batch_size=32, callbacks=[es])

score = model.evaluate(test_ds, test_labels, batch_size=32)
x_valid_output_images = model.predict(test_ds)

# Get training and test loss histories
training_loss = history.history['loss']
test_loss = history.history['val_loss']

# Create count of the number of epochs
epoch_count = range(1, len(training_loss) + 1)


############################ 5.1.6 ####################################

# Visualize loss history
plt.plot(epoch_count, history.history['loss'], 'r--')
plt.plot(epoch_count, history.history['val_loss'], 'b-')
plt.legend(['Training Loss', 'Test Loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()

plt.figure()
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

end = datetime.datetime.now()
elapsed = end - start
print('Training time:', str(elapsed))
print('Test score:', score[0])
print('Test accuracy:', score[1])


############################ 5.1.7 ####################################


## Loading MNIST dataset
(train_ds, train_labels), (test_ds, test_labels) = tf.keras.datasets.mnist.load_data()

## Displaying an image
image_index = 10
plt.imshow(train_ds[image_index], cmap='gray')
plt.axis('off')
plt.show()

## Rescaling images
train_ds = train_ds / 255.0
test_ds = test_ds / 255.0

## Remaining code for model training and evaluation
# (Please copy the code provided in the previous response here)

# Use the image for prediction
input_image = tf.image.grayscale_to_rgb(tf.expand_dims(train_ds[image_index], -1))
input_image = tf.image.resize(input_image, (32, 32))
input_image= preprocess_input(input_image)
input_image = tf.expand_dims(input_image, axis=0)


## Transforming labels to correct format
train_labels = to_categorical(train_labels, num_classes=10)
test_labels = to_categorical(test_labels, num_classes=10)

predicted_label = model.predict(input_image)
predicted_class = tf.argmax(predicted_label, axis=1).numpy()[0]

actual_class = train_labels[image_index]

print("Actual class:", actual_class)
print("Predicted class:", predicted_class)