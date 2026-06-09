# Walkthrough - Structured JSON Storage System

We have designed and implemented a structured JSON-based storage database and a Python CLI administration manager inside the virtual environment `.venv`.

---

## Architectural Implementation

### 1. [course_db.json](file:///Users/dcronin05/app_development/cpsi-27603-notes/course_db.json)
This structured JSON file serves as the single source of truth database. It is highly extensible, allowing custom fields and objects to be added without any schema alterations or database regeneration. It structures the data for:
- Course Metadata (prerequisites, objectives, description)
- Instructor Information
- Textbook Link and metadata
- Grading Scale and Weights
- Interactive Course Schedule Calendar (modules, deadlines, events, exams)
- File Registry (tracking and mapping all raw course documents)

### 2. [manage_db.py](file:///Users/dcronin05/app_development/cpsi-27603-notes/manage_db.py)
A CLI management tool equipped with the following sub-commands:
- `validate`: Performs schema validation of `course_db.json` against a defined JSON Schema using `jsonschema`.
- `summary`: Outputs a clean text representation of the course info, textbook, instructor details, and grading rules.
- `schedule`: Renders a chronological grid of modules and deadlines (with support for a verbose `--verbose` view).
- `register-file`: Appends new documents to the database registry. It accepts a `--custom key=value` parameter to insert new custom metadata fields dynamically.

### 3. [Virtual Environment](file:///Users/dcronin05/app_development/cpsi-27603-notes/.venv)
Created `.venv` to manage and isolate all Python packages (e.g. `jsonschema`).

---

## Git Commit History
The commits were grouped logically and made individually on the feature branch `feature/design-storage-system`:
- **`7e37510`** - Update README.md with database and CLI manager instructions
- **`146298a`** - Implement manage_db.py Python database CLI manager
- **`0d05f4b`** - Populate course database JSON with course details
- **`8307ec6`** - Initialize Python virtual environment configuration

---

## Verification Results

We verified that the CLI tool executes perfectly using the `.venv` Python:

1. **Schema Validation**:
   ```bash
   .venv/bin/python manage_db.py validate
   # Output: ✓ Database structure is valid.
   ```

2. **Course Summary**:
   ```bash
   .venv/bin/python manage_db.py summary
   # Output: Prints formatted header, instructor contact, textbook details, and grading scale.
   ```

3. **Course Schedule**:
   ```bash
   .venv/bin/python manage_db.py schedule --verbose
   # Output: Prints chronological grid of dates, types, modules, and detailed topic bullet-points.
   ```

4. **File Registration**:
   ```bash
   .venv/bin/python manage_db.py register-file raw/syllabus.pdf --type "syllabus" --description "Official syllabus with grading rules" --force --custom term=summer2026 course=cpsi-27603
   # Output:
   # ✓ Registered file 'syllabus.pdf' in database.
   #   Custom fields added: {'term': 'summer2026', 'course': 'cpsi-27603'}
   ```
