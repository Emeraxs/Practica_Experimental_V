# CHANGELOG - FabroGym PE5

## v2.0.3 - 2026-08-20 - cierre de modelos y evidencia M6

- Se incorporan DFD Nivel 0 y Nivel 1 derivados de los procesos P-01 a P-15 de la matriz final.
- Se incorporan cuatro máquinas de estados: Membresía, Pago, Novedad y Rutina.
- Se incorporan tres secuencias conceptuales representativas: autenticación, pago y venta.
- Se añade `04_Auditoria_Metricas/Registro_Reinspeccion_M6.md`, un script reproducible y su resultado, con SHA-256 de la ERS inspeccionada.
- Se añade la hoja `Reinspeccion M6` al libro Excel y se refuerza la trazabilidad de la evidencia de M6.
- No se modifican los 40 RF, 27 RNF, 40 CU ni los valores finales M1--M6; los cambios son de cierre documental y modelado.
- La presentación permanece como entregable separado.

## v2.0.2 - 2026-08-20 - alineación final con Equipo F

- Se sustituyó la conformación temporal de tres estudiantes por el Equipo F original del PFC FabroGym: Alvia, Mera, Mora, Ponce y Vaca.
- Se eliminó la narrativa de “proyecto base seleccionado” y se presenta FabroGym directamente como PFC del equipo vigente.
- Se actualizó la URL de entrega a `https://github.com/Emeraxs/Practica_Experimental_v`.
- Se actualizó la distribución de aportes y la retrospectiva para cinco integrantes, sin atribuir commits inexistentes.
- Se reorganizó el paquete conforme a la estructura del repositorio PE5 (`03_Matriz_Trazabilidad` y `04_Auditoria_Metricas`).
- Se retiró la imagen desactualizada del equipo y se excluyeron del paquete público las transcripciones y evidencias con datos identificables.
- Se actualizó Pohl a la 2.a edición de 2025 e IREB CPRE FL a la versión 3.3.0 de 2026, conforme a la Guía PE5.
- La parte técnica de requisitos, métricas, trazabilidad e IA se conserva sin cambios sustantivos.

## v2.0.1 - 2026-08-18 - saneamiento final PE5

- Se corrigieron 21 defectos residuales de redacción en RF.
- Se sustituyeron los BDD genéricos de los 40 RF por criterios con resultados observables.
- Se especificaron textualmente los 40 casos de uso.
- M1 se desglosó en M1a, M1b y M1c.
- M6 se corrigió para medir defectos residuales de re-inspección, no actividades pendientes.
- Se cerraron documentalmente las ocho discrepancias y se separaron de las limitaciones de implementación.
- Se añadió control explícito de huérfanos y cadenas rotas.
- Se reforzó la base de legitimación y los controles de privacidad para IA.
- Se actualizaron referencias y citas obligatorias.
- Se corrigió el README para compilación reproducible con `-jobname`.

## v2.0.0 - 2026-08-17

- Integración inicial PE5 sobre FabroGym.
