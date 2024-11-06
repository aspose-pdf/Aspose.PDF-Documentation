---
title: Membuka dokumen PDF secara pemrograman
linktitle: Buka PDF
type: docs
weight: 20
url: id/net/open-pdf-document/
description: Pelajari cara membuka file PDF dalam C# Aspose.PDF untuk perpustakaan PDF .NET. Anda dapat membuka PDF yang sudah ada, dokumen dari aliran, dan dokumen PDF terenkripsi.
aliases:
    - /net/opening-a-pdf-document/
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Kode berikut juga dapat digunakan dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Membuka dokumen PDF yang sudah ada

Ada beberapa cara untuk membuka dokumen. Cara termudah adalah dengan menentukan nama file.

```csharp
public static void OpenDocument()
{
    var fileName = @"C:\tmp\tourguidev2_gb_tags.pdf";
    using (var pdfDocument = new Aspose.Pdf.Document(fileName))
    {
        Console.WriteLine($"Halaman {pdfDocument.Pages.Count}");
    }
}
```

## Membuka dokumen PDF yang sudah ada dari aliran

```csharp
public static void OpenDocumentStream()
{
    const string fileName = "SJPR0033_Folder_Utland_16sid_ENG_web3.pdf";
    var remoteUri = "https://www.sj.se/content/dam/SJ/pdf/Engelska/";
    // Buat instance WebClient baru.
    var webClient = new WebClient();
    // Gabungkan domain dengan nama file sumber web.
    var strWebResource = remoteUri + fileName;
    Console.WriteLine("Mengunduh File \"{0}\" dari \"{1}\" .......\n\n", fileName, strWebResource);

    var stream = new MemoryStream();
    webClient.OpenRead(strWebResource)?.CopyTo(stream);

    using (var pdfDocument = new Aspose.Pdf.Document(stream))
    {
        Console.WriteLine($"Halaman {pdfDocument.Pages.Count}");
    }
}
```
## Membuka dokumen PDF yang terenkripsi

```csharp
    public static void OpenDocumentWithPassword()
    {
        const string fileName = @"C:\tmp\DocSite.pdf";
        const string password = "Aspose2020";
        try
        {
            using (var pdfDocument = new Aspose.Pdf.Document(fileName, password))
            {
                Console.WriteLine($"Halaman {pdfDocument.Pages.Count}");
            }
        }
        catch (InvalidPasswordException e)
        {
            Console.WriteLine(e);
        }
    }
```
