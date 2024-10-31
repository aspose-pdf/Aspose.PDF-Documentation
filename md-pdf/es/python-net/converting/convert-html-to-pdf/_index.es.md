---
title: Convertir HTML a PDF en Python
linktitle: Convertir HTML a archivo PDF
type: docs
weight: 40
url: /python-net/convert-html-to-pdf/
lastmod: "2022-12-22"
description: Este tema te muestra cómo convertir HTML a PDF y MHTML a PDF usando Aspose.PDF. para Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Descripción general

Aspose.PDF para Python a través de .NET es una solución profesional que te permite crear archivos PDF a partir de páginas web y código HTML en bruto en tus aplicaciones.

Este artículo explica cómo **convertir HTML a PDF usando Python**. Cubre los siguientes temas.

_Formato_: **HTML**
- [Python HTML a PDF](#python-html-to-pdf)
- [Python Convertir HTML a PDF](#python-html-to-pdf)
- [Python Cómo convertir HTML a PDF](#python-html-to-pdf)

## Conversión de HTML a PDF en Python

**Aspose.PDF para Python** es una API de manipulación de PDF que te permite convertir cualquier documento HTML existente a PDF sin problemas. El proceso de convertir HTML a PDF puede ser personalizado de manera flexible.

## Convertir HTML a PDF

El siguiente ejemplo de código en Python muestra cómo convertir un documento HTML a un PDF.

1. Cree una instancia de la clase [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
2. Inicialice el objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
3. Guarde el documento PDF de salida llamando al método **Document.Save()**.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "little_html.html"
    output_pdf = DIR_OUTPUT + "convert_html_to_pdf.pdf"
    options = ap.HtmlLoadOptions()
    document = ap.Document(input_pdf, options)
    document.save(output_pdf)
```

{{% alert color="success" %}}
**Intente convertir HTML a PDF en línea**

Aspose le presenta la aplicación gratuita en línea ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Convertion HTML to PDF using Free App](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}