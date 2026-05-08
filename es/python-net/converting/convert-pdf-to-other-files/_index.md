---
title: Convertir PDF a EPUB, Texto, XPS y más en Python
linktitle: Convertir PDF a otros formatos
type: docs
weight: 90
url: /es/python-net/convert-pdf-to-other-files/
lastmod: "2026-04-14"
description: Aprenda cómo convertir archivos PDF a EPUB, LaTeX, Markdown, texto, XPS y MobiXML en Python con Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a otros formatos en Python
Abstract: El artículo ofrece una guía completa sobre la conversión de archivos PDF a varios formatos utilizando Aspose.PDF for Python. Cubre la conversión de PDFs a formatos EPUB, LaTeX/TeX, Texto, XPS y XML. Cada sección comienza con una invitación a probar las aplicaciones en línea proporcionadas por Aspose para convertir PDFs a los formatos correspondientes, resaltando la facilidad de uso y la calidad de estas herramientas.
---

## Convertir PDF a EPUB

{{% alert color="success" %}}
**Intenta convertir PDF a EPUB en línea**

Aspose.PDF for Python le presenta una aplicación en línea ["PDF a EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a EPUB con App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> es un estándar gratuito y abierto de libros electrónicos del International Digital Publishing Forum (IDPF). Los archivos tienen la extensión .epub.
EPUB está diseñado para contenido refluible, lo que significa que un lector EPUB puede optimizar el texto para un dispositivo de visualización particular. EPUB también admite contenido de diseño fijo. El formato está pensado como un único formato que los editores y casas de conversión pueden utilizar internamente, así como para distribución y venta. Reemplaza el estándar Open eBook.

Aspose.PDF for Python también admite la función de convertir documentos PDF al formato EPUB. Aspose.PDF for Python tiene una clase llamada \u0027EpubSaveOptions\u0027 que puede usarse como el segundo argumento para [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método, para generar un archivo EPUB.
Por favor, intente usar el siguiente fragmento de código para cumplir con este requisito con Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_EPUB(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Conversiones relacionadas

- [Convertir PDF a Word](/pdf/es/python-net/convert-pdf-to-word/) para salida de documento de oficina editable.
- [Convertir PDF a HTML](/pdf/es/python-net/convert-pdf-to-html/) para salida orientada al navegador.
- [Convertir PDF a PDF/A, PDF/E y PDF/X](/pdf/es/python-net/convert-pdf-to-pdf_x/) para flujos de trabajo de conversión archivísticos y compatibles con normas.

## Convertir PDF a LaTeX/TeX

**Aspose.PDF for Python via .NET** soporta la conversión de PDF a LaTeX/TeX.
El formato de archivo LaTeX es un formato de archivo de texto con marcado especial y se utiliza en el sistema de preparación de documentos basado en TeX para una composición tipográfica de alta calidad.

{{% alert color="success" %}}
**Intenta convertir PDF a LaTeX/TeX en línea**

Aspose.PDF for Python le presenta una aplicación en línea ["PDF a LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión PDF a LaTeX/TeX con App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Para convertir archivos PDF a TeX, Aspose.PDF tiene la clase [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) que proporciona la propiedad OutDirectoryPath para guardar imágenes temporales durante el proceso de conversión.

El siguiente fragmento de código muestra el proceso de convertir archivos PDF al formato TEX con Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TeX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.LaTeXSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir PDF a texto

**Aspose.PDF for Python** admite la conversión de un documento PDF completo y de una sola página a un archivo de texto. Puedes convertir un documento PDF a un archivo TXT usando la clase 'TextDevice'. El siguiente fragmento de código explica cómo extraer los textos de todas las páginas.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TXT(infile, outfile):
    document = ap.Document(infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intenta convertir Convert PDF a Texto en línea**

Aspose.PDF for Python le presenta una aplicación en línea ["PDF a Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de PDF a Texto con App de Aspose.PDF](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convertir PDF a XPS

**Aspose.PDF for Python** brinda la posibilidad de convertir archivos PDF al formato XPS. Intentemos usar el fragmento de código presentado para convertir archivos PDF al formato XPS con Python.

{{% alert color="success" %}}
**Intenta convertir PDF a XPS en línea**

Aspose.PDF for Python le presenta una aplicación en línea ["PDF a XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a XPS con App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

El tipo de archivo XPS está asociado principalmente con la XML Paper Specification de Microsoft Corporation. La XML Paper Specification (XPS), anteriormente con el nombre en código Metro y que engloba el concepto de marketing Next Generation Print Path (NGPP), es la iniciativa de Microsoft para integrar la creación y visualización de documentos en el sistema operativo Windows.

Para convertir archivos PDF a XPS, Aspose.PDF tiene la clase [OpcionesDeGuardadoXps](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) que se utiliza como el segundo argumento para el [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método para generar el archivo XPS.

El siguiente fragmento de código muestra el proceso de convertir un archivo PDF al formato XPS.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_XPS(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir PDF a MD

Aspose.PDF tiene la clase ‘MarkdownSaveOptions()’, que convierte un documento PDF al formato Markdown (MD) mientras preserva las imágenes y los recursos.

1. Cargue el PDF de origen usando 'ap.Document'.
1. Crea una instancia de 'MarkdownSaveOptions'.
1. Establezca 'resources_directory_name' a 'images' – las imágenes extraídas se almacenarán en esta carpeta.
1. Guarda el documento Markdown convertido usando las opciones configuradas.
1. Imprima un mensaje de confirmación después de la conversión.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MD(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

Un archivo Markdown con texto e imágenes enlazadas almacenadas en la carpeta de imágenes especificada.

## Convertir PDF a MobiXML

Este método convierte un documento PDF al formato MOBI (MobiXML), que se usa comúnmente para libros electrónicos en dispositivos Kindle.

1. Cargue el documento PDF de origen usando 'ap.Document'.
1. Guarde el documento con el formato 'ap.SaveFormat.MOBI_XML'.
1. Imprima un mensaje de confirmación una vez que la conversión haya finalizado.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MobiXML(infile, outfile):
    document = ap.Document(infile)
    document.save(outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
