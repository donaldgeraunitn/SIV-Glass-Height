def get_glass_height_cm(type):
    if(type == 'A'): return 8.30
    elif(type == 'B' or type == 'C'): return 8.80
    else: raise ValueError("This type does not exists")