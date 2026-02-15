def total_salary(path: str) -> tuple[int, float]:
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                stripped_line = line.strip()
                if not stripped_line:
                    continue

                parts_by_comma = stripped_line.split(",")
                if len(parts_by_comma) != 2:
                    raise ValueError(f"Invalid line format: {stripped_line}")

                _, salary = parts_by_comma
                total += int(salary)
                count += 1

        average = total / count if count else 0
        return total, average

    except FileNotFoundError:
        print(f"File not found: {path}")
        return 0, 0
    except (ValueError, OSError) as error:
        print(f"Error processing file: {error}")
        return 0, 0


if __name__ == "__main__":

    path = "data/salary_file.txt"
    total, average = total_salary(path)
    print(
        f"Загальна сума заробітної плати: {total}, "
        f"Середня заробітна плата: {average}"
    )
