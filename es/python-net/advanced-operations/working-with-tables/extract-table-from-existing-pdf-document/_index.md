---
title: Extraer tabla de documento PDF
linktitle: Extraer tabla
type: docs
weight: 20
url: /es/python-net/extracting-table/
description: Aspose.PDF for Python via .NET permite realizar diversas manipulaciones con las tablas contenidas en su documento PDF.
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer una tabla de PDF usando Python
Abstract: Este artículo analiza el proceso de extracción de tablas de documentos PDF usando Python, aprovechando específicamente la biblioteca Aspose.PDF for Python via .NET. Proporciona un ejemplo de código que muestra cómo cargar un documento PDF, iterar a través de sus páginas y utilizar la clase `TableAbsorber` para identificar y extraer datos de tabla. El código recorre cada tabla, fila y celda, recopilando fragmentos de texto y mostrando el texto extraído. Este método se destaca como una herramienta poderosa para tareas de extracción y análisis de datos que involucran datos tabulares dentro de PDFs.
---

## Extraer tabla de PDF

Extraer tablas de PDFs usando Python puede ser increíblemente útil para la extracción y análisis de datos. Con la biblioteca Aspose.PDF for Python via .NET, puedes trabajar de manera eficiente con tablas incrustadas en documentos PDF para diversas tareas relacionadas con datos.

Este fragmento de código abre un archivo PDF existente, escanea cada página en busca de tablas y extrae el contenido de texto de sus celdas. Utiliza el 'TableAbsorber' para detectar tablas y luego itera a través de filas y celdas para imprimir el texto interno.

1. Carga el PDF en un objeto ap.Document.
1. Recorre las páginas.
1. Crea un objeto TableAbsorber.
1. Itera a través de las tablas.
1. Itera a través de filas y celdas.
1. Extrae e imprime el texto de las celdas.

Este ejemplo lee un PDF, encuentra todas las tablas y muestra el contenido de sus celdas fila por fila.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    document = ap.Document(path_infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row")
                for cell in row.cell_list:
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        txt = ""
                        for seg in fragment.segments:
                            txt += seg.text
                        print(txt)
```


