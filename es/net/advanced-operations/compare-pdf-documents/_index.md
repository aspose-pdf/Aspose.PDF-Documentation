---
title: Comparar documentos PDF
linktitle: Comparar PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /es/net/compare-pdf-documents/
description: Desde el lanzamiento 24.7 es posible comparar el contenido de documentos PDF con marcas de anotación y salida lado a lado
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Compare PDF documents",
    "alternativeHeadline": "Enhanced PDF Document Comparison with Visual Highlights",
    "abstract": "La nueva función de comparación de PDF en Aspose.PDF for .NET permite a los usuarios identificar eficientemente las diferencias entre dos documentos PDF, ya sea por páginas específicas o por todo el contenido. Con salidas lado a lado y opciones personalizables como marcadores de cambio adicionales y varios modos de comparación, esta poderosa herramienta mejora la colaboración al facilitar el seguimiento y la revisión de revisiones",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Compare PDF documents, PDF comparison, Aspose.PDF for .NET, comparing specific pages, comparing entire documents, graphical PDF comparer, side-by-side comparison, change markers, document accuracy, ImagesDifference",
    "wordcount": "1180",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/compare-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/compare-pdf-documents/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

Tenga en cuenta que todas las herramientas de comparación están disponibles en la biblioteca [Aspose.PDF.Drawing](https://docs.aspose.com/pdf/net/drawing/).

## Formas de comparar documentos PDF

Al trabajar con documentos PDF, hay momentos en los que necesitas comparar el contenido de dos documentos para identificar diferencias. La biblioteca Aspose.PDF for .NET proporciona un conjunto de herramientas poderoso para este propósito. En este artículo, exploraremos cómo comparar documentos PDF utilizando un par de fragmentos de código simples.

La funcionalidad de comparación en Aspose.PDF te permite comparar dos documentos PDF página por página. Puedes elegir comparar ya sea páginas específicas o documentos completos. El documento de comparación resultante resalta las diferencias, facilitando la identificación de cambios entre los dos archivos.

Aquí hay una lista de posibles formas de comparar documentos PDF utilizando Aspose.PDF para la biblioteca .NET:

1. **Comparar Páginas Específicas** - Comparar las primeras páginas de dos documentos PDF.

1. **Comparar Documentos Completos** - Comparar todo el contenido de dos documentos PDF.

1. **Comparar documentos PDF gráficamente**:

- Comparar PDF con el método GetDifference - imágenes individuales donde se marcan los cambios.

- Comparar PDF con el método CompareDocumentsToPdf - documento PDF con imágenes donde se marcan los cambios.

## Comparar Páginas Específicas

El primer fragmento de código demuestra cómo comparar las primeras páginas de dos documentos PDF.

Pasos:

1. Inicialización del Documento.
El código comienza inicializando dos documentos PDF utilizando sus respectivas rutas de archivo (documentPath1 y documentPath2). Las rutas se especifican como cadenas vacías por ahora, pero en la práctica, reemplazarías estas con las rutas de archivo reales.

2. Proceso de Comparación.

- Selección de Página - la comparación se limita a la primera página de cada documento ('Pages[1]').
- Opciones de Comparación:

'AdditionalChangeMarks = true' - esta opción asegura que se muestren marcadores de cambio adicionales. Estos marcadores resaltan diferencias que podrían estar presentes en otras páginas, incluso si no están en la página actual que se está comparando.

'ComparisonMode = ComparisonMode.IgnoreSpaces' - este modo le dice al comparador que ignore los espacios en el texto, enfocándose solo en los cambios dentro de las palabras.

3. El documento de comparación resultante, que resalta las diferencias entre las dos páginas, se guarda en la ruta de archivo especificada en 'resultPdfPath'.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingSpecificPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], dataDir + "ComparingSpecificPages_out.pdf", new Aspose.Pdf.Comparison.SideBySideComparisonOptions
            {
                AdditionalChangeMarks = true,
                ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
            });
        }
    }
}
```

## Comparar Documentos Completos

El segundo fragmento de código amplía el alcance para comparar todo el contenido de dos documentos PDF.

Pasos:

1. Inicialización del Documento.
Al igual que en el primer ejemplo, se inicializan dos documentos PDF con sus rutas de archivo.

2. Proceso de Comparación.

- Comparación de Documento Completo - a diferencia del primer fragmento, este código compara todo el contenido de los dos documentos.

- Opciones de Comparación - las opciones son las mismas que en el primer fragmento, asegurando que se ignoren los espacios y se muestren marcadores de cambio adicionales.

3. El resultado de la comparación, que resalta las diferencias en todas las páginas de los dos documentos, se guarda en el archivo especificado por 'resultPdfPath'.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingEntireDocuments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(
                document1,
                document2,
                dataDir + "ComparingEntireDocuments_out.pdf",
                new Aspose.Pdf.Comparison.SideBySideComparisonOptions
                {
                    AdditionalChangeMarks = true,
                    ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
                });
        }
    }
}
```

