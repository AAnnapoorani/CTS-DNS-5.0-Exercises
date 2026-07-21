# Module 2: Data Structures and Algorithms (DSA)

## Overview
This module covers fundamental data structures and algorithms essential for competitive programming, software development, and technical interviews. It focuses on implementing and understanding core DSA concepts using Python.

## Module Structure
```
Module_2/
├── DSA/
│   ├── exercise1.py         # DSA Exercise 1
│   ├── exercise2.py         # DSA Exercise 2
│   ├── exercise3.py         # DSA Exercise 3
│   ├── exercise4.py         # DSA Exercise 4
│   ├── exercise5.py         # DSA Exercise 5
│   ├── exercise6.py         # DSA Exercise 6
│   ├── exercise7.py         # DSA Exercise 7
│   └── (additional exercises)
└── Output/                  # Output files directory
```

## Topics Covered

### Data Structures
- Arrays and Lists
- Linked Lists (Singly, Doubly, Circular)
- Stacks and Queues
- Trees (Binary, BST, AVL)
- Graphs
- Hash Tables and Dictionaries
- Heaps
- Tries

### Algorithms
- Sorting Algorithms (Bubble, Merge, Quick, Heap)
- Searching Algorithms (Linear, Binary, BFS, DFS)
- Dynamic Programming
- Greedy Algorithms
- Backtracking
- Recursion
- Divide and Conquer
- Graph Algorithms (Dijkstra, BFS, DFS)

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Basic understanding of programming concepts
- Familiarity with loops, conditionals, and functions

### Installation
```bash
# No external dependencies needed
# Just ensure Python 3.8+ is installed
python --version
```

## Usage

### Running Exercises
Each exercise file is a standalone Python script:

```bash
# Example: Run DSA Exercise 1
python DSA/exercise1.py

# Example: Run DSA Exercise 2
python DSA/exercise2.py

# Example: Run DSA Exercise 3
python DSA/exercise3.py
```

## Learning Objectives
- Master fundamental data structures
- Understand time and space complexity analysis
- Learn various algorithm design paradigms
- Solve complex problems efficiently
- Prepare for technical interviews
- Develop computational thinking

## Time Complexity Guide
- **O(1)**: Constant time - array access
- **O(log n)**: Logarithmic - binary search
- **O(n)**: Linear - simple loop
- **O(n log n)**: Linearithmic - merge sort, quick sort
- **O(n²)**: Quadratic - nested loops, bubble sort
- **O(2ⁿ)**: Exponential - recursive algorithms
- **O(n!)**: Factorial - permutations

## Key Concepts

### Recursion
- Base case and recursive case
- Call stack
- Time and space complexity analysis
- Tail recursion optimization

### Sorting Algorithms Comparison
| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

### Tree Traversals
- In-order, Pre-order, Post-order (DFS)
- Level-order (BFS)

### Graph Algorithms
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Dijkstra's Algorithm
- Bellman-Ford Algorithm

## Output Files
- Generated output and results are saved in the `Output/` directory
- Check this directory for test results and visualizations

## Problem-Solving Approach
1. **Understand**: Read and understand the problem completely
2. **Analyze**: Identify constraints and edge cases
3. **Plan**: Outline solution approach and complexity
4. **Code**: Implement the solution
5. **Test**: Verify with test cases
6. **Optimize**: Improve if possible

## Practice Tips
- Start with simpler problems and progress to complex ones
- Practice multiple approaches to same problem
- Analyze time and space complexity
- Trace through examples step-by-step
- Solve similar problems to build pattern recognition
- Review and refactor code for clarity

## Common Pitfalls to Avoid
- Not considering edge cases (empty input, single element, etc.)
- Inefficient algorithms for large inputs
- Not managing memory properly
- Off-by-one errors in loops
- Not resetting variables between test cases

## Further Reading
- Introduction to Algorithms (CLRS)
- Cracking the Coding Interview
- LeetCode and HackerRank problems
- GeeksforGeeks DSA tutorials

## Notes
- All code uses Python standard library only
- Each exercise can be run independently
- Focus on understanding concepts, not just memorizing
- Practice is key to mastering DSA

## Author
CTS DNS 5.0 Exercises

## License
Educational - Use for learning purposes
