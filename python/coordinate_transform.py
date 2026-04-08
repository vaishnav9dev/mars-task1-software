# Problem: Convert coordinates from camera frame to world frame
# Approach:
# 1. Apply rotation using angle (theta)
# 2. Apply translation (tx, ty)
# This mimics real robotic coordinate transformation

import math

def transform_coordinates(x, y, theta, tx, ty):
    # Step 1: Rotation
    x_rot = x * math.cos(theta) - y * math.sin(theta)
    y_rot = x * math.sin(theta) + y * math.cos(theta)

    # Step 2: Translation
    world_x = x_rot + tx
    world_y = y_rot + ty

    return world_x, world_y


# 🔹 Example usage
if __name__ == "__main__":
    # Camera coordinates

    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    theta = float(input("Enter rotation angle (degrees): "))
    tx = float(input("Enter translation x: "))
    ty = float(input("Enter translation y: "))

    theta_rad = math.radians(theta)

    wx, wy = transform_coordinates(x, y, theta_rad, tx, ty)

    print("World Coordinates:", wx, wy)


# 🔹 Next Step:
# This logic can be extended to 3D transformations using matrices.
