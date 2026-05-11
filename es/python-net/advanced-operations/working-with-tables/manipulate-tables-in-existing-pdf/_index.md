---
title: Manipular tablas en documentos PDF existentes
linktitle: Manipular tablas
type: docs
weight: 40
url: /es/python-net/manipulating-tables/
description: Aprenda cómo inspeccionar y modificar tablas en documentos PDF existentes usando Python.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspeccionar y modificar tablas PDF existentes con Python
Abstract: Este artículo explica cómo manipular tablas ya presentes en documentos PDF usando Aspose.PDF for Python via .NET. Aprenda cómo localizar tablas con TableAbsorber, acceder a filas y celdas específicas, actualizar el contenido de texto de la tabla y guardar el PDF modificado en Python.
---

## Manipular tablas en PDF existente

Aspose.PDF for Python via .NET le permite actualizar tablas que ya existen en un documento PDF. Puede usar el [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) clase para encontrar tablas en una página, acceder a filas y celdas, cambiar el contenido de texto, y guardar el archivo actualizado.

Utilice esta página cuando necesite actualizar el contenido de tablas existente en PDFs sin recrear el diseño completo del documento.

## Buscar y Reemplazar Texto en Celdas de Tablas PDF

Este ejemplo encuentra la primera tabla en la página 1, accede a la primera celda, reemplaza su texto y guarda el PDF de salida.

1. Abra el PDF de entrada.
1. Cree un TableAbsorber y visite la página 1.
1. Asegúrese de que se detecte al menos una tabla.
1. Acceda a la primera celda de la primera fila de la primera tabla.
1. Asegúrese de que la celda contenga fragmentos de texto, luego actualice el primer fragmento.
1. Guardar el PDF modificado.

```python
import aspose.pdf as ap

def replace_cell_text(infile: str, outfile: str) -> None:
    """Replace text in the first cell of the first detected table."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    first_cell = absorber.table_list[0].row_list[0].cell_list[0]
    if len(first_cell.text_fragments) == 0:
        raise ValueError("The target cell has no text fragments.")

    # Change text of the first text fragment in the cell
    first_cell.text_fragments[0].text = "New Value"

    # Save PDF document
    document.save(outfile)
```

## Reemplazar una tabla existente por una tabla nueva

También puedes reemplazar una tabla detectada con una recién creada. Este enfoque es útil cuando tanto la estructura como el contenido deben cambiar.

El código a continuación abre un PDF, encuentra la primera tabla en la página 1, crea una tabla de reemplazo, intercambia la tabla antigua con la nueva y guarda el resultado.

```python
import aspose.pdf as ap

def replace_table(infile: str, outfile: str) -> None:
    """Replace an entire table with a new one."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    # Get first table on the page
    old_table = absorber.table_list[0]

    # Create new table
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1.0)

    row = new_table.rows.add()
    row.cells.add("Col 1")
    row.cells.add("Col 2")
    row.cells.add("Col 3")
    row = new_table.rows.add()
    row.cells.add("Col 12")
    row.cells.add("Col 22")
    row.cells.add("Col 32")

    # Replace the old table with the new one
    absorber.replace(document.pages[1], old_table, new_table)

    # Save PDF document
    document.save(outfile)
```

## Temas relacionados de la tabla

- [Trabajar con tablas en PDF usando Python](/pdf/es/python-net/working-with-tables/)
- [Agregar tablas al PDF usando Python](/pdf/es/python-net/adding-tables/)
- [Extraer tablas de documentos PDF](/pdf/es/python-net/extracting-table/)
- [Eliminar tablas de PDFs existentes](/pdf/es/python-net/removing-tables/)
