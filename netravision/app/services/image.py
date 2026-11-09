from PIL import Image
import io
import os

ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png"]
MAX_IMAGE_DIMENSION = 2048


def validate_image(content:bytes , content_type:str) -> dict:

    if not content_type.startswith("image/"):
        return {"is_valid":False , "message":"The file is not valid"}
    if content_type not in ALLOWED_IMAGE_TYPES:
        return {"is_valid":False , "message": "The file is not valid"}

    

    size_in_mb = len(content) / (1024 * 1024)

    if size_in_mb > 15:
        return { "is_valid": False , "message" : "Image size exceeds 15MB limit"}

    image = Image.open(io.BytesIO(content))
    width ,height = image.size

    return{
        "is_valid":True,
        "message":"Image is valid",
        "width":width,
        "height":height,
        "size_mb":size_in_mb
    }


def resize_if_needed(content:bytes) -> bytes:
    """Resize yhr image if exceeds 15mb"""

    image = Image.open(io.BytesIO(content))

    width , height = image.size

    if  width <= MAX_IMAGE_DIMENSION and height <= MAX_IMAGE_DIMENSION:
        return content

    if width > height:
        new_width = MAX_IMAGE_DIMENSION
        new_height = int((MAX_IMAGE_DIMENSION / width) * height)

    else:
        new_height = MAX_IMAGE_DIMENSION
        new_width = int((MAX_IMAGE_DIMENSION / height) * width)

    resized_image = image.resize((new_width , new_height) , Image.Resampling.LANCZOS)
    output = io.BytesIO()
    resized_image.save(output , format=image.format)
    return output.getvalue()

def save_image(content:bytes , upload_path:str , filename :str) -> str:
    os.makedirs(upload_path , exist_ok=True)
    file_path=os.path.join(upload_path , filename)

    with open(file_path , "wb") as f:
        f.write(content)
    return file_path