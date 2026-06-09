# CPSI-27603 Programming II Notes Database

This repository contains notes, archived files, and a structured database for CPSI 27603 (Programming II) at UA Little Rock.

---

## Architecture Overview

1. **`course_db.json`**: A structured, single source of truth document database storing:
   - Course overview (credit hours, prerequisites, objectives).
   - Instructor contact & office hours.
   - Textbook details.
   - Course policies (grading criteria, AI usage, late and resubmission policies).
   - Chronological course schedule (modules, topics, deadlines, exams).
   - Archived files registry (mapping current filenames to their original source names with descriptions and extensible custom fields).
2. **`manage_db.py`**: A CLI administration tool to query, validate, and register documents within the database.
3. **`.venv/`**: A local virtual environment isolating Python dependencies (such as `jsonschema` for validating the database schema).

---

## Setup & Installation

To initialize the Python virtual environment and install dependencies, run the following commands:

```bash
# Initialize virtual environment
python3 -m venv .venv

# Install dependencies (such as jsonschema)
.venv/bin/pip install -r requirements.txt
```

---

## CLI database Manager: `manage_db.py`

Always execute the manager using the virtual environment's Python binary:

### 1. Validate Database Schema
Ensure the `course_db.json` structure is strictly valid against the JSON Schema:
```bash
.venv/bin/python manage_db.py validate
```

### 2. View Course Summary
Print course details, instructor info, grading criteria, and textbook links:
```bash
.venv/bin/python manage_db.py summary
```

### 3. View Course Schedule
Print the calendar of modules and deadlines:
```bash
# Basic view
.venv/bin/python manage_db.py schedule

# Verbose view (prints module topics)
.venv/bin/python manage_db.py schedule --verbose
```

### 4. Register a New File
Register a new file from `raw/` into the database registry, prompting for metadata and allowing arbitrary custom fields:
```bash
.venv/bin/python manage_db.py register-file raw/new_material.pdf \
  --type "assignment" \
  --description "Project 1 specifications" \
  --original-name "Proj1Spec.pdf" \
  --custom module=3 tags=project,cpp
```
Any custom fields provided with `--custom key=value` will be stored under the `custom_fields` object in the JSON registry without violating the schema.
