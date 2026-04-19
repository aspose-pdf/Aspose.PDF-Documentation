---
title: Agregar fondos PDF en Python
linktitle: Agregar fondos
type: docs
weight: 20
url: /es/python-net/add-backgrounds/
description: Aprenda como agregar una imagen de fondo a las paginas PDF en Python utilizando la clase BackgroundArtifact en Aspose.PDF para Python a traves de .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar fondo a un PDF con Python
Abstract: Este articulo analiza el uso de imagenes de fondo en documentos PDF utilizando Aspose.PDF para Python a traves de .NET. Destaca la capacidad de agregar marcas de agua o diseños sutiles a los documentos mediante la clase `BackgroundArtifact`, que permite la incorporacion de imagenes de fondo en objetos de pagina individuales. El articulo proporciona un ejemplo de codigo practico que muestra como implementar esta funcionalidad. El proceso implica crear un nuevo documento PDF, agregar una pagina, crear un objeto `BackgroundArtifact`, establecer una imagen de fondo y adjuntar el artefacto de fondo a la coleccion de artefactos de la pagina. Finalmente, el documento modificado se guarda como un archivo PDF. Esta tecnica permite una presentacion visual mejorada de los documentos PDF.
---

Las imagenes de fondo pueden usarse para agregar una marca de agua u otro diseño sutil a los documentos. En Aspose.PDF para Python a traves de .NET, cada documento PDF es una coleccion de paginas y cada pagina contiene una coleccion de artefactos. La clase [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) puede usarse para agregar una imagen de fondo a un objeto de pagina.

Este enfoque es útil cuando necesitas colocar una imagen decorativa detrás del contenido principal del PDF sin convertirla en texto buscable del documento.

El siguiente fragmento de código muestra cómo agregar una imagen de fondo a páginas PDF usando el objeto BackgroundArtifact con Python.

```python
import aspose.pdf as ap
import io


def add_background_image(input_image_file, output_pdf):
    # Create a new PDF document
    document = ap.Document()

    # Add a blank page to the document
    page = document.pages.add()

    # Create a BackgroundArtifact object
    background = ap.BackgroundArtifact()

    # Load the image as a binary stream
    with open(input_image_file, "rb") as image_stream:
        background.background_image = image_stream

        # Add the background artifact to the page
        page.artifacts.append(background)

    # Save the resulting PDF
    document.save(output_pdf)
```

## Temas relacionados con artefactos

- [Trabajar con artefactos PDF en Python](/pdf/es/python-net/artifacts/)
- [Agregar marcas de agua a PDF en Python](/pdf/es/python-net/add-watermarks/)
- [Agregar numeración Bates al PDF en Python](/pdf/es/python-net/add-bates-numbering/)
- [Contar tipos de artefactos en archivos PDF](/pdf/es/python-net/counting-artifacts/)

