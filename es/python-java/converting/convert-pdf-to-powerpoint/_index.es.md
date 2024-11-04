---
title: Convertir PDF a PowerPoint en Python
linktitle: Convertir PDF a PowerPoint
type: docs
weight: 30
url: /python-java/convert-pdf-to-powerpoint/
description: Aspose.PDF te permite convertir PDF a formato PPT (PowerPoint) usando Python. Hay una posibilidad de convertir PDF a PPTX con diapositivas como imágenes.
lastmod: "2023-04-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Visión general

¿Es posible convertir un archivo PDF en un PowerPoint? ¡Sí, puedes! ¡Y es fácil!
Este artículo explica cómo **convertir PDF a PowerPoint usando Python**. Cubre estos temas.

_Formato_: **PPTX**
- [Python PDF a PPTX](#python-pdf-a-pptx)
- [Python Convertir PDF a PPTX](#python-pdf-a-pptx)
- [Python Cómo convertir un archivo PDF a PPTX](#python-pdf-a-pptx)

_Formato_: **PowerPoint**
- [Python PDF a PowerPoint](#python-pdf-a-powerpoint)
- [Python Convertir PDF a PowerPoint](#python-pdf-a-powerpoint)
- [Python Cómo convertir un archivo PDF a PowerPoint](#python-pdf-a-powerpoint)


## Conversión de PDF a PowerPoint y PPTX en Python

**Aspose.PDF for Python via Java** le permite rastrear el progreso de la conversión de PDF a PPTX.

Tenemos una API llamada Aspose.Slides que ofrece la función de crear y manipular presentaciones PPT/PPTX. Esta API también proporciona la función de convertir archivos PPT/PPTX al formato PDF. Durante esta conversión, las páginas individuales del archivo PDF se convierten en diapositivas separadas en el archivo PPTX.

Durante la conversión de PDF a <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, el texto se representa como Texto donde puede seleccionarlo/actualizarlo. Tenga en cuenta que para convertir archivos PDF al formato PPTX, Aspose.PDF proporciona una clase llamada [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions). Un objeto de la clase PptxSaveOptions se pasa como segundo argumento al [`Document.Save(..) method`](https://reference.aspose.com/pdf/java/aspose.pdf/document/methods/save). El siguiente fragmento de código muestra el proceso para convertir archivos PDF en formato PPTX.

## Conversión simple de PDF a PowerPoint usando Python y Aspose.PDF para Python

Para convertir PDF a PPTX, Aspose.PDF para Python recomienda usar los siguientes pasos de código.

<a name="csharp-pdf-to-powerpoint"><strong>Pasos: Convertir PDF a PowerPoint en Python</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Pasos: Convertir PDF a PPTX en Python</strong></a>

1. Crear una instancia de la clase [Document](https://reference.aspose.com/pdf/java/aspose.pdf/document)
2. Crear una instancia de la clase [PptxSaveOptions](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions)
3. Utilizar el método **Save** del objeto **Document** para guardar el PDF como PPTX

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# Abrir documento PDF
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SeparateImages = True
save_options._OptimizeTextBoxes = True

# Guardar el archivo en formato de documento MS Word
document.save(output_pdf, save_options)
```


## Convertir PDF a PPTX con Diapositivas como Imágenes

{{% alert color="success" %}}
**Intenta convertir PDF a PowerPoint en línea**

Aspose.PDF para Python te presenta la aplicación gratuita en línea ["PDF a PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión PDF a PPTX con Aplicación Gratuita](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

En caso de que necesites convertir un PDF con capacidad de búsqueda a PPTX como imágenes en lugar de texto seleccionable, Aspose.PDF proporciona tal característica a través de la clase [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/). Para lograr esto, establece la propiedad [SlidesAsImages](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/#properties) de la clase [PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/) a 'true' como se muestra en el siguiente ejemplo de código.

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# Abrir documento PDF
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SlidesAsImages = True

# Guardar el archivo en formato de documento de MS Word
document.save(output_pdf, save_options)
```


## Ver También

Este artículo también cubre estos temas. Los códigos son los mismos que arriba.

_Formato_: **PowerPoint**
- [Código Python de PDF a PowerPoint](#python-pdf-to-powerpoint)
- [API Python de PDF a PowerPoint](#python-pdf-to-powerpoint)
- [Convertir PDF a PowerPoint con Python Programáticamente](#python-pdf-to-powerpoint)
- [Biblioteca Python de PDF a PowerPoint](#python-pdf-to-powerpoint)
- [Guardar PDF como PowerPoint con Python](#python-pdf-to-powerpoint)
- [Generar PowerPoint desde PDF con Python](#python-pdf-to-powerpoint)
- [Crear PowerPoint desde PDF con Python](#python-pdf-to-powerpoint)
- [Convertidor de PDF a PowerPoint con Python](#python-pdf-to-powerpoint)

_Formato_: **PPTX**
- [Código Python de PDF a PPTX](#python-pdf-to-pptx)
- [API Python de PDF a PPTX](#python-pdf-to-pptx)
- [Convertir PDF a PPTX con Python Programáticamente](#python-pdf-to-pptx)
- [Biblioteca Python de PDF a PPTX](#python-pdf-to-pptx)
- [Guardar PDF como PPTX con Python](#python-pdf-to-pptx)
- [Generar PPTX desde PDF con Python](#python-pdf-to-pptx)
- [Crear PPTX desde PDF con Python](#python-pdf-to-pptx)
- [Convertidor de PDF a PPTX con Python](#python-pdf-to-pptx)