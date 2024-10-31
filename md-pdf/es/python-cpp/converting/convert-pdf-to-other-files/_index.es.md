---
title: Convertir PDF a Texto en Python
linktitle: Convertir PDF a otros formatos
type: docs
weight: 90
url: /python-cpp/convert-pdf-to-other-files/
lastmod: "2022-12-23"
keywords: convertir, PDF, EPUB, LaText, Texto, XPS, Python
description: Este tema muestra cómo convertir un archivo PDF a otros formatos de archivo como Texto usando Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF a Texto

**Aspose.PDF para Python** soporta la conversión de un documento PDF completo y de una sola página a un archivo de texto.

### Convertir documento PDF a archivo de Texto

Puede convertir un documento PDF a un archivo TXT usando la clase 'TextDevice'.

1. Crear la ruta del archivo de entrada y salida
1. Crear una instancia de la fachada del extractor PDF con [extractor_create](https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)
1. Vincular el archivo PDF al extractor con [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)

1. Extrayendo el texto del archivo PDF usando [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)
1. Escribiendo el texto extraído en el archivo de salida
1. Guardar el PDF de salida con el método 'document.save'.

El siguiente fragmento de código explica cómo extraer los textos de todas las páginas.

```python

    from AsposePdfPython import *

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"

    extactor = extractor_create()
    extractor_bind_pdf(extactor,input_pdf)
    text = extractor_extract_text(extactor)

    with open(output_pdf, 'w') as f:
        f.write(text)
```