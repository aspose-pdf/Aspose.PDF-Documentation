---
title: Agregar un adjunto a un documento PDF usando Python
linktitle: Agregar un adjunto a un documento PDF
type: docs
weight: 10
url: /es/python-net/add-attachment-to-pdf-document/
description: Esta página describe cómo agregar un adjunto a un archivo PDF con Aspose.PDF para Python a través de la biblioteca .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar adjuntos a PDF con Python
Abstract: Este artículo ofrece una guía paso a paso sobre cómo agregar adjuntos a un archivo PDF usando Python y la biblioteca Aspose.PDF. Detalla el proceso de configurar un nuevo proyecto Python, importar el paquete necesario de Aspose.PDF y crear un objeto `Document`. El artículo explica cómo crear un objeto `FileSpecification` con el archivo deseado y la descripción, y cómo agregar este objeto a la `EmbeddedFileCollection` del documento PDF mediante el método `add`. La `EmbeddedFileCollection` contiene todos los adjuntos dentro del PDF. Se incluye un fragmento de código para demostrar el proceso de abrir un documento, configurar un archivo para adjuntar, añadirlo a la colección de adjuntos del documento y guardar el PDF actualizado.
---

Los adjuntos pueden contener una amplia variedad de información y pueden ser de diversos tipos de archivo. Este artículo explica cómo agregar un adjunto a un archivo PDF.

1. Crear un nuevo proyecto Python.
1. Importar el paquete Aspose.PDF
1. Crear un objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 
1. Crear un objeto [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) con el archivo que está añadiendo y la descripción del archivo.
1. Añadir el objeto [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) al objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) en la colección [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) usando el método [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) de la colección.

La colección [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) contiene todos los adjuntos en el archivo PDF. El siguiente fragmento de código le muestra cómo agregar un adjunto en un documento PDF.

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


