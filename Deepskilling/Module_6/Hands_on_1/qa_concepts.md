# Hands-On 1 – QA Concepts, Functional Testing & Defect Lifecycle

# Task 1: Map Testing Types to a Real System

## 1. Testing Types for the Course Management API

### Unit Testing

**Description:**  
Unit Testing verifies an individual function or method in isolation without involving external systems such as databases or APIs.

**Test Case:**  
Verify that the course validation function rejects an empty course name.

**Input:**
```python
validate_course({"course_name": ""})
```

**Expected Result:**
```python
ValueError("Course name is required")
```

**Classification:** Functional Testing

### Integration Testing

**Description:**  
Integration Testing verifies that multiple components work together correctly.

**Test Case:**  
Verify that the POST `/api/courses/` endpoint successfully inserts course data into the database.

**Steps:**

1. Send a POST request with valid course data.
2. Check the database table.

**Expected Result:**

- API returns HTTP Status Code 201.
- New course record is stored in the database.

**Classification:** Functional Testing

### System Testing

**Description:**  
System Testing validates the complete application workflow.

**Test Case:**  
Create a new course and retrieve it using the GET endpoint.

**Steps:**

1. Create a course using POST `/api/courses/`.
2. Retrieve the created course using GET `/api/courses/{id}`.

**Expected Result:**

- Course is successfully created.
- Same course information is returned by the GET request.

**Classification:** Functional Testing

### User Acceptance Testing (UAT)

**Description:**  
User Acceptance Testing validates the system from the end user's perspective.

**Test Case:**  
A college administrator creates a new course.

**Steps:**

1. Login as College Admin.
2. Navigate to Course Management.
3. Create a new course.
4. Verify the course appears in the course list.

**Expected Result:**

- Course is created successfully.
- Course appears in the course catalog.

**Classification:** Functional Testing

## 2. Functional vs Non-Functional Testing

### Functional Testing

Functional Testing verifies whether the system performs the intended functions correctly.

**Examples:**

- Create Course
- Update Course
- Delete Course
- Retrieve Course Details
- Enroll Student

### Non-Functional Testing

Non-Functional Testing evaluates how well the system performs.

**Example: Performance Testing**

**Test Case:**  
100 concurrent users send requests to:

```http
GET /api/courses/
```

**Expected Result:**

- Average response time less than 2 seconds.
- No server crashes.
- Error rate below 1%.

**Classification:** Non-Functional Testing

## 3. Black-Box Testing vs White-Box Testing

| Black-Box Testing | White-Box Testing |
|------------------|------------------|
| No knowledge of source code is required. | Knowledge of source code is required. |
| Focuses on inputs and outputs. | Focuses on internal logic and code paths. |
| Performed from user perspective. | Performed from developer perspective. |
| Used in Functional and Acceptance Testing. | Used in Unit Testing and Code Reviews. |
| Tests system behavior. | Tests code structure and logic. |

### Who Performs Each Type?

**QA Tester:**  
Typically performs Black-Box Testing because they validate system behavior without examining the source code.

**Developer:**  
Typically performs White-Box Testing because they understand and test the internal implementation.

## 4. Formal Test Cases for POST /api/courses/

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|-------------|-------------|---------------|------------|----------------|--------------|-----------|
| TC_001 | Create course with valid data | API is running | Send POST request with valid course data | HTTP 201 Created and course stored successfully | | |
| TC_002 | Create course with missing course name | API is running | Send POST request without course_name | HTTP 400 Bad Request with validation message | | |
| TC_003 | Create course using duplicate course code | Existing course code already present | Send POST request with duplicate course code | Duplicate course error message displayed | | |

# Task 2: Defect Lifecycle & Severity Classification

## 5. Defect Lifecycle

The complete defect lifecycle is:

```text
New
 ↓
Assigned
 ↓
Open
 ↓
Fixed
 ↓
Retest
 ↓
Verified
 ↓
Closed
```

### Rejected Path

```text
New
 ↓
Assigned
 ↓
Rejected
```

A defect may be rejected if:

- The issue is not reproducible.
- The issue is not a defect.
- The reported behavior is expected.

### Deferred Path

```text
New
 ↓
Assigned
 ↓
Deferred
```

A defect may be deferred if:

- The fix is low priority.
- The release deadline is near.
- The defect will be fixed in a future version.

## 6. Severity and Priority Classification

### Bug A

**Issue:**  
POST `/api/courses/` returns HTTP 500 Internal Server Error for all requests.

**Severity:** Critical

**Priority:** P1

**Justification:**  
The core functionality of course creation is completely broken, preventing all users from creating courses.

### Bug B

**Issue:**  
Course names longer than 150 characters are silently truncated.

**Severity:** Medium

**Priority:** P3

**Justification:**  
The system still functions, but data integrity is affected.

### Bug C

**Issue:**  
Swagger `/docs` page contains a typo.

**Severity:** Low

**Priority:** P4

**Justification:**  
The issue does not impact functionality and is purely cosmetic.

### Bug D

**Issue:**  
Login occasionally returns HTTP 401 on the first attempt.

**Severity:** High

**Priority:** P1

**Justification:**  
Although intermittent, login failures affect user access and indicate possible system instability.

## 7. Defect Report

### Defect ID

BUG-001

### Title

POST /api/courses/ returns HTTP 500 Internal Server Error

### Environment

- Operating System: Windows 11
- Browser: Chrome 138+
- API Environment: Localhost
- Python Version: 3.10+

### Build Version

v1.0.0

### Severity

Critical

### Priority

P1

### Steps to Reproduce

1. Start the Course Management API.
2. Open Swagger UI.
3. Navigate to POST `/api/courses/`.
4. Enter valid course information.
5. Click Execute.

### Expected Result

The course should be created successfully and return HTTP 201 Created.

### Actual Result

API returns HTTP 500 Internal Server Error.

### Attachments

Screenshot of 500 Error

### Status

New

## 8. Difference Between Severity and Priority

### Severity

Severity indicates how much impact the defect has on the system.

### Priority

Priority indicates how urgently the defect should be fixed.

### Example

A spelling mistake in the CEO's dashboard:

**Severity:** Low

Reason:
The application continues to function correctly.

**Priority:** High

Reason:
The CEO sees the issue directly, so it must be fixed immediately.

## Conclusion

This hands-on covered:

- Testing Levels (Unit, Integration, System, UAT)
- Functional and Non-Functional Testing
- Black-Box and White-Box Testing
- Formal Test Case Design
- Defect Lifecycle
- Severity and Priority Classification
- Defect Reporting Process

These concepts form the foundation of Quality Assurance and Test Automation practices.