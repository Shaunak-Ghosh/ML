import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os

def plot_accuracy_and_loss(history):
  acc = history.history['accuracy']
  val_acc = history.history['val_accuracy']

  loss = history.history['loss']
  val_loss = history.history['val_loss']

  plt.figure(figsize=(8, 8))
  plt.subplot(2, 1, 1)
  plt.plot(acc, label='Training Accuracy')
  plt.plot(val_acc, label='Validation Accuracy')
  plt.legend(loc='lower right')
  plt.ylabel('Accuracy')
  plt.ylim([min(plt.ylim()),1])
  plt.title('Training and Validation Accuracy')

  plt.subplot(2, 1, 2)
  plt.plot(loss, label='Training Loss')
  plt.plot(val_loss, label='Validation Loss')
  plt.legend(loc='upper right')
  plt.ylabel('Cross Entropy Loss')
  plt.ylim([0,1.0])
  plt.title('Training and Validation Loss')
  plt.xlabel('epoch')
  plt.show()

IMAGE_SIZE = 28
training_labels = None

def get_image_from_url(image_url):
  # If the temporary test_image.jpg file already exists,
  # delete it so a new one can be made.
  if os.path.exists('/root/.keras/datasets/test_image.jpg'):
    os.remove('/root/.keras/datasets/test_image.jpg')

  image_path = tf.keras.utils.get_file('test_image.jpg', origin=image_url)
  return image_path

def predict_image(image_url, labels = training_labels):
  image_path = get_image_from_url(image_url)

  image = tf.keras.preprocessing.image.load_img(image_path, target_size=(IMAGE_SIZE, IMAGE_SIZE)).convert('L')

  plt.figure()
  plt.imshow(image, cmap='gray')

  image = tf.keras.preprocessing.image.img_to_array(image)
  image = np.expand_dims(image, axis=0)
  prediction_result = model.predict(image, batch_size=1)
  print('Your model predicts this number is {}'.format(prediction_result.argmax()))


numbers = tf.keras.datasets.mnist

(training_images, training_labels), (validation_images, validation_labels) = numbers.load_data()

plt.imshow(training_images[0], cmap='gray')
print(training_labels[0])

print(training_images[0])

training_images = training_images / 255.0
validation_images = validation_images / 255.0

model = tf.keras.Sequential([
                                    tf.keras.layers.Flatten(input_shape=(28,28)),
                                    tf.keras.layers.Dense(500, activation='relu'),
                                    tf.keras.layers.Dense(300, activation='relu'),
                                    tf.keras.layers.Dense(10, activation= 'softmax')
                                    ])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

model.summary()

history = model.fit(training_images,
                    training_labels,
                    batch_size=100,
                    epochs=10,
                    validation_data = (validation_images, validation_labels)
                    )

plot_accuracy_and_loss(history)
