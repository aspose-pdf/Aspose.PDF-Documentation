---
title: Crear documento PDF N-Up
type: docs
weight: 10
url: /es/python-net/create-n-up-pdf-document/
description: Aprenda cómo crear un documento PDF N-Up mientras maneja de forma segura posibles errores usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear un diseño PDF N-Up en Python
Abstract: Aprenda cómo generar un diseño PDF N-Up usando Aspose.PDF for Python. Este ejemplo demuestra cómo combinar varias páginas de un documento PDF en una sola página usando el método 'make_n_up' o 'try_make_n_up' de la clase PdfFileEditor.
---

Un diseño N-Up coloca varias páginas de un documento PDF en una sola página en formato de cuadrícula. Este diseño se utiliza a menudo para imprimir presentaciones, folletos o informes donde se pueden ver varias páginas a la vez.

Con Aspose.PDF for Python, los desarrolladores pueden crear rápidamente un documento N-Up especificando el número de filas y columnas que determinan cuántas páginas originales aparecen en cada página de salida.

En este fragmento de código, el método 'make_n_up' de la [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) clase organiza las páginas del PDF de entrada en una cuadrícula de 2 × 2, lo que significa que cuatro páginas originales aparecen en una sola página en el documento de salida.

En el ejemplo mostrado, el diseño utiliza 2 filas y 2 columnas, produciendo cuatro páginas por hoja:

1. Abra el archivo PDF de origen.
1. Cree una instancia de PdfFileEditor.
1. Especifique el número de filas y columnas para el diseño N-Up.
1. Genere un nuevo PDF con las páginas combinadas.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    nup_maker.make_n_up(
        FileIO(infile), FileIO(outfile, "w"), 2, 2
    )  # 2 rows and 2 columns for N-Up layout
```

Aspose.PDF for Python via .NET le permite generar diseños N-Up con la clase PdfFileEditor. El método 'try_make_n_up' funciona de manera similar a make_n_up, pero en lugar de lanzar una excepción cuando una operación falla, devuelve un valor booleano que indica si el proceso tuvo éxito.

El diseño N-Up organiza varias páginas PDF en una sola página mediante una cuadrícula definida por filas y columnas.

El método 'try_make_n_up' ofrece una forma más segura de realizar esta operación porque:

- Devuelve True si el diseño se crea correctamente
- Devuelve False si la operación falla
- No interrumpe la ejecución del programa con excepciones

En el ejemplo a continuación, el documento se organiza usando una cuadrícula de 2 × 2, lo que coloca cuatro páginas originales en cada página de salida.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def try_create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    if not nup_maker.try_make_n_up(FileIO(infile), FileIO(outfile, "w"), 2, 2):
        print("Failed to create N-Up PDF document.")
```
