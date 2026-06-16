---
title: Convertir PDF a PowerPoint en Python
linktitle: Convertir PDF a PowerPoint
type: docs
weight: 30
url: /es/python-net/convert-pdf-to-powerpoint/
description: Aprenda cómo convertir PDF a PowerPoint en Python, incluyendo PDF a PPTX, diapositivas como imágenes y resolución de imagen personalizada con Aspose.PDF.
lastmod: "2026-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Convertir PDF a diapositivas PPTX PowerPoint en Python
Abstract: Este artículo muestra cómo convertir archivos PDF a presentaciones de PowerPoint con Aspose.PDF for Python via .NET. Cubre la conversión de PDF a PPTX, la conversión de diapositivas como imágenes y la configuración de la resolución de la imagen para la salida de la presentación.
---

## Convertir PDF a PowerPoint en Python

**Aspose.PDF for Python via .NET** le permite convertir archivos PDF a presentaciones PowerPoint PPTX desde código Python.

Utilice este flujo de trabajo cuando necesite reutilizar informes PDF, presentaciones, folletos o documentos como archivos PowerPoint. Durante la conversión, las páginas PDF individuales se convierten en diapositivas separadas en el archivo PPTX.

Durante la conversión de PDF a PPTX, el texto puede renderizarse como texto seleccionable que puede actualizarse en PowerPoint. Para convertir archivos PDF al formato PPTX, Aspose.PDF proporciona el [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) clase. Pasa un `PptxSaveOptions` objeto como el segundo argumento a [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.

## Convertir PDF a PPTX en Python

Para convertir PDF a PPTX, use los siguientes pasos de código.

Pasos: Convertir PDF a PowerPoint en Python

1. Crear una instancia de [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase.
1. Crear una instancia de [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) clase.
1. Llama al [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    document.save(outfile, save_options)
```

## Convertir PDF a PPTX con diapositivas como imágenes

{{% alert color="success" %}}
**Intente convertir PDF a PowerPoint en línea**

Aspose.PDF ofrece una herramienta en línea ["PDF a PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx) aplicación donde puedes probar la calidad de la conversión.


[![Aspose.PDF Conversión PDF a PPTX con App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

En caso de que necesite convertir un PDF buscable a PPTX como imágenes en lugar de texto seleccionable, Aspose.PDF ofrece esa función a través de [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) clase. Para lograr esto, establezca la propiedad [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) de [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) clase a 'true' como se muestra en el siguiente ejemplo de código.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_slides_as_images(infile, outfile):

    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.slides_as_images = True

    document.save(outfile, save_options)
```

## Convertir PDF a PPTX con resolución de imagen personalizada

Este método convierte un documento PDF en un archivo PowerPoint (PPTX) mientras establece una resolución de imagen personalizada (300 DPI) para una mejor calidad.

1. Cargue el PDF en un objeto 'ap.Document'.
1. Cree una instancia de 'PptxSaveOptions'.
1. Establezca la propiedad 'image_resolution' a 300 DPI para una renderización de alta calidad.
1. Guarde el PDF como un archivo PPTX usando las opciones de guardado definidas.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_image_resolution(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.image_resolution = 300

    document.save(outfile, save_options)
```

## Conversiones relacionadas

- [Convertir PDF a Word](/pdf/es/python-net/convert-pdf-to-word/) para obtener documentos editables en lugar de diapositivas.
- [Convertir PDF a Excel](/pdf/es/python-net/convert-pdf-to-excel/) cuando el PDF de origen contiene datos empresariales con muchas tablas.
- [Convertir PDF a HTML](/pdf/es/python-net/convert-pdf-to-html/) para flujos de trabajo de publicación listos para el navegador.
