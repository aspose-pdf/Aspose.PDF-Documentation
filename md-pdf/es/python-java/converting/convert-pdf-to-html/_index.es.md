---
title: Convertir PDF a HTML en Python
linktitle: Convertir PDF a formato HTML
type: docs
weight: 50
url: /python-java/convert-pdf-to-html/
lastmod: "2021-11-01"
description: Este tema le muestra cómo convertir un archivo PDF a formato HTML con la biblioteca Aspose.PDF para Python Java.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Descripción general

Este artículo explica cómo **convertir PDF a HTML usando Python**. Cubre estos temas.

_Formato_: **HTML**
- [Python PDF a HTML](#python-pdf-to-html)
- [Python Convertir PDF a HTML](#python-pdf-to-html)
- [Python Cómo convertir archivo PDF a HTML](#python-pdf-to-html)

## Convertir PDF a HTML

**Aspose.PDF para Python a través de .NET** proporciona muchas características para convertir varios formatos de archivo en documentos PDF y convertir archivos PDF en varios formatos de salida.
 Este artículo discute cómo convertir un archivo PDF en <abbr title="HyperText Markup Language">HTML</abbr>. Puedes usar solo un par de líneas de código Python para convertir PDF a HTML. Puede que necesites convertir PDF a HTML si deseas crear un sitio web o añadir contenido a un foro en línea. Una forma de convertir PDF a HTML es usar Python de manera programática.

{{% alert color="success" %}}
**Intenta convertir PDF a HTML en línea**

Aspose.PDF para Python te presenta una aplicación gratuita en línea ["PDF a HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), donde puedes investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Convertion PDF to HTML with Free App](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

<a name="csharp-pdf-to-html"><strong>Pasos: Convertir PDF a HTML en Python</strong></a>

1. Crea una instancia del objeto [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) con el documento PDF de origen.
2. Guárdalo en [HtmlSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/htmlsaveoptions/) llamando al método [Document.save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods).

```python


from asposepdf import Api

documentName = "../../testdata/source.pdf"
documentOutName = "../../testout/result.html"
# Abrir documento PDF
document = Api.Document(documentName)

# guardar documento en formato HTML
save_options = Api.HtmlSaveOptions()
document.save(documentOutName, save_options)
```

## Ver También 

Este artículo también cubre estos temas. Los códigos son los mismos que arriba.

_Formato_: **HTML**
- [Python PDF a HTML Código](#python-pdf-to-html)
- [Python PDF a HTML API](#python-pdf-to-html)
- [Python PDF a HTML Programáticamente](#python-pdf-to-html)
- [Python PDF a HTML Biblioteca](#python-pdf-to-html)
- [Python Guardar PDF como HTML](#python-pdf-to-html)
- [Python Generar HTML desde PDF](#python-pdf-to-html)
- [Python Crear HTML desde PDF](#python-pdf-to-html)

- [Python PDF a HTML Convertidor](#python-pdf-to-html)