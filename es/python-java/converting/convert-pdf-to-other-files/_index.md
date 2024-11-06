---
title: Convertir PDF a EPUB, LaTeX, Texto, XPS en Python
linktitle: Convertir PDF a otros formatos
type: docs
weight: 90
url: es/python-java/convert-pdf-to-other-files/
lastmod: "2023-04-06"
keywords: convertir, PDF, EPUB, LaText, Texto, XPS, Python
description: Este tema te muestra cómo convertir un archivo PDF a otros formatos de archivo como EPUB, LaTeX, Texto, XPS, etc. usando Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF a EPUB

{{% alert color="success" %}}
**Intenta convertir PDF a EPUB en línea**

Aspose.PDF para Python te presenta una aplicación gratuita en línea ["PDF a EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), donde puedes investigar la funcionalidad y la calidad con la que trabaja.

[![Conversión de Aspose.PDF de PDF a EPUB con Aplicación Gratuita](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** es un estándar de libro electrónico libre y abierto del International Digital Publishing Forum (IDPF).
 Archivos tienen la extensión .epub.  
EPUB está diseñado para contenido adaptable, lo que significa que un lector EPUB puede optimizar el texto para un dispositivo de visualización en particular. EPUB también admite contenido de diseño fijo. El formato está destinado como un único formato que los editores y las casas de conversión pueden usar internamente, así como para distribución y venta. Sustituye al estándar Open eBook.

Aspose.PDF para Python también admite la función de convertir documentos PDF al formato EPUB. Aspose.PDF para Python tiene una clase llamada 'EpubSaveOptions' que puede usarse como el segundo argumento del método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods), para generar un archivo EPUB.  
Por favor, intente usar el siguiente fragmento de código para lograr este requisito con Python.

```python

from asposepdf import Api

# iniciar licencia
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# Convertir a Epub
documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.epub"
doc.save(documentOutName, Api.SaveFormat.Epub)
```

## Convertir PDF a LaTeX/TeX

**Aspose.PDF para Python a través de Java** soporta la conversión de PDF a LaTeX/TeX. El formato de archivo LaTeX es un formato de archivo de texto con una marca especial y se utiliza en sistemas de preparación de documentos basados en TeX para la composición tipográfica de alta calidad.

{{% alert color="success" %}}
**Intenta convertir PDF a LaTeX/TeX en línea**

Aspose.PDF para Python te presenta la aplicación gratuita en línea ["PDF a LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Aspose.PDF Conversión de PDF a LaTeX/TeX con Aplicación Gratuita](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Para convertir archivos PDF a TeX, Aspose.PDF tiene la clase [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/latexsaveoptions/) que proporciona la propiedad OutDirectoryPath para guardar imágenes temporales durante el proceso de conversión.

El siguiente fragmento de código muestra el proceso de conversión de archivos PDF al formato TEX con Python.

```python
from asposepdf import Api

documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.tex"
doc.save(documentOutName, Api.SaveFormat.TeX)
```

## Convertir PDF a Texto

**Aspose.PDF para Python** soporta convertir todo el documento PDF y una sola página a un archivo de texto.

### Convertir documento PDF a archivo de texto

Puede convertir un documento PDF a un archivo TXT usando la clase 'TextDevice'.

El siguiente fragmento de código explica cómo extraer los textos de todas las páginas.

```python

from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_text"
# Abrir documento PDF
document = Api.Document(input_pdf)

device = Device.TextDevice()

for i in range(0, document.getPages.size):
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.txt"
    # Convertir una página en particular y guardar como archivo de texto
    device.process(document.getPages.getPage(i + 1), imageFileName)
```


{{% alert color="success" %}}
**Intenta convertir Convertir PDF a Texto en línea**

Aspose.PDF para Python te presenta la aplicación gratuita en línea ["PDF a Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), donde puedes intentar investigar la funcionalidad y calidad con la que funciona.

[![Conversión de Aspose.PDF PDF a Texto con Aplicación Gratuita](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convertir PDF a XPS

**Aspose.PDF para Python** ofrece la posibilidad de convertir archivos PDF al formato <abbr title="Especificación de Papel XML">XPS</abbr>. Vamos a intentar utilizar el fragmento de código presentado para convertir archivos PDF al formato XPS con Python.

{{% alert color="success" %}}
**Intenta convertir PDF a XPS en línea**

Aspose.PDF para Python te presenta la aplicación gratuita en línea ["PDF a XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), donde puedes intentar investigar la funcionalidad y calidad con la que funciona.

[![Conversión de Aspose.PDF PDF a XPS con Aplicación Gratuita](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

El tipo de archivo XPS está principalmente asociado con la Especificación de Papel XML de Microsoft Corporation. La Especificación de Papel XML (XPS), anteriormente con el nombre en clave Metro y que subsume el concepto de marketing Next Generation Print Path (NGPP), es la iniciativa de Microsoft para integrar la creación y visualización de documentos en el sistema operativo Windows.

Para convertir archivos PDF a XPS, Aspose.PDF tiene la clase [XpsSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/xpssaveoptions/) que se utiliza como el segundo argumento del método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) para generar el archivo XPS.

El siguiente fragmento de código muestra el proceso de conversión de un archivo PDF al formato XPS.

```python

from asposepdf import Api

documentName = "../../testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "../../testout/out.xps"
doc.save(documentOutName, Api.SaveFormat.Xps)

```