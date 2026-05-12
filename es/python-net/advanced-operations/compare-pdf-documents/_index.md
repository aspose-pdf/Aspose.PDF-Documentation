---
title: Comparar documentos PDF en Python
linktitle: Comparar PDF
type: docs
weight: 130
url: /es/python-net/compare-pdf-documents/
description: Aprenda cómo comparar documentos PDF en Python usando salida de diferencias lado a lado y gráfica con Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Compare páginas PDF y documentos completos con salida visual de diferencias en Python
Abstract: Este artículo explica cómo comparar documentos PDF en Aspose.PDF for Python via .NET. Aprende cómo comparar páginas específicas o archivos PDF completos con salida lado a lado, y cómo usar métodos de comparación gráfica para generar informes de diferencias basados en imágenes o basados en PDF.
---

## Formas de comparar documentos PDF

Al trabajar con documentos PDF, a veces necesitas comparar el contenido de dos documentos para identificar diferencias. La biblioteca Aspose.PDF for Python via .NET ofrece un conjunto de herramientas potente para este propósito. En este artículo, exploraremos cómo comparar documentos PDF usando un par de fragmentos de código sencillos.

Utilice la comparación lado a lado cuando desee una salida PDF que resalte los cambios de texto y diseño entre las páginas. Utilice la comparación gráfica cuando necesite detección de diferencias basada en imágenes para flujos de revisión visual, verificaciones de regresión o informes de comparación de PDF.

La funcionalidad de comparación en Aspose.PDF le permite comparar dos documentos PDF página por página. Puede elegir comparar páginas específicas o documentos completos. El documento de comparación resultante resalta las diferencias, facilitando la identificación de cambios entre los dos archivos.

Aquí hay una lista de posibles formas de comparar documentos PDF utilizando la biblioteca Aspose.PDF for Python via .NET:

1. **Comparando Páginas Específicas** - Compare las primeras páginas de dos documentos PDF.
1. **Comparar documentos completos** - Compara el contenido completo de dos documentos PDF.
1. **Comparar documentos PDF gráficamente**:

- Compara PDF con el método 'comparer.get_difference' - imágenes individuales donde se marcan los cambios.
- Compara PDF con el método 'comparer.compare_documents_to_pdf' - documento PDF con imágenes donde se marcan los cambios.

## Comparación de páginas específicas

El primer fragmento de código muestra cómo comparar las primeras páginas de dos documentos PDF usando la clase SideBySidePdfComparer.

1. Inicialización del documento.
1. Cree una función para realizar la comparación.
1. Proceso de comparación:

- document1.pages[1] y document2.pages[1]: - especifican la primera página de cada documento para la comparación. Tenga en cuenta que la numeración de páginas comienza en 1 en Aspose.PDF.
- SideBySideComparisonOptions - esta clase permite personalizar el comportamiento de la comparación.
- additional_change_marks = True - habilita la visualización de marcadores de cambio adicionales, resaltando diferencias que podrían estar presentes en otras páginas, incluso si no están en la página actual que se compara.
- comparison_mode = ComparisonMode.IgnoreSpaces - establece el modo de comparación para ignorar los espacios en el texto, enfocándose solo en los cambios dentro de las palabras.

1. El resultado de la comparación se guarda como un nuevo archivo PDF llamado ComparingSpecificPages_out.pdf en el data_dir especificado.

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_specific_pages(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1.pages[1], document_2.pages[1], outfile, options
    )
```

## Comparando documentos completos

El segundo fragmento de código amplía el alcance para comparar el contenido completo de dos documentos PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_entire_documents(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1, document_2, outfile, options
    )
```

El código proporcionado demuestra la comparación de dos documentos PDF usando Aspose.PDF for Python via .NET. Utiliza la clase SideBySidePdfComparer para realizar una comparación página por página, generando un nuevo PDF que muestra las diferencias lado a lado. La comparación se configura con SideBySideComparisonOptions, donde additional_change_marks se establece en True para resaltar cambios no solo en la página actual sino también en otras páginas, y comparison_mode se establece en IgnoreSpaces para centrarse en diferencias de contenido significativas al ignorar variaciones de espacios en blanco.

## Comparar usando GraphicalPdfComparer

