---
title: Rotar páginas PDF usando Python
linktitle: Rotar páginas PDF
type: docs
weight: 110
url: /es/python-net/rotate-pages/
description: Este tema describe cómo rotar la orientación de la página en un archivo PDF existente de forma programática con Python.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo rotar páginas en PDF con Python
Abstract: Este artículo ofrece una guía sobre cómo actualizar o cambiar programáticamente la orientación de las páginas en un archivo PDF existente usando Python. Utilizando Aspose.PDF para Python a través de .NET, los usuarios pueden cambiar fácilmente entre orientaciones horizontal y vertical ajustando las propiedades MediaBox de la página. El artículo incluye un fragmento de código Python que demuestra cómo iterar a través de las páginas de un documento PDF, modificar sus dimensiones y posiciones MediaBox, y ajustar el CropBox si es necesario. Además, explica cómo establecer el ángulo de rotación de las páginas usando el método 'rotate' para lograr la orientación deseada. El proceso concluye guardando el archivo PDF actualizado.
---

Este tema describe cómo actualizar o cambiar la orientación de las páginas en un archivo PDF existente de forma programática con Python.

## Cambiar orientación de página

Esta función rota cada página de un PDF [`Documento`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 90 grados en sentido horario usando Aspose.PDF para Python.
Es útil para corregir problemas de orientación de página, como documentos escaneados que están de lado. El PDF original permanece sin cambios y la versión rotada se guarda como un archivo nuevo.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_page(infile, outfile):
    """
    Rotate all pages in a PDF document by 90 degrees clockwise.

    Demonstrates how to rotate PDF pages using the Aspose.PDF library.
    This function applies a 90-degree clockwise rotation to every page
    in the input document and saves the result to a new file.

    Args:
        infile (str): Path to the input PDF file to rotate.
        outfile (str): Path where the rotated PDF will be saved.

    Returns:
        None: The function modifies the PDF pages and saves to the output path.

    Note:
        - Applies 90-degree clockwise rotation (ap.Rotation.ON90) to all pages
        - Rotates every page in the document uniformly
        - The original document is not modified; a new file is created
        - Rotation options include: ON90 (90°), ON180 (180°), ON270 (270°)
        - Useful for correcting page orientation or adjusting layout

    Example:
        >>> rotate_page("input.pdf", "rotated_output.pdf")
        # Rotates all pages 90 degrees clockwise and saves to rotated_output.pdf
    """
    document = ap.Document(infile)
    for page in document.pages:
        # `page` is a `Page` object; `rotate` uses the `Rotation` enum
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```


