---
title: Travailler avec la rotation des pages
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/working-with-page-rotation/
description: Cette section explique comment travailler avec la rotation des pages en utilisant la classe PdfPageEditor.
lastmod: "2021-07-07"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Page Rotation",
    "alternativeHeadline": "Effortlessly Rotate PDF Pages with PdfPageEditor",
    "abstract": "Découvrez la puissante fonctionnalité de rotation des pages dans la classe PdfPageEditor, permettant une manipulation précise des pages de document grâce à des angles de rotation personnalisables. Avec des options pour spécifier des rotations de pages individuelles ou appliquer une rotation uniforme sur les pages sélectionnées, cette fonctionnalité améliore les capacités d'édition PDF, offrant plus de flexibilité et de contrôle aux utilisateurs.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "202",
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
    "url": "/net/working-with-page-rotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-page-rotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

{{% alert color="primary" %}}

La classe [PdfPageEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfpageeditor) fournit la possibilité de faire pivoter une page.

{{% /alert %}}

## Faire pivoter une page en utilisant PageRotations

Pour faire pivoter des pages dans un document, nous pouvons utiliser [PageRotations](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfpageeditor/properties/pagerotations).
`PageRotations` contient le numéro de page et le degré de rotation, la clé représente le numéro de page, la valeur de la clé représente la rotation en degrés.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void RotatePages1()
 {
    // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     using (var editor = new Aspose.Pdf.Facades.PdfPageEditor())
     {
         // Bind PDF document
         editor.BindPdf(dataDir + "sample.pdf");

         // Specify the page rotation dictionary
         editor.PageRotations = new System.Collections.Generic.Dictionary<int, int>
         {
             { 1, 90 },
             { 2, 180 },
             { 3, 270 }
         };

         // Save PDF document
         editor.Save(dataDir + "sample-rotate-a.pdf");
     }
 }
```

## Faire pivoter une page en utilisant Rotation

Nous pouvons également utiliser la propriété [Rotation](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfpageeditor/properties/rotation). La rotation doit être 0, 90, 180 ou 270.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RotatePages2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    using (var editor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");

        // Specify the pages to rotate and the rotation angle
        editor.ProcessPages = new int[] { 1, 3 };
        editor.Rotation = 90;

        // Save PDF document
        editor.Save(dataDir + "sample-rotate-a.pdf");
    }
}
```