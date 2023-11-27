import math

# Function to calculate the solutions of a quadratic equation
def calculate_quadratic_solutions(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check the nature of the discriminant
    if discriminant > 0:
        # Two real and distinct solutions
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # Two real and identical solutions (both roots are the same)
        root = -b / (2*a)
        return root,
    else:
        # No real solutions (complex roots)
        return None

# Input coefficients from the user
while True:
    try:
        a = float(input("Enter the coefficient 'a': "))
        b = float(input("Enter the coefficient 'b': "))
        c = float(input("Enter the coefficient 'c': "))
        break
    except ValueError:
        print("Invalid input. Please enter numerical coefficients.")

# Calculate solutions and display results
solutions = calculate_quadratic_solutions(a, b, c)

if solutions is not None:
    print("Solutions:")
    for solution in solutions:
        print(f"{solution:.2f}")
else:
    print("No real solutions (complex roots).")
