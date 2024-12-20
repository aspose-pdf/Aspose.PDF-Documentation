---
title: Ouvrir un document PDF de manière programmable
linktitle: Ouvrir PDF
type: docs
weight: 20
url: /fr/net/open-pdf-document/
description: Apprenez comment ouvrir un fichier PDF en C# avec la bibliothèque Aspose.PDF pour .NET. Vous pouvez ouvrir un PDF existant, un document depuis un flux et un document PDF crypté.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Ouvrir un document PDF existant

Il existe plusieurs façons d'ouvrir un document. La plus simple est de spécifier un nom de fichier.

```csharp
public static void OpenDocument()
{
    var fileName = @"C:\tmp\tourguidev2_gb_tags.pdf";
    using (var pdfDocument = new Aspose.Pdf.Document(fileName))
    {
        Console.WriteLine($"Pages {pdfDocument.Pages.Count}");
    }
}
```

## Ouvrir un document PDF existant depuis un flux

```csharp
public static void OpenDocumentStream()
{
    const string fileName = "SJPR0033_Folder_Utland_16sid_ENG_web3.pdf";
    var remoteUri = "https://www.sj.se/content/dam/SJ/pdf/Engelska/";
    // Créez une nouvelle instance de WebClient.
    var webClient = new WebClient();
    // Concaténez le domaine avec le nom du fichier ressource Web.
    var strWebResource = remoteUri + fileName;
    Console.WriteLine("Téléchargement du fichier \"{0}\" depuis \"{1}\" .......\n\n", fileName, strWebResource);

    var stream = new MemoryStream();
    webClient.OpenRead(strWebResource)?.CopyTo(stream);

    using (var pdfDocument = new Aspose.Pdf.Document(stream))
    {
        Console.WriteLine($"Pages {pdfDocument.Pages.Count}");
    }
}
```
## Ouvrir un document PDF crypté

```csharp
    public static void OpenDocumentWithPassword()
    {
        const string fileName = @"C:\tmp\DocSite.pdf";
        const string password = "Aspose2020";
        try
        {
            using (var pdfDocument = new Aspose.Pdf.Document(fileName, password))
            {
                Console.WriteLine($"Pages {pdfDocument.Pages.Count}");
            }
        }
        catch (InvalidPasswordException e)
        {
            Console.WriteLine(e);
        }
    }
```
