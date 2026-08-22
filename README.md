# PE5 FabroGym - Equipo F

## Identificación

**Asignatura:** Ingeniería de Requerimientos (ISR-401)  
**Actividad:** Práctica Experimental PE5 - Integración, métricas y defensa del Proyecto Integrador  
**PFC:** FabroGym  
**Repositorio de la actividad:** https://github.com/Emeraxs/Practica_Experimental_V.git

## Integrantes

- Alvia Villegas Erick Adalberto
- Mera Arias Erick Jhair
- Mora Duarte Alex José
- Ponce Rivera Mery Helenmey
- Vaca Romero David Octavio

## Entregables incluidos

- `01_Informe_Final/`: informe PE5 en LaTeX y PDF.
- `02_ERS_Final/`: ERS/SRS final v2.0.3 en LaTeX y PDF.
- `03_Matriz_Trazabilidad/`: libro Excel con requisitos, trazabilidad, métricas, backlog, hallazgos, retrospectiva y aportes.
- `03_Matriz_Trazabilidad/Jira/`: CSV de importación y exportación de FabroGym, configuración reutilizable del importador, capturas, README y registro de importación.
- `04_Auditoria_Metricas/`: guía de auditoría y ubicación de los conteos verificables.
- `05_Gestion/`: backlog, retrospectiva, aportes, declaración de uso de IA y documentación de validación no identificable.
- `_generados/`: fragmentos LaTeX cargados por el informe y la ERS.
- `assets/`: figuras empleadas en los documentos.
- `diagramas_fuente/`: fuentes LaTeX de los diagramas.

La presentación de defensa se gestiona como entregable separado.

## Modelos incorporados para cierre PE5

La versión 2.0.3 incorpora DFD Nivel 0/Nivel 1, cuatro máquinas de estados y tres secuencias conceptuales representativas. Sus fuentes están en `diagramas_fuente/` y sus PDF en `assets/`. Los modelos derivan de la ERS y la matriz final y no se presentan como evidencia de backend implementado.

## Compilación reproducible

### Requisitos

- TeX Live o MiKTeX actualizado.
- `pdflatex` disponible en la terminal.
- Los paquetes requeridos se declaran en `_generados/preamble.tex`.

### ERS/SRS final

Desde la raíz del repositorio:

```bash
cd 02_ERS_Final
pdflatex -interaction=nonstopmode ERS_FabroGym_v2.0.3.tex
pdflatex -interaction=nonstopmode ERS_FabroGym_v2.0.3.tex
```

Salida esperada:

`02_ERS_Final/ERS_FabroGym_v2.0.3.pdf`

### Informe PE5

Desde la raíz del repositorio:

```bash
cd 01_Informe_Final
pdflatex -interaction=nonstopmode -jobname=PE5_U5_PFC_Final_ALVIA_MERA_MORA_PONCE_VACA informe_main.tex
pdflatex -interaction=nonstopmode -jobname=PE5_U5_PFC_Final_ALVIA_MERA_MORA_PONCE_VACA informe_main.tex
```

Salida esperada:

`01_Informe_Final/PE5_U5_PFC_Final_ALVIA_MERA_MORA_PONCE_VACA.pdf`

## Estado técnico de la línea base

- M1 se reporta como M1a, M1b y M1c.
- M2 cierra sin conflictos de requisitos abiertos.
- M3 usa criterios BDD comprobables para los 40 RF.
- M4 se calcula hacia adelante y hacia atrás por separado.
- M5 se calcula sobre una muestra representativa de cinco requisitos.
- M6 se interpreta como tasa de defectos residuales de re-inspección.
- Se documentan 40 RF, 27 RNF y 40 casos de uso especificados.
- La matriz final reporta 0 requisitos huérfanos y 0 cadenas rotas al cierre.
- IA-01 e IA-02 están especificados y trazados; no se presentan como implementados.
- V7 es un prototipo HTML/JavaScript y no se presenta como backend productivo.
- Los walkthroughs no técnicos siguen declarados como actividad no ejecutada.

## Evidencia Git y línea base final

La evidencia individual se determina con los commits reales, archivos modificados y fechas del historial.

Cuando todos los artefactos estén cargados y verificados mediante una clonación limpia, el equipo debe congelar la línea base con una etiqueta Git:

```bash
git tag -a pe5-final-v2.0.3 -m "Línea base final PE5 FabroGym"
git push origin pe5-final-v2.0.3
```

## Uso responsable de IA

La declaración completa, desglosada por secciones, está en `05_Gestion/Declaracion_Uso_IA.md` y en el Anexo E del informe.
