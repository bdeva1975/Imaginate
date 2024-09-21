import os
from openai import OpenAI
import base64
from io import BytesIO

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_image_response(prompt_content):
    try:
        # Call the OpenAI API to generate an image
        response = client.images.generate(
            model="dall-e-3",  # Using DALL-E 3 model
            prompt=prompt_content,
            size="1024x1024",  # You can adjust the size as needed
            quality="standard",
            n=1,
        )

        # Get the image URL from the response
        image_url = response.data[0].url

        # Download the image
        import requests
        image_data = requests.get(image_url).content

        # Return the image as a BytesIO object
        return BytesIO(image_data)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Example usage
prompt = "A whimsical treehouse nestled in a vibrant forest"
image_bytes = get_image_response(prompt)

if image_bytes:
    # You can save the image or process it further here
    with open("generated_image.png", "wb") as f:
        f.write(image_bytes.getvalue())
    print("Image generated and saved as 'generated_image.png'")
else:
    print("Failed to generate image")