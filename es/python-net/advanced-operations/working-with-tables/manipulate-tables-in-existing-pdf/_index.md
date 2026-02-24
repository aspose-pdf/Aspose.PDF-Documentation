---
title: Manipular tablas en PDF existente
linktitle: Manipular tablas
type: docs
weight: 40
url: /es/python-net/manipulating-tables/
description: Aprenda cómo trabajar con tablas en PDFs existentes usando Aspose.PDF para Python a través de .NET, proporcionando flexibilidad en la modificación de documentos.
lastmod: "2025-09-27"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Manipular tablas en PDF existente

Aspose.PDF para Python muestra cómo modificar el contenido de una celda específica dentro de una tabla en un documento PDF. Utiliza la clase TableAbsorber para localizar tablas en la primera página, accede a un fragmento de texto particular dentro de la primera celda de la primera tabla, actualiza su texto y guarda el PDF modificado en un nuevo archivo.

1. Abra el archivo PDF usando 'ap.Document()'.
1. Cree un objeto TableAbsorber para detectar tablas en el PDF.
1. Llama a absorber.visit() para encontrar todas las tablas en la primera página.
1. Acceda a un fragmento de texto específico:
- Recupera la primera tabla.
- Obtiene la primera fila de la tabla.
- Selecciona el segundo fragmento de texto en la celda.
1. Modifique el texto.
1. Guarde el PDF actualizado.
1. Imprime la confirmación del archivo guardado.

```python

    import aspose.pdf as ap
    from os import path

    # Define file names and data directory
    data_dir = "."  # or specify your data directory
    infile = "input.pdf"   # replace with your input PDF file name
    outfile = "output.pdf" # replace with your desired output PDF file name

    # Open PDF document
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get access to first table on page, their first cell and text fragments in it
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]

    # Change text of the first text fragment in the cell
    fragment.text = "hi world"

    # Save PDF document

    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```

## Reemplazar tabla antigua con una nueva en documento PDF

Aspose.PDF permite reemplazar una tabla existente en un PDF con una tabla nueva. El fragmento de código abre un PDF, identifica la primera tabla en la primera página usando TableAbsorber, crea una tabla nueva con anchos de columna personalizados y contenido, y luego reemplaza la tabla original con la nueva. Finalmente, guarda el PDF actualizado en un nuevo archivo.

Demuestra cómo modificar la estructura y el contenido de la tabla en un PDF sin alterar el resto del documento.

```python

    import aspose.pdf as ap
    from os import path

    # Open PDF document
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get first table on the page
    table = absorber.table_list[0]

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

    # Replace the table with new one
    absorber.replace(document.pages[1], table, new_table)

    # Save PDF document
    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```
