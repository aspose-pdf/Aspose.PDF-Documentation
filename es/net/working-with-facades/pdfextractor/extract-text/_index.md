---
title: Extraer texto de un archivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /es/net/extract-text/
description: Esta sección explica cómo extraer texto de un PDF utilizando la clase PdfExtractor.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text from PDF File",
    "alternativeHeadline": "Effortless Text Extraction from PDF Files",
    "abstract": "La clase PdfExtractor permite una extracción eficiente de texto de archivos PDF a través de múltiples métodos, permitiendo a los usuarios recuperar texto, imágenes y archivos adjuntos con facilidad. Al utilizar métodos como ExtractText, GetText y GetNextPageText, los desarrolladores pueden extraer y guardar sin problemas contenido textual de páginas individuales o documentos completos, agilizando las tareas de manipulación de PDF. Con modos de extracción flexibles disponibles, esta función mejora el control sobre el formato de salida, convirtiéndola en una herramienta esencial para cualquier persona que trabaje con datos PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "441",
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
    "url": "/net/extract-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

En este artículo, analizaremos los detalles de la extracción de texto de un archivo PDF. Todas estas características de extracción se proporcionan en un solo lugar, en la clase [PdfExtractor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfextractor). Veremos cómo utilizar estas características en nuestro código.

La clase [PdfExtractor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfextractor) proporciona tres tipos de capacidades de extracción. Estas tres categorías son Texto, Imágenes y Archivos Adjuntos. Para realizar la extracción en cada una de estas tres categorías, PdfExtractor proporciona varios métodos que trabajan juntos para darte el resultado final.

Por ejemplo, para extraer texto puedes usar tres métodos, es decir, [ExtractText, GetText, HasNextPageText y GetNextPageText](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfextractor/methods/index). Ahora, para comenzar a extraer texto, primero debes llamar al método [ExtractText](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfextractor/methods/extracttext/index); esto extraerá el texto del archivo PDF y lo almacenará en memoria. Después de eso, el método [GetText](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfextractor/methods/gettext/index) tomará este texto extraído y lo guardará en el disco en la ubicación especificada en un archivo. [HasNextPageText](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfextractor/methods/hasnextpagetext) te ayuda a recorrer cada página y verificar si la siguiente página tiene texto o no. Si contiene texto, entonces [GetNextPageText](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfextractor/methods/getnextpagetext/index) te ayudará a guardar el texto de una página individual en el archivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    bool wholeText = true;
    // Create an object of the PdfExtractor class
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "sample.pdf");

        // ExtractText
        pdfExtractor.ExtractText();

        if (!wholeText)
        {
            pdfExtractor.GetText(dataDir + "sample.txt");
        }
        else
        {
            // Extract the text into separate files
            int pageNumber = 1;
            while (pdfExtractor.HasNextPageText())
            {
                pdfExtractor.GetNextPageText($"{dataDir}\\sample{pageNumber:D3}.txt");
                pageNumber++;
            }
        }
    }
}
```

Para extraer el modo de extracción de texto, utiliza el siguiente código:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextExtractonMode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    bool wholeText = true;
    // Create an object of the PdfExtractor class
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "ExtractTextExtractonMode.pdf");

        // ExtractText
        // pdfExtractor.ExtractTextMode = 0; // pure mode
        pdfExtractor.ExtractTextMode = 1; // raw mode
        pdfExtractor.ExtractText();

        if (!wholeText)
        {
            pdfExtractor.GetText(dataDir + "ExtractTextExtractonMode_out.txt");
        }
        else
        {
            // Extract the text into separate files
            int pageNumber = 1;
            while (pdfExtractor.HasNextPageText())
            {
                pdfExtractor.GetNextPageText($"{dataDir}\\sample{pageNumber:D3}.txt");
                pageNumber++;
            }
        }
    }
}
```