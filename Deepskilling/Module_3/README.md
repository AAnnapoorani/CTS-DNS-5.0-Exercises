# Module 3: SQLAlchemy and Database Operations

## Overview
This module covers SQLAlchemy, a powerful Python Object-Relational Mapping (ORM) library. It demonstrates how to design database schemas, perform CRUD operations, manage relationships, and handle database migrations.

## Module Structure
```
Module_3/
├── hands_on_1/              # Database basics
├── hands_on_2/              # SQLAlchemy setup
├── hands_on_3/              # CRUD operations
├── hands_on_4/              # Advanced queries
├── hands_on_5/              # Relationships
├── hands_on_6/              # Database design
│   ├── models.py            # SQLAlchemy models
│   └── crud.py              # CRUD operations
├── hands_on_7/              # Migrations with Alembic
│   ├── models.py            # Database models
│   ├── migrations/          # Database migration files
│   │   ├── env.py
│   │   └── versions/        # Migration versions
│   └── alembic.ini          # Alembic configuration
└── Output/                  # Output files directory
```

## Topics Covered

### Database Fundamentals
- Relational databases (SQL basics)
- Tables, columns, rows, keys
- Primary keys and foreign keys
- Data types and constraints
- SQL CRUD operations

### SQLAlchemy Core
- Engine and connections
- Table definitions
- SQL expressions
- Result sets

### SQLAlchemy ORM
- Declarative base
- Model definitions
- Session management
- Query API
- Relationships (One-to-Many, Many-to-Many, One-to-One)
- Eager loading and lazy loading
- Query filtering and ordering

### Database Design
- Normalization
- Schema design patterns
- Relationship modeling
- Constraints and validations

### Migrations with Alembic
- Version control for database schema
- Auto-migration generation
- Upgrade and downgrade scripts
- Migration history management

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Basic SQL knowledge
- Understanding of OOP concepts
- PostgreSQL or MySQL installed (or SQLite for testing)

### Installation
```bash
# Install required packages
pip install -r requirements.txt

# Alternative: Install individual packages
pip install SQLAlchemy==2.0.23
pip install alembic==1.13.0
pip install psycopg2-binary==2.9.9  # For PostgreSQL
# or
pip install pymysql  # For MySQL
```

### Database Setup
```bash
# For PostgreSQL
createdb module3_db

# For MySQL
mysql -u root -p -e "CREATE DATABASE module3_db;"

# SQLite (no setup needed, uses file)
# Database file will be created automatically
```

## Usage

### Running Hands-on Exercises
```bash
# Example: Run hands_on_6 CRUD operations
python hands_on_6/crud.py

# Example: Run hands_on_7 model definitions
python hands_on_7/models.py
```

### Using SQLAlchemy ORM

#### Creating Models
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
```

#### Session Management
```python
from sqlalchemy.orm import Session

# Create session
session = Session(engine)

# Add objects
user = User(name="John", email="john@example.com")
session.add(user)
session.commit()

# Query
users = session.query(User).filter(User.name == "John").all()

# Close session
session.close()
```

#### Database Relationships
```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    employees = relationship("Employee", back_populates="department")

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    dept_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="employees")
```

## Database Migration with Alembic

### Initialize Alembic
```bash
alembic init alembic
```

### Generate Migration
```bash
alembic revision --autogenerate -m "Initial schema"
```

### Apply Migration
```bash
alembic upgrade head
```

### Revert Migration
```bash
alembic downgrade -1
```

## Learning Objectives
- Understand relational database concepts
- Master SQLAlchemy ORM and Core
- Design effective database schemas
- Implement relationships between tables
- Manage database migrations
- Write efficient queries
- Handle sessions and transactions

## SQL Relationship Types
- **One-to-Many**: One parent, multiple children (Department → Employees)
- **Many-to-One**: Multiple children, one parent (Employees → Department)
- **Many-to-Many**: Multiple records on both sides (Students ↔ Courses)
- **One-to-One**: Single parent, single child (User ↔ Profile)

## CRUD Operations Reference
```python
# CREATE
user = User(name="Alice", email="alice@example.com")
session.add(user)
session.commit()

# READ
user = session.query(User).filter_by(name="Alice").first()
all_users = session.query(User).all()

# UPDATE
user.email = "newemail@example.com"
session.commit()

# DELETE
session.delete(user)
session.commit()
```

## Query Best Practices
1. Use filter() and filter_by() for WHERE clauses
2. Use join() for relationships
3. Use eager loading (joinedload) to avoid N+1 queries
4. Use order_by() for sorting
5. Use limit() and offset() for pagination
6. Use group_by() and having() for aggregation

## Output Files
- Generated data and query results saved in `Output/` directory
- Migration scripts stored in `hands_on_7/migrations/versions/`

## Common Patterns

### Context Manager for Sessions
```python
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)

with SessionLocal() as session:
    users = session.query(User).all()
    # Session automatically closes
```

### Bulk Operations
```python
# Bulk insert
session.bulk_insert_mappings(User, [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"}
])
session.commit()
```

## Troubleshooting

### Connection Issues
- Verify database is running
- Check connection string format
- Ensure required driver is installed

### Migration Errors
- Check Alembic configuration
- Verify database permissions
- Review migration script for conflicts

### Query Performance
- Add appropriate indexes
- Use eager loading for relationships
- Monitor query execution time

## Further Reading
- SQLAlchemy Official Documentation
- Alembic Migration Tutorial
- PostgreSQL/MySQL Documentation
- Database Design Best Practices

## Notes
- Each hands_on folder builds on previous concepts
- Database configurations may need adjustment for your environment
- Practice with different database backends (PostgreSQL, MySQL, SQLite)

## Author
CTS DNS 5.0 Exercises

## License
Educational - Use for learning purposes
