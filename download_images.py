"""Download all cloud.tsinghua.edu.cn images to static/images/ and generate URL->filename mapping."""
import urllib.request
import json
import os
import re
from pathlib import Path

HEXO_SOURCE = Path(r"F:\hexo\blog\source")
HUGO_IMAGES = Path(r"F:\hugo\static\images")
MAPPING_FILE = HUGO_IMAGES / "image_map.json"

def extract_urls():
    """Extract all cloud.tsinghua.edu.cn URLs from posts and drafts."""
    urls = set()
    for subdir in ['_posts', '_drafts']:
        source_dir = HEXO_SOURCE / subdir
        if not source_dir.exists():
            continue
        for f in source_dir.glob("*.md"):
            content = f.read_text(encoding='utf-8')
            found = re.findall(r'https?://cloud\.tsinghua\.edu\.cn[^\s")]+', content)
            urls.update(found)
    return list(urls)

def download_all(urls):
    """Download all images and generate a URL->filename mapping."""
    import ssl
    # Create unverified SSL context for some CDN setups
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url_to_file = {}
    total = len(urls)

    for i, url in enumerate(urls):
        # Extract file ID from URL /f/FILEID/
        match = re.search(r'/f/([a-zA-Z0-9]+)', url)
        if match:
            file_id = match.group(1)
        else:
            file_id = f"img_{i:03d}"

        # Try to download and determine extension from Content-Type
        filename = f"{file_id}.tmp"
        dest = HUGO_IMAGES / filename

        print(f"[{i+1}/{total}] Downloading {url} -> {file_id}...")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
                content_type = resp.headers.get('Content-Type', '')
                data = resp.read()

                # Determine extension
                ext = '.webp'  # default
                if 'image/jpeg' in content_type or 'image/jpg' in content_type:
                    ext = '.jpg'
                elif 'image/png' in content_type:
                    ext = '.png'
                elif 'image/gif' in content_type:
                    ext = '.gif'
                elif 'image/webp' in content_type:
                    ext = '.webp'
                elif 'image/svg' in content_type:
                    ext = '.svg'

                filename = f"{file_id}{ext}"
                dest = HUGO_IMAGES / filename
                dest.write_bytes(data)
                url_to_file[url] = filename
                print(f"  -> {filename} ({len(data)} bytes)")
        except Exception as e:
            print(f"  FAILED: {e}")
            # Still map it, use .webp as fallback
            url_to_file[url] = f"{file_id}.webp"

    return url_to_file

def main():
    HUGO_IMAGES.mkdir(parents=True, exist_ok=True)

    print("=== Extracting URLs from Hexo source ===")
    urls = extract_urls()
    print(f"Found {len(urls)} unique URLs\n")

    # Filter out already downloaded ones
    new_urls = []
    for url in urls:
        match = re.search(r'/f/([a-zA-Z0-9]+)', url)
        if match:
            file_id = match.group(1)
            existing = list(HUGO_IMAGES.glob(f"{file_id}.*"))
            if not existing:
                new_urls.append(url)
            else:
                print(f"Skipping {file_id} (already exists as {existing[0].name})")

    if new_urls:
        print(f"\n=== Downloading {len(new_urls)} new images ===")
        url_to_file = download_all(new_urls)
    else:
        url_to_file = {}

    # Also build full mapping from existing files + new downloads
    full_map = {}
    for url in urls:
        match = re.search(r'/f/([a-zA-Z0-9]+)', url)
        if match:
            file_id = match.group(1)
            existing = list(HUGO_IMAGES.glob(f"{file_id}.*"))
            if existing:
                full_map[url] = existing[0].name
            elif url in url_to_file:
                full_map[url] = url_to_file[url]

    # Save mapping
    with open(MAPPING_FILE, 'w', encoding='utf-8') as f:
        json.dump(full_map, f, ensure_ascii=False, indent=2)
    print(f"\n=== Mapping saved to {MAPPING_FILE} ({len(full_map)} entries) ===")

if __name__ == "__main__":
    main()
