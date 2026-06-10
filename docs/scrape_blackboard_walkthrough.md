# Walkthrough - Scrape Blackboard Saved Pages and Retrieve YouTube Transcripts

We have successfully scraped the saved Blackboard HTML pages, extracted the course instructions and lecture slides/links, downloaded interactive YouTube transcripts for embedded videos, registered everything cleanly in the database, and removed the heavy HTML pages and files from the workspace.

---

## Changes Made

### 1. Ingestion Script (`scrape_course_files.py`)
Created and refined `scrape_course_files.py` to:
- Parse `lecture_videos.html` using BeautifulSoup to extract embedded YouTube links and lecture slides. Saved output as `raw/module-01/lecture_videos.md`.
- Parse `participation01.html` using BeautifulSoup to extract assignment instructions for Practice 01. Saved output as `raw/module-01/practice01_instructions.md`.
- Retrieve YouTube transcripts via `youtube-transcript-api` and titles via oEmbed API. Saved as markdown files with timestamps:
  - `raw/module-01/programming-2-how-to-use-github-and-codespace_transcript.md` (99 lines)
  - `raw/module-01/programming-2-module-1-lecture-slides-part-a_transcript.md` (346 lines)
  - `raw/module-01/programming-2-module-1-lecture-slides-part-b_transcript.md` (808 lines)
- Automatically register all new files in `course_db.json` using the `manage_db.py register-file` tool.
- Remove source `.html` files and `_files` directories.

### 2. Dependency updates
- Added `beautifulsoup4` and `youtube-transcript-api` to `requirements.txt`.
- Ignore the local `scratch/` directory in `.gitignore`.

### 3. File Registry in Database
Added registries for the following files under module `module-01`:
- `lecture_videos.md` (type: `lecture`)
- `practice01_instructions.md` (type: `assignment`)
- The three `transcript` files.
- `quiz01.md` (type: `assignment`)

---

## Verification Results

### Database Validation
```bash
.venv/bin/python manage_db.py validate
# Output: ✓ Database structure is valid.
```

### Git Status (Clean Working Tree)
```bash
git status
# Output:
# On branch main
# Your branch is ahead of 'origin/main' by 4 commits.
# nothing to commit, working tree clean
```

### Transcript File verification
Transcripts are fully retrieved with timestamps (e.g. `[02:15] text`) which helps in searching and reading lecture content.