Los resultados de comparación generados por estos fragmentos son documentos PDF que puedes abrir en un visor como Adobe Acrobat. Si usas la vista de dos páginas en Adobe Acrobat, verás los cambios lado a lado:

- Eliminaciones - estas se anotan en la página izquierda.
- Inserciones - estas se anotan en la página derecha.

Al establecer 'AdditionalChangeMarks' en 'true', también puedes ver marcadores para cambios que pueden ocurrir en otras páginas, incluso si esos cambios no están en la página actual que se está viendo.

**Aspose.PDF for .NET** proporciona herramientas robustas para comparar documentos PDF, ya sea que necesites comparar páginas específicas o documentos completos. Al usar opciones como 'AdditionalChangeMarks' y diferentes configuraciones de 'ComparisonMode', puedes adaptar el proceso de comparación a tus necesidades específicas. El documento resultante proporciona una vista clara, lado a lado de los cambios, facilitando el seguimiento de revisiones y asegurando la precisión del documento.

## Comparar documentos PDF usando GraphicalPdfComparer

Al colaborar en documentos, especialmente en entornos profesionales, a menudo terminas con múltiples versiones del mismo archivo.

Puedes usar la clase [GraphicalPdfComparer](https://reference.aspose.com/pdf/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/) para comparar documentos y páginas PDF. La clase es adecuada para comparar cambios en el contenido gráfico de una página.

Con Aspose.PDF for .NET, es posible comparar documentos y páginas y exportar el resultado de la comparación a un documento PDF o archivo de imagen.

Puedes establecer las siguientes propiedades de la clase:

- Resolución - resolución en unidades DPI para imágenes de salida, así como para imágenes generadas durante la comparación.
- Color - el color de los marcadores de cambio.
- Umbral - umbral de cambio en porcentaje. El valor predeterminado es cero. Establecer un valor diferente de cero te permite ignorar cambios gráficos que son insignificantes para ti.

La clase tiene un método que te permite obtener diferencias de imagen de página en una forma adecuada para un procesamiento posterior: **ImagesDifference GetDifference(Page page1, Page page2)**.

Este método devuelve un objeto de la clase [ImagesDifference](https://reference.aspose.com/pdf/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/) que contiene una imagen de la primera página que se compara y un array de diferencias. El array de diferencias y la imagen original tienen el formato de píxel **RGB24bpp**.

ImagesDifference te permite generar una imagen diferente y obtener una imagen de la segunda página que se compara al agregar un array de diferencias a la imagen original. Para hacer esto, utiliza los métodos **ImagesDifference.GetDestinationImage y ImagesDifference.DifferenceToImage**.

### Comparar PDF con el método GetDifference

El código proporcionado define un método [GetDifference](https://reference.aspose.com/pdf/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/#methods) que compara dos documentos PDF y genera representaciones visuales de las diferencias entre ellos.

Este método compara las primeras páginas de dos archivos PDF y genera dos imágenes PNG:

- Una imagen (diffPngFilePath) resalta las diferencias entre las páginas en rojo.
- La otra imagen (destPngFilePath) es una representación visual de la página PDF de destino (segunda).

Este proceso puede ser útil para comparar visualmente cambios o diferencias entre dos versiones de un documento.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithGetDifferenceMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod2.pdf"))
        {
            // Create comparer 
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer();
            // Compare
            using (var imagesDifference = comparer.GetDifference(document1.Pages[1], document2.Pages[1]))
            {
                using (var diffImg = imagesDifference.DifferenceToImage(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.White))
                {
                    diffImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png");
                }
                using (var destImg = imagesDifference.GetDestinationImage())
                {
                    destImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png");
                }
            }
        }
    }
}
```

### Comparar PDF con el método CompareDocumentsToPdf

El fragmento de código proporcionado utilizó el método [CompareDocumentsToPdf](https://reference.aspose.com/pdf/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/comparedocumentstopdf/) que compara dos documentos y genera un informe PDF de los resultados de la comparación.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithCompareDocumentsToPdfMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf"))
        {
            // Create comparer
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer()
            {
                Threshold = 3.0,
                Color = Aspose.Pdf.Color.Blue,
                Resolution = new Aspose.Pdf.Devices.Resolution(300)
            };
            // Compare
            comparer.CompareDocumentsToPdf(document1, document2, dataDir + "compareDocumentsToPdf_out.pdf");
        }
    }
}
```