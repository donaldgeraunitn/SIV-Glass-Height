def get_glass_height_mm(type):
    if(type == 'A'): return 83.0
    elif(type == 'B' or type == 'C'): return 88.0
    else: raise ValueError("This type does not exists")

def center_crop(image, crop_width, crop_height):
    height, width, _ = image.shape

    center_x, center_y = width // 2, height // 2

    x1 = center_x - crop_width // 2
    y1 = center_y - crop_height // 2

    x2 = center_x + crop_width // 2
    y2 = center_y + crop_height // 2

    return image[y1:y2, x1:x2]