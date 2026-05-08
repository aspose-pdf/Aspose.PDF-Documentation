---
title: Agregar sellos de página a PDF en Python
linktitle: Agregar sellos de página
type: docs
weight: 30
url: /es/python-net/page-stamps-in-the-pdf-file/
description: Aprende cómo agregar sellos de página PDF como superposiciones o fondos en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar sellos de página a PDF usando Python
Abstract: Este artículo explica cómo agregar un sello de página a un documento PDF usando Aspose.PDF for Python. Un sello de página le permite superponer o subyacer contenido —como logotipos, marcas de agua o anotaciones— a una página específica en un PDF. El ejemplo muestra cómo abrir un PDF existente, crear un objeto PdfPageStamp a partir de otra página PDF, configurarlo como sello de fondo y aplicarlo a una página en particular. El PDF sellado se guarda luego como un nuevo documento. Esta técnica es útil para la marca, el marcado de agua o para resaltar contenido a nivel de página en flujos de trabajo PDF automatizados.
---

Aspose.PDF for Python via .NET muestra cómo aplicar un sello de página (marca de agua o superposición) a una página específica en un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). El sello de página puede ser una página PDF existente utilizada como capa de fondo o de primer plano (ver [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)). Esto es útil para agregar logotipos, marcas de agua u otro contenido de página repetitivo.

1. Abra el documento PDF usando `ap.Document()` (ver [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Cree un `PdfPageStamp` objeto usando la página PDF o archivo a usar como sello (ver [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)).
1. Establezca las propiedades del sello, p. ej., `background = True` para colocarlo detrás del contenido.
1. Agregar el sello a una página específica usando `document.pages[page_number].add_stamp(page_stamp)` (ver [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) y [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)).
1. Guarda el PDF modificado en el archivo de salida especificado usando [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```

## Temas relacionados con el estampado

- [Estampar páginas PDF en Python](/pdf/es/python-net/stamping/)
- [Agregar números de página al PDF en Python](/pdf/es/python-net/add-page-number/)
- [Agregar sellos de imagen al PDF en Python](/pdf/es/python-net/image-stamps-in-pdf-page/)
- [Agregar sellos de texto al PDF en Python](/pdf/es/python-net/text-stamps-in-the-pdf-file/)