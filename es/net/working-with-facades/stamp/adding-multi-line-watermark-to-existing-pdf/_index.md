---
title: Agregar marca de agua de varias líneas
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/adding-multi-line-watermark-to-existing-pdf/
description: Esta sección explica cómo agregar una marca de agua de varias líneas a un PDF existente utilizando la clase FormattedText.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding multi line watermark",
    "alternativeHeadline": "Enhance PDFs with Multi-Line Watermarks Easily",
    "abstract": "Presentando la capacidad de agregar marcas de agua de varias líneas a PDFs existentes utilizando el espacio de nombres Aspose.Pdf.Facades. Esta nueva funcionalidad simplifica el proceso, permitiendo a los usuarios incorporar fácilmente múltiples líneas de texto en sus documentos con el nuevo método AddNewLineText() implementado en la clase FormattedText. Mejora tus presentaciones en PDF con marcas de agua personalizadas de varias líneas sin esfuerzo",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "188",
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
    "url": "/net/adding-multi-line-watermark-to-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-multi-line-watermark-to-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

{{% alert color="primary" %}}

Muchos usuarios quieren estampar sus documentos PDF con texto de varias líneas. Por lo general, intentan usar `\n` y `<br>`, pero estos tipos de caracteres no son compatibles con el espacio de nombres Aspose.Pdf.Facades. Por lo tanto, para hacerlo posible, hemos agregado otro método llamado [AddNewLineText()](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext/methods/addnewlinetext/index) en la clase [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) del espacio de nombres Aspose.Pdf.Facades.

{{% /alert %}}

## Detalles de implementación

Por favor, consulta el siguiente bloque de código para agregar una marca de agua de varias líneas en un PDF existente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampToPdf()
{
    // Instantiate a stamp object
    var logoStamp = new Aspose.Pdf.Facades.Stamp();

    // Instantiate an object of FormattedText class
    var formatText = new Aspose.Pdf.Facades.FormattedText("Hello World!",
        System.Drawing.Color.FromArgb(180, 0, 0), 
        Aspose.Pdf.Facades.FontStyle.TimesItalic,
        Aspose.Pdf.Facades.EncodingType.Winansi, false, 50);

    // Add another line for Stamp
    formatText.AddNewLineText("Good Luck");
    // BindLogo to PDF
    logoStamp.BindLogo(formatText);
}
```