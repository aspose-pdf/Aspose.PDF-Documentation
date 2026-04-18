---
title: Extraer imágenes de PDF usando Python
linktitle: Extraer imágenes de PDF
type: docs
weight: 20
url: /es/python-net/extract-images-from-the-pdf-file/
description: Aprenda cómo extraer imágenes incrustadas de archivos PDF con Aspose.PDF for Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer imágenes de PDF vía Python
Abstract: Este artículo explica cómo extraer imágenes incrustadas de un documento PDF con Aspose.PDF for Python. Cubre la apertura del PDF de origen con la clase Document, el acceso a una imagen de la colección de recursos de la página y la guardado de la XImage extraída en un archivo externo para reutilización, inspección o procesamiento posterior.
---

Usar [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para abrir el PDF, luego acceder a los recursos de la página para recuperar un [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximage/) objeto y guárdelo como un archivo separado. Este enfoque es útil cuando necesita reutilizar imágenes, inspeccionar los recursos extraídos o crear flujos de trabajo de procesamiento de imágenes a partir del contenido PDF.

1. Abra el PDF como un `Document`.
1. Acceda al recurso de imagen de la página objetivo.
1. Recuperar lo requerido `XImage` de la colección de imágenes de la página.
1. Guarde la imagen extraída en un archivo de salida.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```
