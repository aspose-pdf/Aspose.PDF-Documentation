---
title: Trabajar con Portafolio en PDF usando Python
linktitle: Portafolio
type: docs
weight: 20
url: /es/python-net/portfolio/
description: Cómo crear un Portafolio PDF con Python. Debe usar un archivo de Microsoft Excel, un documento de Word y un archivo de imagen para crear un Portafolio PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo trabajar con Portafolio en PDF con Python
Abstract: Este artículo analiza la creación y gestión de portafolios PDF usando Aspose.PDF para Python a través de .NET. Un portafolio PDF facilita la consolidación de varios tipos de archivos —como archivos de texto, imágenes, hojas de cálculo y presentaciones— en un único documento organizado, garantizando que todos los materiales relevantes se almacenen colectivamente. El artículo describe el proceso de creación de un portafolio PDF, resaltando el uso de la clase `Document` y la clase `FileSpecification` para agregar archivos a una colección de documentos. Se proporciona un ejemplo que muestra la inclusión de un archivo de Microsoft Excel, un documento de Word y un archivo de imagen en un portafolio PDF. Además, el artículo incluye fragmentos de código tanto para crear un portafolio como para eliminar archivos de él, ilustrando la simplicidad y eficiencia de gestionar portafolios PDF con Aspose.PDF para Python.
---

Crear un portafolio PDF permite consolidar y archivar diferentes tipos de archivos en un único documento coherente. Dicho documento puede incluir archivos de texto, imágenes, hojas de cálculo, presentaciones y otros materiales, y garantiza que todo el material relevante se almacene y organise en un solo lugar.

El portafolio PDF ayudará a mostrar su presentación de manera de alta calidad, dondequiera que lo use. En general, crear un portafolio PDF es una tarea muy actual y moderna.

## Cómo crear un Portafolio PDF

Aspose.PDF para Python a través de .NET permite crear documentos de Portafolio PDF usando la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) . Agregue un archivo al objeto document.collection después de obtenerlo con la clase [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) . Cuando los archivos se hayan agregado, use el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de la clase Document para guardar el documento del portafolio.

El siguiente ejemplo usa un archivo de Microsoft Excel, un documento de Word y un archivo de imagen para crear un Portafolio PDF.

El código a continuación produce el siguiente portafolio.

### Un Portafolio PDF creado con Aspose.PDF para Python

![Un Portafolio PDF creado con Aspose.PDF para Python](working-with-pdf-portfolio_1.jpg)

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

## Eliminar archivos del Portafolio PDF

Para eliminar archivos del portafolio PDF, intente usar las siguientes líneas de código.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    document.collection.delete()

    # Save updated file
    document.save(output_pdf)
```


