---
title: Update Links in PDF
linktitle: Update Links
type: docs
weight: 20
url: /net/update-links/
description: Mettre à jour les liens dans un PDF de manière programmatique. Ce guide concerne la mise à jour des liens dans un PDF en langage C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Update Links in PDF",
    "alternativeHeadline": "How to update Links in PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, update link in pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "url": "/net/update-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/update-links/"
    },
    "dateModified": "2022-02-04",
    "description": "Mettre à jour les liens dans un PDF de manière programmatique. Ce guide concerne la mise à jour des liens dans un PDF en langage C#."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Mettre à jour les liens dans un fichier PDF

Comme discuté dans Ajouter un hyperlien dans un fichier PDF, la classe [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) permet d'ajouter des liens dans un fichier PDF. Il existe également une classe similaire utilisée pour obtenir des liens existants à l'intérieur des fichiers PDF. Utilisez cela si vous avez besoin de mettre à jour un lien existant. Pour mettre à jour un lien existant :

1. Chargez un fichier PDF.
1. Allez à une page spécifique dans le fichier PDF.
1. Spécifiez la destination du lien en utilisant la propriété Destination de l'objet [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction).
1. La page de destination est spécifiée en utilisant le constructeur [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination).

### Définir la cible du lien vers une page dans le même document

Le code suivant vous montre comment mettre à jour un lien dans un fichier PDF et définir sa cible sur la deuxième page du document.
Le code suivant montre comment mettre à jour un lien dans un fichier PDF et définir sa cible sur la deuxième page du document.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez vous rendre sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Charger le fichier PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");
// Obtenir la première annotation de lien de la première page du document
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// Modification du lien : changer la destination du lien
GoToAction goToAction = (GoToAction)linkAnnot.Action;
// Spécifier la destination pour l'objet lien
// Le premier paramètre est l'objet document, le second est le numéro de la page de destination.
// Le 5ème argument est le facteur de zoom lors de l'affichage de la page respective. Lorsqu'on utilise 2, la page sera affichée avec un zoom de 200%
goToAction.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 1, 2, 2);
dataDir = dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf";
// Sauvegarder le document avec le lien mis à jour
doc.Save(dataDir);
```
### Définir la destination du lien vers une adresse Web

Pour mettre à jour l'hyperlien afin qu'il pointe vers une adresse Web, instanciez l'objet [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) et passez-le à la propriété Action de LinkAnnotation. Le fragment de code suivant montre comment mettre à jour un lien dans un fichier PDF et définir sa cible sur une adresse Web.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Charger le fichier PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");

// Obtenir la première annotation de lien de la première page du document
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// Modification du lien : changer l'action du lien et définir la cible comme adresse Web
linkAnnot.Action = new GoToURIAction("www.aspose.com");

dataDir = dataDir + "SetDestinationLink_out.pdf";
// Sauvegarder le document avec le lien mis à jour
doc.Save(dataDir);
```
### Définir la cible du lien vers un autre fichier PDF

Le code suivant montre comment mettre à jour un lien dans un fichier PDF et définir sa cible vers un autre fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Charger le fichier PDF
Document document = new Document(dataDir + "UpdateLinks.pdf");

LinkAnnotation linkAnnot = (LinkAnnotation)document.Pages[1].Annotations[1];

GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.Action;
// La ligne suivante met à jour la destination, ne met pas à jour le fichier
goToR.Destination = new XYZExplicitDestination(2, 0, 0, 1.5);
// La ligne suivante met à jour le fichier
goToR.File = new FileSpecification(dataDir +  "input.pdf");

dataDir = dataDir + "SetTargetLink_out.pdf";
// Sauvegarder le document avec le lien mis à jour
document.Save(dataDir);
```

### Mettre à jour la couleur du texte de LinkAnnotation

L'annotation de lien ne contient pas de texte.
L'annotation de lien ne contient pas de texte.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Charger le fichier PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    if (annotation is LinkAnnotation)
    {
        // Rechercher le texte sous l'annotation
        TextFragmentAbsorber ta = new TextFragmentAbsorber();
        Rectangle rect = annotation.Rect;
        rect.LLX -= 10;
        rect.LLY -= 10;
        rect.URX += 10;
        rect.URY += 10;
        ta.TextSearchOptions = new TextSearchOptions(rect);
        ta.Visit(doc.Pages[1]);
        // Changer la couleur du texte.
        foreach (TextFragment tf in ta.TextFragments)
        {
            tf.TextState.ForegroundColor = Color.Red;
        }
    }

}
dataDir = dataDir + "UpdateLinkTextColor_out.pdf";
// Sauvegarder le document avec le lien mis à jour
doc.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Bibliothèque Aspose.PDF pour .NET",
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

