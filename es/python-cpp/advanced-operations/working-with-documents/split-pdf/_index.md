---
title: Dividir PDF programáticamente en Python
linktitle: Dividir archivos PDF
type: docs
weight: 20
url: /es/python-cpp/split-pdf-document/
keywords: dividir pdf en múltiples archivos, dividir pdf en pdfs separados, dividir pdf python
description: Este tema muestra cómo dividir páginas de PDF en archivos PDF individuales en sus aplicaciones de Python a través de C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Dividir páginas de PDF puede ser una característica útil para aquellos que desean dividir un archivo grande en páginas separadas o grupos de páginas.

## Ejemplo en Vivo

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) es una aplicación web gratuita en línea que le permite investigar cómo funciona la funcionalidad de división de presentaciones.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Este tema muestra cómo dividir páginas de PDF en archivos PDF individuales en sus aplicaciones de Python C++. Para dividir páginas de PDF en archivos PDF de una sola página usando Python, se pueden seguir los siguientes pasos:

El fragmento de código configura los directorios y rutas de archivos necesarios, abre un documento PDF y luego recorre cada página del documento.
 Para cada página, crea un nuevo documento, copia la página actual al nuevo documento y guarda el nuevo documento como un archivo PDF separado con una convención de nombres específica.

1. Abre el documento de entrada
1. Inicializa el conteo de páginas
1. Recorre todas las páginas del documento

## Dividir PDF en múltiples archivos o PDFs separados en Python

El siguiente fragmento de código en Python te muestra cómo dividir páginas de un PDF en archivos PDF individuales.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file= os.path.join(dataDir , "sample.pdf")
    outputFolder = os.path.join(dataDir , "results")
    # Abre el documento
    document = apw.Document(inputFile)

    pageCount = 1

    # Recorre todas las páginas

    while (pageCount <= document.pages.count()):
        page = document.pages[pageCount]    
        newDocument = apw.Document()
        newDocument.pages.copy_page(page)
        newDocument.save(os.path.join(outputFolder,"page_" + str(pageCount) + "_out" + ".pdf"))
        pageCount += 1
```