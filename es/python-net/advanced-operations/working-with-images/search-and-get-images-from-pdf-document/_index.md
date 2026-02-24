---
title: Obtener y buscar imágenes en PDF
linktitle: Obtener y buscar imágenes
type: docs
weight: 40
url: /es/python-net/search-and-get-images-from-pdf-document/
description: Aprenda cómo buscar y obtener imágenes del documento PDF en Python usando Aspose.PDF.
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: Buscar y extraer imágenes de PDF
Abstract: La biblioteca Aspose.PDF para Python mediante .NET ofrece capacidades robustas para buscar y extraer imágenes de documentos PDF. Utilizando la clase 'ImagePlacementAbsorber', los desarrolladores pueden localizar y acceder de manera eficiente a las imágenes incrustadas en todas las páginas de un PDF.
---

## Inspeccionar propiedades de ubicación de imágenes en una página PDF

Este ejemplo muestra cómo analizar y mostrar las propiedades de todas las imágenes en una página PDF específica usando Aspose.PDF para Python mediante .NET.

1. Crear un 'ImagePlacementAbsorber' para recopilar todas las imágenes de la página.
1. Llamar a 'document.pages[1].accept(absorber)' para analizar la ubicación de imágenes en la primera página.
1. Recorrer 'absorber.image_placements' y mostrar las propiedades clave de cada imagen:
- Ancho y alto (puntos).
- Coordenadas X (LLX) e Y (LLY) inferiores.
- Resolución horizontal (X) y vertical (Y) (DPI).

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        # Display image placement properties for all placements
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## Extraer y contar tipos de imágenes en un PDF

Esta función analiza todas las imágenes en la primera página de un PDF y cuenta cuántas son en escala de grises y cuántas son RGB.

1. Crear un 'ImagePlacementAbsorber' para recopilar todas las imágenes de la página.
1. Inicializar contadores para imágenes en escala de grises y RGB.
1. Llamar a 'document.pages[1].accept(absorber)' para analizar la ubicación de imágenes.
1. Imprimir el número total de imágenes encontradas.
1. Recorrer cada imagen en 'absorber.image_placements':
- Obtener el tipo de color de la imagen usando 'image_placement.image.get_color_type()'.
- Incrementar el contador correspondiente (escala de grises o rgb).
- Imprimir un mensaje para cada imagen indicando si es en escala de grises o RGB.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
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
```

## Extraer información detallada de imágenes de un PDF

Esta función analiza todas las imágenes en la primera página de un PDF y calcula sus dimensiones escaladas y resolución efectiva basándose en las transformaciones gráficas de la página.

1. Cargar PDF e inicializar variables
1. Recopilar recursos de imágenes
1. Procesar operadores de contenido de la página:
- 'GSave' - empujar la CTM actual a la pila.
- 'GRestore' - sacar la última CTM de la pila.
- 'ConcatenateMatrix' - actualizar la CTM actual multiplicándola con la matriz del operador.
1. Imprimir el nombre de la imagen, dimensiones escaladas y resolución calculada.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)

    default_resolution = 72
    graphics_state = []

    image_names = list(document.pages[1].resources.images.names)

    graphics_state.append(drawing.drawing2d.Matrix(float(1), float(0), float(0), float(1), float(0), float(0)))

    for op in document.pages[1].contents:
        if is_assignable(op, ap.operators.GSave):
            graphics_state.append(cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone())

        elif is_assignable(op, ap.operators.GRestore):
            graphics_state.pop()

        elif is_assignable(op, ap.operators.ConcatenateMatrix):
            opCM = cast(ap.operators.ConcatenateMatrix, op)
            cm = drawing.drawing2d.Matrix(
                float(opCM.matrix.a),
                float(opCM.matrix.b),
                float(opCM.matrix.c),
                float(opCM.matrix.d),
                float(opCM.matrix.e),
                float(opCM.matrix.f),
            )

            graphics_state[-1].multiply(cm)
            continue

        elif is_assignable(op, ap.operators.Do):
            opDo = cast(ap.operators.Do, op)
            if opDo.name in image_names:
                last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                index = image_names.index(opDo.name) + 1
                image = document.pages[1].resources.images[index]

                scaled_width = math.sqrt(last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2)
                scaled_height = math.sqrt(last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2)

                original_width = image.width
                original_height = image.height

                res_horizontal = original_width * default_resolution / scaled_width
                res_vertical = original_height * default_resolution / scaled_height

                print(
                    f"{self.data_dir}image {opDo.name} "
                    f"({scaled_width:.2f}:{scaled_height:.2f}): "
                    f"res {res_horizontal:.2f} x {res_vertical:.2f}"
                )
```

## Extraer texto alternativo de imágenes en un PDF

Esta función recupera el texto alternativo (alt text) de todas las imágenes en la primera página de un PDF, útil para la accesibilidad y verificaciones de conformidad PDF/UA.

1. Cargar el documento PDF usando 'ap.Document()'.
1. Crear un 'ImagePlacementAbsorber' para recopilar todas las imágenes de la página.
1. Aceptar el absorber en la primera página (page.accept(absorber)).
1. Recorrer cada imagen en 'absorber.image_placements':
- Imprimir el nombre de la imagen en la colección de recursos de la página (get_name_in_collection()).
- Recuperar el texto alternativo usando 'get_alternative_text(page)'.
- Imprimir la primera línea del texto alternativo.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: "
            + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```
