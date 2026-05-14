---
title: Extraer tablas de PDF en Python
linktitle: Extraer tabla
type: docs
weight: 20
url: /es/python-net/extracting-table/
description: Aprenda cómo extraer datos de tabla de documentos PDF existentes en Python.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraer datos de tabla de archivos PDF con Python
Abstract: Este artículo explica cómo extraer tablas de documentos PDF usando Aspose.PDF for Python via .NET. Muestra cómo usar `TableAbsorber` para detectar tablas por página, iterar filas y celdas, y recuperar el texto de las celdas para análisis y procesamiento de datos posteriores.
---

## Extraer tabla de PDF

Extraer tablas de PDFs es útil para la generación de informes, la migración de datos y los flujos de trabajo de análisis. Con Aspose.PDF for Python via .NET, puedes detectar y leer el contenido de tablas de documentos PDF existentes de manera eficiente.

Este fragmento de código abre un archivo PDF existente, escanea cada página en busca de tablas y extrae el contenido de texto de las celdas. Utiliza `TableAbsorber` para detectar tablas y luego iterar a través de filas y celdas para imprimir el texto extraído.

1. Carga el PDF en un objeto ap.Document.
1. Recorre las páginas.
1. Crea un objeto TableAbsorber.
1. Itera a través de las tablas.
1. Iterar a través de filas y celdas.
1. Extraer e imprimir texto de las celdas.

Este ejemplo lee un PDF, encuentra todas las tablas y muestra su contenido de celdas fila por fila.

```python
import aspose.pdf as ap
from os import path
import sys

def extract(infile: str) -> None:
    """Extract and print all tables from a PDF file."""
    document = ap.Document(infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row:")
                row_txt = ""
                for cell in row.cell_list:
                    cell_txt = ""
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        for seg in fragment.segments:
                            cell_txt += seg.text
                    row_txt += " | "
                    row_txt += cell_txt
                print(row_txt)
```

## Temas relacionados de la tabla

- [Trabajar con tablas en PDF usando Python](/pdf/es/python-net/working-with-tables/)
- [Agregar tablas al PDF usando Python](/pdf/es/python-net/adding-tables/)
- [Integrar tablas PDF con fuentes de datos](/pdf/es/python-net/integrate-table/)
- [Eliminar tablas de PDFs existentes](/pdf/es/python-net/removing-tables/)