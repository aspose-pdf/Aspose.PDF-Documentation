---
title: Extraer datos de tabla en PDF con Python
linktitle: Extraer datos de tabla
type: docs
weight: 40
url: /es/python-net/extract-data-from-table-in-pdf/
description: Aprende cómo extraer tablas de PDF usando Aspose.PDF para Python
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer datos de tabla en PDF mediante Python
Abstract: Este artículo ofrece una guía completa sobre cómo extraer y procesar programáticamente tablas de documentos PDF utilizando Aspose.PDF, una biblioteca de Python. El artículo presenta un script en Python que abre un documento PDF, itera por cada página y extrae tablas mediante la clase `TableAbsorber`. Los datos de tabla extraídos se estructuran y se imprimen para un análisis posterior. Esta sección describe cómo extraer tablas de regiones marcadas específicas dentro de un PDF, como áreas delimitadas por anotaciones cuadradas. El script identifica estas anotaciones, inicializa el `TableAbsorber` y verifica si las tablas se encuentran dentro de las regiones anotadas antes de extraer e imprimir los datos. La sección final detalla un método para convertir los datos tabulares extraídos de un PDF a formato de archivo CSV.
---

## Extraer tablas de PDF programáticamente

Este código extrae tablas de PDF y convierte los datos tabulares de un archivo PDF en un formato legible y estructurado para su posterior procesamiento o análisis.

1. Abrir el documento PDF
1. Iterar a través de las páginas del PDF
1. Extraer datos de tabla

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    # Iterate through each page in the document
    for page in document.pages:
        absorber = apdf.text.TableAbsorber()
        absorber.visit(page)

        for table in absorber.table_list:
            print("Table")
            for row in table.row_list:
                row_text = []
                for cell in row.cell_list:
                    cell_text = []
                    for fragment in cell.text_fragments:
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## Extraer tabla en un área específica de la página PDF

Este fragmento de código extrae datos tabulares de regiones marcadas específicas en un PDF, como datos dentro de un recuadro resaltado o una anotación específica.

1. Abrir documento PDF
1. Obtener la primera página
1. Encontrar la primera anotación cuadrada
1. Inicializar el TableAbsorber
1. Iterar a través de las tablas en la página
1. Verificar si la tabla está dentro de la región de anotación

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    # Get the first page (index starts from 1 in Aspose.PDF)
    page = document.pages[1]

    # Find the first square annotation
    square_annotation = next(
        (
            ann
            for ann in page.annotations
            if ann.annotation_type == apdf.annotations.AnnotationType.SQUARE
        ),
        None,
    )

    if square_annotation is None:
        print("No square annotation found.")
        return

    # Initialize the TableAbsorber
    absorber = apdf.text.TableAbsorber()
    absorber.visit(page)

    # Iterate through tables on the page
    for table in absorber.table_list:
        table_rect = table.rectangle
        annotation_rect = square_annotation.rect

        # Check if the table is inside the annotation region
        is_in_region = (
            annotation_rect.llx < table_rect.llx
            and annotation_rect.lly < table_rect.lly
            and annotation_rect.urx > table_rect.urx
            and annotation_rect.ury > table_rect.ury
        )

        if is_in_region:
            for row in table.row_list:
                row_text = []
                for cell in row.cell_list:
                    cell_text = []
                    for fragment in cell.text_fragments:
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## Extraer datos de tabla de PDF y guardarlos en un archivo Excel

El siguiente fragmento de código extrae datos tabulares de un PDF y los exporta como archivo CSV para su posterior análisis o manipulación en aplicaciones de hojas de cálculo como Excel o Google Sheets.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    excel_save = apdf.ExcelSaveOptions()
    excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, excel_save)
```

