# Test Plan Documentation
## Pytest Test Driver
We utilize a simple test driver that calls `pytest` for each test file using these modules:

- **test_food_item.py:** Validates food item functionality.
- **test_path.py:** Ensures correct path computation and validation.
- **test_graph.py:** Tests graph-related operations.

# Test Cases

### 1.csv

- Energy needed for a successful path is at least 36.
- Should be able to connect to at least 0 -> 4 -> 1 or 0 -> 1 -> 4 with 35 energy.

This test runs through a regular seeded plot, where the calculated min energy needed to find a solution is at least 36.

```bash
python .\main.py --input_file "test_cases/1.csv"
```

```csv
Node Number,X,Y,Z,Energy
0,7.0,7.0,8.0,0
1,7.0,4.0,4.0,3
2,1.0,3.0,10.0,7
3,3.0,6.0,9.0,8
4,7.0,0.0,5.0,3
```

### 2.csv

This test asserts how the gradient system works. The cost to move is just above 12 based on the Euclidean distance calculation. With our gradient scalar, it is amplified for uphill movement. This results in a greater energy requirement of at least 22 energy to start.

```bash
python .\main.py --input_file "test_cases/2.csv"
```

```csv
Node Number,X,Y,Z,Energy
0,0,0,0,0
1,5,5,10,0
```

### 3.csv

This is the inverse of test_cases_2, showing how little energy is needed to descend a gradient.

```bash
python .\main.py --input_file "test_cases/3.csv"
```

```csv
Node Number,X,Y,Z,Energy
0,5,5,10,0
1,0,0,0,0
```

### 4.csv
This test involves showcasing same plane, no gradient, calculation. The Euclidean distance of the same plane is equal to the energy cost (cost == 7.071). The min energy required to traverse is 8.

```bash
python .\main.py --input_file "test_cases/4.csv"
```

```csv
Node Number,X,Y,Z,Energy
0,5,5,5,0
1,0,0,5,0
```

### 5.csv

This method involves too much energy gain at each node, and a high starting energy, resulting in effectively a worse case scenario brute force method.

```bash
python .\main.py --input_file "test_cases/5.csv"
```

```csv
Node Number,X,Y,Z,Energy
0,0,2,1,0
1,8,7,0,5
2,3,10,0,5
3,1,3,2,1
4,9,3,3,1
5,10,5,2,1
```

### 6.csv

```bash
python .\main.py --input_file "test_cases/6.csv"
```

```csv
Node Number,X,Y,Z,Energy
0,2,3,2,0
1,1,3,1,1
2,1,1,0,3
3,2,1,0,1
4,3,2,1,2
5,0,3,1,2
6,3,3,1,2
7,3,1,2,1
8,3,1,2,1
9,3,3,2,1
10,2,3,3,3
11,3,2,2,2
12,1,1,2,3
```

### 7.csv

```bash
python .\main.py --input_file "test_cases/7.csv"
```

```csv
Node Number,X,Y,Z,Energy
0, 0,0,0,20
1, 3,3,3,2
2, 6,7,8,5
3, 8,9,10,5
4, 10,11,12,4
5, 13,14,15,6
6, 15,15,15,0
7, 3,3,3,2
8, 6,7,8,5
```

### noSolution.csv

Test case should find no solutions.

```bash
python .\main.py --input_file "test_cases/noSolution.csv"
```

```csv
Node Number,X,Y,Z,Energy
0, 0, 0, 0, 10
1, 10, 0, 0, 10
2, 10, 10, 0, 20
3, 10, 10, 10, 10
4, 0, 10, 10, 5
5, 0, 0, 10, 10
```

### multiSolutions.csv

Test case should find several solutions.

```bash
python .\main.py --input_file "test_cases/multiSolutions.csv"
```

```csv
Node Number,X,Y,Z,Energy
0,0,0,0,5
1,1,0,0,2
2,0,1,0,2
3,1,1,0,2
4,2,0,0,2
```

### oneSolution.csv

Test case should find a single solution.

```bash
python .\main.py --input_file "test_cases/oneSolutions.csv"
```

```csv
Node Number,X,Y,Z,Energy
0, 0, 0, 0, 12
1, 10, 0, 0, 10
2, 10, 10, 0, 20
3, 10, 10, 10, 10
4, 0, 10, 10, 5
5, 0, 0, 10, 10
```
