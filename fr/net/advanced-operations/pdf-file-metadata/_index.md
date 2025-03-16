---
title: Travailler avec les métadonnées de fichiers PDF en C#
linktitle: Métadonnées de fichiers PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 200
url: /fr/net/pdf-file-metadata/
description: Explorez comment extraire et gérer les métadonnées PDF, telles que l'auteur et le titre, en .NET en utilisant Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with PDF File Metadata in C#",
    "alternativeHeadline": "Extracting and Managing PDF Metadata in C#",
    "abstract": "Débloquez le pouvoir de la gestion des fichiers PDF avec notre nouvelle fonctionnalité pour les développeurs C#, permettant un accès fluide aux métadonnées des fichiers PDF. Obtenez des informations sur les propriétés des fichiers, extrayez les métadonnées XMP et mettez facilement à jour les informations du document, rationalisant ainsi votre processus de gestion des documents. Découvrez une fonctionnalité améliorée pour maintenir et manipuler efficacement les métadonnées PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF file metadata, C# PDF manipulation, get PDF file information, set PDF file information, XMP metadata, Aspose.PDF for .NET, document properties, PDF metadata management",
    "wordcount": "834",
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
    "url": "/net/pdf-file-metadata/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-file-metadata/"
    },
    "dateModified": "2024-11-25",
    "description": "Cette section explique comment obtenir des informations sur les fichiers PDF, comment obtenir des métadonnées XMP d'un fichier PDF, définir des informations sur les fichiers PDF."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Obtenir des informations sur le fichier PDF

Pour obtenir des informations spécifiques à un fichier PDF, vous devez d'abord obtenir l'objet [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) en utilisant la propriété [Info](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/info) de l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Une fois l'objet [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) récupéré, vous pouvez obtenir les valeurs des propriétés individuelles. Le code suivant vous montre comment obtenir des informations sur le fichier PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPDFFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetFileInfo.pdf"))
    {
        // Get document information
        var docInfo = document.Info;

        // Display document information
        Console.WriteLine("Author: {0}", docInfo.Author);
        Console.WriteLine("Creation Date: {0}", docInfo.CreationDate);
        Console.WriteLine("Keywords: {0}", docInfo.Keywords);
        Console.WriteLine("Modify Date: {0}", docInfo.ModDate);
        Console.WriteLine("Subject: {0}", docInfo.Subject);
        Console.WriteLine("Title: {0}", docInfo.Title);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPDFFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetFileInfo.pdf"))
    {
        // Get document information
        var docInfo = document.Info;
        // Display document information
        Console.WriteLine("Author: {0}", docInfo.Author);
        Console.WriteLine("Creation Date: {0}", docInfo.CreationDate);
        Console.WriteLine("Keywords: {0}", docInfo.Keywords);
        Console.WriteLine("Modify Date: {0}", docInfo.ModDate);
        Console.WriteLine("Subject: {0}", docInfo.Subject);
        Console.WriteLine("Title: {0}", docInfo.Title);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Définir des informations sur le fichier PDF

Aspose.PDF for .NET vous permet de définir des informations spécifiques à un fichier pour un PDF, des informations telles que l'auteur, la date de création, le sujet et le titre. Pour définir ces informations :

1. Créez un objet [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo).
1. Définissez les valeurs des propriétés.
1. Enregistrez le document mis à jour en utilisant la méthode Save de la classe Document.

Le code suivant vous montre comment définir des informations sur le fichier PDF.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFileInfo.pdf"))
    {
        // Specify document information
        var docInfo = new Aspose.Pdf.DocumentInfo(document);

        docInfo.Author = "Aspose";
        docInfo.CreationDate = DateTime.Now;
        docInfo.Keywords = "Aspose.Pdf, DOM, API";
        docInfo.ModDate = DateTime.Now;
        docInfo.Subject = "PDF Information";
        docInfo.Title = "Setting PDF Document Information";

        // Save PDF document
        document.Save(dataDir + "SetFileInfo_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFileInfo.pdf"))
    {
        // Specify document information
        var docInfo = new Aspose.Pdf.DocumentInfo(document);

        docInfo.Author = "Aspose";
        docInfo.CreationDate = DateTime.Now;
        docInfo.Keywords = "Aspose.Pdf, DOM, API";
        docInfo.ModDate = DateTime.Now;
        docInfo.Subject = "PDF Information";
        docInfo.Title = "Setting PDF Document Information";

        // Save PDF document
        document.Save(dataDir + "SetFileInfo_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Obtenir des métadonnées XMP d'un fichier PDF

Aspose.PDF vous permet d'accéder aux métadonnées XMP d'un fichier PDF. Pour obtenir les métadonnées d'un fichier PDF :

1. Créez un objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) et ouvrez le fichier PDF d'entrée.
1. Obtenez les métadonnées du fichier en utilisant la propriété [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata).

Le code suivant vous montre comment obtenir des métadonnées du fichier PDF.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXMPMetadata.pdf"))
    {
        // Get and display properties
        Console.WriteLine($"Create Date: {document.Metadata["xmp:CreateDate"]}");
        Console.WriteLine($"Nickname: {document.Metadata["xmp:Nickname"]}");
        Console.WriteLine($"Custom Property: {document.Metadata["xmp:CustomProperty"]}");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXMPMetadata.pdf"))
    {
        // Get and display properties
        Console.WriteLine($"Create Date: {document.Metadata["xmp:CreateDate"]}");
        Console.WriteLine($"Nickname: {document.Metadata["xmp:Nickname"]}");
        Console.WriteLine($"Custom Property: {document.Metadata["xmp:CustomProperty"]}");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Définir des métadonnées XMP dans un fichier PDF

Aspose.PDF vous permet de définir des métadonnées dans un fichier PDF. Pour définir des métadonnées :

1. Créez un objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Définissez les valeurs des métadonnées en utilisant la propriété [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata).
1. Enregistrez le document mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) de l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Le code suivant vous montre comment définir des métadonnées dans un fichier PDF.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Set properties
        document.Metadata["xmp:CreateDate"] = DateTime.Now.ToString("o");
        document.Metadata["xmp:Nickname"] = "Nickname";
        document.Metadata["xmp:CustomProperty"] = "Custom Value";

        // Save PDF document
        document.Save(dataDir + "SetXMPMetadata_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Set properties
        document.Metadata["xmp:CreateDate"] = DateTime.Now.ToString("o");
        document.Metadata["xmp:Nickname"] = "Nickname";
        document.Metadata["xmp:CustomProperty"] = "Custom Value";

        // Save PDF document
        document.Save(dataDir + "SetXMPMetadata_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Insérer des métadonnées avec préfixe

Certains développeurs ont besoin de créer un nouvel espace de noms de métadonnées avec un préfixe. Le code suivant montre comment insérer des métadonnées avec un préfixe.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrefixMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Register a namespace URI for the 'xmp' prefix
        document.Metadata.RegisterNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");

        // Set the metadata property using the registered prefix
        document.Metadata["xmp:ModifyDate"] = DateTime.Now.ToString("o"); // ISO 8601 format for datetime

        // Save PDF document
        document.Save(dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrefixMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Register a namespace URI for the 'xmp' prefix
        document.Metadata.RegisterNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");

        // Set the metadata property using the registered prefix
        document.Metadata["xmp:ModifyDate"] = DateTime.Now.ToString("o"); // ISO 8601 format for datetime

        // Save PDF document
        document.Save(dataDir + "SetPrefixMetadata_out.pdf");
    }
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