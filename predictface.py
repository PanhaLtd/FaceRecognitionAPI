import numpy as np
import tensorflow as tf
from tensorflow.keras import models


def predictStudent(img):
    data_dir = "Facedatabase"
    BATCH_SIZE = 32
    IMAGE_SIZE = 224
    default_image_size = tuple((IMAGE_SIZE, IMAGE_SIZE))

    dataset = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        seed=123,
        image_size=default_image_size,
        batch_size=BATCH_SIZE
    )

    class_names = dataset.class_names

    model = tf.keras.models.load_model("app_model_with_normal")
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    print(np.argmax(predictions[0]))

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class
