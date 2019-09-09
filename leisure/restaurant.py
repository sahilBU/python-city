

def draw_restaurant(star, location):
    if star <= 0 or star > 7:
        raise ValueError("Enter valid star rating for the restaurant")
    print("Located at", location)
    printRestaurantStar(star)
    return

"""
function to draw a restaurant based on star rating
The restaurants can range from 1 star to 7 star, and the size of the restaurant depends on the star rating
"""
def printRestaurantStar(n):

    # Printing the upper triangle
    for i in range(n):
        for j in range(i + 1, n):
            print(' ', end='')

        for j in range(0, 2 * i + 1):
            print('*', end='')
        print()

    # Printing the lower rectangles
    for i in range(3):
        for j in range(3):
            print('*', end='')

        for j in range(2 * n - 7):
            print(' ', end='')

        for j in range(3):
            print('*', end='')
        print()