# Registro reproducible de re-inspección documental M6

## Propósito
Este artefacto documenta el control de cierre usado para sustentar **M6 - Corrección** en la PE5. La guía define M6 como defectos encontrados después de la inspección dividido para el total de requisitos. El paquete conserva el conteo histórico de **21 defectos editoriales** detectados durante la primera revisión del material de trabajo; el control final comprueba que esos defectos no permanecen en la versión saneada.

## Versión y alcance
- Fecha del control: **2026-08-20**.
- Versión documental: **PE5 v2.0.3**.
- Línea base funcional de requisitos: **v2.0**.
- Universo: **40 RF + 27 RNF = 67 requisitos**.
- Alcance: defectos editoriales/estructurales que afectaban la corrección documental (formas verbales defectuosas, conteos de catálogo y presencia de BDD).
- Fuera de alcance: ejecución de backend, restauración, modelos IA y walkthrough no técnico. Estas condiciones continúan tratándose como limitaciones de implementación/validación y no se convierten artificialmente en defectos M6.

## Método reproducible
Ejecutar desde la raíz del repositorio:

```bash
python3 04_Auditoria_Metricas/reinspeccion_m6.py
```

El script:
1. cuenta los 40 RF y 27 RNF desde los catálogos LaTeX;
2. verifica que cada requisito conserve su criterio BDD;
3. busca los patrones editoriales que motivaron el saneamiento inicial;
4. calcula M6 sobre la versión entregada; y
5. registra el SHA-256 de la ERS inspeccionada.

El resultado se guarda en `04_Auditoria_Metricas/resultado_reinspeccion_m6.txt`.

## Interpretación
Un resultado `M6 = 0/67 = 0,000` significa únicamente que **no quedaron defectos residuales dentro de los controles documentales definidos para esta re-inspección**. No declara que todo el sistema haya sido implementado o validado empíricamente.
