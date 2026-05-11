---
title: Crear sello de goma con archivo de apariencia
type: docs
weight: 20
url: /es/python-net/create-rubber-stamp-with-appearance-file/
description: El ejemplo enlaza un PDF de entrada, crea un sello de goma en la página 1 usando un archivo de imagen como apariencia del sello, y guarda el PDF actualizado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear un sello de goma con apariencia personalizada en un PDF usando PdfContentEditor
Abstract: Este ejemplo muestra cómo agregar una anotación de sello de goma con una apariencia personalizada (imagen) a un documento PDF usando Aspose.PDF for Python via the Facades API. Los sellos personalizados le permiten incluir logotipos, firmas o elementos visuales de marca como parte del sello.
---

Las anotaciones de sello de goma pueden personalizarse no solo con texto sino también usando un archivo de imagen como su apariencia. Este enfoque es útil para agregar logotipos de la empresa, sellos de firma o cualquier indicación visual a sus páginas PDF.

1. Crear un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instancia.
1. Vincula el documento PDF de entrada.
1. Defina un rectángulo para el sello.
1. Utilice un archivo de imagen personalizado para definir la apariencia del sello de caucho.
1. Establezca el texto y el color del sello.
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
