# PE5 FabroGym - Castro / Mera / Sánchez

## Contexto de la actividad

FabroGym se utiliza **como proyecto base seleccionado para la PE5 de aula**. El equipo ejecutor de esta práctica está conformado temporalmente por:

- Castro Bajaña Ariel Omar
- Mera Arias Erick Jhair
- Sánchez Centeno Roselyn Andreina

Esta conformación corresponde únicamente a la actividad PE5 y **no modifica la autoría ni la composición del proyecto FabroGym original**.

**Commit de referencia del proyecto base:** `f7c9524023ef3156026b4dd1fe82f0b85cd62b22` (17-08-2026). Se cita únicamente como punto de referencia del proyecto seleccionado; no se atribuye a los tres integrantes de la PE5.

## Entregables incluidos

- `01_Informe_Final/`: informe PE5 en LaTeX y PDF.
- `02_ERS_Final/`: ERS/SRS v2.0 saneada en LaTeX y PDF.
- `03_Matrices/`: matriz Excel con requisitos, trazabilidad, métricas, control de huérfanos, backlog, hallazgos y aportes.
- `04_Validacion/`: evidencia de validación técnica y protocolo no técnico.
- `05_Gestion/`: retrospectiva, aportes, declaración de uso de IA y checklist.
- `06_Anexos/`: línea base anterior y modelos previos.
- `assets/` y `diagramas_fuente/`: recursos gráficos y fuentes de diagramas.
- `MANIFIESTO_SHA256.txt`: huellas de integridad del paquete.

La presentación de 15-20 diapositivas **no se incluye en este ZIP** porque se prepara como entregable separado por distribución interna del equipo.

## Compilación reproducible

### Requisitos
- TeX Live con `pdflatex`.
- Paquetes LaTeX utilizados por `_generados/preamble.tex`.

### ERS/SRS final

Desde la raíz del paquete:

```bash
cd 02_ERS_Final
pdflatex -interaction=nonstopmode ERS_FabroGym_v2.0.1.tex
pdflatex -interaction=nonstopmode ERS_FabroGym_v2.0.1.tex
```

Salida:

`02_ERS_Final/ERS_FabroGym_v2.0.1.pdf`

### Informe PE5

```bash
cd ../01_Informe_Final
pdflatex -interaction=nonstopmode -jobname=PE5_U5_PFC_Final_CASTRO_MERA_SANCHEZ main.tex
pdflatex -interaction=nonstopmode -jobname=PE5_U5_PFC_Final_CASTRO_MERA_SANCHEZ main.tex
```

Salida:

`01_Informe_Final/PE5_U5_PFC_Final_CASTRO_MERA_SANCHEZ.pdf`

## Criterio de evidencia

- El prototipo V7 es HTML/JavaScript y no se presenta como backend implementado.
- Los componentes IA-01 e IA-02 están especificados y trazados, pero no se presentan como implementados.
- Respaldo/restauración permanecen como requisitos de arquitectura objetivo.
- Los walkthroughs no técnicos no se presentan como sesiones ejecutadas; solo se incluye el protocolo preparado.
- Las limitaciones de implementación no se contabilizan como defectos residuales de M6.
- No se atribuyen commits del repositorio FabroGym a los tres integrantes de esta actividad temporal.

## Estado del saneamiento

- M1 desglosada en M1a, M1b y M1c.
- M2 con cero conflictos de requisitos abiertos al cierre.
- M3 re-auditada con BDD observables para los 40 RF.
- M4 adelante y atrás calculadas por separado.
- M6 corregida como tasa de defectos residuales de re-inspección.
- 21 defectos de redacción en RF corregidos.
- 40/40 casos de uso especificados.
- 0 requisitos huérfanos y 0 cadenas rotas al cierre.
- Base de legitimación y controles de privacidad de IA explicitados.
- Referencias obligatorias incorporadas y citadas.
