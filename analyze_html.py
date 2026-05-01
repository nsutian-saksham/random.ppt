import re

with open('dummy.html', 'r', encoding='utf-8') as f:
    content = f.read()

html_tags = re.findall(r'<html[^>]*>', content, re.IGNORECASE)
print(f"Number of <html> tags: {len(html_tags)}")

canvas_ids = re.findall(r'<canvas[^>]*id="([^"]+)"', content, re.IGNORECASE)
print("Canvas IDs found:")
for cid in canvas_ids:
    print(cid)
