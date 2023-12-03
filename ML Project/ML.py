import cv2
import easyocr
import gradio as gr
import numpy as np
import requests

API_URL = "https://api-inference.huggingface.co/models/dima806/facial_emotions_image_detection"
headers = {"Authorization": "Bearer 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"}

# Instance text detector
reader = easyocr.Reader(['en'], gpu=False)


def query(image):
    image_data = np.array(image, dtype=np.uint8)

    # Convert the image data to binary format (JPEG)
    _, buffer = cv2.imencode('.jpg', image_data)

    # Convert the binary data to bytes
    binary_data = buffer.tobytes()

    response = requests.post(API_URL, headers=headers, data=binary_data)
    return response.json()

def text_extraction(image):

    # Facial Expression Detection
    global text_content
    text_content = ''
    facial_data = query(image)

    text_ = reader.readtext(image)

    threshold = 0.25
    # draw bbox and text
    for t_, t in enumerate(text_):
        bbox, text, score = t

        text_content = text_content + ' ' + ' '.join(text)

        if score > threshold:
            cv2.rectangle(image, tuple(map(int, bbox[0])), tuple(map(int, bbox[2])), (0, 255, 0), 5)

    #output the image
    return image, text_content, facial_data

# Define Gradio interface
iface = gr.Interface(
    fn=text_extraction,
    inputs=gr.Image(),
    outputs=[gr.Image(), gr.Textbox(label="Text Content"), gr.JSON(label="Facial Data")]
)

# Launch the Gradio interface
iface.launch()