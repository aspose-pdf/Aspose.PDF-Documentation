---
title: Agregar archivos adjuntos a PDF en Python
linktitle: Agregar un adjunto a un documento PDF
type: docs
weight: 10
url: /es/python-net/add-attachment-to-pdf-document/
description: Aprenda cómo agregar archivos adjuntos a documentos PDF en Python usando Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar archivos adjuntos a PDF con Python
Abstract: Este artículo brinda una guía paso a paso sobre cómo agregar adjuntos a un archivo PDF usando Python y la biblioteca Aspose.PDF. Detalla el proceso de configurar un nuevo proyecto Python, importar el paquete necesario de Aspose.PDF y crear un objeto `Document`. El artículo explica cómo crear un objeto `FileSpecification` con el archivo y la descripción deseados, y cómo agregar este objeto a la `EmbeddedFileCollection` del documento PDF mediante el método `add`. La `EmbeddedFileCollection` contiene todos los adjuntos dentro del PDF. Se incluye un fragmento de código para demostrar el proceso de abrir un documento, configurar un archivo para adjuntar, añadirlo a la colección de adjuntos del documento y guardar el PDF actualizado.
---

Los adjuntos pueden contener una amplia variedad de información y pueden ser de diferentes tipos de archivo. Este artículo explica cómo agregar un adjunto a un archivo PDF.

Utilice archivos adjuntos PDF incrustados cuando necesite empaquetar archivos fuente de soporte, hojas de cálculo, imágenes o documentos relacionados junto con el PDF principal.

1. Cree un nuevo proyecto Python.
1. Importe el paquete Aspose.PDF
1. Cree un [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto.
1. Cree un [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) objeto con el archivo que estás añadiendo y la descripción del archivo.
1. Agregar el [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) objeto al [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) del objeto [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) colección, con la de la colección [agregar](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) método.

El [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) La colección contiene todos los archivos adjuntos en el archivo PDF. El siguiente fragmento de código muestra cómo agregar un archivo adjunto en un documento PDF.

```python
from os import path
import aspose.pdf as ap

def add_attachments(infile, attachment_path, outfile):
    with ap.Document(infile) as document:
        file_spec = ap.FileSpecification(attachment_path, "Sample text file")
        document.embedded_files.add(path.basename(attachment_path), file_spec)
        document.save(outfile)
```

## Temas relacionados con archivos adjuntos

- [Trabajar con archivos adjuntos PDF en Python](/pdf/es/python-net/attachments/)
- [Eliminar archivos adjuntos de PDF en Python](/pdf/es/python-net/removing-attachment-from-an-existing-pdf/)
- [Crear y gestionar portafolios PDF en Python](/pdf/es/python-net/portfolio/)

