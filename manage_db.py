#!/usr/bin/env python3
import argparse
import json
import os
import sys
from datetime import datetime

# Path to the database file
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "course_db.json")

# Database JSON schema definition
SCHEMA = {
    "type": "object",
    "required": ["course", "instructor", "materials", "policies", "schedule", "archived_files", "assignments"],
    "properties": {
        "course": {
            "type": "object",
            "required": ["code", "name", "section", "term", "credit_hours"],
            "properties": {
                "code": {"type": "string"},
                "name": {"type": "string"},
                "section": {"type": "string"},
                "term": {"type": "string"},
                "credit_hours": {"type": "integer"},
                "description": {"type": "string"},
                "prerequisites": {"type": "string"},
                "learning_objectives": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            }
        },
        "instructor": {
            "type": "object",
            "required": ["name", "email"],
            "properties": {
                "name": {"type": "string"},
                "pronouns": {"type": "string"},
                "email": {"type": "string"},
                "office_location": {"type": "string"},
                "office_hours": {"type": "string"},
                "availability_note": {"type": "string"}
            }
        },
        "materials": {
            "type": "object",
            "required": ["textbook"],
            "properties": {
                "textbook": {
                    "type": "object",
                    "required": ["link"],
                    "properties": {
                        "title": {"type": "string"},
                        "subtitle": {"type": "string"},
                        "authors": {"type": "array", "items": {"type": "string"}},
                        "isbn": {"type": "string"},
                        "required": {"type": "boolean"},
                        "link": {"type": "string"},
                        "sourcing": {
                            "type": "object",
                            "properties": {
                                "platform": {"type": "string"},
                                "repository": {"type": "string"},
                                "local_path": {"type": "string"}
                            }
                        }
                    }
                },
                "optional_textbook": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "subtitle": {"type": "string"},
                        "authors": {"type": "array", "items": {"type": "string"}},
                        "isbn": {"type": "string"},
                        "required": {"type": "boolean"},
                        "link": {"type": "string"}
                    }
                }
            }
        },
        "policies": {
            "type": "object",
            "required": ["grading_scale", "grading_criteria"],
            "properties": {
                "grading_scale": {
                    "type": "object",
                    "additionalProperties": {"type": "string"}
                },
                "grading_criteria": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["category", "weight"],
                        "properties": {
                            "category": {"type": "string"},
                            "weight": {"type": "number"}
                        }
                    }
                },
                "ai_use": {
                    "type": "object",
                    "properties": {
                        "instructional_toolchain": {"type": "string"},
                        "student_guidelines": {"type": "array", "items": {"type": "string"}},
                        "constraints": {"type": "array", "items": {"type": "string"}}
                    }
                },
                "late_policy": {"type": "string"},
                "resubmission_policy": {"type": "string"}
            }
        },
        "schedule": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["type"],
                "properties": {
                    "type": {"type": "string", "enum": ["event", "module", "deadline", "exam"]},
                    "date": {"type": "string"},
                    "title": {"type": "string"},
                    "module_number": {"type": "integer"},
                    "start_date": {"type": "string"},
                    "end_date": {"type": "string"},
                    "topics": {"type": "array", "items": {"type": "string"}},
                    "description": {"type": "string"}
                }
            }
        },
        "assignments": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "title", "type"],
                "properties": {
                    "id": {"type": "string"},
                    "title": {"type": "string"},
                    "type": {"type": "string"},
                    "description": {"type": "string"},
                    "prompts": {"type": "array", "items": {"type": "string"}},
                    "requirements": {"type": "object"}
                }
            }
        },
        "archived_files": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["filename", "original_name", "path", "type"],
                "properties": {
                    "filename": {"type": "string"},
                    "original_name": {"type": "string"},
                    "path": {"type": "string"},
                    "type": {"type": "string"},
                    "module": {"type": "string"},
                    "description": {"type": "string"},
                    "added_at": {"type": "string"},
                    "custom_fields": {"type": "object"}
                }
            }
        }
    }
}

