---
title: Comparar documentos PDF en Python
linktitle: Comparar PDF
type: docs
weight: 130
url: /es/python-net/compare-pdf-documents/
description: Aprenda a comparar documentos PDF en Python usando salidas de diferencias lado a lado y graficas con Aspose.PDF para Python a traves de .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Comparar páginas PDF y documentos completos con salida visual de diferencias en Python
Abstract: Este articulo explica como comparar documentos PDF en Aspose.PDF para Python a traves de .NET. Aprenda como comparar paginas especificas o archivos PDF completos con salida lado a lado, y como usar metodos de comparacion grafica para generar informes de diferencias basados en imagenes o en PDF.
---

## Formas de comparar documentos PDF

Al trabajar con documentos PDF, hay ocasiones en las que necesita comparar el contenido de dos documentos para identificar diferencias. La biblioteca Aspose.PDF para Python a traves de .NET proporciona un conjunto de herramientas potente para este proposito. En este articulo, exploraremos como comparar documentos PDF usando un par de fragmentos de codigo simples.

Utilice la comparación lado a lado cuando desee una salida PDF que resalte los cambios de texto y diseño entre páginas. Utilice la comparación gráfica cuando necesite detección de diferencias basada en imágenes para flujos de trabajo de revisión visual, verificaciones de regresión o informes de comparación de PDF.

La funcionalidad de comparación en Aspose.PDF le permite comparar dos documentos PDF página por página. Puede elegir comparar páginas específicas o documentos completos. El documento de comparación resultante resalta las diferencias, facilitando la identificación de cambios entre los dos archivos.

Aqui hay una lista de posibles formas de comparar documentos PDF utilizando la biblioteca Aspose.PDF para Python a traves de .NET:

1. **Comparar paginas especificas** - compare las primeras paginas de dos documentos PDF.
1. **Comparación de documentos completos** - Compara el contenido completo de dos documentos PDF.
1. **Comparar documentos PDF gráficamente**:

- Comparar PDF con el método 'comparer.get_difference' - imágenes individuales donde se marcan los cambios.
- Comparar PDF con el método 'comparer.compare_documents_to_pdf' - documento PDF con imágenes donde se marcan los cambios.

## Comparar páginas específicas

El primer fragmento de código demuestra cómo comparar las primeras páginas de dos documentos PDF utilizando la clase SideBySidePdfComparer.

1. Inicialización del documento.
1. Cree una función para realizar la comparación.
1. Proceso de comparación:

- document1.pages[1] y document2.pages[1]: - especifican la primera página de cada documento para la comparación. Tenga en cuenta que la indexación de páginas comienza en 1 en Aspose.PDF.
- SideBySideComparisonOptions - esta clase permite personalizar el comportamiento de la comparación.
- additional_change_marks = True - habilita la visualización de marcas de cambio adicionales, resaltando diferencias que podrían estar presentes en otras páginas, incluso si no están en la página actual que se está comparando.
- comparison_mode = ComparisonMode.IgnoreSpaces - establece el modo de comparación para ignorar los espacios en el texto, centrándose solo en los cambios dentro de las palabras.

1. El resultado de la comparación se guarda como un nuevo archivo PDF llamado ComparingSpecificPages_out.pdf en el data_dir especificado.

```python
import aspose.pdf as ap
from aspose.pdf.comparison import (
    SideBySidePdfComparer,
    SideBySideComparisonOptions,
    ComparisonMode,
)


def comparing_specific_pages():
    # The path to the documents directory
    data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

    # Open PDF documents
    document1 = ap.Document(data_dir + "ComparingSpecificPages1.pdf")
    document2 = ap.Document(data_dir + "ComparingSpecificPages2.pdf")

    # Compare
    options = SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ComparisonMode.IgnoreSpaces

    # Perform comparison and save the result
    SideBySidePdfComparer.compare(
        document1.pages[1],
        document2.pages[1],
        data_dir + "ComparingSpecificPages_out.pdf",
        options,
    )
```

## Comparar documentos completos

El segundo fragmento de código amplía el alcance para comparar el contenido completo de dos documentos PDF.

```python
import aspose.pdf as ap
from aspose.pdf.comparison import (
    SideBySidePdfComparer,
    SideBySideComparisonOptions,
    ComparisonMode,
)


def comparing_entire_documents():
    # The path to the documents directory
    data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

    # Open PDF documents
    document1 = ap.Document(data_dir + "ComparingEntireDocuments1.pdf")
    document2 = ap.Document(data_dir + "ComparingEntireDocuments2.pdf")

    # Compare
    options = SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ComparisonMode.IgnoreSpaces

    # Perform comparison and save the result
    SideBySidePdfComparer.compare(
        document1, document2, data_dir + "ComparingEntireDocuments_out.pdf", options
    )
```

El codigo proporcionado demuestra como comparar dos documentos PDF usando Aspose.PDF para Python a traves de .NET. Utiliza la clase `SideBySidePdfComparer` para realizar una comparacion pagina por pagina, generando un nuevo PDF que muestra las diferencias lado a lado. La comparacion se configura con `SideBySideComparisonOptions`, donde `additional_change_marks` se establece en `True` para resaltar los cambios no solo en la pagina actual sino tambien en otras paginas, y `comparison_mode` se establece en `IgnoreSpaces` para centrarse en diferencias de contenido significativo al ignorar variaciones de espacios en blanco.

