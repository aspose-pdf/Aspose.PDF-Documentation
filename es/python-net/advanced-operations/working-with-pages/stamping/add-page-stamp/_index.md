---
title: Agregar sellos de página al PDF con Python
linktitle: Agregar sellos de página
type: docs
weight: 30
url: /es/python-net/page-stamps-in-the-pdf-file/
description: Aspose.PDF for Python a través de .NET le permite agregar un sello de página a su archivo PDF.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar sellos de página a PDF usando Python
Abstract: Este artículo explica cómo agregar un sello de página a un documento PDF usando Aspose.PDF para Python. Un sello de página le permite superponer o subponer contenido—como logotipos, marcas de agua o anotaciones—sobre una página específica en un PDF. El ejemplo muestra cómo abrir un PDF existente, crear un objeto PdfPageStamp a partir de otra página PDF, configurarlo como sello de fondo y aplicarlo a una página determinada. El PDF sellado se guarda luego como un nuevo documento. Esta técnica es útil para la marca, marcas de agua o para enfatizar contenido a nivel de página en flujos de trabajo PDF automatizados.
---

Aspose.PDF for Python via .NET muestra cómo aplicar un sello de página (marca de agua o superposición) a una página específica en un PDF [`Documento`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). El sello de página puede ser una página PDF existente utilizada como capa de fondo o de primer plano (vea [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)). Esto es útil para agregar logotipos, marcas de agua u otro contenido repetitivo de página.

1. Abra el documento PDF usando `ap.Document()` (vea [`Documento`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Cree un objeto `PdfPageStamp` usando la página PDF o el archivo que se usará como sello (vea [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)).
1. Establezca las propiedades del sello, p. ej., `background = True` para colocarlo detrás del contenido.
1. Añada el sello a una página específica usando `document.pages[page_number].add_stamp(page_stamp)` (vea [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) y [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)).
1. Guarde el PDF modificado en el archivo de salida especificado usando [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```

