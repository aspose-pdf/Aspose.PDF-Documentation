---
title: Convertir PDF a HTML en Python 
linktitle: Convertir PDF a formato HTML
type: docs
weight: 50
url: /es/python-net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: Este tema te muestra cómo convertir un archivo PDF a formato HTML con la biblioteca Aspose.PDF para Python .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Resumen

Este artículo explica cómo **convertir PDF a HTML usando Python**. Cubre estos temas.

_Formato_: **HTML**
- [Python PDF a HTML](#python-pdf-to-html)
- [Python Convertir PDF a HTML](#python-pdf-to-html)
- [Python Cómo convertir un archivo PDF a HTML](#python-pdf-to-html)


## Convertir PDF a HTML

**Aspose.PDF para Python vía .NET** ofrece muchas características para convertir varios formatos de archivo en documentos PDF y convertir archivos PDF en varios formatos de salida.
 Este artículo discute cómo convertir un archivo PDF en <abbr title="Lenguaje de Marcado de Hipertexto">HTML</abbr>. Puedes usar solo un par de líneas de código en Python para convertir PDF a HTML. Es posible que necesites convertir PDF a HTML si deseas crear un sitio web o agregar contenido a un foro en línea. Una forma de convertir PDF a HTML es usar Python de manera programática.

{{% alert color="success" %}}
**Intenta convertir PDF a HTML en línea**

Aspose.PDF para Python te presenta una aplicación gratuita en línea ["PDF a HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión de PDF a HTML con Aplicación Gratuita](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

<a name="csharp-pdf-to-html"><strong>Pasos: Convertir PDF a HTML en Python</strong></a>

1. Crea una instancia del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el documento PDF de origen.
2. Guárdalo en [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) llamando al método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_html.html"
    # Abre el documento PDF
    document = ap.Document(input_pdf)

    # guarda el documento en formato HTML
    save_options = ap.HtmlSaveOptions()
    document.save(output_pdf, save_options)
```

## Ver También

Este artículo también cubre estos temas. Los códigos son los mismos que arriba.

_Formato_: **HTML**
- [Código Python PDF a HTML](#python-pdf-to-html)
- [API Python PDF a HTML](#python-pdf-to-html)
- [Python PDF a HTML Programáticamente](#python-pdf-to-html)
- [Biblioteca Python PDF a HTML](#python-pdf-to-html)
- [Python Guardar PDF como HTML](#python-pdf-to-html)
- [Python Generar HTML desde PDF](#python-pdf-to-html)
- [Python Crear HTML desde PDF](#python-pdf-to-html)

- [Convertidor Python PDF a HTML](#python-pdf-to-html)