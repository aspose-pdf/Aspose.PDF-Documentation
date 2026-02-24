---
title: Obtener y establecer propiedades de página usando Python
linktitle: Obtener y establecer propiedades de página
type: docs
weight: 90
url: /es/python-net/get-and-set-page-properties/
description: Esta sección muestra cómo obtener el número de páginas en un archivo PDF, obtener información sobre las propiedades de página del PDF como el color y establecer propiedades de página.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo obtener y establecer propiedades de página usando Python
Abstract: Este artículo analiza las capacidades de Aspose.PDF para Python a través de .NET, centrado en la lectura y configuración de propiedades de página en archivos PDF usando Python. El artículo cubre diversas funcionalidades, incluyendo la determinación del número de páginas de un PDF, el acceso y la modificación de propiedades de página, y el manejo de información de color. Para obtener el número de páginas, se utilizan la clase `Document` y la colección `PageCollection`, con fragmentos de código que demuestran cómo recuperar el recuento de páginas, incluso sin guardar el documento. El artículo explica diferentes propiedades de página como MediaBox, BleedBox, TrimBox, ArtBox y CropBox, y proporciona ejemplos de código para acceder a estas propiedades. Además, cubre la extracción de una página específica de un PDF y su guardado como un documento separado, así como la determinación del tipo de color de cada página. Los ejemplos están implementados en Python, ilustrando aplicaciones prácticas de estas funciones.
---

Aspose.PDF para Python a través de .NET le permite leer y establecer propiedades de páginas en un archivo PDF en sus aplicaciones Python. Esta sección muestra cómo obtener el número de páginas en un archivo PDF, obtener información sobre las propiedades de página del PDF como el color y establecer propiedades de página. Los ejemplos utilizan las API [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) y [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) y están escritos en Python.

## Obtener número de páginas en un archivo PDF

Al trabajar con documentos, a menudo desea saber cuántas páginas contienen. Con Aspose.PDF esto no lleva más de dos líneas de código.

Para obtener el número de páginas en un archivo PDF:

1. Abra el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. Luego use la colección [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) y su propiedad Count (del objeto Document) para obtener el número total de páginas del documento.

El siguiente fragmento de código muestra cómo obtener el número de páginas de un archivo PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count(input_file_name):
    """
    Get the total number of pages in a PDF document.
    Args:
        input_file_name (str): Path to the input PDF file.
    Returns:
        None: Prints the page count to console.
    Example:
        get_page_count("example.pdf")
        # Output: Page Count: 10
    """
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### Obtener recuento de páginas sin guardar el documento

A veces generamos los archivos PDF sobre la marcha y, durante la creación del archivo PDF, podemos encontrarnos con la necesidad (crear tabla de contenidos, etc.) de obtener el recuento de páginas del PDF sin guardar el archivo en el sistema o en un flujo. Por ello, para satisfacer este requisito, se ha introducido un método [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) en la clase Document. Por favor, revise el siguiente fragmento de código que muestra los pasos para obtener el recuento de páginas sin guardar el documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count_without_saving(input_file_name):
    """
    Get the page count of a PDF document after adding content without saving the file.

    This function opens an existing PDF document, adds a new page with 300 text fragments,
    processes the paragraphs to ensure accurate page counting, and prints the total number
    of pages in the document. The document is not saved to disk.

    Args:
        input_file_name (str): Path to the input PDF file to be processed.

    Returns:
        None: This function prints the page count but does not return a value.

    Example:
        >>> get_page_count_without_saving("sample.pdf")
        Number of pages in document = 2
    """
    # Instantiate Document instance
    document = ap.Document(input_file_name)
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

Cada página en un archivo PDF tiene varias propiedades, como el ancho, la altura, y las cajas bleed, crop y trim. Aspose.PDF le permite acceder a estas propiedades.

### Comprender las propiedades de página: la diferencia entre Artbox, BleedBox, CropBox, MediaBox, TrimBox y la propiedad Rect

- **Media box**: La media box es la caja de página más grande. Corresponde al tamaño de la página (por ejemplo A4, A5, US Letter, etc.) seleccionado cuando el documento se imprimió a PostScript o PDF. En otras palabras, la media box determina el tamaño físico del medio en el que se muestra o imprime el documento PDF.
- **Bleed box**: Si el documento tiene sangrado, el PDF también tendrá una bleed box. El sangrado es la cantidad de color (o arte) que se extiende más allá del borde de una página. Se utiliza para asegurarse de que, cuando el documento se imprima y se corte al tamaño (“recortado”), la tinta llegue hasta el borde de la página. Incluso si la página se recorta de manera incorrecta - cortada ligeramente fuera de las marcas de recorte - no aparecerán bordes blancos en la página.
- **Trim box**: La trim box indica el tamaño final de un documento después de imprimir y recortar.
- **Art box**: La art box es la caja que rodea el contenido real de las páginas en sus documentos. Esta caja de página se utiliza al importar documentos PDF en otras aplicaciones.
- **Crop box**: La crop box es el tamaño de “página” en el que su documento PDF se muestra en Adobe Acrobat. En la vista normal, solo se muestra el contenido de la crop box en Adobe Acrobat.
Para descripciones detalladas de estas propiedades, lea la especificación Adobe.Pdf, particularmente 10.10.1 Page Boundaries.
-- **Page.Rect**: la intersección (rectángulo visible comúnmente) de la MediaBox y DropBox (`Page.rect`). Consulte el tipo [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) para las propiedades del rectángulo. La imagen a continuación ilustra estas propiedades.

Para obtener más detalles, visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Acceso a propiedades de página

La clase [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) proporciona todas las propiedades relacionadas con una página PDF en particular. Todas las páginas de los archivos PDF están contenidas en la colección [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Desde allí, es posible acceder a objetos `Page` individuales usando su índice, o iterar a través de la colección para obtener todas las páginas. Una vez que se accede a una página individual, podemos obtener sus propiedades. El siguiente fragmento de código muestra cómo obtener propiedades de página (la API `Page`).

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_properties(input_file_name):
    """
    Retrieves and displays various page properties for the first page of a PDF document.

    Args:
        input_file_name (str): Path to the PDF file to analyze.
    """
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
        "Rect": page.rect
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}")

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## Determinar color de página

La clase [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) proporciona las propiedades relacionadas con una página en particular de un documento PDF, incluido el tipo de color — RGB, blanco y negro, escala de grises o indefinido — que usa la página.

Todas las páginas de los archivos PDF están contenidas por la colección [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/). La propiedad [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) especifica el color de los elementos en la página. Para obtener o determinar la información de color de una página PDF en particular, use la propiedad [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) del objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

El siguiente fragmento de código muestra cómo iterar a través de cada página individual de un archivo PDF para obtener información de color.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_color_type(input_file_name):
    """
    Analyzes and prints the color type information for each page in a PDF document.

    This function opens a PDF file and iterates through all pages to determine
    the color type of each page (black and white, grayscale, RGB, or undefined).
    The results are printed to the console with human-readable descriptions.

    Args:
        input_file_name (str): Path to the PDF file to analyze.

    Returns:
        None: This function prints results directly to console and doesn't return a value.

    Example:
        >>> get_page_color_type("sample.pdf")
        Page # 1 is RGB.
        Page # 2 is Gray Scale.
        Page # 3 is Black and white.

    Note:
        Requires the aspose.pdf library (imported as ap) to be installed and available.
        The PDF file must be accessible at the specified path.
    """
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
            ap.ColorType.UNDEFINED: "undefined"
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```


