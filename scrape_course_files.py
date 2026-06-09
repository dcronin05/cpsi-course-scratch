#!/usr/bin/env python3
import os
import re
import ssl
import json
import shutil
import urllib.request
import subprocess
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi

WORKSPACE_PATH = "/Users/dcronin05/app_development/cpsi-27603-notes"
MODULE_PATH = os.path.join(WORKSPACE_PATH, "raw/module-01")

LECTURE_HTML = os.path.join(MODULE_PATH, "lecture_videos.html")
PARTICIPATION_HTML = os.path.join(MODULE_PATH, "participation01.html")
QUIZ_MD = os.path.join(MODULE_PATH, "quiz01.md")

def get_video_title(video_id):
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            data = json.loads(response.read().decode())
            return data.get("title", f"video_{video_id}")
    except Exception as e:
        print(f"Warning: Could not fetch title for {video_id}: {e}")
        return f"video_{video_id}"

def extract_youtube_id(url):
    if not url:
        return None
    if 'youtube.com/embed/' in url:
        match = re.search(r'youtube\.com/embed/([a-zA-Z0-9_-]{11})', url)
        if match:
            return match.group(1)
    elif 'youtube.com/watch' in url:
        match = re.search(r'v=([a-zA-Z0-9_-]{11})', url)
        if match:
            return match.group(1)
    elif 'youtu.be/' in url:
        match = re.search(r'youtu\.be/([a-zA-Z0-9_-]{11})', url)
        if match:
            return match.group(1)
    # Fallback search anywhere for 11 chars
    match = re.search(r'([a-zA-Z0-9_-]{11})', url)
    if match:
        return match.group(1)
    return None

def download_transcript(video_id, title):
    print(f"Downloading transcript for video: '{title}' ({video_id})...")
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        lines = []
        for entry in transcript_list:
            start = int(entry['start'])
            minutes = start // 60
            seconds = start % 60
            timestamp = f"[{minutes:02d}:{seconds:02d}]"
            text = entry['text'].replace('\n', ' ')
            lines.append(f"{timestamp} {text}")
        content = f"# Transcript: {title}\n\n" + "\n".join(lines) + "\n"
        print(f"✓ Successfully retrieved transcript ({len(lines)} lines).")
        return content
    except Exception as e:
        print(f"✗ Failed to download transcript for {video_id}: {e}")
        # Return fallback content
        return f"# Transcript: {title}\n\nTranscript not available: {e}\n"

def html_to_markdown(elem):
    if elem is None:
        return ""
    if isinstance(elem, str):
        # Escape markdown characters where appropriate, but generally keep clean
        return elem
    
    tag = elem.name
    if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        level = int(tag[1])
        text = "".join(html_to_markdown(child) for child in elem.children).strip()
        return f"\n\n{'#' * level} {text}\n\n"
    elif tag == 'p':
        # If it has a video/iframe, handle inside div or let it flow
        text = "".join(html_to_markdown(child) for child in elem.children)
        if text.strip() == "":
            return ""
        return f"\n\n{text.strip()}\n\n"
    elif tag == 'br':
        return "\n"
    elif tag in ['strong', 'b']:
        text = "".join(html_to_markdown(child) for child in elem.children)
        return f"**{text}**"
    elif tag in ['em', 'i']:
        text = "".join(html_to_markdown(child) for child in elem.children)
        return f"*{text}*"
    elif tag == 'a':
        text = "".join(html_to_markdown(child) for child in elem.children).strip()
        href = elem.get('href', '')
        if not text:
            text = href
        return f"[{text}]({href})"
    elif tag == 'ul':
        items = []
        for child in elem.children:
            if child.name == 'li':
                items.append(f"- {html_to_markdown(child).strip()}")
        return "\n" + "\n".join(items) + "\n"
    elif tag == 'ol':
        items = []
        idx = 1
        for child in elem.children:
            if child.name == 'li':
                items.append(f"{idx}. {html_to_markdown(child).strip()}")
                idx += 1
        return "\n" + "\n".join(items) + "\n"
    elif tag == 'li':
        return "".join(html_to_markdown(child) for child in elem.children)
    elif tag == 'pre':
        code = elem.get_text()
        return f"\n\n```cpp\n{code}\n```\n\n"
    elif tag == 'div':
        # Check if it's a video
        if elem.get('data-bbtype') == 'video' or 'bb-video' in elem.get('class', []):
            video_info = elem.get('data-bbfile', '')
            video_url = ""
            if video_info:
                try:
                    info = json.loads(video_info)
                    video_url = info.get('src', '')
                except Exception:
                    pass
            if not video_url:
                iframe = elem.find('iframe')
                if iframe:
                    video_url = iframe.get('src', '')
                    if not video_url:
                        video_url = iframe.get('title', '')
            if video_url:
                video_id = extract_youtube_id(video_url)
                if video_id:
                    title = get_video_title(video_id)
                    watch_url = f"https://youtube.com/watch?v={video_id}"
                    return f"\n\n[Video: {title}]({watch_url})\n\n"
        return "".join(html_to_markdown(child) for child in elem.children)
    else:
        return "".join(html_to_markdown(child) for child in elem.children)

def clean_markdown_whitespace(md):
    # Normalize excessive newlines
    md = re.sub(r'\n{3,}', '\n\n', md)
    # Strip whitespace at start/end of lines
    lines = [line.rstrip() for line in md.split('\n')]
    return '\n'.join(lines).strip() + '\n'

