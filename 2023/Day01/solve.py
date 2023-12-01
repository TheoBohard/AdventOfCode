def solve(path: str):
    with open(path) as file:
        text = file.read()

    calibration_value = 0

    for data in text.split("\n"):
        data = (
            data.replace("one", "one1one")
            .replace("two", "two2two")
            .replace("three", "three3three")
            .replace("four", "four4four")
            .replace("five", "five5five")
            .replace("six", "six6six")
            .replace("seven", "seven7seven")
            .replace("eight", "eight8eight")
            .replace("nine", "nine9nine")
        )

        calibration_low, calibration_high = None, None

        for char in data:
            if char.isnumeric():
                if not calibration_low:
                    calibration_low = char
                else:
                    calibration_high = char

        calibration_low = 0 if not calibration_low else calibration_low
        calibration_high = calibration_low if not calibration_high else calibration_high
        calibration_value += int(f"{calibration_low+calibration_high}")

    return calibration_value


if __name__ == "__main__":
    print(solve("input/input.txt"))
