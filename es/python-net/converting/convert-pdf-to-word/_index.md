---
title: Convertir PDF a Word en Python
linktitle: Convertir PDF a Word
type: docs
weight: 10
url: /es/python-net/convert-pdf-to-word/
lastmod: "2026-04-14"
description: Aprenda cómo convertir PDF a Word en Python, incluyendo PDF a DOC, PDF a DOCX y reconocimiento avanzado de diseño con Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Convertir PDF a DOC y DOCX en Python
Abstract: Este artículo muestra cómo convertir archivos PDF a formatos de Microsoft Word con Aspose.PDF for Python via .NET. Cubre PDF a DOC, PDF a DOCX y opciones avanzadas de reconocimiento de diseño para crear documentos Word editables a partir del contenido del PDF.
---

Esta página muestra cómo **convertir PDF a Word en Python**. Use estos ejemplos cuando necesite una salida DOC o DOCX editable a partir de un archivo PDF para revisión, reutilización o flujos de trabajo de documentos de oficina.

## Convertir PDF a DOC en Python

Una de las funciones más populares es la conversión de PDF a Microsoft Word DOC, lo que facilita la gestión de contenidos. **Aspose.PDF for Python via .NET** le permite convertir archivos PDF no solo a DOC sino también al formato DOCX, de manera fácil y eficiente.

Utilice la conversión a Word cuando necesite revisar texto, reutilizar contenido en flujos de trabajo de oficina o trasladar contenido PDF a documentos DOC o DOCX editables.

El [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) clase proporciona numerosas propiedades que mejoran el proceso de conversión de archivos PDF a formato DOC. Entre estas propiedades, Mode le permite especificar el modo de reconocimiento para el contenido PDF. Puede especificar cualquier valor de la enumeración RecognitionMode para esta propiedad. Cada uno de estos valores tiene beneficios y limitaciones específicos:

Pasos: Convertir PDF a DOC en Python

1. Cargue el PDF en un objeto 'ap.Document'.
1. Cree una instancia de 'DocSaveOptions'.
1. Establezca la propiedad format a 'DocFormat.DOC' para asegurar que la salida esté en formato .doc (formato Word antiguo).
1. Guarde el PDF como un documento de Word usando las opciones de guardado especificadas.
1. Imprima un mensaje de confirmación.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOC(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intenta convertir PDF a DOC en línea**

Aspose.PDF for Python le presenta una aplicación en línea [“PDF to DOC”](https://products.aspose.app/pdf/conversion/pdf-to-doc), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Convertir PDF a DOC](/pdf/es/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF a DOCX en Python

Aspose.PDF for Python API le permite leer y convertir documentos PDF a DOCX usando Python via .NET. DOCX es un formato bien conocido para documentos de Microsoft Word cuya estructura se cambió de binario simple a una combinación de archivos XML y binarios. Los archivos Docx pueden abrirse con Word 2007 y versiones laterales pero no con las versiones anteriores de MS Word que admiten extensiones de archivo DOC.

El siguiente fragmento de código Python muestra el proceso de convertir un archivo PDF al formato DOCX.

Pasos: Convertir PDF a DOCX en Python

1. Cargue el PDF de origen usando 'ap.Document'.
1. Crear una instancia de 'DocSaveOptions'.
1. Establezca la propiedad format a 'DocFormat.DOC_X' para generar un archivo .docx (formato Word moderno).
1. Guarde el PDF como un archivo DOCX con las opciones de guardado configuradas.
1. Imprima un mensaje de confirmación después de la conversión.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    document.save(outfile, save_options)
```

## Convertir PDF a DOCX con reconocimiento avanzado de diseño

Convertir un documento PDF en un archivo DOCX (Word) utilizando Python y Aspose.PDF con configuraciones avanzadas de reconocimiento. Utiliza el modo de flujo mejorado para preservar la estructura del documento, haciendo que la salida sea más editable y más cercana al diseño original.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX_advanced(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    save_options.mode = ap.DocSaveOptions.RecognitionMode.ENHANCED_FLOW
    document.save(outfile, save_options)
```

El [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) La clase tiene una propiedad llamada Format que brinda la capacidad de especificar el formato del documento resultante, es decir, DOC o DOCX. Para convertir un archivo PDF al formato DOCX, por favor pase el valor Docx de la enumeración DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Intenta convertir PDF a DOCX en línea**

Aspose.PDF for Python le presenta una aplicación en línea ["PDF a Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión PDF a Word App](/pdf/es/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Conversiones relacionadas

- [Convertir PDF a Excel](/pdf/es/python-net/convert-pdf-to-excel/) para exportaciones orientadas a hojas de cálculo.
- [Convertir PDF a PowerPoint](/pdf/es/python-net/convert-pdf-to-powerpoint/) cuando necesitas diapositivas de presentación en lugar de una salida de procesamiento de texto.
- [Convertir PDF a HTML](/pdf/es/python-net/convert-pdf-to-html/) para la publicación web y flujos de trabajo basados en el navegador.
