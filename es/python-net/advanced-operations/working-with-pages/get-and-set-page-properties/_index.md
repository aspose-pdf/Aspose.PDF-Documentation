---
title: Obtener y establecer propiedades de página PDF en Python
linktitle: Obtener y establecer propiedades de página
type: docs
weight: 90
url: /es/python-net/get-and-set-page-properties/
description: Aprende cómo inspeccionar y actualizar las propiedades de página PDF, como el tamaño, el recuento y la información de color, en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo obtener y establecer propiedades de página usando Python
Abstract: Este artículo discute las capacidades de Aspose.PDF for Python via .NET, centrándose en la lectura y configuración de propiedades de página en archivos PDF usando Python. El artículo cubre varias funcionalidades, incluyendo la determinación del número de páginas en un PDF, el acceso y la modificación de propiedades de página, y el manejo de información de color. Para obtener el número de páginas, se utilizan la clase `Document` y la colección `PageCollection`, con fragmentos de código que demuestran cómo recuperar el recuento de páginas, incluso sin guardar el documento. El artículo explica diferentes propiedades de página como MediaBox, BleedBox, TrimBox, ArtBox y CropBox, y proporciona ejemplos de código para acceder a estas propiedades. Además, cubre la recuperación de una página específica de un PDF y su guardado como un documento separado, así como la determinación del tipo de color de cada página. Los ejemplos a lo largo del texto se implementan en Python, ilustrando aplicaciones prácticas de estas funciones.
---

Aspose.PDF for Python via .NET le permite leer y establecer propiedades de páginas en un archivo PDF en sus aplicaciones Python. Esta sección muestra cómo obtener el número de páginas en un archivo PDF, obtener información sobre las propiedades de la página PDF, como el color, y establecer propiedades de la página. Los ejemplos usan el [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) y [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) APIs y están escritas en Python.

Utilice esta guía cuando necesite inspeccionar los metadatos de la página, determinar el recuento de páginas o actualizar las características a nivel de página como parte del análisis o tareas de normalización de documentos.

## Obtener número de páginas en un archivo PDF

Al trabajar con documentos, a menudo deseas saber cuántas páginas contienen. Con Aspose.PDF esto no requiere más de dos líneas de código.

Para obtener el número de páginas en un archivo PDF:

