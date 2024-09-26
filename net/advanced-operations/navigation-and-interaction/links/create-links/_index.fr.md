---
title: Créer des liens dans un fichier PDF avec C#
linktitle: Créer des liens
type: docs
weight: 10
url: /net/create-links/
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
    "headline": "Créer des liens dans un fichier PDF avec C#",
    "alternativeHeadline": "Comment créer des liens dans un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, créer un lien dans pdf",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de documentation Aspose.PDF",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
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
    "dateModified": "2022-02-04",
    "description": "Cette section explique comment créer des liens dans votre document PDF avec C#."
}
</script>
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Créer des Liens

En ajoutant un lien vers une application dans un document, il est possible de lier des applications depuis un document. Cela est utile lorsque vous souhaitez que les lecteurs prennent une action spécifique à un moment précis d'un tutoriel, par exemple, ou pour créer un document riche en fonctionnalités. Pour créer un lien vers une application :

1. [Créez un objet Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Obtenez la [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) à laquelle vous voulez ajouter un lien.
1. Créez un objet [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) en utilisant les objets Page et [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle).
1. Définissez les attributs du lien en utilisant l'objet [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation).
1. Lors de la création de l'objet [LaunchAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction), spécifiez l'application que vous souhaitez lancer.
1. Ajoutez le lien à la propriété [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/annotations) de l'objet Page.
1. Enfin, enregistrez le PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) de l'objet Document.

Le code suivant montre comment créer un lien vers une application dans un fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Ouvrir le document
Document document = new Document(dataDir + "CreateApplicationLink.pdf");

// Créer un lien
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
page.Annotations.Add(link);

dataDir = dataDir + "CreateApplicationLink_out.pdf";
// Enregistrer le document mis à jour
document.Save(dataDir);
```
### Créer un lien de document PDF dans un fichier PDF

Aspose.PDF pour .NET vous permet d'ajouter un lien vers un fichier PDF externe afin que vous puissiez lier plusieurs documents ensemble. Pour créer un lien de document PDF :

1. Tout d'abord, créez un objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
2. Ensuite, obtenez la [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) spécifique à laquelle vous souhaitez ajouter le lien.
3. Créez un objet [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) en utilisant les objets Page et [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle).
4. Définissez les attributs du lien à l'aide de l'objet [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation).
5. Définissez la propriété Action sur l'objet [GoToRemoteAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoremoteaction).
1. Ajoutez le lien à la collection Annotations de l'objet Page.
1. Enregistrez le PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) de l'objet Document.

Le code suivant illustre comment créer un lien de document PDF dans un fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Ouvrir le document
Document document = new Document(dataDir+ "CreateDocumentLink.pdf");
// Créer le lien
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
page.Annotations.Add(link);
dataDir = dataDir + "CreateDocumentLink_out.pdf";
// Enregistrer le document mis à jour
document.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour la bibliothèque .NET",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
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
    "applicationCategory": "Bibliothèque de manipulation de PDF pour .NET",
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
```