Al colaborar en documentos, especialmente en entornos profesionales, a menudo terminas con múltiples versiones del mismo archivo.
El código proporcionado demuestra cómo comparar visualmente páginas específicas de dos documentos PDF usando Aspose.PDF for Python via .NET. Al utilizar el `GraphicalPdfComparer` clase, resalta las diferencias entre las primeras páginas de los dos PDFs y genera imágenes correspondientes para representar esas diferencias.

Puedes establecer las siguientes propiedades de la clase:

- Resolution - resolución en unidades DPI para las imágenes de salida, así como para las imágenes generadas durante la comparación.
- Color - el color de las marcas de cambio.
- Umbral - umbral de cambio en porcentaje. El valor predeterminado es cero. Establecer un valor distinto de cero le permite ignorar los cambios gráficos que son insignificantes para usted.

Con Aspose.PDF for Python via .NET, es posible comparar documentos y páginas y exportar el resultado de la comparación a un documento PDF o archivo de imagen.

El `GraphicalPdfComparer` la clase tiene un método que le permite obtener diferencias de imágenes de página en un formato adecuado para un procesamiento posterior: `get_difference(document1.pages[1], document2.pages[1])`.

Este método devuelve un objeto de `images_difference` tipo, que contiene una imagen de la primera página comparada y una matriz de diferencias.

El `images_difference` objeto le permite generar una imagen diferente y obtener una imagen de la segunda página comparada aplicando una matriz de diferencias a la imagen original. Para hacer esto, use el `difference_to_image` y `get_destination_image` métodos.

### Comparar PDF con el método Get Difference

El código proporcionado define un método `get_difference` que compara dos documentos PDF y genera representaciones visuales de las diferencias entre ellos.

Este método compara las primeras páginas de dos archivos PDF y genera dos imágenes PNG:

- Una imagen resalta las diferencias entre las páginas en rojo.
- La otra imagen es una representación visual de la página PDF de destino (segunda).

Este proceso puede ser útil para comparar visualmente los cambios o diferencias entre dos versiones de un documento.

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_get_difference_method(infile1, infile2, outfile1, outfile2):
    # Open PDF documents
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)

    # Create comparer
    comparer = ap.comparison.GraphicalPdfComparer()

    # Compare specific pages
    images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

    # Get image showing differences in red over a white background
    diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
    diff_img.save(outfile1)

    # Get the second image representing the destination page
    dest_img = images_difference.get_destination_image()
    dest_img.save(outfile2)
```

### Comparar PDF con el método CompareDocumentsToPdf

El fragmento de código proporcionado utiliza el `compare_documents_to_pdf` método, que compara dos documentos y genera un informe PDF de los resultados de la comparación.

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_compare_documents_to_pdf_method(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Create comparer and set options
    pdf_comparer = ap.comparison.GraphicalPdfComparer()
    pdf_comparer.threshold = 3.0
    pdf_comparer.color = ap.Color.blue
    pdf_comparer.resolution = ap.devices.Resolution(300)

    # Compare and output to a PDF file
    pdf_comparer.compare_documents_to_pdf(document_1, document_2, outfile)
```

Este ejemplo demuestra cómo realizar una comparación gráfica de dos documentos PDF completos usando Aspose.PDF for Python via .NET. Al aprovechar el `GraphicalPdfComparer` clase, genera un nuevo archivo PDF que resalta visualmente las diferencias entre los documentos.

- La propiedad de umbral está establecida en 3.0, lo que significa que las diferencias menores por debajo de este porcentaje se ignoran durante la comparación, centrándose en cambios más significativos.
- Las diferencias se marcan en azul estableciendo la propiedad color a ap.Color.blue, lo que permite una clara distinción visual.
- La comparación se lleva a cabo a una resolución de 300 DPI estableciendo la propiedad de resolución, lo que asegura una salida detallada y clara.

El `compare_documents_to_pdf` El método compara todas las páginas de ambos documentos y genera el resultado en un nuevo archivo PDF, compareDocumentsToPdf_out.pdf, con las diferencias resaltadas visualmente.

## Temas relacionados

- [Operaciones avanzadas de PDF en Python](/pdf/es/python-net/advanced-operations/)
- [Trabajar con documentos PDF en Python](/pdf/es/python-net/working-with-documents/)
- [Trabajar con páginas PDF en Python](/pdf/es/python-net/working-with-pages/)
- [Trabajar con texto PDF en Python](/pdf/es/python-net/working-with-text/)
