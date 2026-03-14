import sys, re
import os

files = ["index.html", "rules.html", "store.html", "story.html", "support.html", "jobs.html"]
directory = r"f:\GBRP\ROUNDANTIG"

for f_name in files:
    fp = os.path.join(directory, f_name)
    with open(fp, 'r', encoding='utf-8') as file:
        content = file.read()
    
    pattern = re.compile(r'(\s*<!-- Mobile Menu Overlay -->\s*<div id="mobile-menu".*?</div>)\s*</header>', re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub(r'\n    </header>\n\1', content)
        with open(fp, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f_name}")
    else:
        print(f"Pattern not found in {f_name}")
