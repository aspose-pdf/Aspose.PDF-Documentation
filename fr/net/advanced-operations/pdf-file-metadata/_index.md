---
title: Travailler avec les métadonnées de fichiers PDF | C#
linktitle: Métadonnées de fichiers PDF
type: docs
weight: 140
url: fr/net/pdf-file-metadata/
description: Cette section explique comment obtenir les informations d'un fichier PDF, comment obtenir les métadonnées XMP d'un fichier PDF, définir les informations d'un fichier PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Travailler avec les métadonnées de fichiers PDF | C#",
    "alternativeHeadline": "Comment obtenir les métadonnées de fichiers PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, métadonnées de fichiers pdf",
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
    "url": "/net/pdf-file-metadata/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-file-metadata/"
    },
    "dateModified": "2022-02-04",
    "description": "Cette section explique comment obtenir les informations d'un fichier PDF, comment obtenir les métadonnées XMP d'un fichier PDF, définir les informations d'un fichier PDF."
}
</script>
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Obtenir les informations du fichier PDF

Pour obtenir des informations spécifiques à un fichier PDF, vous devez d'abord obtenir l'objet [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) en utilisant la propriété [Info](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/info) de l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Une fois l'objet [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) récupéré, vous pouvez obtenir les valeurs des propriétés individuelles. Le code suivant vous montre comment obtenir les informations d'un fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "GetFileInfo.pdf");
// Obtenir les informations du document
DocumentInfo docInfo = pdfDocument.Info;
// Afficher les informations du document
Console.WriteLine("Auteur : {0}", docInfo.Author);
Console.WriteLine("Date de création : {0}", docInfo.CreationDate);
Console.WriteLine("Mots-clés : {0}", docInfo.Keywords);
Console.WriteLine("Date de modification : {0}", docInfo.ModDate);
Console.WriteLine("Sujet : {0}", docInfo.Subject);
Console.WriteLine("Titre : {0}", docInfo.Title);
```
## Définir les informations du fichier PDF

Aspose.PDF pour .NET vous permet de définir des informations spécifiques à un fichier pour un PDF, des informations comme l'auteur, la date de création, le sujet et le titre. Pour définir ces informations :

1. Créez un objet [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo).
1. Définissez les valeurs des propriétés.
1. Enregistrez le document mis à jour en utilisant la méthode Save de la classe Document.

{{% alert color="primary" %}}

Veuillez noter que vous ne pouvez pas définir de valeurs pour les champs *Application* et *Producer*, car Aspose Ltd. et Aspose.PDF pour .NET x.x.x seront affichés contre ces champs.

{{% /alert %}}

Le code suivant montre comment définir les informations d'un fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "SetFileInfo.pdf");

// Spécifier les informations du document
DocumentInfo docInfo = new DocumentInfo(pdfDocument);

docInfo.Author = "Aspose";
docInfo.CreationDate = DateTime.Now;
docInfo.Keywords = "Aspose.Pdf, DOM, API";
docInfo.ModDate = DateTime.Now;
docInfo.Subject = "Informations PDF";
docInfo.Title = "Définition des informations du document PDF";

dataDir = dataDir + "SetFileInfo_out.pdf";
// Enregistrer le document de sortie
pdfDocument.Save(dataDir);
```
## Obtenir les métadonnées XMP d'un fichier PDF

Aspose.PDF vous permet d'accéder aux métadonnées XMP d'un fichier PDF. Pour obtenir les métadonnées d'un fichier PDF :

1. Créez un objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) et ouvrez le fichier PDF d'entrée.
1. Obtenez les métadonnées du fichier en utilisant la propriété [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata).

Le fragment de code suivant vous montre comment obtenir les métadonnées du fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "GetXMPMetadata.pdf");

// Obtenir les propriétés
Console.WriteLine(pdfDocument.Metadata["xmp:CreateDate"]);
Console.WriteLine(pdfDocument.Metadata["xmp:Nickname"]);
Console.WriteLine(pdfDocument.Metadata["xmp:CustomProperty"]);
```

## Définir les métadonnées XMP dans un fichier PDF

Aspose.PDF vous permet de définir des métadonnées dans un fichier PDF.
Aspose.PDF vous permet de définir les métadonnées dans un fichier PDF.

1. Créez un objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Définissez les valeurs des métadonnées à l'aide de la propriété [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata).
1. Enregistrez le document mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) de l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Le code suivant montre comment définir les métadonnées dans un fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");

// Définir les propriétés
pdfDocument.Metadata["xmp:CreateDate"] = DateTime.Now;
pdfDocument.Metadata["xmp:Nickname"] = "Nickname";
pdfDocument.Metadata["xmp:CustomProperty"] = "Custom Value";

dataDir = dataDir + "SetXMPMetadata_out.pdf";
// Enregistrer le document
pdfDocument.Save(dataDir);
```
## Insérer des métadonnées avec un préfixe

Certains développeurs ont besoin de créer un nouvel espace de noms de métadonnées avec un préfixe. Le fragment de code suivant montre comment insérer des métadonnées avec un préfixe.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");
pdfDocument.Metadata.RegisterNamespaceUri("xmp", "http:// Ns.adobe.com/xap/1.0/"); // Le préfixe Xmlns a été supprimé
pdfDocument.Metadata["xmp:ModifyDate"] = DateTime.Now;

dataDir = dataDir + "SetPrefixMetadata_out.pdf";
// Sauvegarder le document
pdfDocument.Save(dataDir);
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


