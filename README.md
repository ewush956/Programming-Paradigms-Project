# **Comp 3649 Project**

## *Concept memo by Dru, Evan, and Amtoj*

# Executive Summary

This project presents an approach to solving a variant of the Traveling Salesman Problem (TSP) by adapting principles inspired by the slime mold algorithms food/energy-based system. The primary goal is to enable a resource-constrained agent, the "Tendril Agent," to traverse all nodes, each only once, in a Cartesian space while optimizing energy usage. Unlike traditional TSP, this approach does not require returning to the starting point, and decisions are made based on current energy constraints when making movements rather than solely on the distance to an additional node.

# Overview

The Tendril Agent begins its journey at a designated starting node with an initial energy reserve. Nodes are distributed on a Cartesian plane and characterized by their number, coordinates, and energy gain values. The agent dynamically decides its path, prioritizing feasible moves within its current energy limitations. When the agent successfully reaches a node, the node's energy reserve is added to the agent's energy pool for future moves. Energy gain at a node is only realized upon successful arrival, and subsequent moves are recalculated based solely on the remaining energy.

The goal is to establish a connection to *every* node in the plane starting from a single point. The agent evaluates its available energy against the movement cost to potential nodes at any given state. If the agent has insufficient energy to reach any feasible node, it *backtracks* to previously visited nodes and re-evaluates its options. This decision-making process reflects a modified Breadth-First Search (BFS) approach, inspired by the slime mold's natural searching pattern. While real slime molds do not use recursive backtracking, the algorithm integrates backtracking as a component to handle dead ends or avoid running out of energy.  

Additionally, the initial energy allocated to the Tendril Agent could significantly influence its behavior. Insufficient energy may prevent the agent from completing its traversal, while excessive energy may lead to too many available solutions. By experimenting with variable energy levels, this project introduces an additional layer of complexity, allowing for insights into how initial energy impacts the outcomes of the traversal.

The Agent's behavior can be categorized into three phases:

1. **Exploring**: Checking available nodes for a viable path.  
2. **Moving**: Moving to an accessible location.  
3. **Eating**: The agent “eats” the node and gains the energy at that node.  
   * Note: Nodes will retain their energy for simplicity since they are only visited once in a solution.  
4. **Expending Energy**: Each move reduces the current Tendril Agent energy by the Euclidean distance to the next node.

# Problem Instance and Solution

A problem instance consists of:

1. A set of 𝑁 nodes distributed on a Cartesian plane, where each node is defined by:  
* A unique identifier (node number).  
* Coordinates (𝑥,𝑦) as decimal-point numbers.  
* An energy gain value (positive number).  
2. A starting node where the Tendril Agent begins with a specified initial energy reserve.  
3. A list that contains all unvisited nodes. Backtracking appends nodes back to this list.  
   

The solution to the problem is a traversal path that allows the Tendril Agent to visit all nodes in the plane exactly once while ensuring that it does not run out of energy at any point during the traversal. The agent's remaining energy after visiting all nodes should be maximized.

# Input Format

The input is provided either as a CSV file in the following format (Hard-coded values may also be used as an alternative):

| node\_id | x | y | node\_energy |
| :---: | :---: | :---: | :---: |
| 0 | 0.0 | 0.0 | 10.5 |
| 1 | 5.6 | 3.2 | 8.0 |
| 2 | 2.5 | 1.0 | 5.0 |
| … | … | … | … |

# Valid Solutions and Output

All nodes must have been visited once the final result. The output would ideally be in a visual format, but without a full understanding of Haskell functionality, this may be a pending change. The alternative output could look as follows:

**Output Example 1:**  
	Path: 0 → 2 → 3 → 4 → 1  
Remaining Energy: 15.2

*(Possible Additional Outputs)*  
*Starting Energy: 10.0*  
*Total Energy Gain (Starting Energy vs Remaining Energy): 5.2*

**Output Example 2:**  
	Path: 1 → 3 → 4 → 0 → 2  
Remaining Energy: 4.5

*(Possible Additional Outputs)*  
*Starting Energy: 10.0*  
*Total Energy Gain (Starting Energy vs Remaining Energy): \-5.5*

# Programming Language and Development Environment

* Imperative solution: Python  
* Declarative solution: Haskell  
* Development Environment: VS Code, possibly using Jupyter Notebook (ipynd) files.  
* Project Management Environment: Github   
* Communication: Discord  
* Conflict Resolution: Nerf Guns

# Search Space Exploration

The search space consists of all possible permutations of node traversal paths, subject to energy constraints. To navigate this search space effectively:

**Node Selection**:

* At each step, the agent considers all unvisited nodes reachable with its current energy reserve.  
* A heuristic approach prioritizes nodes based on traversal cost, given by the Euclidean distance, and available energy of the agent.  
  **Backtracking**:  
* If the agent cannot proceed to any feasible node, it backtracks to previously visited nodes and explores alternative paths.  
  **Energy Constraints**:  
* Nodes are excluded from consideration if the agent's remaining energy is insufficient to reach them.

# Testing Approach

We plan on taking an incremental testing approach, preferably using unit tests. For example, testing if individual nodes can make connections that look *reasonably* accurate. This helps to ensure that current builds in the codespace work correctly before moving forward. We also plan to use debugging functions so the visited locations are evident.

# Time, Skill, & Patience Permitting Features

- Potential “cap” on energy storage for the Agent.  
- Some nodes can’t be reached from other nodes.  
- Final Result Visualization.  
- Animated Visualization of active pathfinding.  
- Export data to CSV format.  
- Searching (looking at a possible next node) imposes a small energy cost.  
- Agent choice enhancements using perceived energy gain at a future node before movement. Such as, the distance to one node is 5.0 and the perceived energy gain is 8.3 making a net positive of \+3.3.  
- TBD…

