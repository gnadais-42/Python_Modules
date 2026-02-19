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


def calculate_distance(coordinates: tuple) -> float:
    x, y, z = coordinates
    return round(math.sqrt(x ** 2 + y ** 2 + z ** 2), 1)


def position_tracker(coordinates: str):
    try:
        parsed: tuple = parse_coordinates(coordinates)
        print("Distance between (0, 0, 0) and "
              f"{parsed}: {calculate_distance(parsed)}\n")
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, "
              f"Args: {e.args}\n")


def tuple_unpacking(tup: tuple) -> None:
    x, y, z = tup
    print(f"Player at x={x}, y={y}, z={z}\n"
          f"Coordinates: X={x}, Y={y}, Z={z}")


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
