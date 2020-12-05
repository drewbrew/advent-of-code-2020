from typing import Tuple, List

TEST_INPUTS = {
    "FBFBBFFRLR": (44, 5, 357),
    "BFFFBBFRRR": (70, 7, 567),
    "FFFBBBFRRR": (14, 7, 119),
    "BBFFBBFRLL": (102, 4, 820),
}

with open("day05.txt") as infile:
    REAL_INPUT = [line.strip() for line in infile]


def boarding_pass_to_seat(boarding_pass: str) -> Tuple[int, int]:
    binary_row = "".join(str(int(char == "B")) for char in boarding_pass[:7])
    binary_col = "".join(str(int(char == "R")) for char in boarding_pass[7:])
    row = int(binary_row, 2)
    col = int(binary_col, 2)
    return row, col


def seat_to_seat_id(seat: Tuple[int, int]) -> int:
    return seat[0] * 8 + seat[1]


def part_one(puzzle_input: List[str]) -> int:
    return max(seat_to_seat_id(boarding_pass_to_seat(line)) for line in puzzle_input)


def part_two(puzzle_input: List[str]) -> int:
    seat_ids = sorted(
        seat_to_seat_id(boarding_pass_to_seat(line)) for line in puzzle_input
    )
    for last_seat, current_seat in zip(
        seat_ids[:-1],
        seat_ids[1:],
    ):
        if current_seat != last_seat + 1:
            return last_seat + 1


for boarding_pass, (row, col, seat_id) in TEST_INPUTS.items():
    assert boarding_pass_to_seat(boarding_pass) == (row, col), boarding_pass
    assert seat_to_seat_id((row, col)) == seat_id, boarding_pass

print(part_one(REAL_INPUT))
print(part_two(REAL_INPUT))
