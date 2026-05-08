---
title: Integrar tablas PDF con fuentes de datos en Python
linktitle: Integrar tabla
type: docs
weight: 30
url: /es/python-net/integrate-table/
description: Aprenda cómo integrar tablas PDF con fuentes de datos como bases de datos y DataFrames de pandas en Python.
lastmod: "2026-05-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Integrar tablas PDF con bases de datos y DataFrames usando Python
Abstract: Este artículo explica cómo integrar tablas PDF con fuentes de datos externas usando Aspose.PDF for Python via .NET. Aprenda cómo crear tablas PDF a partir de DataFrames de pandas y otras fuentes estructuradas, insertarlas en documentos y controlar el flujo de la tabla al renderizarse en varias páginas PDF en Python.
---

## Crear PDF a partir de DataFrame

El `create_pdf_from_dataframe` función crea un nuevo PDF e inserta una tabla generada a partir de un DataFrame de pandas. Este enfoque es útil para flujos de trabajo de generación de informes donde sus datos ya existen en forma tabular.

La función realiza los siguientes pasos:

1. Crear un documento PDF vacío con `ap.Document()`.
1. Agregue una página al documento.
1. Convierta el DataFrame en una tabla Aspose.PDF llamando `create_table_from_dataframe(df, max_rows)`.
1. Agregar la tabla a la página con `page.paragraphs.add(table)`.
1. Guarda el PDF en la ruta de salida.

```python
from os import path
import sys

import pandas as pd
import aspose.pdf as ap
from config import set_license, initialize_data_dir

def create_pdf_from_dataframe(
    outfile: str, df: pd.DataFrame, max_rows: int = 20
) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    table = create_table_from_dataframe(df, max_rows)

    # Add table object to first page of input document
    page.paragraphs.add(table)
    document.save(outfile)
```

## Crear tabla a partir de DataFrame

El `create_table_from_dataframe` función convierte un DataFrame en un Aspose.PDF `Table` objeto que puedes añadir a cualquier página.

Hace lo siguiente:

1. Crear un vacío `ap.Table()` instancia.
1. Establecer bordes de tabla y celda para un formato consistente.
1. Agregar una fila de encabezado usando los nombres de columna del DataFrame.
1. Agregar filas de datos de `df.head(max_rows)`.
1. Devolver el objeto de tabla poblado.

```python
from os import path
import sys

import pandas as pd
import aspose.pdf as ap
from config import set_license, initialize_data_dir

def create_table_from_dataframe(df: pd.DataFrame, max_rows: int = 20) -> ap.Table:
    """Create an Aspose.PDF table from a pandas DataFrame."""
    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )

    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = False  # Prevent header row from being split across pages
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

## Temas relacionados de la tabla

- [Trabajar con tablas en PDF usando Python](/pdf/es/python-net/working-with-tables/)
- [Agregar tablas al PDF usando Python](/pdf/es/python-net/adding-tables/)
- [Extraer tablas de documentos PDF](/pdf/es/python-net/extracting-table/)
- [Manipular tablas en PDFs existentes](/pdf/es/python-net/manipulating-tables/)