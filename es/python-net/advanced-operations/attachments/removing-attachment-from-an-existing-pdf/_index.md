---
title: Eliminar archivo adjunto de PDF usando Python
linktitle: Eliminar archivo adjunto de un PDF existente
type: docs
weight: 30
url: /es/python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF puede eliminar archivos adjuntos de sus documentos PDF. Use la API de PDF de Python para eliminar archivos adjuntos en archivos PDF usando Aspose.PDF para Python a través de la biblioteca .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo eliminar archivos adjuntos de PDF con Python
Abstract: Este artículo analiza cómo eliminar archivos adjuntos de archivos PDF usando Aspose.PDF para Python. Los archivos adjuntos en un documento PDF se almacenan dentro de la colección `EmbeddedFiles` del objeto `Document`. Para eliminar todos los archivos adjuntos de un PDF, puede invocar el método `delete()` en la colección `EmbeddedFiles` y luego guardar el documento actualizado usando el método `save()` del objeto `Document`. Se proporciona un fragmento de código para demostrar este proceso, mostrando los pasos de abrir un documento, eliminar sus archivos adjuntos y guardar el archivo modificado.
---

Aspose.PDF para Python puede eliminar archivos adjuntos de archivos PDF. Los archivos adjuntos de un documento PDF se almacenan en la colección [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) del objeto Document.

Para eliminar todos los archivos adjuntos asociados a un archivo PDF:

1. Llame al método [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) de la colección [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/).
1. Guarde el archivo actualizado usando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

El siguiente fragmento de código muestra cómo eliminar archivos adjuntos de un documento PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all attachments
    document.embedded_files.delete()

    # Save updated file
    document.save(output_pdf)
```


