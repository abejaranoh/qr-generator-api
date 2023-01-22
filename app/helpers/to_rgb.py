# convert hex to rgb
def to_rgb(color):
    #remove #
    if color[0] == "#":
        new_color = color[1:]
        # rgb generate
        rgb = tuple(int(new_color[i:i+2], 16) for i in (0,2,4))
    else:
        # rgb generate
        rgb = tuple(int(color[i:i+2], 16) for i in (0,2,4))
    # float to int 
    return rgb