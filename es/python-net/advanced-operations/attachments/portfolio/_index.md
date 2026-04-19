---
title: Crear portafolios PDF en Python
linktitle: Portafolio
type: docs
weight: 20
url: /es/python-net/portfolio/
description: Aprenda como crear y administrar portafolios PDF en Python con Aspose.PDF para Python a traves de .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Construya y edite portafolios PDF con archivos incrustados en Python
Abstract: Este articulo explica como crear y administrar portafolios PDF usando Aspose.PDF para Python a traves de .NET. Aprenda como agrupar varios tipos de archivos en un solo portafolio PDF, agregar archivos a una coleccion de documentos y eliminar elementos del portafolio mediante programacion con Python.
---

Crear un portafolio PDF permite consolidar y archivar diferentes tipos de archivos en un único documento coherente. Ese documento puede incluir archivos de texto, imágenes, hojas de cálculo, presentaciones y otros materiales, y garantiza que todo el material relevante se almacene y organice en un solo lugar.

El portafolio PDF le ayudará a mostrar su presentación de manera de alta calidad, dondequiera que lo use. En general, crear un portafolio PDF es una tarea muy actual y moderna.

Utilice un portafolio PDF cuando desee distribuir una colección de archivos relacionados juntos, manteniendo cada archivo en su formato original dentro de un contenedor PDF.

## Como crear un portafolio PDF

Aspose.PDF para Python a traves de .NET permite crear documentos de portafolio PDF usando la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Agregue un archivo a un objeto `document.collection` despues de obtenerlo con la clase [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/). Cuando se hayan agregado los archivos, use el metodo [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de la clase `Document` para guardar el documento de portafolio.

El siguiente ejemplo usa un archivo de Microsoft Excel, un documento de Word y un archivo de imagen para crear un portafolio PDF.

El código a continuación produce el siguiente portafolio.

### Un portafolio PDF creado con Aspose.PDF para Python

![Un portafolio PDF creado con Aspose.PDF para Python](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(output_pdf)
```

## Eliminar archivos del portafolio PDF

Para eliminar/quitar archivos del portafolio PDF, intente usar las siguientes líneas de código.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    document.collection.delete()

    # Save updated file
    document.save(output_pdf)
```

## Temas relacionados con archivos adjuntos

- [Trabajar con archivos adjuntos PDF en Python](/pdf/es/python-net/attachments/)
- [Agregar archivos adjuntos al PDF en Python](/pdf/es/python-net/add-attachment-to-pdf-document/)
- [Eliminar archivos adjuntos de PDF en Python](/pdf/es/python-net/removing-attachment-from-an-existing-pdf/)

