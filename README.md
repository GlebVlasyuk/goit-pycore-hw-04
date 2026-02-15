# goit-pycore-hw-04

## Tasks Overview

- `task1.py` - function `total_salary(path)` reads salary data from a text file and returns total and average salary.
- `task2.py` - function `get_cats_info(path)` reads cats data from a text file and returns a list of dictionaries with `id`, `name`, `age`.
- `hw03.py` - CLI script that prints a directory tree with colored output (`colorama`): directories and files are shown in different colors.
- `task4.py` - assistant bot CLI that supports contact commands: `hello`, `add`, `change`, `phone`, `all`, `close`, `exit`.

## Notes

- Data files for examples are stored in `data/`.
- Python cache and virtual environment are ignored via `.gitignore`.
- `requirements.txt` contains project dependency for task 3.

## How To Run

### Task 1

```bash
python task1.py
```

### Task 2

```bash
python task2.py
```

### Task 3

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python hw03.py /absolute/path/to/directory
```

### Task 4

```bash
python task4.py
```
