-- Task 1: Baseline Performance — No Indexes

-- Run EXPLAIN on the JOIN query

EXPLAIN SELECT s.first_name, s.last_name, c.course_name FROM enrollments e 
JOIN students s ON s.student_id = e.student_id JOIN courses c ON c.course_id = e.course_id WHERE s.enrollment_year = 2022;

-- Observation:

-- PostgreSQL may use Sequential Scan (Seq Scan) on students, enrollments or courses because the sample tables are very small.
-- This is normal behaviour.
-- Seq Scan is efficient for small datasets.

-- Estimated Cost

-- Output
-- Nested Loop cost=12.16..42.16 rows=9 width=554
-- Hash Join  (cost=12.01..40.40 rows=9 width=240) Hash Cond: (e.student_id = s.student_id)
-- Seq Scan on enrollments e  (cost=0.00..24.50 rows=1450 width=8)
-- Hash  (cost=12.00..12.00 rows=1 width=240)
-- Seq Scan on students s  (cost=0.00..12.00 rows=1 width=240) Filter: (enrollment_year = 2022)
-- Index Scan using courses_pkey on courses c  (cost=0.14..0.20 rows=1 width=322)
-- Index Cond: (course_id = e.course_id)

-- Task 2 : Add Indexes and Compare Plans

-- B-Tree Index

CREATE INDEX idx_students_enrollment_year ON students(enrollment_year);

-- Verify

SELECT * FROM pg_indexes WHERE tablename='students';

-- Composite UNIQUE Index

CREATE UNIQUE INDEX idx_enrollment_unique ON enrollments(student_id,course_id);

-- Verify

SELECT * FROM pg_indexes WHERE tablename='enrollments';

-- Index on Course Code

CREATE INDEX idx_course_code ON courses(course_code);

-- Verify

SELECT * FROM pg_indexes WHERE tablename='courses';

-- Compare Query Plan

EXPLAIN SELECT s.first_name,s.last_name,c.course_name FROM enrollments e JOIN students s ON s.student_id=e.student_id
JOIN courses c ON c.course_id=e.course_id WHERE s.enrollment_year=2022;

-- Observation

-- Explaination of output before and after indexing.
-- PostgreSQL may STILL choose Sequential Scan because the dataset contains only a few rows.
-- PostgreSQL automatically chooses whichever execution plan is faster.
-- In a production database containing thousands of rows, PostgreSQL would typically prefer Index Scan.

-- Partial Index

CREATE INDEX idx_null_grades ON enrollments(student_id) WHERE grade IS NULL;

-- Verify Partial Index

SELECT indexname FROM pg_indexes WHERE tablename='enrollments';

-- Test Query Using Partial Index

EXPLAIN SELECT * FROM enrollments WHERE grade IS NULL;

-- Final Observation

-- Indexes Created:

-- 1. idx_students_enrollment_year
-- 2. idx_enrollment_unique
-- 3. idx_course_code
-- 4. idx_null_grades

-- PostgreSQL Query Planner may continue using Seq Scan because of the small sample dataset. This behaviour is expected.
