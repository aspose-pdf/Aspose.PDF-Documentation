---
title: Agregar imagen a PDF usando Python
linktitle: Agregar imagen
type: docs
weight: 10
url: /es/python-net/add-image-to-existing-pdf-file/
description: Aprende cómo agregar imágenes a archivos PDF existentes en Python.
lastmod: "2026-05-05"
TechArticle: true
AlternativeHeadline: Agregar imágenes a archivos PDF existentes con Python
Abstract: Este artículo muestra cómo agregar imágenes a documentos PDF con Aspose.PDF for Python via .NET. Cubre la inserción de una imagen en coordenadas fijas, la colocación de imágenes con operadores de bajo nivel, la asignación de texto alternativo para accesibilidad y la incrustación de imágenes con compresión Flate.
---

## Agregar imagen en un archivo PDF existente

Este ejemplo muestra cómo colocar una imagen en una posición fija en una página PDF existente usando Aspose.PDF for Python via .NET.

Utilice estos ejemplos de esta página cuando necesite colocar logotipos, fotos u otros gráficos en coordenadas fijas dentro de un diseño PDF existente.

1. Cargar un PDF existente con `ap.Document(infile)`.
1. Seleccione la página objetivo (`document.pages[1]` para la primera página).
1. Llamada `page.add_image()` con:
    - La ruta del archivo de imagen.
    - A `Rectangle` definir coordenadas de colocación.
1. Guarda el PDF actualizado.

```python
import aspose.pdf as ap


def add_image(infile, image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))
    document.save(outfile)
```

## Agregar una imagen usando operadores

Este enfoque agrega una imagen con operadores PDF de bajo nivel en lugar de los de alto nivel `add_image()` ayudante.

1. Crear un nuevo `Document` y agregue una página.
1. Agregar la imagen a los recursos de la página (`page.resources.images`).
1. Crear operadores de transformación (`GSave`, `ConcatenateMatrix`, `Do`, `GRestore`).
1. Agregar operadores al contenido de la página.
1. Guarda el PDF resultante.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_using_operators(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream)

    rectangle = ap.Rectangle(0, 0, page.media_box.width, page.media_box.height, True)

    operators = [
        ap.operators.GSave(),
        ap.operators.ConcatenateMatrix(
            ap.Matrix(
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            )
        ),
        ap.operators.Do(image_id),
        ap.operators.GRestore(),
    ]

    page.contents.add(operators)
    document.save(outfile)
```

## Agregar imagen con texto alternativo

Este ejemplo agrega una imagen y asigna texto alternativo para accesibilidad.

1. Crear un nuevo `Document` y agregue una página.
1. Añadir la imagen a la página con `page.add_image()`.
1. Obtener recursos de imagen de `page.resources.images`.
1. Establecer texto alternativo usando `try_set_alternative_text()`.
1. Guarda el PDF resultante.

```python
import aspose.pdf as ap


def add_image_set_alternative_text(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)

    page.add_image(image_file, ap.Rectangle(0, 0, 842, 595, True))
    resources_images = page.resources.images
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text("Alternative text for image", page)

    if result:
        print("Alternative text has been added successfully")

    document.save(outfile)
```

## Agregar una imagen a un PDF con compresión Flate

Este ejemplo inserta una imagen usando `ImageFilterType.FLATE` compresión.

1. Crear un nuevo `Document` y agregue una página.
1. Agregar la imagen a los recursos de la página con compresión Flate.
1. Usar operadores de matriz para colocar y dibujar la imagen.
1. Guarde el documento.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_to_pdf_with_flate_compression(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream, ap.ImageFilterType.FLATE)

    rectangle = ap.Rectangle(0, 0, 600, 600, True)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.lly,
    )

    page.contents.add([ap.operators.GSave()])
    page.contents.add([ap.operators.ConcatenateMatrix(matrix)])
    page.contents.add([ap.operators.Do(image_id)])
    page.contents.add([ap.operators.GRestore()])

    document.save(outfile)
```

## Temas de imágenes relacionadas

- [Trabajar con imágenes en PDF usando Python](/pdf/es/python-net/working-with-images/)
- [Reemplazar imágenes en archivos PDF existentes](/pdf/es/python-net/replace-image-in-existing-pdf-file/)
- [Eliminar imágenes de archivos PDF](/pdf/es/python-net/delete-images-from-pdf-file/)
- [Extraer imágenes de archivos PDF](/pdf/es/python-net/extract-images-from-pdf-file/)
