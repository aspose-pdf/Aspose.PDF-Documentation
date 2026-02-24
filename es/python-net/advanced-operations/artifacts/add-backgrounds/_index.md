---
title: Trabajando con fondos como artefactos con Python
linktitle: Añadiendo fondos
type: docs
weight: 20
url: /es/python-net/add-backgrounds/
description: Añade una imagen de fondo a tu archivo PDF con Python. Usa la clase BackgroundArtifact.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo añadir fondo a un PDF con Python
Abstract: Este artículo analiza el uso de imágenes de fondo en documentos PDF utilizando Aspose.PDF para Python a través de .NET. Destaca la capacidad de añadir marcas de agua o diseños sutiles a los documentos mediante la clase `BackgroundArtifact`, que permite la incorporación de imágenes de fondo en objetos de página individuales. El artículo proporciona un ejemplo práctico de código que muestra cómo implementar esta función. El proceso implica crear un nuevo documento PDF, añadir una página, crear un objeto `BackgroundArtifact`, establecer una imagen de fondo y agregar el artefacto de fondo a la colección de artefactos de la página. Finalmente, el documento modificado se guarda como un archivo PDF. Esta técnica permite una presentación visual mejorada de los documentos PDF.
---

Las imágenes de fondo pueden usarse para añadir una marca de agua, u otro diseño sutil, a los documentos. En Aspose.PDF para Python a través de .NET, cada documento PDF es una colección de páginas y cada página contiene una colección de artefactos. La clase [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) puede usarse para añadir una imagen de fondo a un objeto de página.

El siguiente fragmento de código muestra cómo añadir una imagen de fondo a páginas PDF usando el objeto BackgroundArtifact con Python.

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


