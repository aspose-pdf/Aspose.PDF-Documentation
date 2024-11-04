---
title: Convertir PDF a TXT en Python
linktitle: Convertir PDF a TXT
type: docs
weight: 20
url: /python-cpp/convert-pdf-to-txt/
lastmod: "2024-04-23"
description: La biblioteca Aspose.PDF para Python a través de C++ le permite convertir PDF a formato TXT usando Python.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Convertir PDF a TXT

Aspose.PDF para Python a través de C++ admite la conversión de documentos PDF a un archivo de texto mediante los siguientes pasos:

1. Crear la ruta de archivo de entrada y salida
1. Crear una instancia de la fachada del extractor de PDF con [extractor_create](https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)
1. Vincular el archivo PDF al extractor con [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)
1. Extraer el texto del archivo PDF usando [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)
1. Escribir el texto extraído en el archivo de salida
1. Guardar el PDF de salida con el método 'document.save'.

El siguiente fragmento de código muestra cómo convertir una imagen JPG a PDF usando Python a través de C++:

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # Creando la ruta del directorio de datos
    dataDir = os.path.join(os.getcwd(), "samples")

    # Creando la ruta del archivo de entrada
    input_file = os.path.join(dataDir, "sample.pdf")

    # Creando la ruta del archivo de salida
    output_file = os.path.join(dataDir, "results", "pdf-to-txt.txt")

    # Creando una instancia de la fachada del extractor de PDF
    extactor = apCore.facades_pdf_extractor_create()

    # Vinculando el archivo PDF al extractor
    apCore.facades_facade_bind_pdf(extactor, input_file)

    # Extrayendo el texto del archivo PDF
    text = apCore.facades_pdf_extractor_extract_text(extactor)

    # Escribiendo el texto extraído en el archivo de salida
    with open(output_file, 'w') as f:
        f.write(text)
```