import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, size / 3)  # Adjusted starting position
    t.pendown()

    # Draw three sides of the snowflake
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)  # Turn 120 degrees to form a triangle

    window.mainloop()

def main():
    while True:
        try:
            order = int(input("Enter the order of the Koch snowflake: "))
            if order >= 0:
                break
            print("Please enter a non-negative integer.")
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        try:
            size = int(input("Enter the size of the Koch snowflake: "))
            if size > 0:
                break
            print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")
    
    draw_koch_snowflake(order, size)

if __name__ == "__main__":
    main()
