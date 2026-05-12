---
title: Reemplazar imagen en archivo PDF existente usando Python
linktitle: Reemplazar imagen
type: docs
weight: 70
url: /es/python-net/replace-image-in-existing-pdf-file/
description: Aprenda cómo reemplazar imágenes incrustadas en archivos PDF existentes con Python.
lastmod: "2026-05-05"
TechArticle: true
AlternativeHeadline: Reemplazar imágenes en archivos PDF existentes con Python
Abstract: Este artículo muestra cómo reemplazar imágenes en documentos PDF con Aspose.PDF for Python via .NET. Cubre el reemplazo de una imagen por índice de recurso y el reemplazo de una imagen específica encontrada con ImagePlacementAbsorber.
---

## Reemplazar una imagen en PDF

Utilice esta página cuando necesite actualizar logotipos, diagramas u otros gráficos incrustados en un PDF sin reconstruir el diseño del documento.

1. Cargar el PDF de origen con `ap.Document(infile)`.
1. Abra la imagen de reemplazo como un flujo binario.
1. Reemplace un recurso de imagen por índice en una página.
1. Guarda el PDF actualizado.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image(infile, image_file, outfile):
    document = ap.Document(infile)

    with FileIO(image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(outfile)
```

## Reemplazar una imagen específica

Este ejemplo reemplaza una ubicación de imagen específica encontrada por `ImagePlacementAbsorber`.

1. Cargar el PDF de origen.
1. Crear `ImagePlacementAbsorber` y recopilar las ubicaciones de imágenes en la página.
1. Verifique si existen ubicaciones de imágenes en la página.
1. Reemplace la ubicación seleccionada con una nueva secuencia de imagen.
1. Guarda el PDF actualizado.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image_with_absorber(infile, image_file, outfile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(outfile)
```

## Temas de imágenes relacionadas

- [Trabajar con imágenes en PDF usando Python](/pdf/es/python-net/working-with-images/)
- [Eliminar imágenes de archivos PDF](/pdf/es/python-net/delete-images-from-pdf-file/)
- [Extraer imágenes de archivos PDF](/pdf/es/python-net/extract-images-from-pdf-file/)
- [Agregar imágenes a archivos PDF existentes](/pdf/es/python-net/add-image-to-existing-pdf-file/)
