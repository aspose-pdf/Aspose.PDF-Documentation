---
title: Ajout d'une pièce jointe à un document PDF
linktitle: Ajout d'une pièce jointe à un document PDF
type: docs
weight: 10
url: /net/add-attachment-to-pdf-document/
description: Cette page décrit comment ajouter une pièce jointe à un fichier PDF avec la bibliothèque Aspose.PDF pour . NET
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/adding-to-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajout d'une pièce jointe à un document PDF",
    "alternativeHeadline": "Comment ajouter des pièces jointes à un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, pièces jointes dans pdf",
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
    "url": "/net/add-attachment-to-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-attachment-to-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Cette page décrit comment ajouter une pièce jointe à un fichier PDF avec la bibliothèque Aspose.PDF pour . NET"
}
</script>
Les pièces jointes peuvent contenir une grande variété d'informations et peuvent être de différents types de fichiers. Cet article explique comment ajouter une pièce jointe à un fichier PDF.

Le prochain extrait de code fonctionne également avec une nouvelle interface graphique [Aspose.Drawing](/pdf/net/drawing/).

1. Créez un nouveau projet C#.
1. Ajoutez une référence au DLL Aspose.PDF.
1. Créez un objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Créez un objet [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) avec le fichier que vous ajoutez, et la description du fichier.
1. Ajoutez l'objet [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) à la collection [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) de l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), avec la méthode Add de la collection.

La collection [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) contient toutes les pièces jointes dans le fichier PDF.
changefreq: "monthly"
type: docs
La collection [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) contient toutes les pièces jointes dans le fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "AddAttachment.pdf");

// Configurer le nouveau fichier à ajouter en tant que pièce jointe
FileSpecification fileSpecification = new FileSpecification(dataDir + "test.txt", "Fichier texte d'exemple");

// Ajouter la pièce jointe à la collection de pièces jointes du document
pdfDocument.EmbeddedFiles.Add(fileSpecification);

// Sauvegarder le document mis à jour
pdfDocument.Save(dataDir + "AddllAnnotations_out.pdf");
```

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

