import numpy as np
import tensorflow as tf

def predictStudent(img, student_ids):
    model = tf.keras.models.load_model("data/models/app_model_with_normal")
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    IMAGE_SIZE = 224

    predictions = model.predict(img_array)
    print(np.argmax(predictions[0]))

    predicted_class = student_ids[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class
