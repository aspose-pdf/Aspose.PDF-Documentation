---
title: Extraer fuentes de PDF C#
linktitle: Extraer fuentes de PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /es/net/extract-fonts-from-pdf/
description: Utilice la biblioteca Aspose.PDF para .NET para extraer todas las fuentes incrustadas de su documento PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Fonts from PDF C#",
    "alternativeHeadline": "Effortlessly Extract All Fonts from PDF Documents",
    "abstract": "Desbloquee el poder de sus documentos PDF con la funcionalidad de la biblioteca Aspose.PDF for .NET que le permite extraer sin esfuerzo todas las fuentes incrustadas. Utilizando el método FontUtilities.GetAllFonts(), los desarrolladores pueden acceder y listar fácilmente las fuentes dentro de cualquier archivo PDF, mejorando las capacidades de análisis y personalización de documentos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "156",
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
    "url": "/net/extract-fonts-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-fonts-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulte la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

En caso de que desee obtener todas las fuentes de un documento PDF, puede utilizar el método FontUtilities.GetAllFonts() proporcionado en la clase Document. Consulte el siguiente fragmento de código para obtener todas las fuentes de un documento PDF existente:

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).
  
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractFonts.pdf"))
    {
        Aspose.Pdf.Text.Font[] fonts = document.FontUtilities.GetAllFonts();
        foreach (Aspose.Pdf.Text.Font font in fonts)
        {
            Console.WriteLine(font.FontName);
        }
    }
}
```