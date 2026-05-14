---
title: Dividir archivos PDF en Python
linktitle: Dividir archivos PDF
type: docs
weight: 60
url: /es/python-net/split-pdf-document/
description: Aprenda cómo dividir páginas PDF en archivos PDF separados en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dividir páginas PDF usando Python
Abstract: El artículo analiza el proceso de dividir páginas PDF en archivos individuales usando Python, destacando la utilidad de esta función para gestionar documentos PDF grandes. Hace referencia al Aspose.PDF Splitter, una herramienta en línea diseñada para demostrar la funcionalidad de división de PDF. El artículo proporciona un método detallado para lograrlo en aplicaciones Python, que implica iterar a través de las páginas de un documento PDF mediante la `PageCollection` del objeto `Document`. Para cada página, se crea un nuevo objeto `Document`, se añade la página a este, y el nuevo archivo PDF se guarda usando el método `save()`. Un fragmento de código Python adjunto ilustra este proceso, mostrando los pasos necesarios para dividir un documento PDF en archivos separados al iterar por sus páginas y guardar cada una como un PDF individual.
---

Dividir páginas PDF puede ser una función útil para quienes necesitan separar un archivo grande en páginas individuales o grupos de páginas.

Utilice este flujo de trabajo cuando necesite dividir documentos PDF grandes en archivos de una sola página o en conjuntos más pequeños para distribución, revisión o procesamiento posterior.

## Ejemplo en vivo

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) es una aplicación web gratuita en línea que le permite comprobar cómo funciona la división de archivos PDF.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Este tema muestra cómo dividir páginas de PDF en archivos PDF individuales en sus aplicaciones Python. Para dividir páginas de PDF en archivos PDF de una sola página usando Python, se pueden seguir los siguientes pasos:

1. Recorra las páginas del documento PDF mediante la colección [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Para cada iteración, cree un nuevo objeto `Document` y agregue el objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) al documento vacío
1. Guarde el nuevo PDF usando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)

## Dividir PDF en varios archivos o PDFs separados en Python

El siguiente fragmento de código Python muestra cómo dividir las páginas PDF en archivos PDF individuales.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    page_count = 1

    # Loop through all the pages
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1
```

## Temas relacionados del documento

- [Trabajar con documentos PDF en Python](/pdf/es/python-net/working-with-documents/)
- [Combinar archivos PDF en Python](/pdf/es/python-net/merge-pdf-documents/)
- [Optimizar archivos PDF en Python](/pdf/es/python-net/optimize-pdf/)
- [Manipular documentos PDF en Python](/pdf/es/python-net/manipulate-pdf-document/)
