import math


class ParseError(Exception):
    pass


def parse_coordinates(coordinates: str) -> tuple:
    parsed: list = coordinates.split(",")
    if len(parsed) != 3:
        raise ParseError("Please give three coordinates "
                         "separated by commas")
    final: list = []
    for coordinate in parsed:
        final.append(int(coordinate))
    return tuple(final)


def calculate_distance(position1: tuple, position2: tuple) -> float:
    try:
        x1, y1, z1 = position1
        x2, y2, z2 = position2
    except ValueError as e:
        print("Error:", e)
        return 0.0
    return round(math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2 + (z2-z1) ** 2), 1)


def position_tracker(coordinates: str):
    try:
        parsed: tuple = parse_coordinates(coordinates)
        print("Distance between (0, 0, 0) and "
              f"{parsed}: {calculate_distance(parsed, (0,0,0))}\n")
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, "
              f"Args: {e.args}\n")


def tuple_unpacking(tup: tuple) -> None:
    try:
        x, y, z = tup
        print(f"Player at x={x}, y={y}, z={z}\n"
              f"Coordinates: X={x}, Y={y}, Z={z}")
    except ValueError as e:
        print("Error:", e)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Position created: (10, 20, 5)")
    position_tracker("10,20,5")
    print("Parsing coordinates \"3, 4, 0\"")
    position_tracker("3,4,0")
    print("Parsing invalid coordinates: \"abc,def,ghi\"")
    position_tracker("abc,def,ghi")
    print("Unpacking demonstration")
    tuple_unpacking((3, 4, 0))


if __name__ == "__main__":
    main()
