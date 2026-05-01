import re

with open('dummy.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Issue 1: Remove invalid @import
content = content.replace('@import url("https://www.genspark.ai/image_placeholder.png");', '')

# Issue 2: Fix overflow: hidden on body
content = re.sub(r'(body\s*\{[^}]*?)overflow:\s*hidden;', r'\1overflow-y: auto; overflow-x: hidden;', content)

# Issue 3: Fix duplicate ID 'trendChart'
# The first one is around Data Description. The second one is around Visualizing the Data.
# We will find the second occurrence and rename it to 'trendChart2'.

# Find all occurrences of 'trendChart'
parts = content.split('trendChart')
if len(parts) > 3: # means it appears at least 2 times (canvas + js for each)
    # the string "trendChart" appears in canvas id and in getElementById
    # The first 2 occurrences (canvas and script) belong to the first chart.
    # The 3rd and 4th belong to the second chart.
    # We will replace the 3rd and 4th occurrences with 'trendChart2'.
    
    new_content = parts[0] + 'trendChart' + parts[1] + 'trendChart' + parts[2] + 'trendChart2' + parts[3] + 'trendChart2' + parts[4]
    
    # If there are more parts, just append them as is
    for i in range(5, len(parts)):
        new_content += 'trendChart' + parts[i]
        
    content = new_content

with open('dummy.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed 3 issues successfully.")
