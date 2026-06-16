"""Convert Hexo posts/drafts to Hugo format with proper frontmatter and image paths."""
import yaml
import json
import re
from pathlib import Path
from datetime import datetime

HEXO_POSTS = Path(r"F:\hexo\blog\source\_posts")
HEXO_DRAFTS = Path(r"F:\hexo\blog\source\_drafts")
HUGO_POSTS = Path(r"F:\hugo\content\posts")
HUGO_IMAGES = Path(r"F:\hugo\static\images")
MAPPING_FILE = HUGO_IMAGES / "image_map.json"

def load_image_map():
    """Load URL->filename mapping from download script output."""
    if MAPPING_FILE.exists():
        with open(MAPPING_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

IMAGE_MAP = load_image_map()

def split_frontmatter(content):
    """Split markdown content into (frontmatter_yaml_string, body)."""
    content = content.strip()
    if not content.startswith('---'):
        return '', content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return parts[1] if len(parts) > 1 else '', parts[-1]
    return parts[1], parts[2]

def format_hugo_date(date_val):
    """Convert Hexo date to Hugo-compatible ISO 8601 string with timezone."""
    if isinstance(date_val, datetime):
        return date_val.strftime('%Y-%m-%dT%H:%M:%S+08:00')
    s = str(date_val).strip()
    if not s:
        return ''
    # Try common formats
    for fmt in ['%Y-%m-%d %H:%M:%S', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d']:
        try:
            dt = datetime.strptime(s, fmt)
            return dt.strftime('%Y-%m-%dT%H:%M:%S+08:00')
        except ValueError:
            continue
    # If already ISO-like, just return it
    return s

def map_cover_url(url):
    """Convert a remote cover URL to a local /images/ path."""
    url = url.strip()
    if url in IMAGE_MAP:
        return f"/images/{IMAGE_MAP[url]}"
    # Try matching by file ID
    match = re.search(r'/f/([a-zA-Z0-9]+)', url)
    if match:
        file_id = match.group(1)
        # Search for existing file with this ID prefix
        for f in HUGO_IMAGES.glob(f"{file_id}.*"):
            return f"/images/{f.name}"
    return url  # fallback: keep original URL

def replace_body_images(body):
    """Replace all cloud.tsinghua.edu.cn image URLs in markdown body with local paths."""
    for url, filename in IMAGE_MAP.items():
        body = body.replace(url, f"/images/{filename}")
    return body

def to_list(val):
    """Ensure value is a list, handling string/none cases."""
    if val is None:
        return None
    if isinstance(val, list):
        cleaned = [v for v in val if v]
        return cleaned if cleaned else None
    if isinstance(val, str):
        s = val.strip()
        if not s:
            return None
        # Handle comma-separated
        return [x.strip() for x in s.split(',') if x.strip()]
    return None

def convert_frontmatter(yaml_text, is_draft=False, source_file=None):
    """Convert Hexo frontmatter to Hugo/Ananke format."""
    try:
        data = yaml.safe_load(yaml_text) or {}
    except yaml.YAMLError:
        print(f"    WARNING: YAML parse error, using empty frontmatter")
        data = {}

    hugo = {}

    # title
    if 'title' in data and data['title']:
        hugo['title'] = str(data['title']).strip()

    # date
    if 'date' in data and data['date']:
        d = format_hugo_date(data['date'])
        if d:
            hugo['date'] = d
    elif is_draft:
        if source_file:
            mtime = source_file.stat().st_mtime
            dt = datetime.fromtimestamp(mtime)
        else:
            dt = datetime.now()
        hugo['date'] = dt.strftime('%Y-%m-%dT%H:%M:%S+08:00')

    # lastmod (from Hexo 'updated')
    if 'updated' in data and data['updated']:
        d = format_hugo_date(data['updated'])
        if d:
            hugo['lastmod'] = d

    # description
    if 'description' in data and data['description']:
        hugo['description'] = str(data['description']).strip()

    # tags -> always a list
    tags = to_list(data.get('tags'))
    if tags:
        hugo['tags'] = tags

    # categories -> always a list
    cats = to_list(data.get('categories'))
    if cats:
        hugo['categories'] = cats

    # cover -> featured_image (Ananke convention)
    if 'cover' in data and data['cover']:
        cover = str(data['cover']).strip()
        local = map_cover_url(cover)
        hugo['featured_image'] = local

    # draft flag
    if is_draft:
        hugo['draft'] = True

    return hugo

def write_hugo_post(slug, frontmatter, body):
    """Write a Hugo-compatible markdown file."""
    # Clean slug for filesystem safety while preserving readability
    safe_name = slug.replace('\\', '-').replace('/', '-').replace(':', ' -')
    filepath = HUGO_POSTS / f"{safe_name}.md"

    # Serialize frontmatter as YAML
    fm_yaml = yaml.dump(
        frontmatter,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=1000
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("---\n")
        f.write(fm_yaml)
        f.write("---\n")
        f.write(body)

    return filepath

def process_posts():
    """Process all published posts."""
    print("=== Processing Published Posts ===")
    posts = sorted(HEXO_POSTS.glob("*.md"))
    for i, f in enumerate(posts, 1):
        print(f"[{i}/{len(posts)}] {f.name}")
        content = f.read_text(encoding='utf-8')
        fm_yaml, body = split_frontmatter(content)

        if not fm_yaml.strip():
            print(f"  WARNING: No frontmatter, creating minimal")
            hugo_fm = {'title': f.stem}
        else:
            hugo_fm = convert_frontmatter(fm_yaml, is_draft=False, source_file=f)

        body = replace_body_images(body)
        out = write_hugo_post(f.stem, hugo_fm, body)
        status = "DRAFT" if hugo_fm.get('draft') else "OK"
        cats = hugo_fm.get('categories', [])
        print(f"  -> {out.name} [{status}] cats={cats}")

def process_drafts():
    """Process all drafts."""
    print("\n=== Processing Drafts ===")
    if not HEXO_DRAFTS.exists():
        print("No drafts directory found, skipping.")
        return
    drafts = sorted(HEXO_DRAFTS.glob("*.md"))
    for i, f in enumerate(drafts, 1):
        print(f"[{i}/{len(drafts)}] {f.name}")
        content = f.read_text(encoding='utf-8')
        fm_yaml, body = split_frontmatter(content)

        if not fm_yaml.strip():
            hugo_fm = {
                'title': f.stem,
                'draft': True,
                'date': datetime.fromtimestamp(f.stat().st_mtime).strftime('%Y-%m-%dT%H:%M:%S+08:00')
            }
        else:
            hugo_fm = convert_frontmatter(fm_yaml, is_draft=True, source_file=f)

        body = replace_body_images(body)
        out = write_hugo_post(f.stem, hugo_fm, body)
        print(f"  -> {out.name} [DRAFT]")

def main():
    HUGO_POSTS.mkdir(parents=True, exist_ok=True)

    process_posts()
    process_drafts()

    post_count = len(list(HUGO_POSTS.glob("*.md")))
    print(f"\n=== Done! {post_count} files written to {HUGO_POSTS} ===")

if __name__ == "__main__":
    main()
