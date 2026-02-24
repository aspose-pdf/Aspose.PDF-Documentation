---
title: Extraer imágenes de PDF usando Python
linktitle: Extraer imágenes de PDF
type: docs
weight: 20
url: /es/python-net/extract-images-from-the-pdf-file/
description: Cómo extraer una parte de la imagen de un PDF usando Aspose.PDF para Python
lastmod: "2023-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer imágenes de PDF vía Python
Abstract: Este artículo ofrece una guía concisa sobre cómo extraer imágenes incrustadas de un documento PDF usando Python. El proceso implica tres pasos principales cargar el documento PDF, acceder al recurso de la imagen y guardar la imagen en un archivo. El fragmento de código utiliza la biblioteca Aspose.PDF para facilitar estas operaciones. Inicialmente, el documento PDF se carga desde una ruta especificada, y la imagen deseada se accede desde los recursos de la primera página. Finalmente, la imagen se guarda en un archivo de salida especificado mediante una operación de E/S de archivos, lo que permite un análisis, edición o reutilización adicional en otros documentos.
---

Este fragmento de código extrae imágenes incrustadas de un documento PDF para su análisis, edición o reutilización en otros documentos:

1. Cargar el documento PDF
1. Acceder al recurso de la imagen
1. Guardar la imagen en un archivo

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

