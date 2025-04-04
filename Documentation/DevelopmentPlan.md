Return to the [Main README](../README.md).
# Incremental Development Plan and Goals

# Imperative Solution

## Week Commencing February 2nd, 2025 \- Imperative Solution: Initial Exploration

* **Target:** Conduct initial exploratory programming using Live Share to review Python syntax.  
* **Target:** Define the fundamental classes required for the project: FoodItem (conceptualized as a "Node" class) and Path (to represent a problem instance).

## Week Commencing February 9th, 2025 \- Imperative Solution: Core Solver Implementation

* **Target:** Complete the implementation of the main solver for the program.  
* **Achievement:** The imperative solution was successfully developed and produced valid results, confirmed through manual testing.  
* **Ongoing Tasks:** Code cleanup and documentation were the remaining tasks for this week.  
* **Investigation:** Began exploring potential optimizations for the solution.  
* **February 11th, 2025 \- Improvement:** Discovered and implemented a hyperbolic tangent function to address energy scaling issues, preventing excessively high energy values.

## Week Commencing February 16th, 2025 \- Imperative Solution: Reading Break and Minor Enhancements

* **Activity:** The majority of the reading break was taken off from active development.  
* **Target (Minor):** Occasional meetings were held to discuss and implement small additions, such as a minimum energy finder loop.

## Week Commencing February 23rd, 2025 \- Imperative Solution: Visual Component Development

* **Target:** Develop a visual component for the project to enhance understanding of the solution process.  
* **Achievement:** Created a live-tracking graph of nodes to visualize the optimal solution and the backtracking process.  
* **Benefit:** The graph served as a valuable tool for verifying the correctness of the code's computations. The Python solution was finished at the end of this week. 

## Week Commencing March 2nd, 2025 \- Imperative Solution: Refactoring and Logic Error Detection

* **Activity:** Undertook a refactoring effort to improve potential optimizations.  
* **Target:** To clean up and prepare **check-in** submission.    
* **Issue Identified:** A logic error was introduced during refactoring, which was effectively identified by observing the behavior of the live graph.  
* **Specific Error:** An instance was observed where the backtracking process incorrectly returned to the starting node and selected a different, unintended node.  
* **Fix:** This was quickly fixed by looking at the code of the original version as a copy of it was stored.

# Haskell Solution

## Week Commencing March 16th, 2025 \- Initial Module Creation

* **Target:** Begin development of the Haskell solution following discussions.  
* **Achievement:** Created the basic modules, mirroring the Python solution's structure.  
* **Modules Created:** Path, project\_math, Graph, and Node (analogous to the FoodItem class in Python).  
* **Functionality:** These modules initially contained code similar to "getters" and "setters" found in object-oriented languages.  
* **Graph Module Status:** The detailed implementation of the Graph module was still under consideration, particularly regarding data handling.

## Week Commencing March 23rd, 2025 \- Haskell Solution: Input/Output and Solver Module Initiation

* **Target:** Develop input text files with a format similar to CSV to facilitate testing of the Graph module. Also to start the solver module.  
* **Achievement:** Successfully created these input files, enabling thorough testing of the Graph module with actual data  
  * **Graph Module Finalization:** Finalized the type definition for the Graph module, establishing the approach for handling input and output operations.  
  *  The main solver was implemented.  
* **Work Distribution:** The team divided the work for this week:  
  * Dru focused on the Input/Output (IO) part, leveraging prior practice.  
  * Evan and Amtoj concentrated on developing the solving module.  
* **Methodology:** The solving module's development was based on the format of an example 8-queens problem solver.

### March 23rd week \- Solver Issue Resolution

* **Issue Encountered:** The initial implementation of the solver, closely following the 8-queens example, used an "\[empty Solution\]" return type, which was not correctly returning the actual solution given how our solution is determined.  
* **Resolution:** The team looked into the issue and identified that the base case represented the desired solution. The code was adjusted to correctly add the solution to the list of solutions at the base case.

## Week Commencing March 30th, 2025 \- Haskell Solution: Error Handling Cleanup

* **Target:** Prepare code for submission by preparing any outstanding deliverables and adding any last-minute touches.  
* **Achievement:** All documents were prepared and documentation for modules was completed.

