---
title: Agregar archivos adjuntos a PDF en Python
linktitle: Agregar un archivo adjunto a un documento PDF
type: docs
weight: 10
url: /es/python-net/add-attachment-to-pdf-document/
description: Aprenda como agregar archivos adjuntos a documentos PDF en Python usando Aspose.PDF para Python a traves de .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar archivos adjuntos a PDF con Python
Abstract: Este artículo ofrece una guía paso a paso sobre cómo agregar archivos adjuntos a un archivo PDF usando Python y la biblioteca Aspose.PDF. Detalla el proceso de configurar un nuevo proyecto Python, importar el paquete necesario de Aspose.PDF y crear un objeto `Document`. El artículo explica cómo crear un objeto `FileSpecification` con el archivo y la descripción deseados, y cómo agregar este objeto a la `EmbeddedFileCollection` del documento PDF usando el método `add`. La `EmbeddedFileCollection` contiene todos los archivos adjuntos dentro del PDF. Se incluye un fragmento de código para demostrar el proceso de abrir un documento, configurar un archivo para adjuntar, agregarlo a la colección de adjuntos del documento y guardar el PDF actualizado.
---

Los archivos adjuntos pueden contener una amplia variedad de información y pueden ser de diversos tipos de archivo. Este artículo explica cómo agregar un archivo adjunto a un archivo PDF.

Utilice archivos adjuntos PDF incrustados cuando necesite empaquetar archivos fuente de soporte, hojas de cálculo, imágenes o documentos relacionados junto con el PDF principal.

1. Cree un nuevo proyecto Python.
1. Importe el paquete Aspose.PDF
1. Cree un objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Cree un objeto [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) con el archivo que va a agregar y la descripcion del archivo.
1. Agregue el objeto [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) a la coleccion [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) mediante el metodo [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods).

La coleccion [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) contiene todos los archivos adjuntos del archivo PDF. El siguiente fragmento de codigo muestra como agregar un archivo adjunto a un documento PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Setup new file to be added as attachment
    fileSpecification = ap.FileSpecification(attachment_file, "Sample text file")

    # Add attachment to document's attachment collection
    document.embedded_files.append(fileSpecification)

    # Save new output
    document.save(output_pdf)
```

## Temas relacionados con archivos adjuntos

- [Trabajar con archivos adjuntos PDF en Python](/pdf/es/python-net/attachments/)
- [Eliminar archivos adjuntos de PDF en Python](/pdf/es/python-net/removing-attachment-from-an-existing-pdf/)
- [Crear y administrar portafolios PDF en Python](/pdf/es/python-net/portfolio/)

