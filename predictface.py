import numpy as np
import tensorflow as tf

def predictStudent(img):
    model = tf.keras.models.load_model("data/models/app_model_with_normal")
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    data_dir = "data/Facedatabase"
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

    predictions = model.predict(img_array)
    print(np.argmax(predictions[0]))

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class
