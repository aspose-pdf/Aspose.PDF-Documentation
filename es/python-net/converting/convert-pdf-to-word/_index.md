---
title: Convertir PDF a Word en Python
linktitle: Convertir PDF a Word
type: docs
weight: 10
url: /es/python-net/convert-pdf-to-word/
lastmod: "2026-04-14"
description: Aprenda cómo convertir archivos PDF a DOC y DOCX en Python con Aspose.PDF for Python via .NET para facilitar la edición y reutilización de documentos.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a Word en Python
Abstract: Este artículo ofrece una guía completa sobre la conversión de archivos PDF a formatos de Microsoft Word (DOC y DOCX) utilizando Python, específicamente con la biblioteca Aspose.PDF. Describe las ventajas de convertir PDFs a documentos Word editables, lo que permite una manipulación más fácil del contenido, como texto, tablas e imágenes. El artículo detalla el proceso de conversión de PDF a DOC (formato Word 97-2003) y DOCX, con fragmentos de código que demuestran estas conversiones mediante Python. El proceso implica crear un objeto `Document` a partir del PDF y guardarlo en el formato deseado utilizando el método `save()` y la enumeración `SaveFormat`. Además, introduce la clase `DocSaveOptions`, que permite una mayor personalización del proceso de conversión, como especificar modos de reconocimiento. El artículo también destaca las aplicaciones en línea proporcionadas por Aspose.PDF para probar la calidad y funcionalidad de la conversión. El contenido incluye una visión estructurada y enlaces a las secciones correspondientes para cada formato.
---

## Convertir PDF a DOC

Una de las características más populares es la conversión de PDF a Microsoft Word DOC, lo que hace que la gestión de contenidos sea más fácil. **Aspose.PDF for Python via .NET** le permite convertir archivos PDF no solo a DOC sino también al formato DOCX, de manera fácil y eficiente.

Utilice la conversión a Word cuando necesite revisar texto, reutilizar contenido en flujos de trabajo de oficina, o trasladar contenido PDF a documentos editables DOC o DOCX.

El [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) La clase proporciona numerosas propiedades que mejoran el proceso de conversión de archivos PDF a formato DOC. Entre estas propiedades, Mode le permite especificar el modo de reconocimiento para el contenido PDF. Puede especificar cualquier valor de la enumeración RecognitionMode para esta propiedad. Cada uno de estos valores tiene beneficios y limitaciones específicas:

Pasos: Convertir PDF a DOC en Python

1. Cargue el PDF en un objeto 'ap.Document' object.
1. Cree una instancia de 'DocSaveOptions'.
1. Establezca la propiedad format a 'DocFormat.DOC' para garantizar que la salida esté en formato .doc (formato Word antiguo).
1. Guarde el PDF como un documento Word usando las opciones de guardado especificadas.
1. Imprime un mensaje de confirmación.

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

Aspose.PDF for Python le presenta una aplicación en línea ["PDF a DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Convertir PDF a DOC](/pdf/es/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF a DOCX

Aspose.PDF for Python API le permite leer y convertir documentos PDF a DOCX usando Python a través de .NET. DOCX es un formato bien conocido para documentos de Microsoft Word cuya estructura cambió de binario simple a una combinación de archivos XML y binarios. Los archivos DOCX pueden abrirse con Word 2007 y versiones posteriores, pero no con las versiones anteriores de MS Word que admiten extensiones de archivo DOC.

El siguiente fragmento de código Python muestra el proceso de convertir un archivo PDF a formato DOCX.

Pasos: Convertir PDF a DOCX en Python

1. Cargue el PDF de origen usando 'ap.Document'.
1. Crear una instancia de 'DocSaveOptions'.
1. Establezca la propiedad format en 'DocFormat.DOC_X' para generar un archivo .docx (formato Word moderno).
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

## Convertir PDF a DOCX con Reconocimiento de Diseño Avanzado

Convertir un documento PDF a un archivo DOCX (Word) usando Python y Aspose.PDF con configuraciones de reconocimiento avanzadas. Utiliza el modo de flujo mejorado para preservar la estructura del documento, haciendo que la salida sea más editable y más cercana al diseño original.

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

El [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) class tiene una propiedad llamada Format que brinda la capacidad de especificar el formato del documento resultante, es decir, DOC o DOCX. Para convertir un archivo PDF al formato DOCX, pase el valor Docx del enumerado DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Intenta convertir PDF a DOCX en línea**

Aspose.PDF for Python le presenta una aplicación en línea ["PDF a Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión PDF a Word App](/pdf/es/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Conversiones relacionadas

- [Convertir PDF a Excel](/pdf/es/python-net/convert-pdf-to-excel/) para exportaciones orientadas a hojas de cálculo.
- [Convertir PDF a PowerPoint](/pdf/es/python-net/convert-pdf-to-powerpoint/) cuando necesitas diapositivas de presentación en lugar de salida de procesamiento de texto.
- [Convertir PDF a HTML](/pdf/es/python-net/convert-pdf-to-html/) para la publicación web y flujos de trabajo de contenido basados en el navegador.
