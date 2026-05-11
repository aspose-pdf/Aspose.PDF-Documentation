---
title: Crear folleto PDF
linktitle: Crear folleto PDF
type: docs
weight: 20
url: /es/python-net/create-pdf-booklet/
description: Generar un PDF con estilo de folleto a partir de un documento existente usando Aspose.PDF para Python
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear un folleto PDF a partir de un PDF existente usando Python
Abstract: Aprenda cómo generar un PDF con estilo de folleto a partir de un documento existente usando Aspose.PDF para Python. Este ejemplo muestra cómo utilizar la clase PdfFileEditor para reorganizar las páginas de modo que puedan imprimirse y plegarse como un folleto. El método ordena automáticamente las páginas para producir un diseño de folleto correcto.
---

Crear documentos con estilo de folleto es un requisito común al preparar PDFs para impresión. En un diseño de folleto, las páginas se reorganizan de modo que, al imprimirse y plegarse, aparezcan en el orden correcto.

Usando Aspose.PDF para Python, los desarrolladores pueden convertir fácilmente un PDF estándar en un folleto usando el [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class. El método \u0027make_booklet\u0027 reorganiza automáticamente las páginas del documento de entrada y genera un nuevo PDF optimizado para la impresión de folletos.

1. Abra un documento PDF existente.
1. Cree una instancia de PdfFileEditor.
1. Utiliza el método make_booklet para reorganizar las páginas.
1. Guarda la salida como un archivo PDF listo para folleto.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create PDF Booklet
def create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    booklet_maker.make_booklet(FileIO(infile), FileIO(outfile, "w"))
```

Este fragmento de código muestra cómo usar el método ‘try_make_booklet’ de la [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) clase para reorganizar páginas para la impresión de folletos sin lanzar excepciones si la operación falla.

Un diseño de folleto reorganiza las páginas de modo que, al imprimir y doblar, el documento se lea en el orden correcto. Automatizar este proceso garantiza resultados consistentes y elimina la necesidad de reorganizar manualmente las páginas.

El método ‘try_make_booklet’ funciona de manera similar a ‘make_booklet’, pero con una diferencia importante:

- 'make_booklet' lanza una excepción si la operación falla.
- 'try_make_booklet' devuelve True o False, permitiendo a los desarrolladores gestionar los errores de forma más segura.

1. Abra un documento PDF existente.
1. Cree una instancia de PdfFileEditor.
1. Intentar crear el folleto.
1. Manejar el resultado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def try_create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    # The try_make_booklet method is like the make_booklet method,
    # except the try_make_booklet method does not throw an exception if the operation fails.
    if not booklet_maker.try_make_booklet(FileIO(infile), FileIO(outfile, "w")):
        print("Failed to create booklet.")
```
