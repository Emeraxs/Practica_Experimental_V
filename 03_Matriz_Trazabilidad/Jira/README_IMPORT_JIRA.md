# Importación del backlog FabroGym a Jira

Archivo principal: `backlog_import_jira.csv`

## Contenido

- 15 épicas reales derivadas de los módulos del backlog FabroGym.
- 40 historias de usuario, una por cada RF del ERS/SRS PE5 v2.0.3.
- Total: 55 ítems.
- No se reutilizan los 84 ítems de SIMPA.
- No se generan subtareas artificiales; pueden crearse después solo cuando la implementación lo requiera.

## Jerarquía

El CSV usa:
- `Work item ID`
- `Work type`
- `Parent`

Las épicas aparecen primero y cada historia referencia en `Parent` el `Work item ID` de su épica.

## Mapeo recomendado en Jira

- Work item ID -> Work item ID
- Work type -> Work type / Issue Type
- Summary -> Summary
- Description -> Description
- Priority -> Priority
- Parent -> Parent
- Labels -> Labels

## Importación

Para conservar la jerarquía Épica -> Historia, utilizar el importador de sistema externo CSV de Jira.

## Criterio académico

Cada historia conserva:
- ID del RF;
- historia de usuario;
- enunciado verificable;
- criterio BDD;
- fuente;
- CU;
- CP;
- componente;
- estado de traza;
- prioridad MoSCoW.

Fuente: `03_Matriz_Trazabilidad/PE5_Matrices_FabroGym.xlsx`.
