---
title: Extraer datos de una tabla en PDF con Python
linktitle: Extraer datos de una tabla
type: docs
weight: 40
url: /es/python-net/extract-data-from-table-in-pdf/
description: Aprenda cómo extraer datos de tabla de archivos PDF con Aspose.PDF for Python y exportar los resultados para un procesamiento posterior.
lastmod: "2025-03-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer datos de una tabla en PDF mediante Python
Abstract: Este artículo explica cómo extraer y procesar datos de tablas de documentos PDF con Aspose.PDF for Python. Muestra cómo escanear cada página con TableAbsorber, leer filas y celdas de las tablas detectadas, limitar la extracción a una región anotada específica y exportar el contenido del PDF a formato CSV para su uso en herramientas de hojas de cálculo y procesamiento posterior.
---

## Extraer tablas de PDF programáticamente

Usar [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) para detectar tablas en cada página de un [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Después de visitar una página, iterar a través de `table_list`, luego recorre cada fila y celda para reconstruir el contenido de la tabla en un formato de texto legible.

1. Abra el PDF como un `Document`.
1. Iterar a través de las páginas en `document.pages`.
1. Crear un `TableAbsorber` para cada página y llama `visit(page)`.
1. Recorre las tablas, filas y celdas detectadas.
1. Lee fragmentos de texto de cada celda y ensambla la salida de fila extraída.

```python
import aspose.pdf as apdf
from os import path

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
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## Extraer tabla en un área específica de la página PDF

Si necesita extraer solo tablas ubicadas dentro de una región marcada, combine [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) con un [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/). En este ejemplo, el rectángulo de anotación se usa como límite, y solo se procesan las tablas que están completamente contenidas dentro de esa región.

1. Abra el PDF como un `Document`.
1. Seleccione la página objetivo.
1. Encuentre la anotación cuadrada que marca la región de interés.
1. Crear un `TableAbsorber` y visite la página.
1. Compare cada rectángulo de tabla detectado con el rectángulo de la anotación.
1. Procese solo las tablas que quedan completamente dentro del área marcada.

```python
import aspose.pdf as apdf
from os import path

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
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## Exportar datos de tabla de PDF a CSV

Cuando necesites los datos extraídos en un formato compatible con hojas de cálculo, guarda el PDF usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) y establece el formato de salida a CSV. El archivo resultante puede abrirse en Excel, Google Sheets, o importarse en flujos de trabajo de análisis.

1. Abre el PDF de origen como un [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear un `ExcelSaveOptions` instancia.
1. Conjunto `excel_save.format` a `ExcelSaveOptions.ExcelFormat.CSV`.
1. Guarda el documento en la ruta CSV de destino.

```python
import aspose.pdf as apdf
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

document = apdf.Document(path_infile)
excel_save = apdf.ExcelSaveOptions()
excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
document.save(path_outfile, excel_save)
```
