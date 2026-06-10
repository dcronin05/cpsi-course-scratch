# Scrape Blackboard Saved Pages and Retrieve YouTube Transcripts

This plan details how we will scrape the Blackboard HTML files saved in `raw/module-01/`, clean them into structured Markdown files, download YouTube transcripts for embedded videos, register all new files in the database, and clean up the original bulky HTML files and their asset folders.

## User Review Required

> [!IMPORTANT]
> **Scraping Target Paths & Database Schema**
> - The two HTML pages (`raw/module-01/participation01.html` and `raw/module-01/lecture_videos.html`) will be parsed using `beautifulsoup4` and converted to clean Markdown.
> - The files generated will be:
>   1. `raw/module-01/practice01_instructions.md` (parsed from `participation01.html` which is titled "Practice01" on Blackboard)
>   2. `raw/module-01/lecture_videos.md` (parsed from `lecture_videos.html`)
>   3. `raw/module-01/programming-2-how-to-use-github-and-codespace_transcript.md` (Sanitized title from YouTube video ID `ADncVDH2wLo` embedded in `participation01.html`)
>   4. `raw/module-01/programming-2-module-1-lecture-slides-part-a_transcript.md` (Sanitized title from YouTube video ID `XKEVQ4EA9sY` embedded in `lecture_videos.html`)
>   5. `raw/module-01/programming-2-module-1-lecture-slides-part-b_transcript.md` (Sanitized title from YouTube video ID `deJ5JSGAL7g` embedded in `lecture_videos.html`)
> - The `quiz01.md` file will also be registered in the database, as it is currently untracked and unregistered.
> - All bulky HTML files and their associated asset directories (`*_files/`) will be permanently deleted from the repository.

## Open Questions

> [!NOTE]
> **Transcript Format**
> We plan to format the downloaded transcripts using periodic timestamps (e.g. `[MM:SS]`) to make them easily searchable and readable for study. If you prefer plain un-timestamped paragraphs, please let us know.

## Proposed Changes

We will work inside [cpsi-27603-notes](file:///Users/dcronin05/app_development/cpsi-27603-notes).

### 1. [MODIFY] [requirements.txt](file:///Users/dcronin05/app_development/cpsi-27603-notes/requirements.txt)
Add `beautifulsoup4` and `youtube-transcript-api` as dependencies.

### 2. [NEW] [scrape_course_files.py](file:///Users/dcronin05/app_development/cpsi-27603-notes/scrape_course_files.py)
A Python script to execute inside the virtual environment:
- Install dependencies.
- Parse `participation01.html` to extract assignment instructions for Practice 01 and output them as `raw/module-01/practice01_instructions.md`.
- Parse `lecture_videos.html` to extract video links and lecture slide links, outputting them as `raw/module-01/lecture_videos.md`.
- Scrape YouTube links from both pages, fetch their titles via the YouTube oEmbed API, download transcripts via `youtube-transcript-api`, format them with timestamps, and save them as `raw/module-01/<title>_transcript.md`.
- Run the CLI registration commands (`manage_db.py register-file ...`) for the new files and `quiz01.md`.
- Delete the original `.html` files and their `_files/` folders.

### 3. [DELETE] Bulky HTML Files
- `raw/module-01/participation01.html`
- `raw/module-01/participation01_files/`
- `raw/module-01/lecture_videos.html`
- `raw/module-01/lecture_videos_files/`

---

## Verification Plan

### Automated Tests
- Run `.venv/bin/python manage_db.py validate` to ensure `course_db.json` is perfectly valid.
- Run `git status` to verify no leftover untracked HTML files/folders exist and all new files are tracked.

### Manual Verification
- Review the generated Markdown files (`practice01_instructions.md`, `lecture_videos.md`, and the transcripts) to ensure formatting is correct and clean.
- Verify that `course_db.json` has registrations for:
  - `raw/module-01/practice01_instructions.md`
  - `raw/module-01/lecture_videos.md`
  - `raw/module-01/quiz01.md`
  - The three transcript files.
