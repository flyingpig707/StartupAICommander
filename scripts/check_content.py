"""Check manuscript links, chapter status and common scenario disclosures."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
book = root / 'book'
errors = []
files = sorted(book.glob('*.md'))
for path in files:
    text = path.read_text()
    if '\ufffd' in text:
        errors.append(f'{path.name}: replacement character')
    for target in re.findall(r'\]\((\./[^)#]+)(?:#[^)]*)?\)', text):
        dest = path.parent / target
        if not dest.exists() and not dest.with_suffix('.md').exists():
            errors.append(f'{path.name}: broken link {target}')
for filename in ('02-project.md', '06-agent.md', '17-sales.md'):
    text = (book / filename).read_text()
    if any(term not in text for term in ('教学演练','示例培训机构','课程咨询资料整理服务')):
        errors.append(f'{filename}: missing scenario or disclosure')
    count = len(re.findall(r'[\u4e00-\u9fff]', text))
    print(f'{filename}: {count} Han characters / {len(text)} total chars')
contents = (book / 'contents.md').read_text()
if len(re.findall(r'^\d+\. ', contents, re.M)) != 24:
    errors.append('contents.md: expected 24 planned chapters')
if '三章样章' not in contents or '规划中' not in contents:
    errors.append('contents.md: missing progress disclosure')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'OK: {len(files)} Markdown pages; local links and scenario checks passed')
