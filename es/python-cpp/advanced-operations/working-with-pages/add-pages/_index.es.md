---
title: Agregar Páginas en PDF con Python a través de C++
linktitle: Agregar Páginas
type: docs
weight: 10
url: /python-cpp/add-pages/
description: Este artículo enseña cómo insertar (agregar) una página en la ubicación deseada de un archivo PDF en Python usando C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Insertar Página Vacía en un Archivo PDF en la Ubicación Deseada

El fragmento de código abre un documento PDF, agrega una página vacía y guarda el documento modificado como un nuevo archivo PDF.

Para insertar una página vacía en un archivo PDF:

1. Abre el documento PDF
1. Agrega una nueva página en blanco al documento
1. Guarda el documento modificado en el archivo de salida con el método 'document.save'

El siguiente fragmento de código muestra cómo insertar una página en un archivo PDF:

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Establecer la ruta del directorio donde se encuentran los archivos PDF de muestra
    dataDir = os.path.join(os.getcwd(), "samples")

    # Establecer la ruta del archivo de entrada
    input_file = os.path.join(dataDir, "sample0.pdf")

    # Establecer la ruta del archivo de salida
    output_file = os.path.join(dataDir, "results", "blank_pdf_document.pdf")

    # Abrir el documento PDF
    document = apw.Document(input_file)

    # Agregar una nueva página en blanco al documento
    document.pages.add()

    # Guardar el documento modificado en el archivo de salida
    document.save(output_file)
```