def get_cats_info(path: str) -> list[dict[str, str]]:
    cats_info: list[dict[str, str]] = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                stripped_line = line.strip()
                if not stripped_line:
                    continue

                parts_by_comma = stripped_line.split(",")
                if len(parts_by_comma) != 3:
                    raise ValueError(f"Invalid line format: {stripped_line}")

                cat_id, name, age = parts_by_comma
                cats_info.append({
                    "id": cat_id,
                    "name": name,
                    "age": age,
                })

        return cats_info

    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except (ValueError, OSError) as error:
        print(f"Error processing file: {error}")
        return []


if __name__ == "__main__":
    path = "data/cats_file.txt"
    print(get_cats_info(path))
