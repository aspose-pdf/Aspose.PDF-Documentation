---
title: Recortar páginas PDF en Python
linktitle: Recorte de páginas PDF
type: docs
weight: 70
url: /es/python-net/crop-pages/
description: Aprenda cómo recortar páginas PDF y ajustar las cajas crop, trim, bleed y media en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo acceder y modificar las propiedades de página en PDF usando Python
Abstract: El artículo proporciona una visión general de cómo acceder y modificar las propiedades de página en un documento PDF usando Aspose.PDF for Python. Describe varias propiedades de página, incluyendo la media box, bleed box, trim box, art box y crop box, explicando sus funciones para definir las dimensiones y los límites de una página PDF con fines de impresión y visualización. La media box representa el tamaño de página más grande, mientras que la bleed box garantiza la cobertura de tinta más allá del borde de la página para el recorte. La trim box indica el tamaño final del documento después del recorte, y la art box engloba el contenido real de la página. La crop box define el área visible en Adobe Acrobat. El artículo incluye un fragmento de código Python que demuestra cómo establecer una nueva crop box, junto con otras cajas, para una página específica en un documento PDF. Los ejemplos visuales ilustran la apariencia de la página antes y después de aplicar el recorte, mostrando la aplicación práctica de la modificación de estas propiedades.
---

## Obtener propiedades de página

Cada página en un archivo PDF tiene varias propiedades, como el ancho, la altura, bleed-, crop- y trimbox. Aspose.PDF for Python le permite acceder a estas propiedades.

Utilice esta página cuando necesite reducir el área visible de la página, preparar archivos para flujos de trabajo de impresión o inspeccionar la geometría de los recuadros de página en documentos PDF.

- **media_box**: La media box es el recuadro de página más grande. Corresponde al tamaño de página (por ejemplo A4, A5, US Letter, etc.) seleccionado cuando el documento se imprimió a PostScript o PDF. En otras palabras, la media box determina el tamaño físico del medio en el que se muestra o imprime el documento PDF.
- **bleed_box**: Si el documento tiene sangrado, el PDF también tendrá un bleed box. El sangrado es la cantidad de color (o arte) que se extiende más allá del borde de una página. Se utiliza para asegurarse de que cuando el documento se imprime y se corta al tamaño (\u0022trimmed\u0022), la tinta llegue hasta el borde de la página. Incluso si la página se corta incorrectamente - recortada ligeramente fuera de las marcas de recorte - no aparecerán bordes blancos en la página.
- **trim_box**: El trim box indica el tamaño final de un documento después de la impresión y el recorte.
- **art_box**: El art box es el cuadro dibujado alrededor del contenido real de las páginas en sus documentos. Este cuadro de página se utiliza al importar documentos PDF en otras aplicaciones.
- **crop_box**: El crop box es el tamaño "página" con el que se muestra su documento PDF en Adobe Acrobat. En la vista normal, solo se muestra el contenido del crop box en Adobe Acrobat. Para descripciones detalladas de estas propiedades, lea la especificación Adobe.Pdf, particularmente 10.10.1 Límites de página.

Recortar el primero [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) de un PDF a un área rectangular específica usando Aspose.PDF for Python. La función ajusta múltiples cajas de página—`crop_box`, `trim_box`, `art_box`, y `bleed_box`—para garantizar resultados visuales consistentes. El recorte puede ser útil para eliminar márgenes no deseados o enfocar una región particular de una página.

1. Cargar el PDF como un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (usar `ap.Document()`).
1. Defina el rectángulo de recorte usando [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) con las coordenadas deseadas (en puntos).
1. Establecer el [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)es `crop_box`, `trim_box`, `art_box`, y `bleed_box` al rectángulo definido.
1. Guarde lo modificado [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) a un nuevo archivo de salida.

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

En este ejemplo utilizamos un archivo de muestra [aquí](crop_page.pdf). Inicialmente, nuestra página se ve como se muestra en la Figura 1.
![Figura 1. Página recortada](crop_page.png)

Después del cambio, la página se verá como la Figura 2.
![Figura 2. Página recortada](crop_page2.png)

## Recortar página PDF según el contenido de la primera imagen

Recortar el primero [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) dinámicamente basado en los límites de la primera imagen encontrada en la página. Al usar [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/), el script identifica la primera imagen y ajusta la página `crop_box` para coincidir con las dimensiones de la imagen. Este enfoque es útil cuando deseas enfocarte en contenido visual específico en lugar de coordenadas predefinidas.

1. Cargar el PDF como un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Ubica imágenes en la primera página usando [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/).
1. Verifica si existen imágenes:
    - Si se encuentran, establece el [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) `crop_box` para que coincida con la de la primera imagen [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
    - Si no, mantenga la página sin cambios y notifique al usuario.
1. Guarde lo modificado [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) al archivo de salida especificado.

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page_by_content(input_file_name, output_file_name):
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

## Temas de página relacionados

- [Trabajar con páginas PDF en Python](/pdf/es/python-net/working-with-pages/)
- [Cambiar el tamaño de página del PDF en Python](/pdf/es/python-net/change-page-size/)
- [Obtener y establecer propiedades de página PDF en Python](/pdf/es/python-net/get-and-set-page-properties/)
- [Rotar páginas PDF en Python](/pdf/es/python-net/rotate-pages/)