# Degree-Planning-System
Assignment for COMP 3649

# Concept Memo: Degree Planner System

## Executive Summary
The Degree Planner System is a Python-based tool that generates optimized course schedules for university students based on degree requirements, user preferences, and course availability. It will process input from CSV files containing course and degree requirement data to produce a term-by-term schedule that ensures all prerequisites, credit requirements, and general education mandates are satisfied. Recursive backtracking will form the core algorithm, enabling efficient exploration of scheduling possibilities while adhering to constraints. 

---

## Problem Instance Example
**Input:**  
- Degree Requirements: 120 total credits, including 30 general education, 60 major-specific, and 30 elective credits.  
- Courses: CS101 (3 credits, no prerequisites, available Fall/Spring), CS201 (3 credits, requires CS101, available Spring), CS301 (3 credits, requires CS201, available Fall).  

**Output:**  
A sample four-semester schedule:  
- **Semester 1 (Fall):** CS101  
- **Semester 2 (Spring):** CS201  
- **Semester 3 (Fall):** CS301  

---

## Input Format
The system will accept two CSV files:
1. **Courses.csv:**  
   | Course Code | Name   | Credits | Prerequisites | Availability  |  
   |-------------|--------|---------|---------------|---------------|  
   | COMP 1701        | Introduction to Programming  | 3       | None          | Fall, Spring  |  
   | COMP 1633       | Introduction to Computer Science II   | 3       | COMP 1701         | Fall, Winter        |  

2. **Requirements.csv:**  
   | Requirement Type   | Credits | Details        |  
   |--------------------|---------|----------------|  
   | General Education  | 30      | List of GenEd  |  
   | Major Courses      | 60      | List of major  |  

Command-line invocation:  
```bash
python degree_planner.py --courses Courses.csv --requirements Requirements.csv --semesters 4
```
## Valid Solutions and Outputs
A valid schedule must meet the following:

- Total credits satisfy the degree requirement.
- Prerequisites are completed before dependent courses.
- All Major requirements are met. 
- Elective and general education courses are appropriately distributed.
- User-defined constraints, such as avoiding summer terms, are respected.

## Programming Languages
- Imperative Language: Python
- Declarative Language: Haskell

## Recursive Backtracking
Our solution will represent courses on a tree or graph like structure, with edges representing 
the relationship between prerequisites. The program will have to backtrack if a courses is selected if the prerequisite is not met.  