## Why Testing Matters

Testing ensures software works correctly and reliably.  
It helps confirm that code behaves as expected, especially when working with other people’s code or adding new features.

**Main idea:** testing builds confidence that the program works when needed.

---

## Automation Instead of Manual Testing

Manual testing quickly becomes repetitive and error-prone.  
The solution is to automate tests using programs designed to check outputs automatically.

Python tools:

- `unittest` — built into Python
- `pytest` — external and lightweight

---

## Unit Testing

Unit testing focuses on small parts of a program, usually individual functions.

The goal is to isolate behaviour:

- test one function at a time
- replace external systems with simple dummy versions (stubs)

This makes errors easier to locate.

---

## Regression & Stress Testing

**Regression testing** means running existing tests whenever new code is added.  
If something fails, the new change introduced the problem.

**Stress testing** checks unusual or extreme inputs:

- empty values
- very large data
- random inputs

Programs should still behave safely.

---

## Test Driven Development (TDD)

TDD reverses the normal workflow:

1. Write tests first
2. Run tests (they fail)
3. Write code until tests pass

Tests act as documentation of what the software should do and support Agile development.

---

## Python `unittest` Structure

``` python
import unittest

class TestExample(unittest.TestCase):

    def test_example(self):
        self.assertEqual(2 + 2, 4)

if __name__ == "__main__":
    unittest.main()
```

Key ideas:

- Test classes inherit from `TestCase`
- Test functions start with `test_`
- Assertions check correctness

---

## Assertions

Assertions verify program behaviour.  
If the condition is false, the test fails.

Common examples:

- `assertEqual(a, b)`
- `assertTrue(x)`
- `assertFalse(x)`
- `assertIsNone(x)`
- `assertIn(a, b)`

---

## Practical Testing Strategies

### Logging

Record program activity using debug messages or log files to understand behaviour during execution.

### Boundary Testing

Check limits carefully:

- start and end values
- loop ranges  
    Prevents common off-by-one errors.

### Defensive Programming

Assume unexpected situations can occur:

- empty inputs
- divide by zero
- null values

Add checks to prevent crashes.

### Pre/Post Conditions

Verify values before a function runs and confirm results afterwards.

---

## Summary

Testing improves software reliability and maintainability.  
Automated unit tests, defensive coding, and regular regression testing help prevent bugs and make development safer.