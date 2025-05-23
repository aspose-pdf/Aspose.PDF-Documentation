---
title: Ajouter des actions Javascript PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/adding-javascript-actions/
description: Découvrez comment ajouter des actions JavaScript, telles que des clics de bouton ou des soumissions de formulaires, aux PDF dans .NET en utilisant Aspose.PDF.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Javascript actions PDF",
    "alternativeHeadline": "Enhance PDF with Interactive JavaScript Actions",
    "abstract": "Améliorez votre PDF en intégrant des actions Javascript interactives avec la classe Aspose.PDF for .NET PdfContentEditor. Cette fonctionnalité permet aux utilisateurs de créer des liens dynamiques et d'exécuter des actions spécifiques d'éléments de menu, enrichissant l'expérience du document avec des éléments interactifs personnalisés. Rationalisez votre flux de travail en ajoutant des actions basées sur des événements qui répondent sans effort aux interactions des utilisateurs.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "216",
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
    "url": "/net/adding-javascript-actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-javascript-actions/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

La classe [PdfContentEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/PdfContentEditor) présente sous le package Aspose.Pdf.Facades offre la flexibilité d'ajouter des actions Javascript à un fichier PDF. Vous pouvez créer un lien avec les actions en série correspondant à l'exécution d'un élément de menu dans le visualiseur PDF. Cette classe fournit également la fonctionnalité de créer des actions supplémentaires pour les événements du document.

Tout d'abord, un objet est dessiné dans le [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document), dans notre exemple un [Rectangle](https://reference.aspose.com/pdf/fr/net/aspose.pdf.drawing/rectangle). Et définissez l'action [createJavaScriptLink](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfcontenteditor/methods/createjavascriptlink) sur le Rectangle. Après cela, vous pouvez enregistrer votre document.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavascriptAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");

        // Create Javascript link
        var rect = new System.Drawing.Rectangle(50, 750, 50, 50);

        var code = "app.alert('Welcome to Aspose!');";
        editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);

        // Save PDF document
        editor.Save(dataDir + "JavaScriptAdded_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavascriptAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");

    // Create Javascript link
    var rect = new System.Drawing.Rectangle(50, 750, 50, 50);

    var code = "app.alert('Welcome to Aspose!');";
    editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);

    // Save PDF document
    editor.Save(dataDir + "JavaScriptAdded_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}