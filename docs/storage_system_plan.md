# Design and Implement Structured JSON Storage System - Implementation Plan

Design and build a single source of truth database system for course notes and files. 

## Critical Development Rules
1. **Git Version Control**: All changes must be made via feature branches and structured into logical commits (multiple commits per change).
2. **Plan-driven Changes**: All changes must be approved in this plan before execution.
3. **Python Virtual Environment (`.venv`)**: Whenever using Python in any way (creating files, running commands, installing packages, execution), **always** use the project's virtual environment `.venv`.

---

## Architectural Decision: JSON + Python CLI
To meet the requirement of storing all file information in a **single source of truth** that is **easily expandable without database regeneration or schema migration**, we will use a structured **JSON file** (`course_db.json`) managed by a **Python CLI tool** (`manage_db.py`).

We will use a Python virtual environment (`.venv`) to manage dependencies (such as `jsonschema` for database structure validation).

---

## Git Branch & Versioning Strategy
- **Branch**: `feature/design-storage-system`
- **Commits**:
  1. Initialize virtual environment (`.venv`), configure `.gitignore`, and add `requirements.txt`.
  2. Create the `course_db.json` database populated with syllabus, schedule, and instructor data.
  3. Implement the `manage_db.py` CLI tool with validation, summary, and file registration features.
  4. Update `README.md` to document setup and CLI usage.

---

## Proposed Changes
We will work inside [cpsi-27603-notes](file:///Users/dcronin05/app_development/cpsi-27603-notes).

### 1. [.gitignore](file:///Users/dcronin05/app_development/cpsi-27603-notes/.gitignore)
Ignore the `.venv/` directory and python cache files.

### 2. [requirements.txt](file:///Users/dcronin05/app_development/cpsi-27603-notes/requirements.txt)
Define Python dependencies:
- `jsonschema`: For robust structural validation of `course_db.json`.

### 3. [course_db.json](file:///Users/dcronin05/app_development/cpsi-27603-notes/course_db.json)
This JSON file serves as the single source of truth:
- **`course`**: Code, name, section, term, credit hours, description.
- **`instructor`**: Name, pronouns, email, office location, office hours.
- **`materials`**: Textbook links and details.
- **`policies`**: Grading scales, criteria, AI use rules, late policy, and resubmissions.
- **`schedule`**: List of modules, dates, topics, and deliverables.
- **`archived_files`**: Registry of files in `raw/` with custom expandable metadata fields.

### 4. [manage_db.py](file:///Users/dcronin05/app_development/cpsi-27603-notes/manage_db.py)
Python CLI script supporting validation, summary, schedule, and file registration.

### 5. [README.md](file:///Users/dcronin05/app_development/cpsi-27603-notes/README.md)
Document installation steps and CLI usage.

---

## Verification Plan

### Automated Verification
- Activate `.venv` and run `python3 manage_db.py validate` to verify the JSON schema matches the database contents.

### Manual Verification
- Run `python3 manage_db.py summary` to verify correct output.
- Run `python3 manage_db.py schedule` to verify calendar listing.
- Run `python3 manage_db.py register-file raw/syllabus.pdf --type "syllabus" --desc "Test Registration"` to verify write capabilities.
