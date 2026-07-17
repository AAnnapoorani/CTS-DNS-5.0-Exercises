# Hands-On 2 – SDLC vs TDLC, V-Model & Agile QA Integration

# Task 1: V-Model Mapping

## 1. V-Model Diagram

```text
                     Acceptance Testing
                            ↑
Requirements  ----------------------------

                        System Testing
                            ↑
System Design ----------------------------

                     Integration Testing
                            ↑
Architecture Design ----------------------

                         Unit Testing
                            ↑
Module Design ----------------------------

                            Coding
```

The V-Model establishes a direct relationship between development phases and testing phases. Testing activities are planned alongside development activities to ensure quality throughout the software lifecycle.

## 2. SDLC to TDLC Mapping and Test Artifacts

| SDLC Phase | Corresponding TDLC Phase | Test Artifact Produced |
|------------|-------------------------|------------------------|
| Requirements Gathering | Acceptance Testing | Acceptance Test Plan, Acceptance Criteria |
| System Design | System Testing | System Test Cases |
| Architecture Design | Integration Testing | Integration Test Plan |
| Module Design | Unit Testing | Unit Test Cases |
| Coding | Execution of Tests | Source Code and Automated Tests |

### Explanation

#### Requirements → Acceptance Testing

During requirements gathering, QA prepares Acceptance Test Plans to verify that business requirements are met.

#### System Design → System Testing

QA creates System Test Cases to validate the complete application.

#### Architecture Design → Integration Testing

QA prepares Integration Test Plans to verify communication between components.

#### Module Design → Unit Testing

Developers create Unit Test Cases for individual modules.

#### Coding

The actual implementation of the application is performed and all planned tests are executed.

## 3. Entry and Exit Criteria

### Unit Testing

#### Entry Criteria

- Module design completed
- Source code available
- Unit test cases prepared

#### Exit Criteria

- All unit test cases executed
- No critical defects open
- Code coverage meets project standards

### Integration Testing

#### Entry Criteria

- Unit testing completed successfully
- Modules integrated
- Integration test cases prepared

#### Exit Criteria

- All integration test cases executed
- Interfaces verified
- No critical integration defects remain

### System Testing

#### Entry Criteria

- Complete system available
- Integration testing completed
- Test environment ready

#### Exit Criteria

- All system test cases executed
- No open critical or high severity defects
- Functional requirements validated

### Acceptance Testing

#### Entry Criteria

- System testing completed
- Business users available
- Acceptance criteria defined

#### Exit Criteria

- Business users approve the system
- Acceptance criteria satisfied
- Sign-off received from stakeholders

## 4. Early QA Engagement Points in Course Management API

### Requirements Review

QA participates in requirement discussions to identify ambiguities, missing validations, and unclear business rules before development begins.

Example:

Requirement states:

"Admin can create a course."

QA asks:

- Is course code mandatory?
- Should duplicate course codes be allowed?
- What validations are required?

### Design Review

QA reviews API specifications and database design before coding starts.

Example:

Reviewing:

- API request and response structure
- Error handling strategy
- Validation rules
- Database relationships

This helps identify defects before implementation.

# Task 2: Agile QA and Shift-Left Testing

## 5. Problems with Waterfall Testing

In a traditional Waterfall model, testing begins only after development is completed.

### Problem 1: Late Defect Detection

Errors discovered late become expensive to fix.

Example:

A missing validation rule discovered during System Testing may require redesign and recoding.

### Problem 2: Higher Cost

The later a defect is found, the more resources are needed to fix it.

Example:

Fixing a requirement defect during production can cost significantly more than fixing it during analysis.

### Problem 3: Schedule Delays

Large numbers of defects discovered near project completion can delay releases.

Example:

If Course Creation and Enrollment APIs fail during testing, deployment may be postponed.

## 6. QA Role in Agile Ceremonies

### Sprint Planning

Responsibilities:

- Review user stories
- Define acceptance criteria
- Estimate testing effort
- Identify risks

Example:

For "Create Course" feature, QA defines validation and error-handling requirements.

### Daily Standup

Responsibilities:

- Report testing progress
- Highlight blockers
- Discuss defects

Example:

QA reports that Course API testing is blocked due to database connectivity issues.

### Sprint Review

Responsibilities:

- Validate completed features
- Demonstrate test results
- Verify acceptance criteria

Example:

QA demonstrates successful Course Creation functionality.

### Sprint Retrospective

Responsibilities:

- Discuss lessons learned
- Suggest process improvements
- Identify testing bottlenecks

Example:

Recommend earlier API testing to reduce defects.

## 7. Shift-Left Testing Practices

### A. Requirement Review for Testability

QA reviews requirements before development starts.

Application to Course API:

Ensure requirements clearly define validation rules and error responses.

### B. Test Cases Before Code (TDD/BDD)

QA prepares test cases before implementation.

Application:

Write tests for course creation before coding the endpoint.

### C. Static Code Analysis

Analyze code without execution.

Application:

Use tools to identify security vulnerabilities and coding issues in the API.

### D. API Contract Testing

Validate API specifications before integration.

Application:

Verify request and response formats for POST /api/courses/.

## 8. Acceptance Criteria in Given-When-Then Format

### Scenario 1: Successful Course Creation

**Given**

The admin is logged into the system

**When**

The admin enters valid course information and submits the form

**Then**

The course should be created successfully

**And**

The system should display a success message

### Scenario 2: Duplicate Course Code

**Given**

A course already exists with code "CSE101"

**When**

The admin attempts to create another course using code "CSE101"

**Then**

The system should reject the request

**And**

An error message should indicate that the course code already exists

### Scenario 3: Missing Required Fields

**Given**

The admin is on the Create Course page

**When**

The admin submits the form without entering required fields

**Then**

The system should prevent submission

**And**

Validation error messages should be displayed

# Conclusion

This hands-on covered:

- SDLC and TDLC relationship
- Complete V-Model mapping
- Entry and Exit Criteria
- Early QA involvement
- Agile QA integration
- Shift-Left Testing practices
- Given-When-Then Acceptance Criteria

These concepts help QA teams improve software quality by identifying defects early and collaborating closely with development teams throughout the project lifecycle.