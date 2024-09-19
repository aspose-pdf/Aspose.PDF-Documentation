---
title: Abrir documento PDF programáticamente
linktitle: Abrir PDF
type: docs
weight: 20
url: /net/open-pdf-document/
description: Aprenda cómo abrir un archivo PDF en C# Aspose.PDF para la biblioteca PDF de .NET. Puede abrir PDF existente, documento desde un flujo y documento PDF cifrado.
aliases:
    - /net/opening-a-pdf-document/
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Abrir documento PDF existente

Hay varias maneras de abrir un documento. La más fácil es especificar un nombre de archivo.

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

## Abrir documento PDF existente desde un flujo

```csharp
public static void OpenDocumentStream()
{
    const string fileName = "SJPR0033_Folder_Utland_16sid_ENG_web3.pdf";
    var remoteUri = "https://www.sj.se/content/dam/SJ/pdf/Engelska/";
    // Crear una nueva instancia de WebClient.
    var webClient = new WebClient();
    // Concatenar el dominio con el nombre del recurso web.
    var strWebResource = remoteUri + fileName;
    Console.WriteLine("Descargando el archivo \"{0}\" desde \"{1}\" .......\n\n", fileName, strWebResource);

    var stream = new MemoryStream();
    webClient.OpenRead(strWebResource)?.CopyTo(stream);

    using (var pdfDocument = new Aspose.Pdf.Document(stream))
    {
        Console.WriteLine($"Pages {pdfDocument.Pages.Count}");
    }
}
```
## Abrir documento PDF cifrado

```csharp
    public static void OpenDocumentWithPassword()
    {
        const string fileName = @"C:\tmp\DocSite.pdf";
        const string password = "Aspose2020";
        try
        {
            using (var pdfDocument = new Aspose.Pdf.Document(fileName, password))
            {
                Console.WriteLine($"Páginas {pdfDocument.Pages.Count}");
            }
        }
        catch (InvalidPasswordException e)
        {
            Console.WriteLine(e);
        }
    }
```
