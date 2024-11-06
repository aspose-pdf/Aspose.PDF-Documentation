---
title: Extraire et Sauvegarder une Pièce Jointe
linktitle: Extraire et Sauvegarder une Pièce Jointe
type: docs
weight: 20
url: fr/net/extract-and-save-an-attachment/
description: Aspose.PDF pour .NET vous permet de récupérer toutes les pièces jointes d'un document PDF. De plus, vous pouvez récupérer une pièce jointe individuelle de votre document.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extraire et Sauvegarder une Pièce Jointe",
    "alternativeHeadline": "Comment extraire et sauvegarder une pièce jointe",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, sauvegarder des pièces jointes, extraire des pièces jointes",
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
    "url": "/net/extract-and-save-an-attachment/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-and-save-an-attachment/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF pour .NET vous permet de récupérer toutes les pièces jointes d'un document PDF. De plus, vous pouvez récupérer une pièce jointe individuelle de votre document."
}
</script>
## Obtenir Tous les Pièces Jointes

Avec Aspose.PDF, il est possible d'obtenir toutes les pièces jointes d'un document PDF. Cela est utile soit lorsque vous souhaitez enregistrer les documents séparément du PDF, soit si vous avez besoin de retirer les pièces jointes d'un PDF.

Pour obtenir toutes les pièces jointes d'un fichier PDF :

1. Parcourir la collection [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) de l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). La collection [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) contient toutes les pièces jointes. Chaque élément de cette collection représente un objet [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification). Chaque itération de la boucle foreach à travers la collection [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) retourne un objet [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification).
Les extraits de code suivants montrent comment obtenir toutes les pièces jointes d'un document PDF.

L'extrait de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "GetAlltheAttachments.pdf");

// Obtenir la collection des fichiers intégrés
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;

// Obtenir le nombre de fichiers intégrés
Console.WriteLine("Nombre total de fichiers : {0}", embeddedFiles.Count);

int count = 1;

// Parcourir la collection pour obtenir toutes les pièces jointes
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    Console.WriteLine("Nom : {0}", fileSpecification.Name);
    Console.WriteLine("Description : {0}",
    fileSpecification.Description);
    Console.WriteLine("Type MIME : {0}", fileSpecification.MIMEType);

    // Vérifier si l'objet paramètre contient les paramètres
    if (fileSpecification.Params != null)
    {
        Console.WriteLine("Somme de contrôle : {0}",
        fileSpecification.Params.CheckSum);
        Console.WriteLine("Date de création : {0}",
        fileSpecification.Params.CreationDate);
        Console.WriteLine("Date de modification : {0}",
        fileSpecification.Params.ModDate);
        Console.WriteLine("Taille : {0}", fileSpecification.Params.Size);
    }

    // Obtenir la pièce jointe et écrire dans un fichier ou un flux
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0,
    fileContent.Length);
    FileStream fileStream = new FileStream(dataDir + count + "_out" + ".txt",
    FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    fileStream.Close();
    count+=1;
}
```
## Obtenir une pièce jointe individuelle

Pour obtenir une pièce jointe individuelle, nous pouvons spécifier l'index de la pièce jointe dans l'objet `EmbeddedFiles` d'une instance de Document. Veuillez essayer d'utiliser le morceau de code suivant.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "GetIndividualAttachment.pdf");

// Obtenir un fichier embarqué particulier
FileSpecification fileSpecification = pdfDocument.EmbeddedFiles[1];

// Obtenir les propriétés du fichier
Console.WriteLine("Nom : {0}", fileSpecification.Name);
Console.WriteLine("Description : {0}", fileSpecification.Description);
Console.WriteLine("Type MIME : {0}", fileSpecification.MIMEType);

// Vérifier si l'objet paramètre contient les paramètres
if (fileSpecification.Params != null)
{
    Console.WriteLine("Somme de contrôle : {0}",
    fileSpecification.Params.CheckSum);
    Console.WriteLine("Date de création : {0}",
    fileSpecification.Params.CreationDate);
    Console.WriteLine("Date de modification : {0}",
    fileSpecification.Params.ModDate);
    Console.WriteLine("Taille : {0}", fileSpecification.Params.Size);
}

// Obtenir la pièce jointe et écrire dans un fichier ou un flux
byte[] fileContent = new byte[fileSpecification.Contents.Length];
fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);

FileStream fileStream = new FileStream(dataDir + "test_out" + ".txt", FileMode.Create);
fileStream.Write(fileContent, 0, fileContent.Length);
fileStream.Close();
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
    "applicationCategory": "Bibliothèque de manipulation PDF pour .NET",
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