1. Abra el archivo PDF usando el [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase.
1. Luego usa el [ColecciónDePáginas](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) propiedad Count de collection\u0027s (del objeto Document) para obtener el número total de páginas en el documento.

El siguiente fragmento de código muestra cómo obtener el número de páginas de un archivo PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count(input_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### Obtener el recuento de páginas sin guardar el documento

A veces generamos los archivos PDF sobre la marcha y, durante la creación del archivo PDF, podemos encontrarnos con el requisito (crear la Tabla de Contenidos, etc.) de obtener el recuento de páginas del archivo PDF sin guardar el archivo en el sistema o en un flujo. Por lo tanto, para atender este requisito, se ha introducido un método [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) ha sido introducido en la clase Document. Por favor, eche un vistazo al siguiente fragmento de código que muestra los pasos para obtener el recuento de páginas sin guardar el documento.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count_without_saving(input_file_name):
    # Instantiate Document instance
    document = ap.Document()
    # Add page to pages collection of PDF file
    page = document.pages.add()
    # Create loop instance
    for _ in range(0, 300):
        # Add TextFragment to paragraphs collection of page object
        page.paragraphs.add(ap.text.TextFragment("Pages count test"))
    # Process the paragraphs in PDF file to get accurate page count
    document.process_paragraphs()
    # Print number of pages in document
    print("Number of pages in document =", str(len(document.pages)))
```

## Obtener propiedades de página

Cada página en un archivo PDF tiene varias propiedades, como el ancho, la altura, bleed-, crop- y trimbox. Aspose.PDF le permite acceder a estas propiedades.

### Comprendiendo las propiedades de página: la diferencia entre Artbox, BleedBox, CropBox, MediaBox, TrimBox y la propiedad Rect

- **Media box**: La Media box es la caja de página más grande. Corresponde al tamaño de página (por ejemplo A4, A5, US Letter, etc.) seleccionado cuando el documento se imprimió a PostScript o PDF. En otras palabras, la Media box determina el tamaño físico del medio en el que se muestra o imprime el documento PDF.
- **Bleed box**: Si el documento tiene sangrado, el PDF también tendrá un cuadro de sangrado. El sangrado es la cantidad de color (o arte) que se extiende más allá del borde de una página. Se utiliza para asegurarse de que, cuando el documento se imprime y se corta al tamaño (“trimmed”), la tinta llegue hasta el borde de la página. Incluso si la página se corta de manera incorrecta - cortada ligeramente fuera de las marcas de recorte - no aparecerán bordes blancos en la página.
- **Trim box**: El cuadro de recorte indica el tamaño final de un documento después de imprimir y recortar.
- **Art box**: El cuadro de arte es el cuadro dibujado alrededor del contenido real de las páginas en sus documentos. Este cuadro de página se usa al importar documentos PDF en otras aplicaciones.
- **Crop box**: La crop box es el tamaño de “página” en el que su documento PDF se muestra en Adobe Acrobat. En vista normal, sólo el contenido de la crop box se muestra en Adobe Acrobat.
  Para descripciones detalladas de estas propiedades, lea la especificación Adobe.Pdf, particularmente la sección 10.10.1 Page Boundaries.
-- **Page.Rect**: la intersección (rectángulo visible comúnmente) del MediaBox y el DropBox (`Page.rect`). Ver el [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) tipo para las propiedades del rectángulo. La imagen de abajo ilustra estas propiedades.

Para más detalles, por favor visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Accediendo a las propiedades de la página

El [Página](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) La clase proporciona todas las propiedades relacionadas con una página PDF en particular. Todas las páginas de los archivos PDF están contenidas en el de la [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) del objeto [ColecciónDePáginas](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) colección.

Desde allí, es posible acceder a cualquiera de los individuales `Page` objetos usando su índice, o recorrer la colección para obtener todas las páginas. Una vez que se accede a una página individual, podemos obtener sus propiedades. El siguiente fragmento de código muestra cómo obtener las propiedades de la página (la `Page` API).

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_properties(input_file_name):
    # Open document
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Get page properties
    boxes = {
        "ArtBox": page.art_box,
        "BleedBox": page.bleed_box,
        "CropBox": page.crop_box,
        "MediaBox": page.media_box,
        "TrimBox": page.trim_box,
        "Rect": page.rect,
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(
            f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}"
        )

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## Determinar color de página

El [Página](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) La clase proporciona las propiedades relacionadas con una página particular en un documento PDF, incluido el tipo de color - RGB, blanco y negro, escala de grises o indefinido - que utiliza la página.

Todas las páginas de los archivos PDF están contenidas por el [ColecciónDePáginas](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) colección. El [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) la propiedad especifica el color de los elementos en la página. Para obtener o determinar la información de color de una página PDF en particular, use la [Página](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) del objeto [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) propiedad.

El siguiente fragmento de código muestra cómo iterar a través de una página individual del archivo PDF para obtener información de color.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_color_type(input_file_name):
    # Open source PDF file
    document = ap.Document(input_file_name)
    # Iterate through all the page of PDF file
    for page_number in range(1, len(document.pages) + 1):
        # Get the color type information for particular PDF page
        page_color_type = document.pages[page_number].color_type
        color_type_map = {
            ap.ColorType.BLACK_AND_WHITE: "Black and white",
            ap.ColorType.GRAYSCALE: "Gray Scale",
            ap.ColorType.RGB: "RGB",
            ap.ColorType.UNDEFINED: "undefined",
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```

## Temas de página relacionados

- [Trabajar con páginas PDF en Python](/pdf/es/python-net/working-with-pages/)
- [Cambiar el tamaño de página del PDF en Python](/pdf/es/python-net/change-page-size/)
- [Recortar páginas PDF en Python](/pdf/es/python-net/crop-pages/)
- [Rotar páginas PDF en Python](/pdf/es/python-net/rotate-pages/)