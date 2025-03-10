---
title: Exemple de Hello World utilisant le langage C#
linktitle: Bonjour le monde exemple
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/hello-world-example/
description: Cet exemple démontre comment créer un document PDF simple avec le texte Hello World en utilisant Aspose.PDF
aliases:
    - /net/hello-world/
lastmod: "2022-02-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Example of Hello World using C# language",
    "alternativeHeadline": "Aspose.PDF C# example",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "302",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "http://docs.aspose.com/pdf/net/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/net/hello-world-example/"
    },
    "dateModified": "2024-11-26",
    "description": "Cet exemple démontre comment créer un document PDF simple avec le texte Hello World en utilisant Aspose.PDF",
    "articleBody": "A \"Hello World\" example is traditionally used to introduce features of a programming language or software with a simple use case.\nAspose.PDF for .NET is a feature rich PDF API that allows the developers to embed PDF document creation, manipulation & conversion capabilities in their .NET applications. It supports working with many popular file formats including PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX and image file formats. In this article, we are creating a PDF document containing text \"Hello World!\". After installing Aspose.PDF for .NET in your environment, you can execute below code sample to see how Aspose.PDF API works.\nBelow code snippet follows these steps:\n1. // Create PDF document\n2. Add a Page to document object\n3. Create a TextFragment\n4. Add TextFragment to Paragraph collection of the page\n5. Save resultant PDF document\nFollowing code snippet is a Hello World program to exhibit working of Aspose.PDF for .NET API."
}
</script>

Un exemple "Hello World" est traditionnellement utilisé pour introduire les fonctionnalités d'un langage de programmation ou d'un logiciel avec un cas d'utilisation simple.

Aspose.PDF for .NET est une API PDF riche en fonctionnalités qui permet aux développeurs d'intégrer des capacités de création, de manipulation et de conversion de documents PDF dans leurs applications .NET. Elle prend en charge le travail avec de nombreux formats de fichiers populaires, y compris PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX et des formats de fichiers image. Dans cet article, nous créons un document PDF contenant le texte "Hello World!". Après avoir installé Aspose.PDF for .NET dans votre environnement, vous pouvez exécuter l'exemple de code ci-dessous pour voir comment fonctionne l'API Aspose.PDF.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Le code ci-dessous suit ces étapes :

1. Instancier un objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Ajouter une [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) à l'objet document.
1. Créer un objet [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment).
1. Ajouter le TextFragment à la collection [Paragraph](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) de la page.
1. [Enregistrer](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) le document PDF résultant.

Le code suivant est un programme Hello World pour montrer le fonctionnement de l'API Aspose.PDF for .NET.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void HelloWorld()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```