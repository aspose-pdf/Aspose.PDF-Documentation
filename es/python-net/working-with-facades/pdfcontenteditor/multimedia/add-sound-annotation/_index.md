---
title: Agregar anotación de sonido
linktitle: Agregar anotación de sonido
type: docs
weight: 20
url: /es/python-net/add-sound-annotation/
description: Este ejemplo vincula un PDF de entrada, agrega una anotación de sonido en la página 1 y guarda el PDF modificado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar una anotación de sonido a un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo muestra cómo incrustar audio en un documento PDF usando Aspose.PDF for Python a través de la API Facades. Demuestra cómo agregar una anotación de sonido clickeable que reproduzca un archivo de audio directamente dentro del PDF.
---

Las anotaciones de sonido en los PDF le permiten agregar contenido de audio, como notas de voz, música o efectos de sonido a sus documentos. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puede definir un pequeño rectángulo clickeable en una página que reproduce un archivo de audio especificado al activarse.

1. Crea una instancia de PdfContentEditor.
1. Vincula el documento PDF de entrada.
1. Definir un rectángulo para la anotación de sonido.
1. Especifique el archivo de audio, el nombre de la anotación, el número de página y la tasa de muestreo.
1. Guarda el documento PDF actualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_sound_annotation(infile, sound_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add sound annotation to page 1
    content_editor.create_sound(
        apd.Rectangle(80, 450, 30, 30), sound_file, "Speaker", 1, "8000"
    )
    # Save updated document
    content_editor.save(outfile)
```
