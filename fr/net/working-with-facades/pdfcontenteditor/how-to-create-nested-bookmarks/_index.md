---
title: Ajouter des signets à un fichier PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/how-to-create-nested-bookmarks/
description: Cette section explique comment créer des signets imbriqués avec la classe PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Bookmarks to PDF file",
    "alternativeHeadline": "Create Nested Bookmarks in PDF Documents Easily",
    "abstract": "Améliorez vos documents PDF avec la nouvelle fonctionnalité de signets imbriqués en utilisant la classe PdfContentEditor d'Aspose.Pdf.Facades. Cette fonctionnalité vous permet de créer des signets hiérarchiques qui organisent efficacement votre contenu, permettant aux utilisateurs de naviguer facilement à travers les chapitres et les pages associées dans le PDF. Rationalisez la navigation dans le document et améliorez l'expérience utilisateur avec cette solution de signets sophistiquée.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "211",
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
    "url": "/net/how-to-create-nested-bookmarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/how-to-create-nested-bookmarks/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

Les signets vous donnent la possibilité de suivre/lier à une page spécifique à l'intérieur du document PDF. La classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) dans l'[espace de noms Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) fournit une fonctionnalité qui vous permet de créer votre propre signet de manière sophistiquée mais intuitive dans un fichier PDF existant, à une page donnée ou sur toutes les pages.

## Détails de mise en œuvre

En plus de la création de signets simples, il arrive parfois que vous ayez besoin de créer un signet sous la forme de chapitres où vous imbriquez les signets individuels à l'intérieur des signets de chapitre afin que lorsque vous cliquez sur le signe + pour un chapitre, vous puissiez voir les pages à l'intérieur lorsque les signets se développent, comme montré dans l'image ci-dessous.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmarksAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Sample.pdf"))
    {
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        editor.CreateBookmarksAction("Bookmark 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo_Bookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmarksAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "Sample.pdf");

    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    editor.CreateBookmarksAction("Bookmark 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo_Bookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}