import math


def calculate_distance(p1, p2):
    """
    Calculates the Euclidean distance between two 3D points.

    Args:
        p1 (tuple): The first 3D coordinate (x, y, z).
        p2 (tuple): The second 3D coordinate (x, y, z).

    Returns:
        float: The calculated distance between the points.
    """
    x_diff = (p2[0] - p1[0]) ** 2
    y_diff = (p2[1] - p1[1]) ** 2
    z_diff = (p2[2] - p1[2]) ** 2
    return math.sqrt(x_diff + y_diff + z_diff)


def parse_coordinates(coord_string):
    """
    Parses a string of coordinates into a tuple of integers.

    Args:
        coord_string (str): A string formatted as "x,y,z".

    Returns:
        tuple: A tuple containing three integers (x, y, z).

    Raises:
        ValueError: If the string cannot be converted to integers.
    """
    parts = coord_string.split(',')
    return (int(parts[0]), int(parts[1]), int(parts[2]))


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    p1 = (0, 0, 0)
    p2 = (10, 20, 5)
    print(f"\nPosition created: {p2}")

    distance = calculate_distance(p1, p2)
    print(f"Distance between {p1} and {p2}: {distance:.2f}")

    input_str = "3,4,0"
    print(f"\nParsing coordinates: \"{input_str}\"")

    parsed_p = parse_coordinates(input_str)
    print(f"Parsed position: {parsed_p}")

    dist2 = calculate_distance(p1, parsed_p)
    print(f"Distance between {p1} and {parsed_p}: {dist2:.1f}")

    wrong_input = "abc, def,ghi"
    print(f"\nParsing invalid coordinates: \"{wrong_input}\"")

    try:
        parse_coordinates(wrong_input)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print("Error details - Type: ValueError, Args:", end=" ")
        print(f"\"invalid literal for int() with base 10:'{wrong_input}'\",)")

    print("\nUnpacking demonstartion:")
    x, y, z = parsed_p
    X, Y, Z = parsed_p
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={X}, Y={Y}, Z={Z}")
