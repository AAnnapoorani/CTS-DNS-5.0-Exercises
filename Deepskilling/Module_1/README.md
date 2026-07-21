# Module 1: Design Patterns

## Overview
This module covers fundamental design patterns used in software architecture and object-oriented programming. Design patterns are reusable solutions to common problems in software design that can be applied to improve code maintainability, scalability, and reusability.

## Module Structure
```
Module_1/
├── Design Pattern/
│   ├── strategy.py          # Strategy Pattern
│   ├── singleton.py         # Singleton Pattern
│   ├── decorator.py         # Decorator Pattern
│   ├── proxy.py             # Proxy Pattern
│   ├── observer.py          # Observer Pattern
│   ├── mvc.py               # MVC Pattern
│   ├── factory_method.py    # Factory Method Pattern
│   ├── command.py           # Command Pattern
│   ├── builder.py           # Builder Pattern
│   ├── adapter.py           # Adapter Pattern
│   ├── dependency.py        # Dependency Injection Pattern
│   └── (other patterns)
└── Output/                  # Output files directory
```

## Design Patterns Covered

### Creational Patterns
- **Singleton Pattern**: Ensures only one instance of a class exists
- **Factory Method**: Creates objects without specifying exact classes
- **Builder Pattern**: Constructs complex objects step-by-step

### Structural Patterns
- **Adapter Pattern**: Converts interface to compatible one
- **Decorator Pattern**: Adds behavior to objects dynamically
- **Proxy Pattern**: Provides substitute or placeholder for another object

### Behavioral Patterns
- **Strategy Pattern**: Encapsulates interchangeable algorithms
- **Observer Pattern**: Notifies multiple objects about state changes
- **Command Pattern**: Encapsulates requests as objects
- **MVC Pattern**: Separates Model, View, and Controller concerns

### Other Patterns
- **Dependency Injection**: Injects dependencies rather than creating them

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Basic knowledge of Object-Oriented Programming (OOP)

### Installation
```bash
# No external dependencies needed
# Just ensure Python 3.8+ is installed
python --version
```

## Usage

### Running Pattern Examples
Each pattern file is a standalone Python script that demonstrates the pattern:

```bash
# Example: Run Strategy Pattern
python "Design Pattern/strategy.py"

# Example: Run Singleton Pattern
python "Design Pattern/singleton.py"

# Example: Run Factory Method Pattern
python "Design Pattern/factory_method.py"
```

## Learning Objectives
- Understand common design patterns and their use cases
- Learn when and how to apply each pattern
- Improve code organization and maintainability
- Recognize patterns in existing code
- Apply patterns to solve real-world problems

## Key Concepts
- **Reusability**: Use proven solutions repeatedly
- **Maintainability**: Write code that's easier to understand and modify
- **Flexibility**: Design code that adapts to changes easily
- **Scalability**: Build systems that grow gracefully

## Output Files
- Generated output files are saved in the `Output/` directory
- Check this directory for results and demonstrations

## Best Practices
1. Understand the problem before applying a pattern
2. Don't over-engineer - use patterns when they add value
3. Combine patterns to solve complex problems
4. Keep patterns simple and focused
5. Document your use of patterns

## Further Reading
- Design Patterns: Elements of Reusable Object-Oriented Software (Gang of Four)
- Python Design Patterns Documentation
- SOLID Principles in Python

## Notes
- All patterns use Python standard library only
- Code examples demonstrate pattern intent clearly
- Each file can be run independently
- Output files help visualize pattern behavior

## Author
CTS DNS 5.0 Exercises

## License
Educational - Use for learning purposes
