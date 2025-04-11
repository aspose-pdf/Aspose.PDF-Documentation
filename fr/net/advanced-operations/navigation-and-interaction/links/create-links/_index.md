---
title: Créer des liens dans un fichier PDF avec C#
linktitle: Créer des liens
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/create-links/
description: Cette section explique comment créer des liens dans votre document PDF avec C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create Links in PDF file with C#",
    "alternativeHeadline": "Create Interactive Links in PDFs Using C#",
    "abstract": "La nouvelle fonctionnalité permet aux développeurs de créer facilement des liens interactifs dans les documents PDF en utilisant C#. Cette fonctionnalité améliore l'engagement des utilisateurs en liant à des applications externes ou à d'autres fichiers PDF, permettant une expérience de document plus dynamique et riche en fonctionnalités. Idéal pour les tutoriels et pour guider les utilisateurs, cette intégration permet aux utilisateurs de connecter efficacement le contenu.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Create Links, PDF document, C#, LinkAnnotation, LaunchAction, GoToRemoteAction, Aspose.PDF, Document object, PDF manipulation, External link",
    "wordcount": "690",
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
    "url": "/net/create-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-links/"
    },
    "dateModified": "2024-11-25",
    "description": "Cette section explique comment créer des liens dans votre document PDF avec C#."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Créer des liens

En ajoutant un lien vers une application dans un document, il est possible de lier des applications à partir d'un document. Cela est utile lorsque vous souhaitez que les lecteurs effectuent une certaine action à un moment précis dans un tutoriel, par exemple, ou pour créer un document riche en fonctionnalités. Pour créer un lien vers une application :

1. [Créer un Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document) objet.
1. Obtenez la [Page](https://reference.aspose.com/pdf/fr/net/aspose.pdf/page) à laquelle vous souhaitez ajouter le lien.
1. Créez un objet [LinkAnnotation](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/linkannotation) en utilisant les objets Page et [Rectangle](https://reference.aspose.com/pdf/fr/net/aspose.pdf/rectangle).
1. Définissez les attributs du lien en utilisant l'objet [LinkAnnotation](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/linkannotation).
1. De plus, définissez la propriété Action de l'objet [LaunchAction](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/launchaction).
1. Lors de la création de l'objet [LaunchAction](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/launchaction), spécifiez l'application que vous souhaitez lancer.
1. Ajoutez le lien à la propriété [Annotations](https://reference.aspose.com/pdf/fr/net/aspose.pdf/page/properties/annotations) de l'objet Page.
1. Enfin, enregistrez le PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document/methods/save) de l'objet Document.

Le code suivant montre comment créer un lien vers une application dans un fichier PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CreateApplicationLink.pdf"))
    {
        // Create link
        var page = document.Pages[1];
        var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
        link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        link.Action = new Aspose.Pdf.Annotations.LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
        page.Annotations.Add(link);

        // Save PDF document
        document.Save(dataDir + "CreateApplicationLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "CreateApplicationLink.pdf");

    // Create link
    var page = document.Pages[1];
    var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
    link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
    link.Action = new Aspose.Pdf.Annotations.LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
    page.Annotations.Add(link);

    // Save PDF document
    document.Save(dataDir + "CreateApplicationLink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Créer un lien de document PDF dans un fichier PDF

Aspose.PDF for .NET vous permet d'ajouter un lien vers un fichier PDF externe afin que vous puissiez lier plusieurs documents ensemble. Pour créer un lien de document PDF :

1. Tout d'abord, créez un objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document).
1. Ensuite, obtenez la [Page](https://reference.aspose.com/pdf/fr/net/aspose.pdf/page) particulière à laquelle vous souhaitez ajouter le lien.
1. Créez un objet [LinkAnnotation](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/linkannotation) en utilisant les objets Page et [Rectangle](https://reference.aspose.com/pdf/fr/net/aspose.pdf/rectangle).
1. Définissez les attributs du lien en utilisant l'objet [LinkAnnotation](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/linkannotation).
1. Définissez la propriété Action sur l'objet [GoToRemoteAction](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/gotoremoteaction).
1. Lors de la création de l'objet GoToRemoteAction, spécifiez le fichier PDF qui doit être lancé, ainsi que le numéro de page qu'il doit ouvrir.
1. Ajoutez le lien à la collection Annotations de l'objet Page.
1. Enregistrez le PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document/methods/save) de l'objet Document.

Le code suivant montre comment créer un lien de document PDF dans un fichier PDF.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CreateDocumentLink.pdf"))
    {
        // Create link
        var page = document.Pages[1];
        var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
        link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        link.Action = new Aspose.Pdf.Annotations.GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
        page.Annotations.Add(link);

        // Save PDF document
        document.Save(dataDir + "CreateDocumentLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "CreateDocumentLink.pdf");

    // Create link
    var page = document.Pages[1];
    var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
    link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
    link.Action = new Aspose.Pdf.Annotations.GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
    page.Annotations.Add(link);

    // Save PDF document
    document.Save(dataDir + "CreateDocumentLink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>