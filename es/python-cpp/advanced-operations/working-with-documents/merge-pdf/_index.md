---
title: Cómo Unir PDF usando Python a través de C++
linktitle: Unir archivos PDF
type: docs
weight: 10
url: es/python-cpp/merge-pdf-documents/
keywords: "unir múltiples pdf en un solo pdf python, combinar múltiples pdf en uno python, unir múltiples pdf en uno python"
description: Esta página explica cómo unir documentos PDF en un solo archivo PDF con Python.
lastmod: "2024-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Unir o combinar múltiples PDF en un solo PDF en Python a través de C++

Al aprovechar Python y una biblioteca de C++ de Aspose, puedes unir de manera eficiente múltiples archivos PDF en un solo PDF con facilidad.

Para concatenar dos archivos PDF:

1. Abrir el primer documento
1. Luego agregar las páginas del segundo documento al primero
1. Guardar el archivo de salida concatenado con el método 'document.save'.

El siguiente fragmento de código muestra cómo concatenar archivos PDF.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file= os.path.join(dataDir , "sample0.pdf")
    output_file = os.path.join(dataDir , "results", "concatenated-files.pdf")

    # Abrir el primer documento
    document1 = apw.Document(inputFile)
    document2 = apw.Document(inputFile)

    # Agregar las páginas del segundo documento al primero
    document1.pages.add(document2.pages)

    # Guardar el archivo de salida concatenado
    document1.save(output_file)
```