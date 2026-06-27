# Hands-On 5 : MongoDB - Document Modelling, CRUD & Aggregation
## Database : college_nosql
## Collection : feedback

# Task 1

Created database and feedback collection.
Imported 10 documents using feedback.json.
Verification: Document Count = 10

# Task 2 

## Filter

- Find All Feedback for CS101
{
  "course_code": "CS101"
}

- Find Feedback with Rating >= 4
{
  "rating": {
    "$gte": 4
  }
}

- Find Feedback Containing the Tag "database"
{
  "tags": "database"
}

### Update a Feedback Record

{
  "student_id": 4,
  "course_code": "ME101"
}

Change: "rating": 2
to : "rating": 3

Change: "comments": "Needs improvement"
to: "comments": "Improved after revisions"

### Verify
{
  "student_id": 4
}

### Delete Low-Rated Feedback
{
  "rating": {
    "$lt": 3
  }
}

- No rating below 3

### Verification

- Total Documents
{}

- Count
db.feedback.countDocuments()

# Task 3 
## Aggregations

### Multi-stage aggregation pipeline

- Stage 1 – $match
{
  "semester": "2022-ODD"
}

- Stage 2 – $group
{
  "_id": "$course_code",
  "avg_rating": {
    "$avg": "$rating"
  },
  "feedback_count": {
    "$sum": 1
  }
}

- Stage 3 – $sort
{
  "avg_rating": -1
}

### Extended multi-stage aggregation pipeline

- Stage 4 – $project
{
  "_id": 0,
  "course_code": "$_id",
  "average_rating": {
    "$round": [
      "$avg_rating",
      1
    ]
  },
  "feedback_count": 1
}

### Pipeline that uses $unwind on the tags array, then $group

- Stage 1 – $unwind
{
  "path": "$tags"
}
- Stage 2 – $group
{
  "_id": "$tags",
  "count": {
    "$sum": 1
  }
}
- Stage 3 – $sort
{
  "count": -1
}

### Create Index

Field: course_code
Type: Ascending (1)

### Verify Index

db.feedback.find(
{
  course_code: "CS101"
}
).explain("executionStats")

