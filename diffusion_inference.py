def sw_en(text):
    from googletrans import Translator
    translator = Translator()
    text = translator.translate(text=text, src='sw', dest='en').text
    return text


def generate_image(text):
    import requests
    import io
    from PIL import Image

    api = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(api, headers=headers, json=payload)
        return response.content

    image_bytes = query(text)

    # You can access the image with PIL.Image for example
    image = Image.open(io.BytesIO(image_bytes))

    image.save("static/image.jpg", quality=98)


# generate_image("Image of lion")
