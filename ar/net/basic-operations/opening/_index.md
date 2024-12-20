---
title: فتح مستند PDF برمجيًا
linktitle: فتح PDF
type: docs
weight: 20
url: /ar/net/open-pdf-document/
description: تعلم كيفية فتح ملف PDF في C# باستخدام مكتبة Aspose.PDF لـ .NET. يمكنك فتح PDF موجود، مستند من تيار، ومستند PDF المشفر.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## فتح مستند PDF موجود

هناك عدة طرق لفتح مستند. الأسهل هو تحديد اسم ملف.

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

## فتح مستند PDF موجود من تيار

```csharp
public static void OpenDocumentStream()
{
    const string fileName = "SJPR0033_Folder_Utland_16sid_ENG_web3.pdf";
    var remoteUri = "https://www.sj.se/content/dam/SJ/pdf/Engelska/";
    // إنشاء نموذج WebClient جديد.
    var webClient = new WebClient();
    // توصيل النطاق بملف الموارد الويب.
    var strWebResource = remoteUri + fileName;
    Console.WriteLine("Downloading File \"{0}\" from \"{1}\" .......\n\n", fileName, strWebResource);

    var stream = new MemoryStream();
    webClient.OpenRead(strWebResource)?.CopyTo(stream);

    using (var pdfDocument = new Aspose.Pdf.Document(stream))
    {
        Console.WriteLine($"Pages {pdfDocument.Pages.Count}");
    }
}
```
## فتح مستند PDF مشفر

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
