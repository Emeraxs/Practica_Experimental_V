# Fuentes de diagramas PE5 v2.0.3

Esta carpeta contiene las fuentes reproducibles de los modelos incorporados para cerrar la perspectiva funcional y de comportamiento de la PE5.

## Modelos agregados en v2.0.3
- `DFD_N0_FabroGym.dot`: DFD de contexto.
- `DFD_N1_FabroGym.dot`: DFD de nivel 1, alineado con los procesos P-01 a P-15 de la matriz.
- `DE_01_Membresia_v2_0_3.dot` a `DE_04_Rutina_v2_0_3.dot`: máquinas de estados para entidades con ciclo de vida relevante.
- `DS_01_RF-AUT-01_v2_0_3.tex`, `DS_10_RF-PAG-01_v2_0_3.tex` y `DS_15_RF-VEN-01_v2_0_3.tex`: secuencias conceptuales representativas.

Los modelos se regeneraron desde la ERS funcional v2.0, sus BDD y la matriz de trazabilidad. No constituyen evidencia de ejecución de backend. Los DFD y statecharts se compilan con Graphviz (`dot -Tpdf`) y las secuencias con `pdflatex`.
