import math

def calculate_trig_values(degrees):
    """
    Calculates sin, cos, and tan for a given angle in degrees.
    """
    # Convert degrees to radians
    radians = math.radians(degrees)

    # Calculate the values
    sine_value = math.sin(radians)
    cosine_value = math.cos(radians)
    tangent_value = math.tan(radians)

    # Print the results
    print(f"For an angle of {degrees} degrees ({radians:.4f} radians):")
    print(f"  sin({degrees}) = {sine_value:.4f}")
    print(f"  cos({degrees}) = {cosine_value:.4f}")
    print(f"  tan({degrees}) = {tangent_value:.4f}")
    
    # Note: Tangent approaches infinity at 90, 270 degrees, etc.
    # Python might return a very large number or handle it gracefully.

# --- Example Usage ---

# Example 1: A common angle (45 degrees)
calculate_trig_values(45)

print("-" * 20)

# Example 2: Another common angle (90 degrees)
# Note how tan will be a very large number or "infinity"
calculate_trig_values(90)

print("-" * 20)

# Example 3: Using Pi (180 degrees)
calculate_trig_values(180)