---
title: Convertir HTML a PDF en Python
linktitle: Convertir archivo HTML a PDF
type: docs
weight: 40
url: /es/python-java/convert-html-to-pdf/
lastmod: "2023-04-06"
description: Este tema le muestra cómo convertir HTML a PDF y MHTML a PDF usando Aspose.PDF. para Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Descripción general

Aspose.PDF para Python a través de Java es una solución profesional que le permite crear archivos PDF a partir de páginas web y código HTML sin procesar en sus aplicaciones.

Este artículo explica cómo **convertir HTML a PDF usando Python**. Cubre los siguientes temas.

_Formato_: **HTML**
- [Python HTML a PDF](#python-html-to-pdf)
- [Python Convertir HTML a PDF](#python-html-to-pdf)
- [Python Cómo convertir HTML a PDF](#python-html-to-pdf)

## Conversión de HTML a PDF en Python

**Aspose.PDF para Python** es una API de manipulación de PDF que le permite convertir cualquier documento HTML existente a PDF sin problemas. El proceso de convertir HTML a PDF se puede personalizar de manera flexible.

## Convertir HTML a PDF

El siguiente ejemplo de código en Python muestra cómo convertir un documento HTML a un PDF.

1. Cree una instancia de la clase [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
2. Inicialice el objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
3. Guarde el documento PDF de salida llamando al método **Document.Save()**.

```python

from asposepdf import Api


# inicializar licencia
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# conversión desde matriz de bytes
documentName = "input.html"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array, Api.LoadFormat.HTML)
documentOutName = "result_fromHtml.pdf"
doc.save(documentOutName)

# conversión desde archivo
documentName = "input.html"
doc = Api.Document(documentName, Api.LoadFormat.HTML)
documentOutName = "result2_fromHtml.pdf"
doc.save(documentOutName)
```

{{% alert color="success" %}}
**Intenta convertir HTML a PDF en línea**


Aspose te presenta la aplicación gratuita en línea ["HTML a PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de HTML a PDF usando la aplicación gratuita](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}