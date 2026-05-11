---
title: Crear Sello de Goma con Flujo de Apariencia
type: docs
weight: 30
url: /es/python-net/create-rubber-stamp-with-appearance-stream/
description: Este ejemplo carga un PDF, crea un sello de goma en la página 1 usando un archivo de imagen para su apariencia, y guarda el documento modificado. ✨
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear un Sello de Goma con Apariencia de Imagen Personalizada Usando PdfContentEditor en Python
Abstract: Este ejemplo muestra cómo crear una anotación de sello de goma con una apariencia de imagen personalizada en un PDF usando Aspose.PDF for Python via the Facades API. Este enfoque le permite aplicar sellos con marca o visualmente ricos, como logotipos, sellos o firmas.
---

Las anotaciones de sello de goma pueden personalizarse usando un archivo de imagen externo. En lugar de depender solo de sellos basados en texto, puede definir una apariencia visual (por ejemplo, el logotipo de la empresa o una insignia de aprobación) y colocarla en una página.

1. Crear un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instancia.
1. Vincula el documento PDF de entrada.
1. Defina un rectángulo para la ubicación del sello.
1. Utilice un archivo de imagen como apariencia del sello.
1. Aplique configuraciones de texto y color.
1. Guarda el documento PDF actualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_rubber_stamp_with_appearance_file(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create rubber stamp using appearance_file overload (image path)
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(100, 400, 200, 60),
        "Stamp with custom appearance",
        apd.Color.dark_green,
        image_file,
    )
    # Save updated document
    content_editor.save(outfile)
```    
