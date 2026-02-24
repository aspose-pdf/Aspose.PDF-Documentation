---
title: Comparar documentos PDF
linktitle: Comparar PDF
type: docs
weight: 130
url: /es/python-net/compare-pdf-documents/
description: Es posible comparar el contenido de documentos PDF con marcas de anotación y salida lado a lado.
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 
Abstract: 
---

## Maneras de comparar documentos PDF

Al trabajar con documentos PDF, hay ocasiones en las que necesitas comparar el contenido de dos documentos para identificar diferencias. La biblioteca Aspose.PDF para Python a través de .NET brinda un conjunto de herramientas potente para este propósito. En este artículo, exploraremos cómo comparar documentos PDF usando un par de fragmentos de código simples.

La funcionalidad de comparación en Aspose.PDF te permite comparar dos documentos PDF página por página. Puedes elegir comparar páginas específicas o documentos completos. El documento de comparación resultante resalta las diferencias, facilitando la identificación de cambios entre los dos archivos.

Aquí hay una lista de posibles formas de comparar documentos PDF usando la biblioteca Aspose.PDF para Python a través de .NET:

1. **Comparar páginas específicas** - Comparar las primeras páginas de dos documentos PDF.
1. **Comparar documentos completos** - Comparar todo el contenido de dos documentos PDF.
1. **Comparar documentos PDF gráficamente**:

- Comparar PDF con el método 'comparer.get_difference' - imágenes individuales donde se marcan los cambios.
- Comparar PDF con el método 'comparer.compare_documents_to_pdf' - documento PDF con imágenes donde se marcan los cambios.

## Comparando páginas específicas

El primer fragmento de código muestra cómo comparar las primeras páginas de dos documentos PDF usando la clase SideBySidePdfComparer.

1. Inicialización del documento.
1. Crear una función para realizar la comparación.
1. Proceso de comparación:

- document1.pages[1] y document2.pages[1]: - especifican la primera página de cada documento para la comparación. Ten en cuenta que la indexación de páginas comienza en 1 en Aspose.PDF.
- SideBySideComparisonOptions - esta clase permite personalizar el comportamiento de la comparación.
- additional_change_marks = True - habilita la visualización de marcadores de cambio adicionales, resaltando diferencias que pueden estar presentes en otras páginas, incluso si no están en la página actual que se compara.
- comparison_mode = ComparisonMode.IgnoreSpaces - establece el modo de comparación para ignorar espacios en el texto, enfocándose solo en los cambios dentro de las palabras.

1. El resultado de la comparación se guarda como un nuevo archivo PDF llamado ComparingSpecificPages_out.pdf en el directorio data_dir especificado.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

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
        SideBySidePdfComparer.compare(document1.pages[1], document2.pages[1], data_dir + "ComparingSpecificPages_out.pdf", options)
```

## Comparando documentos completos

El segundo fragmento de código amplía el alcance para comparar todo el contenido de dos documentos PDF.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

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
        SideBySidePdfComparer.compare(document1, document2, data_dir + "ComparingEntireDocuments_out.pdf", options)
```

El código proporcionado demuestra cómo comparar dos documentos PDF usando Aspose.PDF para Python a través de .NET. Utiliza la clase SideBySidePdfComparer para realizar una comparación página por página, generando un nuevo PDF que muestra las diferencias lado a lado. La comparación está configurada con SideBySideComparisonOptions, donde additional_change_marks se establece en True para resaltar cambios no solo en la página actual sino también en otras páginas, y comparison_mode se establece en IgnoreSpaces para centrarse en diferencias de contenido significativas ignorando variaciones de espacios en blanco.

## Comparar usando GraphicalPdfComparer

Al colaborar en documentos, especialmente en entornos profesionales, a menudo terminas con múltiples versiones del mismo archivo.
El código proporcionado muestra cómo comparar visualmente páginas específicas de dos documentos PDF usando Aspose.PDF para Python a través de .NET. Al usar la clase `GraphicalPdfComparer`, resalta las diferencias entre las primeras páginas de los dos PDFs y genera imágenes correspondientes para representar esas diferencias.

Puedes establecer las siguientes propiedades de la clase:

- Resolution - resolución en unidades DPI para imágenes de salida, así como para imágenes generadas durante la comparación.
- Color - el color de las marcas de cambio.
- Threshold - umbral de cambio en porcentaje. El valor predeterminado es cero. Establecer un valor distinto de cero permite ignorar cambios gráficos que no son significativos para ti.

Con Aspose.PDF para Python a través de .NET, es posible comparar documentos y páginas y generar el resultado de la comparación en un documento PDF o archivo de imagen.

La clase `GraphicalPdfComparer` tiene un método que permite obtener diferencias de imágenes de página en una forma adecuada para procesamiento posterior: `get_difference(document1.pages[1], document2.pages[1])`.

Este método devuelve un objeto del tipo `images_difference`, que contiene una imagen de la primera página comparada y una matriz de diferencias.

El objeto `images_difference` permite generar una imagen diferente y obtener una imagen de la segunda página comparada aplicando una matriz de diferencias a la imagen original. Para hacerlo, usa los métodos `difference_to_image` y `get_destination_image`.

### Comparar PDF con el método Get Difference

El código proporcionado define un método `get_difference` que compara dos documentos PDF y genera representaciones visuales de las diferencias entre ellos.

Este método compara las primeras páginas de dos archivos PDF y genera dos imágenes PNG:

- Una imagen resalta las diferencias entre las páginas en rojo.
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

El fragmento de código proporcionado utiliza el método `compare_documents_to_pdf`, que compara dos documentos y genera un informe PDF de los resultados de la comparación.

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
        comparer.compare_documents_to_pdf(document1, document2, data_dir + "compareDocumentsToPdf_out.pdf")
```

Este ejemplo muestra cómo realizar una comparación gráfica de dos documentos PDF completos usando Aspose.PDF para Python a través de .NET. Al aprovechar la clase `GraphicalPdfComparer`, genera un nuevo archivo PDF que resalta visualmente las diferencias entre los documentos.

- La propiedad umbral se establece en 3.0, lo que significa que las diferencias menores por debajo de este porcentaje se ignoran durante la comparación, enfocándose en cambios más significativos.
- Las diferencias se marcan en azul estableciendo la propiedad de color a ap.Color.blue, lo que permite una clara distinción visual.
- La comparación se realiza a una resolución de 300 DPI estableciendo la propiedad de resolución, garantizando una salida detallada y clara.

El método `compare_documents_to_pdf` compara todas las páginas de ambos documentos y genera el resultado en un nuevo archivo PDF, compareDocumentsToPdf_out.pdf, con las diferencias resaltadas visualmente.

