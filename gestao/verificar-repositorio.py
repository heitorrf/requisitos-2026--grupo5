from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
CAT = json.loads((ROOT / 'gestao/catalogo.json').read_text(encoding='utf-8'))
CASES = CAT['cases']
errors = []
assert len(CASES) == 45 and {c['n'] for c in CASES} == set(range(1,46))
actors = CAT['actors']
vision = (ROOT / 'docs/01-visao-demanda.md').read_text(encoding='utf-8')
srs = (ROOT / 'docs/srs/SRS-UniShare-v1.1.md').read_text(encoding='utf-8')
rules = (ROOT / 'docs/requisitos/regras-de-negocio.md').read_text(encoding='utf-8')
rnf = (ROOT / 'docs/requisitos/requisitos-nao-funcionais.md').read_text(encoding='utf-8')
rf = (ROOT / 'docs/requisitos/requisitos-funcionais.md').read_text(encoding='utf-8')
backlog = (ROOT / 'gestao/backlog.md').read_text(encoding='utf-8')
for c in CASES:
    cdu, f, rid = c['cdu'], c['f'], c['rf']
    assert cdu in vision and f in vision and rid in srs and rid in rf and rid in backlog
    assert all(a in actors for a in c['actors'].split(', '))
    assert all(re.search(r'^### ' + re.escape(x) + r'$', rules, re.M) for x in c['rules'])
    assert all(re.search(r'^\| ' + re.escape(x) + r' \|', rnf, re.M) for x in c['rnf'])
    spec = ROOT / 'docs' / c['path']
    assert spec.is_file() and spec.read_text(encoding='utf-8').startswith('# '+cdu)
    puml = (ROOT / 'diagramas-uml/casos-de-uso' / (c['module']+'.puml')).read_text(encoding='utf-8')
    alias = 'CDU'+cdu[-2:]
    assert re.search(r'usecase "'+re.escape(cdu)+r'\\n', puml)
    associated = set(re.findall(r'^A(\d+) -- '+alias+r'$', puml, re.M))
    assert associated == {str(int(a[3:])) for a in c['actors'].split(', ')}
for md in ROOT.rglob('*.md'):
    data = md.read_text(encoding='utf-8')
    links = re.findall(r'\]\(([^)]+)\)', data)+re.findall(r'src="([^"\s]+)"', data)
    for raw in links:
        target = unquote(raw.split('#',1)[0])
        if not target or target.startswith(('http://','https://','mailto:')):
            continue
        if not (md.parent / target).exists():
            errors.append((str(md.relative_to(ROOT)),raw))
if errors:
    print('Links locais inválidos:',errors)
    sys.exit(1)
print(f'OK: {len(CASES)} CDUs, IDs de atores/RN/RNF, associações PlantUML, RF/SRS/backlog e links locais de Markdown.')
