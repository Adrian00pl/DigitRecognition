import keras
from keras.models import load_model
import cv2
model = load_model("Model.h5")

def predict(InputImg):
    IMG_SIZE = 9
    img_array = cv2.imread(InputImg, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    new_array = new_array.reshape(1, IMG_SIZE, IMG_SIZE, 1)
    prediction = model.predict(new_array)
    switcher = {
        0: "!",
        1: "@",
        2: "#",
        3: "$",
        4: "%",
        5: "^",
        6: "&",
        7: "*",
        8: "(",
        9: ")"
        }
    return switcher.get(prediction.argmax())
        
