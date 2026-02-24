---
title: Recortando páginas PDF usando Python
linktitle: Recortando páginas PDF
type: docs
weight: 70
url: /es/python-net/crop-pages/
description: Puede cambiar las propiedades de la página, como el ancho, la altura, el Bleed-, Crop- y Trimbox usando Aspose.PDF para Python a través de .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo acceder y modificar las propiedades de la página en PDF usando Python
Abstract: El artículo ofrece una visión general de cómo acceder y modificar las propiedades de la página en un documento PDF usando Aspose.PDF para Python. Describe varias propiedades de la página, incluyendo la media box, bleed box, trim box, art box y crop box, explicando sus funciones en la definición de dimensiones y límites de una página PDF para impresión y visualización. La media box representa el tamaño de página más grande, mientras que la bleed box garantiza la cobertura de tinta más allá del borde de la página para el recorte. La trim box indica el tamaño final del documento después del recorte, y la art box engloba el contenido real de la página. La crop box define el área visible en Adobe Acrobat. El artículo incluye un fragmento de código Python que muestra cómo establecer una nueva crop box, junto con las demás cajas, para una página específica en un documento PDF. Ejemplos visuales ilustran la apariencia de la página antes y después de aplicar el recorte, mostrando la aplicación práctica de modificar estas propiedades.
---

## Obtener propiedades de la página

Cada página en un archivo PDF tiene varias propiedades, como el ancho, la altura, los boxes bleed, crop y trim. Aspose.PDF para Python le permite acceder a estas propiedades.

- **media_box**: La media box es el cuadro de página más grande. Corresponde al tamaño de la página (por ejemplo A4, A5, US Letter, etc.) seleccionado cuando el documento se imprimió a PostScript o PDF. En otras palabras, la media box determina el tamaño físico del medio en el que se muestra o imprime el documento PDF.
- **bleed_box**: Si el documento tiene sangrado, el PDF también tendrá un bleed box. El bleed es la cantidad de color (o arte) que se extiende más allá del borde de una página. Se utiliza para asegurarse de que, cuando el documento se imprima y se corte al tamaño ("recortado"), la tinta llegue hasta el borde de la página. Incluso si la página se recorta incorrectamente – se corta ligeramente fuera de las marcas de recorte – no aparecerán bordes blancos en la página.
- **trim_box**: La trim box indica el tamaño final de un documento después de la impresión y el recorte.
- **art_box**: La art box es el cuadro dibujado alrededor del contenido real de las páginas en sus documentos. Este cuadro de página se utiliza al importar documentos PDF en otras aplicaciones.
- **crop_box**: La crop box es el tamaño de "página" en el que su documento PDF se muestra en Adobe Acrobat. En la vista normal, solo se muestra el contenido de la crop box en Adobe Acrobat. Para descripciones detalladas de estas propiedades, lea la especificación Adobe.Pdf, particularmente la sección 10.10.1 Page Boundaries.

Recorte la primera [`Página`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) de un PDF a un área rectangular específica usando Aspose.PDF para Python. La función ajusta múltiples cajas de página—`crop_box`, `trim_box`, `art_box` y `bleed_box`—para asegurar resultados visuales consistentes. Recortar puede ser útil para eliminar márgenes no deseados o centrar la atención en una región particular de la página.

1. Cargue el PDF como un [`Documento`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (use `ap.Document()`).
1. Defina el rectángulo de recorte usando [`Rectángulo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) con las coordenadas deseadas (en puntos).
1. Establezca el `crop_box`, `trim_box`, `art_box` y `bleed_box` de la [`Página`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) al rectángulo definido.
1. Guarde el [`Documento`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modificado en un nuevo archivo de salida.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to a specified rectangular area.
    This function loads a PDF document, defines a new rectangular boundary,
    and applies this boundary to multiple box types (crop, trim, art, and bleed)
    of the first page. The modified document is then saved to a new file.
    Args:
        input_file_name (str): Path to the input PDF file to be cropped.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Note:
        The cropping rectangle is set to coordinates (200, 220, 2170, 1520)
        which defines the visible area of the page. All box types are set
        to the same dimensions to ensure consistent cropping behavior.
    """
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

En este ejemplo utilizamos un archivo de muestra [aquí](crop_page.pdf). Inicialmente nuestra página se ve como se muestra en la Figura 1.
![Figura 1. Página recortada](crop_page.png)

Después del cambio, la página se verá como la Figura 2.
![Figura 2. Página recortada](crop_page2.png)

## Recortar página PDF basado en el contenido de la primera imagen

Recorte la primera [`Página`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) de forma dinámica basándose en los límites de la primera imagen encontrada en la página. Mediante el uso de [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/), el script identifica la primera imagen y ajusta el `crop_box` de la página para que coincida con las dimensiones de la imagen. Este enfoque es útil cuando desea centrarse en contenido visual específico en lugar de coordenadas predefinidas.

1. Cargue el PDF como un [`Documento`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Ubique imágenes en la primera página usando [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/).
1. Verifique si existen imágenes:
- Si se encuentran, establezca el `crop_box` de la [`Página`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) para que coincida con el [`Rectángulo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) de la primera imagen.
- Si no, mantenga la página sin cambios y notifique al usuario.
1. Guarde el [`Documento`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modificado en el archivo de salida especificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page_by_content(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to the bounds of the first image found on that page.
    This function opens a PDF document, locates the first image on the first page,
    and sets the page's crop box to match the image's rectangle dimensions. If no
    images are found, the page remains unchanged.
    Args:
        input_file_name (str): Path to the input PDF file to be processed.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Raises:
        Exception: May raise exceptions related to file I/O operations or PDF processing
                  if the input file is invalid, corrupted, or inaccessible.
    Note:
        - Only processes the first page of the document
        - Uses the first image found on the page for cropping dimensions
        - If no images are found, prints a message and saves the document unchanged
        - Requires the aspose.pdf library (imported as 'ap')
    """
    document = ap.Document(input_file_name)
    # Find first image on first page using ImagePlacementAbsorber
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        first_image = absorber.image_placements[1]
        document.pages[1].crop_box = first_image.rectangle
    else:
        print("No images found on the first page")
    document.save(output_file_name)
```
