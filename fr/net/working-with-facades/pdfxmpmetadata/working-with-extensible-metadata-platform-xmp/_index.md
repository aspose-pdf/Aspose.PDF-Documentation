---
title: Plateforme de Métadonnées Extensible - XMP
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/working-with-extensible-metadata-platform-xmp/
description: Cette section explique comment travailler avec la Plateforme de Métadonnées Extensible - XMP en utilisant la classe PdfXmpMetadata.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extensible Metadata Platform - XMP",
    "alternativeHeadline": "Enhanced PDF Metadata Management with XMP Integration",
    "abstract": "La fonctionnalité de la Plateforme de Métadonnées Extensible (XMP) dans Aspose.PDF for .NET permet aux utilisateurs d'incorporer et de manipuler efficacement des métadonnées standardisées et propriétaires dans des fichiers PDF. En utilisant la classe PdfXmpMetadata, cette fonctionnalité simplifie le processus de suivi des modifications et d'amélioration des capacités sémantiques des documents PDF, en faisant un outil précieux pour les développeurs cherchant à intégrer une gestion avancée des métadonnées.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "412",
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
    "url": "/net/working-with-extensible-metadata-platform-xmp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-extensible-metadata-platform-xmp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

{{% alert color="primary" %}}

La Plateforme de Métadonnées Extensible (XMP) est une norme créée par Adobe Systems Inc. Cette norme a été développée pour traiter et stocker des métadonnées standardisées et propriétaires. Ces métadonnées peuvent être intégrées dans différents formats de fichiers, mais dans cet article, nous nous concentrerons uniquement sur le format de fichier PDF. Nous verrons comment nous pouvons intégrer des métadonnées dans un fichier PDF en utilisant l'espace de noms Aspose.Pdf.Facades dans Aspose.PDF for .NET. Nous utiliserons la classe [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) pour manipuler XMP dans le document PDF.

{{% /alert %}}

## Contexte

Un fichier PDF passe par de nombreuses étapes au cours de sa vie. Nous créons un document PDF puis le transmettons à d'autres personnes ou départements pour un traitement ultérieur. Cependant, au cours de ce processus, nous devons suivre différents aspects des modifications apportées. XMP sert à cet objectif de suivi des modifications ou d'autres informations sur les données dans le fichier.

## Explication

Afin de manipuler XMP en utilisant Aspose.Pdf.Facades, nous utiliserons la classe [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class). Nous utiliserons cette classe pour manipuler les propriétés de métadonnées prédéfinies. La classe [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) ajoute ces propriétés à un fichier PDF. Elle aide également à ouvrir et à enregistrer des fichiers PDF dans lesquels nous ajoutons des métadonnées. Ainsi, en utilisant la classe [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class), nous pouvons facilement manipuler XMP dans un fichier PDF.
Le code suivant vous aidera à comprendre comment utiliser la classe [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) pour travailler avec XMP :

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create an object of PdfXmpMetadata class
    var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata();

    // Create input and output file streams
    using (var input = new FileStream(dataDir + "FilledForm.pdf", FileMode.Open))
    {
        using (var output = new FileStream(dataDir + "xmp_out.pdf", FileMode.Create))
        {
            // Bind PDF document
            xmpMetaData.BindPdf(input);

            // Add base URL property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.BaseURL, "xmlns:pdf=http:// Ns.adobe.com/pdf/1.3/");

            // Add creation date property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate, DateTime.Now.ToString());

            // Add Metadata Date property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate, DateTime.Now.ToString());

            // Add Creator Tool property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool, "Creator Tool Name");

            // Add Modify Date to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.ModifyDate, DateTime.Now.ToString());

            // Add Nick Name to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.Nickname, "Test");

            // Save PDF document
            xmpMetaData.Save(output);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create an object of PdfXmpMetadata class
    var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata();

    // Create input and output file streams
    using var input = new FileStream(dataDir + "FilledForm.pdf", FileMode.Open);

    using var output = new FileStream(dataDir + "xmp_out.pdf", FileMode.Create);

    // Bind PDF document
    xmpMetaData.BindPdf(input);

    // Add base URL property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.BaseURL, "xmlns:pdf=http:// Ns.adobe.com/pdf/1.3/");

    // Add creation date property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate, DateTime.Now.ToString());

    // Add Metadata Date property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate, DateTime.Now.ToString());

    // Add Creator Tool property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool, "Creator Tool Name");

    // Add Modify Date to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.ModifyDate, DateTime.Now.ToString());

    // Add Nick Name to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.Nickname, "Test");

    // Save PDF document
    xmpMetaData.Save(output);
}
```
{{< /tab >}}
{{< /tabs >}}

## Conclusion

{{% alert color="primary" %}}
Dans cet article, nous avons vu comment nous pouvons travailler avec XMP en utilisant Aspose.Pdf.Facades. La classe [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class), utilisée dans cet article, facilite grandement la manipulation des métadonnées dans un document PDF. Si la classe [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) est utilisée correctement, il sera très facile d'incorporer de l'intelligence dans les fichiers PDF, rapprochant ainsi le web sémantique de sa réalisation.
{{% /alert %}}