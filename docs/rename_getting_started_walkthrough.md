# Walkthrough - Rename Getting Started Course Files

We have renamed and organized the "Getting Started" course files inside `./cpsi-27603-notes/raw` and committed/pushed them.

## Changes Made
We created the branch `feature/rename-getting-started-files` off of `main`, performed the file renames, and successfully merged and pushed them back to `main`.

### File Renames in [cpsi-27603-notes/raw](file:///Users/dcronin05/app_development/cpsi-27603-notes/raw)
1. **Syllabus**: Renamed `LTI Launch.pdf` to `syllabus.pdf`.
2. **AI Use Policy**: Renamed `ai_use.pdf` to `ai_use_policy.pdf`.
3. **Course Schedule**: Renamed `program2_schedule.png` to `course_schedule.png`.
4. **Other files**: Maintained `instructor_info.txt` and `textbook.url` as is.

---

## Git Commit History
The commits were grouped logically and made individually on the feature branch:
- **`e0ed89d`** - Archive instructor info and textbook link
- **`41f76a2`** - Archive course schedule under course_schedule.png
- **`ee69083`** - Archive AI use policy under ai_use_policy.pdf
- **`4989f19`** - Archive syllabus under syllabus.pdf
- **`468169b`** - Initial commit with README (base commit on `main`)

Both `main` and `feature/rename-getting-started-files` have been successfully pushed to the remote repository at `git@github.com:dcronin05/cpsi-course-scratch.git`.

---

## Verification Results

### Raw Directory Listing
```
total 4664
-rw-------@ 1 dcronin05  staff    38948 Jun  9 18:16 ai_use_policy.pdf
-rw-r--r--@ 1 dcronin05  staff  1971594 Jun  9 18:13 course_schedule.png
-rw-r--r--@ 1 dcronin05  staff      244 Jun  9 18:14 instructor_info.txt
-rw-------@ 1 dcronin05  staff   363125 Jun  9 18:14 syllabus.pdf
-rw-r--r--@ 1 dcronin05  staff       42 Jun  9 18:16 textbook.url
```

### Git Status
```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

### Local Branch Cleanup
The feature branch has been deleted locally:
```
Deleted branch feature/rename-getting-started-files (was e0ed89d).
```
