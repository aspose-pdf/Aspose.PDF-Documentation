---
title: Obtener y buscar imágenes en PDF
linktitle: Obtener y buscar imágenes
type: docs
weight: 40
url: /es/python-net/search-and-get-images-from-pdf-document/
description: Aprenda cómo buscar e inspeccionar imágenes en documentos PDF con Python.
lastmod: "2026-04-17"
TechArticle: true
AlternativeHeadline: Buscar e inspeccionar imágenes en archivos PDF con Python
Abstract: Este artículo muestra cómo buscar e inspeccionar imágenes en documentos PDF con Aspose.PDF for Python via .NET. Cubre el uso de ImagePlacementAbsorber para analizar la ubicación de la imagen, el tamaño, la resolución y el texto alternativo.
---

## Inspeccionar las propiedades de ubicación de la imagen en una página PDF

Este ejemplo demuestra cómo analizar y mostrar las propiedades de todas las imágenes en una página PDF específica usando Aspose.PDF for Python via .NET.

Utilice esta página cuando necesite auditar la ubicación de las imágenes, inspeccionar la resolución de la imagen o identificar objetos de imagen incrustados en distintas páginas PDF.

1. Crea un 'ImagePlacementAbsorber' para recopilar todas las imágenes en la página.
1. Llama a 'document.pages[1].accept(absorber)' para analizar la ubicación de las imágenes en la primera página.
1. Itera a través de 'absorber.image_placements' y muestra las propiedades clave de cada imagen:
    - Ancho y Alto (puntos).
    - Coordenadas X (LLX) e Y (LLY) de la esquina inferior izquierda.
    - Resolución horizontal (X) y vertical (Y) (DPI).

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_params(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## Extraer y contar tipos de imagen en un PDF

Esta función analiza todas las imágenes en la primera página de un PDF y cuenta cuántas son imágenes en escala de grises y RGB.

1. Crea un 'ImagePlacementAbsorber' para recopilar todas las imágenes en la página.
1. Inicializar contadores para imágenes en escala de grises y RGB.
1. Llame a 'document.pages[1].accept(absorber)' para analizar la ubicación de las imágenes.
1. Imprima el número total de imágenes encontradas.
1. Itere a través de cada imagen en 'absorber.image_placements':
    - Obtenga el tipo de color de la imagen usando 'image_placement.image.get_color_type()'.
    - Incrementa el contador correspondiente (grayscaled o rgb).
    - Imprime un mensaje para cada imagen indicando si es en escala de grises o RGB.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_types_from_pdf(infile):
    """
    Extract and count image types (grayscale/RGB) with resolution analysis.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_image_types_from_pdf("sample_extr.pdf")

    Note:
        Prints total images count, color type for each image, and resolution info.
    """

    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()

    # Counters for grayscale and RGB images
    grayscaled = 0
    rgb = 0

    document.pages[1].accept(absorber)

    print("--------------------------------")
    print("Total Images = " + str(len(absorber.image_placements)))

    image_counter = 1

    for image_placement in absorber.image_placements:
        # Determine the color type of the image
        colorType = image_placement.image.get_color_type()
        if colorType == ap.ColorType.GRAYSCALE:
            grayscaled += 1
            print(f"Image {image_counter} is Grayscale...")
        elif colorType == ap.ColorType.RGB:
            rgb += 1
            print(f"Image {image_counter} is RGB...")
        image_counter += 1

    print("--------------------------------")
    print("Grayscale Images = " + str(grayscaled))
    print("RGB Images = " + str(rgb))
```

## Extraer información detallada de imágenes de un PDF

Esta función analiza todas las imágenes en la primera página de un PDF y calcula sus dimensiones escaladas y resolución efectiva basándose en las transformaciones gráficas de la página.

1. Cargar PDF e inicializar variables
1. Recopilar recursos de imagen
1. Procesar operadores de contenido de página:
    - 'GSave' - empujar la CTM actual a la pila.
    - 'GRestore' - elimina la última CTM de la pila.
    - 'ConcatenateMatrix' - actualiza la CTM actual multiplicándola por la matriz del operador.
1. Imprime el nombre de la imagen, las dimensiones escaladas y la resolución calculada.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_information_from_pdf(infile):
    with ap.Document(infile) as document:
        default_resolution = 72
        graphics_state = []

        image_names = list(document.pages[1].resources.images.names)

        graphics_state.append(
            drawing.drawing2d.Matrix(
                float(1), float(0), float(0), float(1), float(0), float(0)
            )
        )

        for op in document.pages[1].contents:
            if is_assignable(op, ap.operators.GSave):
                graphics_state.append(
                    cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone()
                )

            elif is_assignable(op, ap.operators.GRestore):
                graphics_state.pop()

            elif is_assignable(op, ap.operators.ConcatenateMatrix):
                op_cm = cast(ap.operators.ConcatenateMatrix, op)
                cm = drawing.drawing2d.Matrix(
                    float(op_cm.matrix.a),
                    float(op_cm.matrix.b),
                    float(op_cm.matrix.c),
                    float(op_cm.matrix.d),
                    float(op_cm.matrix.e),
                    float(op_cm.matrix.f),
                )

                graphics_state[-1].multiply(cm)
                continue

            elif is_assignable(op, ap.operators.Do):
                op_do = cast(ap.operators.Do, op)
                if op_do.name in image_names:
                    last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                    index = image_names.index(op_do.name) + 1
                    image = document.pages[1].resources.images[index]

                    scaled_width = math.sqrt(
                        last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2
                    )
                    scaled_height = math.sqrt(
                        last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2
                    )

                    original_width = image.width
                    original_height = image.height

                    res_horizontal = (
                        original_width * default_resolution / scaled_width
                    )
                    res_vertical = (
                        original_height * default_resolution / scaled_height
                    )

                    info = (
                        f"{infile} image {op_do.name} "
                        f"({scaled_width:.2f}:{scaled_height:.2f}): "
                        f"res {res_horizontal:.2f} x {res_vertical:.2f}\n"
                    )
                    print(info.rstrip())
```

## Extraer texto alternativo de imágenes en un PDF

Esta función recupera el texto alternativo (alt text) de todas las imágenes en la primera página de un PDF, útil para la accesibilidad y las comprobaciones de cumplimiento de PDF/UA.

1. Cargue el documento PDF usando 'ap.Document()'.
1. Crea un 'ImagePlacementAbsorber' para recopilar todas las imágenes en la página.
1. Acepta el absorbente en la primera página (page.accept(absorber)).
1. Itere a través de cada imagen en 'absorber.image_placements':
    - Imprima el nombre de la imagen en la colección de recursos de la página (get_name_in_collection()).
    - Recupera el texto alternativo usando 'get_alternative_text(page)'.
    - Imprime la primera línea del texto alternativo.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_alt_text(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: " + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```

## Temas de imágenes relacionadas

- [Trabajar con imágenes en PDF usando Python](/pdf/es/python-net/working-with-images/)
- [Extraer imágenes de archivos PDF](/pdf/es/python-net/extract-images-from-pdf-file/)
- [Reemplazar imágenes en archivos PDF existentes](/pdf/es/python-net/replace-image-in-existing-pdf-file/)
- [Agregar imágenes a archivos PDF existentes](/pdf/es/python-net/add-image-to-existing-pdf-file/)
