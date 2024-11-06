---
title: Convertir PDF a PowerPoint en Python
linktitle: Convertir PDF a PowerPoint
type: docs
weight: 30
url: es/python-net/convert-pdf-to-powerpoint/
description: Aspose.PDF le permite convertir PDF a formato PPT (PowerPoint) usando Python. Una forma es la posibilidad de convertir PDF a PPTX con diapositivas como imágenes.
lastmod: "2022-12-23"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Descripción general

¿Es posible convertir un archivo PDF en un PowerPoint? ¡Sí, puedes! ¡Y es fácil!
Este artículo explica cómo **convertir PDF a PowerPoint usando Python**. Cubre estos temas.

_Formato_: **PPTX**
- [Python PDF a PPTX](#python-pdf-to-pptx)
- [Python Convertir PDF a PPTX](#python-pdf-to-pptx)
- [Python Cómo convertir archivo PDF a PPTX](#python-pdf-to-pptx)

_Formato_: **PowerPoint**
- [Python PDF a PowerPoint](#python-pdf-to-powerpoint)
- [Python Convertir PDF a PowerPoint](#python-pdf-to-powerpoint)
- [Python Cómo convertir archivo PDF a PowerPoint](#python-pdf-to-powerpoint)


## Conversión de PDF a PowerPoint y PPTX en Python

**Aspose.PDF para Python a través de .NET** te permite rastrear el progreso de la conversión de PDF a PPTX.

Tenemos una API llamada Aspose.Slides que ofrece la característica de crear y manipular presentaciones PPT/PPTX. Esta API también proporciona la característica de convertir archivos PPT/PPTX al formato PDF. Durante esta conversión, las páginas individuales del archivo PDF se convierten en diapositivas separadas en el archivo PPTX.

Durante la conversión de PDF a <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, el texto se representa como Texto donde puedes seleccionarlo/actualizarlo. Por favor, ten en cuenta que para convertir archivos PDF al formato PPTX, Aspose.PDF proporciona una clase llamada [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). Un objeto de la clase PptxSaveOptions se pasa como segundo argumento al [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods). El siguiente fragmento de código muestra el proceso para convertir archivos PDF en formato PPTX.

## Conversión simple de PDF a PowerPoint usando Python y Aspose.PDF para Python

Para convertir PDF a PPTX, Aspose.PDF para Python aconseja usar los siguientes pasos de código.

<a name="csharp-pdf-to-powerpoint"><strong>Pasos: Convertir PDF a PowerPoint en Python</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Pasos: Convertir PDF a PPTX en Python</strong></a>

1. Crear una instancia de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
2. Crear una instancia de la clase [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/)
3. Usar el método **Save** del objeto **Document** para guardar el PDF como PPTX

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx.pptx"
    # Abrir documento PDF
    document = ap.Document(input_pdf)
    # Instanciar la instancia de PptxSaveOptions
    save_option = ap.PptxSaveOptions()
    # Guardar el archivo en formato MS PowerPoint
    document.save(output_pdf, save_option)
```

## Convertir PDF a PPTX con Diapositivas como Imágenes


{{% alert color="success" %}}
**Intenta convertir PDF a PowerPoint en línea**

Aspose.PDF para Python te presenta una aplicación gratuita en línea ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión PDF a PPTX con App Gratuita](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

En caso de que necesites convertir un PDF con búsqueda a PPTX como imágenes en lugar de texto seleccionable, Aspose.PDF proporciona tal característica a través de la clase [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). Para lograr esto, establece la propiedad [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) de la clase [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) a 'true' como se muestra en el siguiente ejemplo de código.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_pptx_with_slides_as_images.pptx"
    # Abrir documento PDF
    document = ap.Document(input_pdf)
    # Instanciar objeto PptxSaveOptions
    save_option = ap.PptxSaveOptions()
    save_option.slides_as_images = True
    # Guardar el archivo en formato MS PowerPoint
    document.save(output_pdf, save_option)
```


## Ver También

Este artículo también cubre estos temas. Los códigos son los mismos que arriba.

_Formato_: **PowerPoint**
- [Código Python PDF a PowerPoint](#python-pdf-to-powerpoint)
- [API Python PDF a PowerPoint](#python-pdf-to-powerpoint)
- [Programa Python PDF a PowerPoint](#python-pdf-to-powerpoint)
- [Librería Python PDF a PowerPoint](#python-pdf-to-powerpoint)
- [Guardar PDF como PowerPoint en Python](#python-pdf-to-powerpoint)
- [Generar PowerPoint desde PDF en Python](#python-pdf-to-powerpoint)
- [Crear PowerPoint desde PDF en Python](#python-pdf-to-powerpoint)
- [Convertidor de Python PDF a PowerPoint](#python-pdf-to-powerpoint)

_Formato_: **PPTX**
- [Código Python PDF a PPTX](#python-pdf-to-pptx)
- [API Python PDF a PPTX](#python-pdf-to-pptx)
- [Programa Python PDF a PPTX](#python-pdf-to-pptx)
- [Librería Python PDF a PPTX](#python-pdf-to-pptx)
- [Guardar PDF como PPTX en Python](#python-pdf-to-pptx)
- [Generar PPTX desde PDF en Python](#python-pdf-to-pptx)
- [Crear PPTX desde PDF en Python](#python-pdf-to-pptx)
- [Convertidor de Python PDF a PPTX](#python-pdf-to-pptx)