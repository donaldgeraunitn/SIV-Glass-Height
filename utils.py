import numpy

def get_glass_height_cm(type):
    if(type == 'A'): return 8.30
    elif(type == 'B' or type == 'C'): return 8.80
    else: raise ValueError("This type does not exists")

def center_crop(image, crop_width, crop_height):
    height, width, _ = image.shape

    # Calculate the center of the image
    center_x, center_y = width // 2, height // 2

    # Define the coordinates for the crop (top-left corner of the ROI)
    x1 = center_x - crop_width // 2
    y1 = center_y - crop_height // 2

    # Define the coordinates for the bottom-right corner of the ROI
    x2 = center_x + crop_width // 2
    y2 = center_y + crop_height // 2

    # Crop the image using the calculated coordinates
    return image[y1:y2, x1:x2]