def load_db():
    if not os.path.exists(DB_PATH):
        print(f"Error: Database file not found at {DB_PATH}", file=sys.stderr)
        sys.exit(1)
    try:
        with open(DB_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading database JSON: {e}", file=sys.stderr)
        sys.exit(1)

def save_db(data):
    try:
        with open(DB_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write('\n')
    except Exception as e:
        print(f"Error saving database JSON: {e}", file=sys.stderr)
        sys.exit(1)

def cmd_validate(args):
    db_data = load_db()
    try:
        from jsonschema import validate, ValidationError
        validate(instance=db_data, schema=SCHEMA)
        print("✓ Database structure is valid.")
    except ImportError:
        print("Warning: 'jsonschema' package not installed in the current environment.", file=sys.stderr)
        print("Running lightweight fallback schema verification...", file=sys.stderr)
        # Basic check for existence of root keys
        missing = [k for k in SCHEMA["required"] if k not in db_data]
        if missing:
            print(f"✗ Validation Failed. Missing root keys: {missing}", file=sys.stderr)
            sys.exit(1)
        print("✓ Basic validation passed (jsonschema was not available).")
    except ValidationError as ve:
        print(f"✗ Validation Failed: {ve.message}", file=sys.stderr)
        print(f"Path: {' -> '.join(str(p) for p in ve.absolute_path)}", file=sys.stderr)
        sys.exit(1)

def cmd_summary(args):
    db = load_db()
    c = db["course"]
    inst = db["instructor"]
    textbook = db["materials"]["textbook"]
    
    print("=" * 60)
    print(f"{c['code']}: {c['name']} (Section {c['section']})")
    print(f"Term: {c['term']} | Credits: {c['credit_hours']}")
    print("-" * 60)
    print(f"Instructor: {inst['name']} ({inst['pronouns']})")
    print(f"Email: {inst['email']}")
    print(f"Office: {inst['office_location']} | Hours: {inst['office_hours']}")
    print("-" * 60)
    print("Textbook:")
    print(f"  Title: {textbook.get('title', 'N/A')}")
    if textbook.get('subtitle'):
        print(f"  Subtitle: {textbook['subtitle']}")
    if textbook.get('authors'):
        print(f"  Author(s): {', '.join(textbook['authors'])}")
    print(f"  Link: {textbook['link']}")
    print("-" * 60)
    print("Grading Criteria:")
    for gc in db["policies"]["grading_criteria"]:
        print(f"  - {gc['category']}: {gc['weight']}%")
    print("=" * 60)

def cmd_schedule(args):
    db = load_db()
    print(f"Schedule for {db['course']['code']}")
    print("=" * 75)
    print(f"{'Date/Range':<22} | {'Type':<8} | {'Title / Content Summary':<40}")
    print("-" * 75)
    
    for item in db["schedule"]:
        itype = item["type"].upper()
        if item["type"] == "module":
            date_range = f"{item['start_date']} to {item['end_date']}"
            title = f"Module {item['module_number']}: {item['title']}"
            print(f"{date_range:<22} | {itype:<8} | {title:<40}")
            if args.verbose and item.get("topics"):
                for topic in item["topics"]:
                    print(f"{'':<22} | {'':<8} |   • {topic}")
        elif item["type"] == "exam":
            date_range = f"{item['start_date']} to {item['end_date']}"
            print(f"{date_range:<22} | {itype:<8} | {item['title']} - {item.get('description', '')}")
        else:
            date_val = item.get("date", "N/A")
            print(f"{date_val:<22} | {itype:<8} | {item['title']}")
    print("=" * 75)

def cmd_register_file(args):
    db = load_db()
    
    # Check if file exists physically
    if not os.path.exists(args.file_path):
        print(f"Warning: File '{args.file_path}' not found on disk. Registering anyway.", file=sys.stderr)
        
    filename = os.path.basename(args.file_path)
    
    # Check for duplicate
    for f in db["archived_files"]:
        if f["filename"] == filename or f["path"] == args.file_path:
            if not args.force:
                print(f"Error: File '{filename}' is already registered at path '{f['path']}'.")
                print("Use --force to overwrite the registration metadata.")
                sys.exit(1)
            else:
                db["archived_files"].remove(f)
                break
                
    # Process custom fields
    custom_dict = {}
    if args.custom:
        for cf in args.custom:
            if '=' in cf:
                k, v = cf.split('=', 1)
                custom_dict[k.strip()] = v.strip()
            else:
                print(f"Warning: Custom field '{cf}' ignored. Must be in key=value format.", file=sys.stderr)

    new_file_record = {
        "filename": filename,
        "original_name": args.original_name or filename,
        "path": args.file_path,
        "type": args.type,
        "description": args.description or "",
        "added_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "custom_fields": custom_dict
    }
    if args.module:
        new_file_record["module"] = args.module
        
    db["archived_files"].append(new_file_record)
    save_db(db)
    print(f"✓ Registered file '{filename}' in database.")
    if custom_dict:
        print(f"  Custom fields added: {custom_dict}")

def cmd_update_textbook(args):
    import subprocess
    db = load_db()
    
    sourcing = db.get("materials", {}).get("textbook", {}).get("sourcing", {})
    if not sourcing:
        print("Error: No textbook sourcing configuration found in course_db.json.", file=sys.stderr)
        sys.exit(1)
        
    local_path = sourcing.get("local_path", "textbook/")
    repo_url = sourcing.get("repository", "https://github.com/NicholasSeward/CppBook.git")
    
    abs_local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), local_path)
    
    if os.path.exists(abs_local_path):
        if os.path.exists(os.path.join(abs_local_path, ".git")):
            print(f"Updating local textbook copy at {local_path} from upstream...")
            try:
                res = subprocess.run(["git", "pull"], cwd=abs_local_path, check=True, capture_output=True, text=True)
                print(res.stdout)
                print("✓ Textbook updated successfully.")
            except subprocess.CalledProcessError as cpe:
                print(f"Error running git pull: {cpe.stderr}", file=sys.stderr)
                sys.exit(1)
        else:
            print(f"Error: Directory '{local_path}' exists but is not a Git repository.", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"Local textbook directory '{local_path}' not found. Cloning repository...")
        try:
            res = subprocess.run(["git", "clone", repo_url, abs_local_path], check=True, capture_output=True, text=True)
            print(res.stdout)
            print("✓ Textbook cloned successfully.")
        except subprocess.CalledProcessError as cpe:
            print(f"Error running git clone: {cpe.stderr}", file=sys.stderr)
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="CPSI Course Storage Database Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="Sub-commands")
    
    # Validate command
    subparsers.add_parser("validate", help="Validate course_db.json structure")
    
    # Summary command
    subparsers.add_parser("summary", help="Print course and instructor summary")
    
    # Schedule command
    parser_sched = subparsers.add_parser("schedule", help="Print course schedule calendar")
    parser_sched.add_argument("-v", "--verbose", action="store_true", help="Print module topics")
    
    # Register file command
    parser_reg = subparsers.add_parser("register-file", help="Register an archived file metadata entry")
    parser_reg.add_argument("file_path", help="Relative path to the archived file")
    parser_reg.add_argument("--type", required=True, help="File type (e.g. syllabus, policy, schedule, assignment)")
    parser_reg.add_argument("--original-name", help="Original filename before archiving")
    parser_reg.add_argument("--description", help="Brief description of file contents")
    parser_reg.add_argument("--force", action="store_true", help="Overwrite existing registration")
    parser_reg.add_argument("--module", help="Module or category associated with this file")
    parser_reg.add_argument("--custom", nargs="*", help="Custom fields in key=value format (e.g. module=3 tags=c++)")
    
    # Update textbook command
    subparsers.add_parser("update-textbook", help="Fetch/pull latest updates from the textbook Git repository")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
        
    cmds = {
        "validate": cmd_validate,
        "summary": cmd_summary,
        "schedule": cmd_schedule,
        "register-file": cmd_register_file,
        "update-textbook": cmd_update_textbook
    }
    
    cmds[args.command](args)

if __name__ == "__main__":
    main()
