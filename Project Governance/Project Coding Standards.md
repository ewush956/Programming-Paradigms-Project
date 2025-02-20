# Python Coding Standards

# 1\. General Guidelines

* Adhere to [Section 3](#3.-naming-conventions) for consistent and standardized Python code styling.  
* Prioritize clarity, readability, and maintainability in code structure and logic.  
* Employ descriptive and meaningful names for variables, functions, and classes.  
* Structure functions and methods to remain concise and single-purpose.  
* Utilize docstring documentation for clarity.

# 

# 2\. Code Formatting

* Use **1 tab space per indentation level.**  
* Keep lines **within 79 characters** for improved readability (72 for docstrings/comments).  
* Utilize blank lines to enhance logical separation within the code.  
* Avoid trailing whitespace to maintain clean version control.  
* Organize imports as follows, with standard, third-party, and local module imports separated:

```py
import os
import sys

import numpy as np
import pandas as pd

from mymodule import myfunction
```

* Ensure a single space around operators and after commas for readability.  
* Use double quotes (`""`) for strings, reserving single quotes (`'`) for cases where necessary.

# 3\. Naming Conventions {#3.-naming-conventions}

| Component | Naming Convention | Example |
| ----- | ----- | ----- |
| Variables | lowercase\_with\_underscores | `user_name = "Alice"` |
| Constants | UPPERCASE\_WITH\_UNDERSCORES | `MAX_RETRIES = 5` |
| Functions | lowercase\_with\_underscores | `def calculate_total():` |
| Classes | CamelCase | `class DataProcessor:` |
| Private Variables | \_single\_leading\_underscore | `_temp_value = 42` |
| Module Names | lowercase snakecase | `my_module.py` |

# 4\. Functions and Methods

* Utilize type hints to improve code clarity and maintainability:

```py
def add_numbers(a: int, b: int) -> int:
    return a + b
```

* Keep functions focused and modular to support reusability and testability.

# 5\. Docstrings and Comments

* Employ triple double-quoted (`"""`) docstrings for modules, classes, and functions:

```py
def square(num: int) -> int:
    """Returns the square of a number."""
    return num * num
```

* Use inline comments judiciously and only to clarify complex logic.  
* Ensure docstrings comprehensively describe purpose, parameters, and return values.

# 6\. Testing

* Develop unit tests with `unittest` or `pytest` frameworks.  
* Ensure sufficient test coverage across all modules.

```py
def test_square():
    assert square(3) == 9
```

# 7\. Version Control

* Utilize Git/Github for version control to track code changes effectively.  
* Create meaningful commit messages to aid in clarity of each commit.  
* If committing multiple files, commit each with a unique commit message according to the respective changes made in that file.

# 8\. Code Reviews

* Conduct thorough code reviews to enforce best practices and maintain high-quality code.  
* Assess code for readability, maintainability, and adherence to standards.  
* Verify compliance with coding guidelines before merging changes.

