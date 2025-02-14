import math

def calculate_trig_values(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    sine_value = math.sin(angle_radians)
    cosine_value = math.cos(angle_radians)
    tangent_value = math.tan(angle_radians) 
    return sine_value, cosine_value, tangent_value

angle = float(input("enter the angle in degrees: "))
sine, cosine, tangent = calculate_trig_values(angle)

print(f"sine of {angle} degrees: {sine}")
print(f"cosine of {angle} degrees: {cosine}")
print(f"tangent of {angle} degrees: {tangent}")
