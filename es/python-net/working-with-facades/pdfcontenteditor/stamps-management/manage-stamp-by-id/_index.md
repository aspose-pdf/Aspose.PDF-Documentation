---
title: Administrar Sello por ID
type: docs
weight: 95
url: /es/python-net/manage-stamp-by-id/
description: Cómo manipular anotaciones de sello de goma en un PDF por sus IDs únicos usando Aspose.PDF for Python
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Administrar sellos de goma por ID en un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo demuestra cómo manipular anotaciones de sello de goma en un PDF por sus IDs únicos usando Aspose.PDF for Python a través de la API Facades. Puedes ocultar o mostrar sellos específicos en determinadas páginas sin afectar a otros sellos.
---

En PDFs con múltiples sellos de goma, puede ser útil controlar sellos individuales basándose en su ID. Los métodos 'hide_stamp_by_id()' y 'show_stamp_by_id()' permiten un control selectivo de la visibilidad. Este ejemplo muestra cómo:

- Agregar múltiples sellos con IDs únicos
- Ocultar un sello en una página específica
- Mostrar un sello en otra página

Al usar operaciones basadas en ID, evitas rastrear sellos por posición de página u otros atributos.

1. Crear un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instancia.
1. Vincula el documento PDF de entrada.
1. Agregar sellos de goma con IDs específicos.
1. Ocultar y mostrar sellos según sus IDs y números de página.
1. Guarda el documento PDF actualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def manage_stamp_by_id(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(200, 380, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 480, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    # Apply ID-based stamp operations
    content_editor.hide_stamp_by_id(1, 1)
    content_editor.show_stamp_by_id(1, 2)

    # Save updated document
    content_editor.save(outfile)
```
