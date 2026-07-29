# Week 2 Python Exercises

This repository contains solutions for the Week 2 Python programming exercises. Each script demonstrates a different Python concept, including variables, data types, conditional statements, loops, functions, and basic program structure.

## Files (A total of 5 files)

### File 1 `profile.py`
Demonstrates the use of variables and data types.

**Features:**
* Stores a name, age, and favorite number.
* Prints a sentence using an f-string.
* Displays the data type of each variable.
* Calculates and prints the age in 10 years without changing the original age variable.

**Run:**

```bash
python3 profile.py
```

or

```bash
python profile.py
```

-

### `fizzbuzz.py`

Implements the classic FizzBuzz exercise using loops and conditional statements.

**Features:**

* Loops through the numbers 1 to 50.
* Prints:

  * `Fizz` for numbers divisible by 3.
  * `Buzz` for numbers divisible by 5.
  * `FizzBuzz` for numbers divisible by both 3 and 5.
  * The number itself otherwise.

**Run:**

```bash
python3 fizzbuzz.py
```

or

```bash
python fizzbuzz.py
```

---

### `calculator.py`

A simple calculator built with functions.

**Features:**

* `add(a, b),`
* `subtract(a, b)`
* `multiply(a, b)`
* `divide(a, b)`
* Prevents division by zero by returning `"Cannot divide by zero"`.

**Run:**

```bash
python3 calculator.py
```

or

```bash
python calculator.py
```

---

### `guessing_game.py`

A simple number guessing program that compares guesses against a secret number.

**Features:**

* Stores a secret number.
* Stores three guesses.
* Uses a `check_guess(secret, guess)` function to determine whether each guess is:

  * `Too high`
  * `Too low`
  * `Correct!`
* Reuses the function instead of repeating comparison logic.

**Run:**

```bash
python3 guessing_game.py
```

or

```bash
python guessing_game.py
```

## Requirements

* Python 3.x

## Author

Created as part of the *Evolve School of Computation – Full-Stack AI Software Engineering: Zero to Hero* Week 2 exercises.
