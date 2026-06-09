# Rename Getting Started Course Files - Implementation Plan

Determine proper archive names for the course files in `./cpsi-27603-notes/raw` and rename them for consistency and clarity.

## Git Branch & Versioning Strategy
We will create a new branch `feature/rename-getting-started-files` off of `main` to perform the changes.
To follow the requirement of multiple commits for each change, we will commit each file rename individually.

- **Branch**: `feature/rename-getting-started-files`
- **Commits**:
  1. Rename `LTI Launch.pdf` -> `syllabus.pdf`
  2. Rename `ai_use.pdf` -> `ai_use_policy.pdf`
  3. Rename `program2_schedule.png` -> `course_schedule.png`

## Proposed Changes
We will rename the files in [cpsi-27603-notes/raw](file:///Users/dcronin05/app_development/cpsi-27603-notes/raw).

### Files to Rename
- **`LTI Launch.pdf`**: This is the official syllabus. We will rename it to `syllabus.pdf` (lowercase, simple, standard).
- **`ai_use.pdf`**: This details the AI use policy in the course. We will rename it to `ai_use_policy.pdf` (clearer, lowercase).
- **`program2_schedule.png`**: This contains the visual course schedule calendar. We will rename it to `course_schedule.png` (more descriptive).
- **`instructor_info.txt`** and **`textbook.url`**: These already have clean, appropriate archive names, so we will keep them as is (but ensure they are committed if untracked).

## Verification Plan

### Manual Verification
- Run `ls -la raw/` to verify that all 5 files are present with their new names.
- Check `git log` to verify the commits have been made correctly.
- Check `git status` to ensure a clean working tree.
