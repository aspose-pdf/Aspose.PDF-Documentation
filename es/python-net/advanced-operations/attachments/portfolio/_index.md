---
title: Crear portafolios PDF en Python
linktitle: Portafolio
type: docs
weight: 20
url: /es/python-net/portfolio/
description: Aprenda cómo crear y administrar portafolios PDF en Python con Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cree y edite portafolios PDF con archivos incrustados en Python
Abstract: Este artículo explica cómo crear y administrar portafolios PDF usando Aspose.PDF for Python via .NET. Aprenda cómo agrupar varios tipos de archivos en un único portafolio PDF, agregar archivos a una colección de documentos y eliminar elementos del portafolio de forma programática con Python.
---

Crear un portafolio PDF permite consolidar y archivar diferentes tipos de archivos en un único documento coherente. Ese documento puede incluir archivos de texto, imágenes, hojas de cálculo, presentaciones y otros materiales, y garantiza que todo el material relevante se almacene y organice en un solo lugar.

El portafolio PDF ayudará a mostrar su presentación de manera de alta calidad, dondequiera que lo utilice. En general, crear un portafolio PDF es una tarea muy actual y moderna.

Utilice un portafolio PDF cuando desee distribuir una colección de archivos relacionados juntos, manteniendo cada archivo en su formato original dentro de un contenedor PDF.

## Cómo crear un portafolio PDF

Aspose.PDF for Python via .NET permite crear documentos de portafolio PDF usando el [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase. Añada un archivo en un document.collection objeto después de obtenerlo con la [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) clase. Cuando los archivos se hayan añadido, use la Document clase' [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método para guardar el documento del portafolio.

El siguiente ejemplo utiliza un archivo Microsoft Excel, un documento Word y un archivo de imagen para crear un PDF Portfolio.

El código a continuación da como resultado el siguiente portafolio.

### Un PDF Portfolio creado con Aspose.PDF for Python

![Un PDF Portfolio creado con Aspose.PDF for Python](working-with-pdf-portfolio_1.jpg)

```python
import aspose.pdf as ap

def create_pdf_portfolio(input_files, outfile):
    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_files[0])
    word = ap.FileSpecification(input_files[1])
    image = ap.FileSpecification(input_files[2])

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(outfile)
```

## Eliminar archivos del Portafolio PDF

Para eliminar/quitar archivos del portafolio PDF, intenta usar las siguientes líneas de código.

```python
import aspose.pdf as ap

def remove_files_from_pdf_portfolio(infile, outfile):
    # Open document
    document = ap.Document(infile)
    document.collection.delete()

    # Save updated file
    document.save(outfile)
```

## Temas relacionados con archivos adjuntos

- [Trabajar con archivos adjuntos PDF en Python](/pdf/es/python-net/attachments/)
- [Agregar archivos adjuntos a PDF en Python](/pdf/es/python-net/add-attachment-to-pdf-document/)
- [Eliminar archivos adjuntos de PDF en Python](/pdf/es/python-net/removing-attachment-from-an-existing-pdf/)

