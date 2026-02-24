---
title: Agregar imagen a PDF usando Python
linktitle: Agregar imagen
type: docs
weight: 10
url: /es/python-net/add-image-to-existing-pdf-file/
description: Esta sección describe cómo agregar una imagen a un archivo PDF existente usando una biblioteca de Python.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Cómo agregar imágenes a un PDF usando Python
Abstract: Este artículo brinda orientación sobre cómo agregar imágenes a archivos PDF existentes usando Python con la biblioteca Aspose.PDF. Se describen dos métodos para lograrlo. El primer método implica usar la clase `Document` de Aspose.PDF, donde el usuario carga el PDF, especifica el número de página y utiliza el método `add_image` de la clase `Page` para posicionar la imagen. El documento se guarda luego con el método `save()`. El segundo método utiliza la clase `PdfFileMend` del espacio de nombres Aspose.PDF.Facades, que ofrece una interfaz más sencilla. Aquí se invoca el método `add_image()` para agregar la imagen a la página y coordenadas especificadas, seguido de guardar el PDF actualizado y cerrar el objeto `PdfFileMend`. Se proporcionan fragmentos de código para ambos métodos que demuestran el proceso.
---

## Agregar imagen en un archivo PDF existente

Este ejemplo muestra cómo insertar una imagen en una posición específica de una página PDF usando Aspose.PDF para Python a través de .NET.

1. Cargue el documento PDF con 'ap.Document'.
1. Seleccione la página objetivo '(document.pages[1]' - la primera página).
1. Utilice 'page.add_image()' para colocar la imagen:
- Ruta del archivo de la imagen.
- Un objeto 'Rectangle' que define las coordenadas de la imagen (left=20, bottom=730, right=120, top=830).
1. Guarde el PDF actualizado.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    page = document.pages[1]
    page.add_image(
        path.join(self.data_dir, image_file),
        ap.Rectangle(20, 730, 120, 830, True),
    )
    document.save(path_outfile)
```

## Agregar una imagen usando operadores

El siguiente fragmento de código muestra un enfoque de bajo nivel para agregar una imagen a una página PDF trabajando manualmente con operadores PDF en lugar de métodos auxiliares de alto nivel.

Pasos:

1. Cree un nuevo 'Document' en blanco.
1. Añada una página y establezca su tamaño (842 × 595 - A4 horizontal).
1. Acceda a los recursos de imágenes de la página (page.resources.images).
1. Cargue el archivo de imagen en un flujo y agréguelo a los recursos.
- El método devuelve un 'image_id'.
- El nuevo objeto de imagen agregado se recupera de los recursos.
1. Defina un rectángulo que mantenga la relación de aspecto de la imagen:
1. Construya una secuencia de operadores:
- 'GSave()' - Guardar el estado gráfico actual.
- 'ConcatenateMatrix(matrix)' - Aplicar transformación (escalar y centrar verticalmente la imagen en la página).
- 'Do(image_id)' - Renderizar la imagen.
- 'GRestore()' - Restaurar el estado gráfico.
1. Añada la secuencia de operadores a 'page.contents'.
1. Guarde el PDF resultante.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    # Get page resources
    resources_images = page.resources.images

    # Add image to resources
    image_stream = FileIO(path.join(self.data_dir, path_infile), "rb")
    image_id = resources_images.add(image_stream)

    x_image = list(resources_images)[-1]

    rectangle = ap.Rectangle(
        0,
        0,
        page.media_box.width,
        (page.media_box.width * x_image.height) / x_image.width,
        True,
    )

    # Create operator sequence for adding image
    operators = []

    # Save graphics state
    operators.append(ap.operators.GSave())

    # Set transformation matrix (position and size)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.llx + (page.media_box.height - rectangle.height) / 2,
    )
    operators.append(ap.operators.ConcatenateMatrix(matrix))

    # Draw the image
    operators.append(ap.operators.Do(image_id))

    # Restore graphics state
    operators.append(ap.operators.GRestore())

    # Add operators to page contents
    page.contents.add(operators)

    document.save(path_outfile)
```

## Agregar imagen con texto alternativo

Este ejemplo muestra cómo agregar una imagen a una página PDF y asignar texto alternativo (alt text) para cumplir con la accesibilidad (como PDF/UA).

1. Cree un nuevo 'Document' y añada una página (842 × 595, A4 horizontal).
1. Coloque la imagen en la página usando 'page.add_image()' con un rectángulo que cubra toda la página.
1. Acceda a los recursos de imágenes de la página ('page.resources.images').
1. Defina una cadena de texto alternativo (p., ej., 'Alternative text for image').
1. Recupere el primer objeto de imagen de los recursos ('x_image = resources_images[1]').
1. Use 'try_set_alternative_text(alt_text, page)' para asignar texto alternativo a la imagen.
1. Guarde el PDF resultante.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    page.add_image(
        path_image_file,
        ap.Rectangle(0, 0, 842, 595, True),
    )

    resources_images = page.resources.images
    alt_text = "Alternative text for image"
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text(alt_text, page)

    # If set is successful, then get the alternative text for the image
    if (result):
        print ("Text has been added successfuly")
    document.save(path_outfile)
```
