---
title: Extraer imágenes de un archivo PDF usando Python
linktitle: Extraer imágenes
type: docs
weight: 30
url: /es/python-net/extract-images-from-pdf-file/
description: Aprenda cómo extraer imágenes incrustadas de archivos PDF en Python.
lastmod: "2026-05-05"
TechArticle: true
AlternativeHeadline: Extraer imágenes de archivos PDF con Python
Abstract: Este artículo muestra cómo extraer imágenes de documentos PDF con Aspose.PDF for Python via .NET. Cubre la extracción de una única imagen incrustada y la exportación de imágenes encontradas dentro de una región rectangular específica en una página.
---

Utilice esta página cuando necesite reutilizar gráficos incrustados, archivar recursos de imágenes o procesar contenido de imágenes fuera del PDF.

1. Cargar el PDF de origen con `ap.Document(infile)`.
1. Seleccione la página objetivo y el índice del recurso de imagen.
1. Guarde el objeto de imagen en un flujo de salida.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image(infile, outfile):
    document = ap.Document(infile)
    x_image = document.pages[1].resources.images[1]
    with FileIO(outfile, "wb") as output_image:
        x_image.save(output_image)
```

## Extraer imágenes de una región específica en PDF

Este ejemplo extrae imágenes ubicadas dentro de una región rectangular especificada en una página PDF y las guarda como archivos separados.

1. Cargar el PDF de origen.
1. Crear `ImagePlacementAbsorber` y aceptarlo en la página de destino.
1. Define el rectángulo de destino.
1. Itera a través de las colocaciones de imágenes y verifica si los límites de cada imagen encajan en la región.
1. Guardar imágenes coincidentes en archivos de salida.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image_from_specific_region(infile, outfile):
    document = ap.Document(infile)
    rectangle = ap.Rectangle(0, 0, 590, 590, True)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(image_placement.rectangle.llx, image_placement.rectangle.lly)
        point2 = ap.Point(image_placement.rectangle.urx, image_placement.rectangle.ury)

        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(outfile.replace("index", str(index)), "wb") as output_image:
                image_placement.image.save(output_image)
            index += 1
```

## Temas de imágenes relacionadas

- [Trabajar con imágenes en PDF usando Python](/pdf/es/python-net/working-with-images/)
- [Reemplazar imágenes en archivos PDF existentes](/pdf/es/python-net/replace-image-in-existing-pdf-file/)
- [Eliminar imágenes de archivos PDF](/pdf/es/python-net/delete-images-from-pdf-file/)
- [Agregar imágenes a archivos PDF existentes](/pdf/es/python-net/add-image-to-existing-pdf-file/)
