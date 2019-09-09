from .museum import draw_museum
from .restaurant import draw_restaurant

def draw_leisure():
    draw_museum()
    draw_restaurant(5, "Allston")
    draw_restaurant(7, "Brighton")
    return