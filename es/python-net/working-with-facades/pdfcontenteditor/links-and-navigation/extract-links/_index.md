---
title: Extraer enlaces
linktitle: Extraer enlaces
type: docs
weight: 70
url: /es/python-net/extract-links/
description: Este ejemplo enlaza un PDF de entrada, extrae todos los enlaces y muestra sus coordenadas y URIs (si están disponibles).
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraer enlaces de un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo demuestra cómo extraer todos los enlaces de un documento PDF usando Aspose.PDF for Python a través de la API Facades. Muestra cómo identificar y recuperar enlaces web u otros enlaces accionables incrustados en el PDF.
---

Los PDF a menudo contienen elementos interactivos como enlaces web, enlaces de documento y acciones personalizadas. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puedes extraer programáticamente todas las anotaciones de enlace de un PDF. Esto te permite inspeccionar o procesar los enlaces, por ejemplo, validar URL o analizar patrones de navegación en un documento.

1. Crea una instancia de PdfContentEditor.
1. Vincula el documento PDF de entrada.
1. Extraiga todos los enlaces usando 'extract_link()'.
1. Itere sobre los enlaces extraídos.
1. Compruebe si un enlace es una LinkAnnotation y si su acción es una GoToURIAction.
1. Imprima las coordenadas del rectángulo y el URI.
1. Muestre un mensaje si no se encuentran enlaces.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def extract_links(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Extract links from the document
    links = content_editor.extract_link()

    count = 0
    for link in links:
        count += 1
        print(f"Link {count}: {link.rect}")
        if is_assignable(link, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"  URI: {action.uri}")

    if count == 0:
        print("No links found")
```
