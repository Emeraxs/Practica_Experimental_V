from pathlib import Path
import hashlib, re

ROOT = Path(__file__).resolve().parents[1]
rf = ROOT / '_generados' / 'catalogo_rf.tex'
rnf = ROOT / '_generados' / 'catalogo_rnf.tex'
ers = ROOT / '02_ERS_Final' / 'ERS_FabroGym_v2.0.3.tex'

rf_text = rf.read_text(encoding='utf-8')
rnf_text = rnf.read_text(encoding='utf-8')
ers_text = ers.read_text(encoding='utf-8')

rf_count = rf_text.count('\\begin{reqbox}')
rnf_count = rnf_text.count('\\begin{reqbox}')
rf_bdd = rf_text.count('Criterio BDD:')
rnf_bdd = rnf_text.count('Criterio BDD:')

# Patrones de los defectos editoriales que motivaron el saneamiento inicial.
patterns = [
    r'\\bpermitira\\b', r'\\bregistrara\\b', r'\\bbuscara\\b',
    r'\\bactualizara\\b', r'\\breactivara\\b', r'\\badministrara\\b',
    r'\\bactivara\\b', r'\\brenovara\\b', r'\\blistara\\b',
    r'\\bcalculara\\b', r'\\bcreara\\b', r'\\bmostrara\\b',
]
combined = rf_text + '\n' + rnf_text + '\n' + ers_text
hits = []
for p in patterns:
    for m in re.finditer(p, combined, flags=re.IGNORECASE):
        hits.append((p, m.group(0)))

structural = []
if rf_count != 40: structural.append(f'RF esperados=40, encontrados={rf_count}')
if rnf_count != 27: structural.append(f'RNF esperados=27, encontrados={rnf_count}')
if rf_bdd != rf_count: structural.append(f'BDD RF={rf_bdd}/{rf_count}')
if rnf_bdd != rnf_count: structural.append(f'BDD RNF={rnf_bdd}/{rnf_count}')

def sha256(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

residual = len(hits) + len(structural)
total = rf_count + rnf_count
m6 = residual / total if total else 1

lines = [
    'REINSPECCION DOCUMENTAL M6 - FABROGYM PE5',
    'Fecha de ejecución: 2026-08-20',
    'Versión documental inspeccionada: PE5 v2.0.3 / línea base funcional v2.0',
    f'ERS SHA-256: {sha256(ers)}',
    f'RF inspeccionados: {rf_count}',
    f'RNF inspeccionados: {rnf_count}',
    f'Requisitos totales: {total}',
    f'RF con BDD: {rf_bdd}/{rf_count}',
    f'RNF con BDD: {rnf_bdd}/{rnf_count}',
    f'Defectos residuales encontrados por los controles definidos: {residual}',
    f'M6 = {residual}/{total} = {m6:.3f}',
    '',
    'Alcance del control: re-inspección documental de defectos editoriales/estructurales del ERS saneado.',
    'No equivale a prueba funcional, validación de backend, ejecución de IA ni walkthrough no técnico.',
]
if hits:
    lines.append('Patrones residuales: ' + '; '.join(x[1] for x in hits))
if structural:
    lines.append('Incidencias estructurales: ' + '; '.join(structural))

out = ROOT / '04_Auditoria_Metricas' / 'resultado_reinspeccion_m6.txt'
out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('\n'.join(lines))
