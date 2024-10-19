import math

# Given parameters
initial_lead = 3.0  # Oscar starts 3 seconds ahead
initial_time_diff = 0.4  # Lando is 0.4 seconds slower on the first lap
oscar_degradation = 0.10  # Oscar's lap time degradation per lap
lando_degradation = 0.06  # Lando's lap time degradation per lap

# Compute the coefficients of the quadratic equation
a = -0.02  # Coefficient of N^2
b = 0.42  # Coefficient of N
c = initial_lead  # Adjusted for the initial 3-second lead

# Formulate the quadratic equation: -0.02N^2 + 0.42N + 3 = 0
# Multiply through by -1 to make 'a' positive
a = -a
b = -b
c = -c

# Multiply both sides by 100 to eliminate decimals
a *= 100
b *= 100
c *= 100

# Simplify coefficients
a = int(a)
b = int(b)
c = int(c)

# Quadratic formula components
discriminant = b ** 2 - 4 * a * c

if discriminant >= 0:
    sqrt_discriminant = math.sqrt(discriminant)
    N1 = (-b + sqrt_discriminant) / (2 * a)
    N2 = (-b - sqrt_discriminant) / (2 * a)

    # Select the positive, meaningful root
    N_values = [N for N in [N1, N2] if N > 0]
    if N_values:
        N = N_values[0]
        # Round up to the next whole number of laps
        N = math.ceil(N)
        print(f"It will take Lando {N} laps to catch Oscar.")
    else:
        print("No positive solution for the number of laps.")
else:
    print("No real solutions; discriminant is negative.")