def scrape_lecture_videos():
    print(f"Parsing {LECTURE_HTML}...")
    with open(LECTURE_HTML, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Target container for lecture content
    editor_container = soup.find('div', class_='ql-editor')
    if not editor_container:
        print("Warning: Could not find editor container in lecture_videos.html. Falling back to body.")
        editor_container = soup.body
        
    markdown_content = html_to_markdown(editor_container)
    markdown_content = clean_markdown_whitespace(markdown_content)
    
    # Prepend title
    markdown_content = f"# Module 1 Lecture Videos\n\n" + markdown_content
    
    out_path = os.path.join(MODULE_PATH, "lecture_videos.md")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    print(f"✓ Saved cleaned lecture videos content to {out_path}")
    return out_path

def scrape_participation01():
    print(f"Parsing {PARTICIPATION_HTML}...")
    with open(PARTICIPATION_HTML, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Target assignment instructions container
    # The container class is makeStylesinstructionsWrapper-0-2-5603 or the ql-editor under it
    editor_container = soup.find('div', id='bb-editorassignment-attempt-authoring-instructions')
    if not editor_container:
        editor_container = soup.find('div', class_='ql-editor')
    if not editor_container:
        print("Warning: Could not find instructions container in participation01.html. Falling back to body.")
        editor_container = soup.body
        
    markdown_content = html_to_markdown(editor_container)
    markdown_content = clean_markdown_whitespace(markdown_content)
    
    # Save as practice01_instructions.md
    out_path = os.path.join(MODULE_PATH, "practice01_instructions.md")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    print(f"✓ Saved cleaned practice instructions to {out_path}")
    return out_path

def scrape_and_download_transcripts():
    # Find all unique YouTube links in both HTML files
    video_ids = set()
    
    for html_file in [LECTURE_HTML, PARTICIPATION_HTML]:
        if not os.path.exists(html_file):
            continue
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Regex search
        for match in re.findall(r'youtube\.com/embed/([a-zA-Z0-9_-]{11})', content):
            video_ids.add(match)
        for match in re.findall(r'youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})', content):
            video_ids.add(match)
        for match in re.findall(r'youtu\.be/([a-zA-Z0-9_-]{11})', content):
            video_ids.add(match)
            
    print(f"Found unique YouTube video IDs: {list(video_ids)}")
    
    transcript_files = []
    for vid in sorted(video_ids):
        title = get_video_title(vid)
        # Sanitize title for filename
        sanitized = re.sub(r'[^a-zA-Z0-9\s-]', '', title).strip().lower()
        sanitized = re.sub(r'[\s-]+', '-', sanitized)
        # Avoid extremely long filenames
        sanitized = sanitized[:60].strip('-')
        filename = f"{sanitized}_transcript.md"
        
        filepath = os.path.join(MODULE_PATH, filename)
        
        transcript_content = download_transcript(vid, title)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(transcript_content)
            
        print(f"✓ Saved transcript to {filepath}")
        transcript_files.append((filepath, title))
        
    return transcript_files

def register_file_in_db(filepath, file_type, description):
    # Get relative path from workspace root
    rel_path = os.path.relpath(filepath, WORKSPACE_PATH)
    print(f"Registering {rel_path} in database as type '{file_type}'...")
    
    cmd = [
        ".venv/bin/python",
        os.path.join(WORKSPACE_PATH, "manage_db.py"),
        "register-file",
        rel_path,
        "--type", file_type,
        "--description", description,
        "--module", "module-01",
        "--force"
    ]
    
    res = subprocess.run(cmd, check=True, capture_output=True, text=True)
    print(res.stdout.strip())

def cleanup_source_files():
    print("Cleaning up original HTML pages and folders...")
    for path in [LECTURE_HTML, PARTICIPATION_HTML]:
        if os.path.exists(path):
            os.remove(path)
            print(f"Deleted file: {path}")
            
    # Clean up associated folders
    for folder_name in ["lecture_videos_files", "participation01_files"]:
        folder_path = os.path.join(MODULE_PATH, folder_name)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print(f"Deleted directory: {folder_path}")

def main():
    print("Starting Blackboard scraper and ingestion script...")
    
    # 1. Scrape HTML pages to Markdown
    lecture_md = scrape_lecture_videos()
    practice_md = scrape_participation01()
    
    # 2. Download Transcripts
    transcripts = scrape_and_download_transcripts()
    
    # 3. Register New Files in Database
    register_file_in_db(lecture_md, "lecture", "Module 01 Lecture Videos and Slide Links")
    register_file_in_db(practice_md, "assignment", "Practice 01: Menu Application Assignment Instructions")
    
    # Register transcripts
    for filepath, title in transcripts:
        register_file_in_db(filepath, "transcript", f"Transcript for video: {title}")
        
    # Also register the quiz01.md file which was added but not registered
    if os.path.exists(QUIZ_MD):
        register_file_in_db(QUIZ_MD, "assignment", "Module 01 Quiz 01 details")
    else:
        print(f"Warning: {QUIZ_MD} not found, skipping registration.")
        
    # 4. Clean up original files
    cleanup_source_files()
    
    print("\nIngestion and scraping process finished successfully!")

if __name__ == "__main__":
    main()
