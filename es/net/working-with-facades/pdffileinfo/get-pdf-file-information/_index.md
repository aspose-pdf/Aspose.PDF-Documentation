---
title: Obtener información del archivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /es/net/get-pdf-file-information/
description: Esta sección explica cómo obtener información del archivo PDF con Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get PDF file information",
    "alternativeHeadline": "Retrieve Detailed Information from PDF Files",
    "abstract": "Desbloquee los metadatos esenciales de PDF con la nueva función que utiliza la clase PdfFileInfo de Aspose.PDF for .NET Facades. Esta funcionalidad permite a los desarrolladores acceder y recuperar fácilmente detalles importantes específicos del archivo, como Asunto, Título, Palabras clave y Creador, mejorando los procesos de gestión y análisis de documentos. Optimice sus interacciones con PDF aprovechando esta poderosa herramienta para la recuperación integral de información del archivo.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "285",
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
    "url": "/net/get-pdf-file-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-pdf-file-information/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulte la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

Para obtener información específica del archivo de un archivo PDF, necesita crear un objeto de la clase [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo). Después de eso, puede obtener los valores de las propiedades individuales como Asunto, Título, Palabras clave y Creador, etc.

El siguiente fragmento de código le muestra cómo obtener información del archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPdfInfo()
{
    // Define the directory for input files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf"))
    {
        // Get and display PDF information
        Console.WriteLine("Subject: {0}", fileInfo.Subject);
        Console.WriteLine("Title: {0}", fileInfo.Title);
        Console.WriteLine("Keywords: {0}", fileInfo.Keywords);
        Console.WriteLine("Creator: {0}", fileInfo.Creator);
        Console.WriteLine("Creation Date: {0}", fileInfo.CreationDate);
        Console.WriteLine("Modification Date: {0}", fileInfo.ModDate);

        // Check if the file is a valid PDF and if it is encrypted
        Console.WriteLine("Is Valid PDF: {0}", fileInfo.IsPdfFile);
        Console.WriteLine("Is Encrypted: {0}", fileInfo.IsEncrypted);

        // Get dimensions of the first page
        Console.WriteLine("Page width: {0}", fileInfo.GetPageWidth(1));
        Console.WriteLine("Page height: {0}", fileInfo.GetPageHeight(1));
    }
}
```

## Obtener información meta

Para obtener información, utilizamos la propiedad [Header](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/header). Con 'Hashtable' obtenemos todos los valores posibles.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetMetaInfo()
{
    // Define the directory for input files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of PdfFileInfo object
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "SetMetaInfo_out.pdf"))
    {
        // Retrieve all existing custom attributes
        var hashTable = new System.Collections.Hashtable(fileInfo.Header);

        // Enumerate and display all custom attributes
        var enumerator = hashTable.GetEnumerator();
        while (enumerator.MoveNext())
        {
            string output = $"{enumerator.Key} {enumerator.Value}";
            Console.WriteLine(output);
        }

        // Retrieve and display a specific custom attribute
        Console.WriteLine("Reviewer: " + fileInfo.GetMetaInfo("Reviewer"));
    }
}
```