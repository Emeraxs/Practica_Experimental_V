# Configuración CSV Jira — FabroGym PE5

Archivo: `CSV-configuration-FabroGym-PE5.txt`
CSV asociado: `backlog_import_jira.csv`

## Mapeo
- Work item ID → Work item ID
- Work type → Work type / Issue Type
- Summary → Summary
- Description → Description
- Priority → Priority
- Parent → Parent
- Labels → Labels

## Uso
1. Jira → Settings/System → External System Import → CSV.
2. Si aparece la experiencia nueva, cambia a la experiencia clásica/old experience.
3. Selecciona `backlog_import_jira.csv`.
4. Marca `Use an existing configuration file`.
5. Carga `CSV-configuration-FabroGym-PE5.txt`.
6. Selecciona el proyecto Jira de FabroGym cuando Jira lo solicite.
7. Ejecuta `Validate` antes de `Begin import`.

## Compatibilidad
El proyecto Jira se deja sin fijar dentro del archivo para no inventar una clave o nombre de proyecto.
Jira deberá pedirte seleccionar el proyecto real.

Atlassian indica que en la nueva experiencia de importación los work types y la jerarquía no siempre se
guardan en los archivos de configuración. Para reutilizar el mapeo completo, especialmente Work type y Parent,
usa External System Import con la experiencia clásica.
