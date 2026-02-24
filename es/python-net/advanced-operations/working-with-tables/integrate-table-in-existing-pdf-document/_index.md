---
title: Integrar tabla con fuentes de datos PDF
linktitle: Integrar tabla
type: docs
weight: 30
url: /es/python-net/integrate-table/
description: Este artículo muestra cómo integrar tablas PDF. Integra la tabla con la base de datos y determina si la tabla se dividirá en la página actual.
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Crear PDF desde DataFrame

La función 'create_pdf_from_dataframe' toma un DataFrame y lo convierte en una tabla dentro de un nuevo PDF. Crea un documento PDF nuevo, agrega una página, genera una tabla a partir del DataFrame (usando un método auxiliar) y guarda el resultado en la ruta de archivo proporcionada. Y no solo es posible, sino que es muy fácil.

1. Inicializa un documento PDF vacío con 'ap.Document()'.
1. La función 'self.create_table_from_dataframe(df, max_rows)' transforma el DataFrame en un objeto tabla de Aspose.PDF.
1. Inserta la tabla en la página PDF. Añade la tabla generada al contenido de la primera página (page.paragraphs.add(table)).
1. Guarda el documento PDF.

```python

from os import path
import pandas as pd
import aspose.pdf as ap

# Example DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "London"]
})

max_rows = 3  # Number of rows to include in the table
path_outfile = "output.pdf"

# Define the function to create a table from DataFrame
def create_table_from_dataframe(df, max_rows):
    table = ap.Table()
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )
    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = False
    for column_name in df.columns:
        cell = header_row.cells.add(str(column_name))
        cell.background_color = ap.Color.light_gray
    # Add data rows
    for row_data in df.head(max_rows).itertuples(index=False):
        row = table.rows.add()
        for value in row_data:
            row.cells.add(str(value))
    return table

# Load source PDF document
document = ap.Document()
page = document.pages.add()

table = create_table_from_dataframe(df, max_rows)

# Add table object to first page of input document
page.paragraphs.add(table)
document.save(path_outfile)
```

## Crear tabla desde DataFrame

Este código convierte un DataFrame en un objeto Table de Aspose.PDF. Configura los bordes de la tabla, agrega una fila de encabezado con los nombres de columnas y rellena la tabla con las primeras max_rows filas del DataFrame. La tabla resultante puede entonces añadirse a un documento PDF.

1. Crea un objeto 'ap.Table()' vacío.
1. Establece el borde de la tabla.
1. Establece el borde de celda predeterminado.
1. Añade la fila de encabezado.
1. Añade filas de datos.
1. Devuelve la tabla.

```python

    from os import path
    import pandas as pd
    import aspose.pdf as ap

    
    table = ap.Table()  # Initializes a new instance of the Table
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )

    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = (
        False  # Prevent header row from being split across pages
    )
    for column_name in df.columns:
        cell = header_row.cells.add(str(column_name))
        cell.background_color = ap.Color.light_gray

    # Add data rows
    for row_data in df.head(max_rows).itertuples(index=False):
        row = table.rows.add()
        for value in row_data:
            row.cells.add(str(value))

    return table
```
