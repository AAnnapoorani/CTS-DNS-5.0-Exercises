# Hands-On 3 – Test Automation Process, Lifecycle & Framework Types

# Task 1: Automation Decision and Test Case Selection

## 1. Criteria for Deciding Whether a Test Case Should Be Automated

### Criterion 1: Repetitive Execution

Tests that are executed frequently are ideal candidates for automation.

**Application to Scenario:**

The POST `/api/courses/` endpoint is tested after every code change, making it highly repetitive and suitable for automation.

### Criterion 2: Stable Functionality

Automation is effective when the functionality changes infrequently.

**Application to Scenario:**

The course creation endpoint is a core feature and is unlikely to undergo major UI or logic changes frequently.

### Criterion 3: High Business Risk

Features critical to business operations should be automated.

**Application to Scenario:**

If course creation fails, administrators cannot create courses, impacting the entire system.

### Criterion 4: Data-Driven Testing

Tests requiring multiple input combinations are ideal for automation.

**Application to Scenario:**

Various combinations of course names, codes, credits, and departments can be tested automatically.

### Criterion 5: Regression Coverage

Regression tests should be automated to save time.

**Application to Scenario:**

Whenever changes are made to the API, automated regression testing ensures the endpoint continues working correctly.

## 2. Automate or Manual Decision

| Test Case | Decision | Justification |
|------------|-----------|--------------|
| Regression testing for all CRUD endpoints after every code change | Automate | Frequent execution and predictable results |
| Exploratory testing of a new search feature | Manual | Requires human intuition and investigation |
| Performance test with 100 concurrent users | Automate | Requires load testing tools and repeated execution |
| UI test for login form | Automate | Common regression scenario |
| Verify Swagger documentation accuracy | Manual | Requires human review and interpretation |
| Smoke test after deployment | Automate | Quick validation required after every deployment |

## 3. Test Automation ROI

### Definition

Test Automation ROI (Return on Investment) measures the value gained from automation compared to the effort invested.

### Given

Automation Development Time:

```text
4 hours
```

Manual Execution Time:

```text
30 minutes = 0.5 hours
```

### Break-Even Calculation

Number of Runs Required:

```text
4 ÷ 0.5 = 8 runs
```

Therefore:

**After 8 executions, automation starts saving time compared to manual testing.**

### Maintenance Overhead

After the 10th run:

Maintenance Cost:

```text
20% of 0.5 hour
= 0.1 hour
```

Effective Saving Per Run:

```text
0.5 - 0.1
= 0.4 hour
```

Even with maintenance costs, automation remains beneficial for long-term execution.

## 4. Flaky Tests

### Definition

A flaky test is a test that sometimes passes and sometimes fails without any changes in the application code.

### Example

A Selenium test clicks a button before it becomes clickable.

Sometimes:

```text
PASS
```

Sometimes:

```text
FAIL
```

depending on system speed.

### Strategies to Prevent Flaky Tests

#### Strategy 1: Use Explicit Waits

Instead of:

```python
time.sleep(5)
```

Use:

```python
WebDriverWait(driver,10)
```

#### Strategy 2: Use Stable Locators

Prefer:

```python
By.ID
```

instead of fragile XPath expressions.

#### Strategy 3: Isolate Test Data

Each test should create and clean up its own data to avoid dependency on previous test runs.

# Task 2: Compare Automation Framework Types

## 5. Automation Framework Comparison

### Linear Framework

#### Description

Tests are written sequentially from start to finish in a single script.

#### Advantage

Simple to understand and implement.

#### Disadvantage

Poor maintainability and code duplication.

#### Example

A small script that creates a course and verifies its creation.

### Modular Framework

#### Description

Application functionality is divided into reusable modules.

#### Advantage

High reusability.

#### Disadvantage

Requires more initial design effort.

#### Example

Separate modules for Login, Course Creation, and Enrollment.

### Data-Driven Framework

#### Description

Test data is separated from test scripts.

#### Advantage

Supports multiple datasets without changing code.

#### Disadvantage

Requires external files and data management.

#### Example

Testing course creation with hundreds of course combinations from Excel or CSV.

### Keyword-Driven Framework

#### Description

Actions are defined using keywords such as Login, Click, Submit.

#### Advantage

Non-technical users can create tests.

#### Disadvantage

Complex framework implementation.

#### Example

Business analysts create tests using predefined keywords.

### Hybrid Framework

#### Description

Combines multiple framework approaches such as Modular, Data-Driven, and Keyword-Driven.

#### Advantage

Highly scalable and flexible.

#### Disadvantage

More complex initial setup.

#### Example

Large enterprise-level automation suites.

## 6. Framework Recommendation

### Scenario

Requirements:

- Test login with 50 user/password combinations
- Reuse login steps across 20 test cases
- Support technical and non-technical team members

### Recommended Framework

**Hybrid Framework**

Combining:

- Modular Framework
- Data-Driven Framework
- Keyword-Driven Framework

### Justification

#### Data-Driven

Supports testing with 50 credential combinations.

#### Modular

Login functionality can be reused across multiple tests.

#### Keyword-Driven

Allows non-technical team members to create tests using keywords.

#### Hybrid

Provides maximum scalability and maintainability.

## 7. Hybrid Framework Folder Structure

```text
CourseManagementAutomation/
│
├── config/
│   ├── config.py
│   └── settings.yaml
│
├── test_data/
│   ├── login_data.csv
│   ├── course_data.csv
│   └── enrollment_data.csv
│
├── pages/
│   ├── login_page.py
│   ├── course_page.py
│   ├── enrollment_page.py
│   └── base_page.py
│
├── utilities/
│   ├── excel_reader.py
│   ├── logger.py
│   ├── screenshots.py
│   └── wait_utils.py
│
├── tests/
│   ├── test_login.py
│   ├── test_courses.py
│   └── test_enrollment.py
│
├── reports/
│   ├── report.html
│   └── screenshots/
│
├── conftest.py
├── requirements.txt
└── README.md
```

## Framework Components

### test_data/

Stores all external datasets.

### pages/

Contains Page Object Model classes.

### utilities/

Reusable helper functions.

### tests/

Contains actual test cases.

### reports/

Stores generated test reports and screenshots.

### config/

Stores environment configuration.

# Conclusion

This hands-on covered:

- Automation decision criteria
- Automate vs Manual test selection
- Automation ROI calculation
- Flaky test analysis
- Framework comparison
- Hybrid framework recommendation
- Enterprise-level folder structure

The Hybrid Framework is the most widely used automation architecture because it combines maintainability, scalability, reusability, and support for both technical and non-technical team members.