## Comparar usando GraphicalPdfComparer

Cuando colaboras en documentos, especialmente en entornos profesionales, a menudo terminas con múltiples versiones del mismo archivo.
El codigo proporcionado demuestra como comparar visualmente paginas especificas de dos documentos PDF usando Aspose.PDF para Python a traves de .NET. Al usar la clase `GraphicalPdfComparer`, resalta las diferencias entre las primeras paginas de los dos PDF y genera imagenes correspondientes para representar esas diferencias.

Puedes establecer las siguientes propiedades de la clase:

- Resolution - resolución en unidades DPI para imágenes de salida, así como para imágenes generadas durante la comparación.
- Color - el color de las marcas de cambio.
- Umbral - umbral de cambio en porcentaje. El valor predeterminado es cero. Establecer un valor diferente de cero le permite ignorar los cambios gráficos que le resulten insignificantes.

Con Aspose.PDF para Python a traves de .NET, es posible comparar documentos y paginas y generar el resultado de la comparacion en un documento PDF o archivo de imagen.

El `GraphicalPdfComparer` clase tiene un método que le permite obtener diferencias de imágenes de página en un formato adecuado para un procesamiento posterior: `get_difference(document1.pages[1], document2.pages[1])`.

Este método devuelve un objeto de `images_difference` tipo, que contiene una imagen de la primera página que se está comparando y una matriz de diferencias.

El `images_difference` El objeto le permite generar una imagen diferente y obtener una imagen de la segunda página que se compara aplicando una matriz de diferencias a la imagen original. Para hacer esto, use el `difference_to_image` y `get_destination_image` métodos.

### Comparar PDF con el método Get Difference

El código proporcionado define un método `get_difference` que compara dos documentos PDF y genera representaciones visuales de las diferencias entre ellos.

Este método compara las primeras páginas de dos archivos PDF y genera dos imágenes PNG:

- Una imagen destaca las diferencias entre las páginas en rojo.
- La otra imagen es una representación visual de la página PDF de destino (segunda).

Este proceso puede ser útil para comparar visualmente los cambios o diferencias entre dos versiones de un documento.

```python
import aspose.pdf as ap
from aspose.pdf.comparison import GraphicalPdfComparer


def compare_pdf_with_get_difference_method():
    # The path to the documents directory
    data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

    # Open PDF documents
    document1 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod1.pdf")
    document2 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod2.pdf")

    # Create comparer
    comparer = GraphicalPdfComparer()

    # Compare specific pages
    images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

    # Get image showing differences in red over a white background
    diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
    diff_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png")

    # Get the second image representing the destination page
    dest_img = images_difference.get_destination_image()
    dest_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png")
```

### Comparar PDF con el método CompareDocumentsToPdf

El fragmento de código proporcionado usa el `compare_documents_to_pdf` método, que compara dos documentos y genera un informe PDF de los resultados de la comparación.

```python
import aspose.pdf as ap
from aspose.pdf.comparison import GraphicalPdfComparer
from aspose.pdf.devices import Resolution


def compare_pdf_with_compare_documents_to_pdf_method():
    # The path to the documents directory
    data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

    # Open PDF documents
    document1 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf")
    document2 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf")

    # Create comparer and set options
    comparer = GraphicalPdfComparer()
    comparer.threshold = 3.0
    comparer.color = ap.Color.blue
    comparer.resolution = Resolution(300)

    # Compare and output to a PDF file
    comparer.compare_documents_to_pdf(
        document1, document2, data_dir + "compareDocumentsToPdf_out.pdf"
    )
```

Este ejemplo demuestra como realizar una comparacion grafica de dos documentos PDF completos usando Aspose.PDF para Python a traves de .NET. Al aprovechar la clase `GraphicalPdfComparer`, genera un nuevo archivo PDF que resalta visualmente las diferencias entre los documentos.

- La propiedad threshold está configurada en 3.0, lo que significa que las diferencias menores por debajo de este porcentaje se ignoran durante la comparación, centrándose en cambios más significativos.
- Las diferencias se marcan en azul estableciendo la propiedad color a ap.Color.blue, lo que permite una clara distinción visual.
- La comparación se realiza a una resolución de 300 DPI estableciendo la propiedad de resolución, lo que garantiza una salida detallada y clara.

El `compare_documents_to_pdf` El método compara todas las páginas de ambos documentos y genera el resultado en un nuevo archivo PDF, compareDocumentsToPdf_out.pdf, con las diferencias resaltadas visualmente.

## Temas relacionados

- [Operaciones avanzadas de PDF en Python](/pdf/es/python-net/advanced-operations/)
- [Trabajar con documentos PDF en Python](/pdf/es/python-net/working-with-documents/)
- [Trabajar con páginas PDF en Python](/pdf/es/python-net/working-with-pages/)
- [Trabajar con texto PDF en Python](/pdf/es/python-net/working-with-text/)
