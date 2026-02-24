---
title: Extraer imágenes de un archivo PDF usando Python
linktitle: Extraer imágenes
type: docs
weight: 30
url: /es/python-net/extract-images-from-pdf-file/
description: Esta sección muestra cómo extraer imágenes de un archivo PDF usando la biblioteca de Python.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Extraer imágenes de PDF con Python
Abstract: Este artículo discute el proceso de extracción de imágenes de archivos PDF utilizando Aspose.PDF para Python. Destaca la utilidad de separar imágenes para propósitos como gestión, archivado, análisis o compartición. El artículo explica que las imágenes dentro de un PDF se almacenan en la colección de recursos de cada página, específicamente en la colección XImage. Para extraer una imagen, los usuarios pueden acceder a una página concreta y recuperar la imagen usando su índice de la colección Images. El objeto XImage devuelto por el índice proporciona un método `save()` para guardar la imagen extraída. Se incluye un fragmento de código para demostrar los pasos necesarios para abrir un documento PDF, extraer una imagen específica de la segunda página usando su índice y guardarla en un archivo.
---

¿Necesita separar imágenes de sus archivos PDF? Para una gestión simplificada, archivado, análisis o compartir imágenes de sus documentos, use **Aspose.PDF for Python** y extraiga imágenes de archivos PDF.

1. Cargue el documento PDF con 'ap.Document()'.
1. Acceda a la página deseada del documento (document.pages[1]).
1. Seleccione la imagen de los recursos de la página (por ejemplo, resources.images[1]).
1. Cree un flujo de salida (FileIO) para el archivo de destino.
1. Guarde la imagen extraída usando 'xImage.save(output_image)'.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

## Extraer imágenes de una región específica en PDF

Este ejemplo extrae imágenes ubicadas dentro de una región rectangular especificada en una página PDF y las guarda como archivos separados.

1. Cargue el documento PDF usando 'ap.Document'.
1. Cree un 'ImagePlacementAbsorber' para recopilar todas las imágenes en la primera página.
1. Llame a 'document.pages[1].accept(absorber)' para analizar la colocación de imágenes.
1. Itere a través de todas las imágenes en 'absorber.image_placements':
- Obtenga el cuadro delimitador de la imagen (llx, lly, urx, ury).
- Verifique si ambas esquinas del rectángulo de la imagen están dentro del rectángulo objetivo (rectangle.contains()).
- Si es verdadero, guarde la imagen en un archivo usando FileIO, reemplazando 'index' en el nombre de archivo con un número secuencial.
1. Incrementa el índice para cada imagen guardada.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    rectangle = ap.Rectangle(0, 0, 590, 590, True)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)
    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(
            image_placement.rectangle.llx, image_placement.rectangle.lly
        )
        point2 = ap.Point(
            image_placement.rectangle.urx, image_placement.rectangle.urx
        )
        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(path_outfile.replace("index", str(index)), "w") as output_image:
                image_placement.image.save(output_image)
            index = index + 1
```

## Extraer información de imagen de PDF

El ejemplo a continuación muestra cómo analizar imágenes incrustadas en una página PDF y calcular su resolución efectiva.

1. Abra el PDF con 'ap.Document'.
1. Rastree el estado gráfico mientras lee el contenido de la página.
1. Maneje los operadores:
- 'GSave'/'GRestore' - apilar/desapilar matriz.
- 'ConcatenateMatrix' - actualizar transformación.
- 'Do' - si es una imagen, obtener tamaño y aplicar transformación.
1. Calcule el DPI efectivo.
1. Imprima el nombre de la imagen, el tamaño escalado y el DPI.

```python

    import aspose.pdf as ap
    from io import FileIO
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
