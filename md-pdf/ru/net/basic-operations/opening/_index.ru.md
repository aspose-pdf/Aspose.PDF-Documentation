---
title: Программное открытие PDF документа
linktitle: Открыть PDF
type: docs
weight: 20
url: /net/open-pdf-document/
description: Узнайте, как открыть PDF файл в C# с использованием библиотеки Aspose.PDF для .NET. Вы можете открыть существующий PDF, документ из потока и зашифрованный PDF документ.
aliases:
    - /net/opening-a-pdf-document/
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Открыть существующий PDF документ

Существует несколько способов открытия документа. Самый простой - указать имя файла.

```csharp
public static void OpenDocument()
{
    var fileName = @"C:\tmp\tourguidev2_gb_tags.pdf";
    using (var pdfDocument = new Aspose.Pdf.Document(fileName))
    {
        Console.WriteLine($"Страницы {pdfDocument.Pages.Count}");
    }
}
```

## Открыть существующий PDF документ из потока

```csharp
public static void OpenDocumentStream()
{
    const string fileName = "SJPR0033_Folder_Utland_16sid_ENG_web3.pdf";
    var remoteUri = "https://www.sj.se/content/dam/SJ/pdf/Engelska/";
    // Создать новый экземпляр WebClient.
    var webClient = new WebClient();
    // Соединить домен с именем веб-ресурса.
    var strWebResource = remoteUri + fileName;
    Console.WriteLine("Загрузка файла \"{0}\" из \"{1}\" .......\n\n", fileName, strWebResource);

    var stream = new MemoryStream();
    webClient.OpenRead(strWebResource)?.CopyTo(stream);

    using (var pdfDocument = new Aspose.Pdf.Document(stream))
    {
        Console.WriteLine($"Страницы {pdfDocument.Pages.Count}");
    }
}
```
## Открыть зашифрованный PDF документ

```csharp
    public static void OpenDocumentWithPassword()
    {
        const string fileName = @"C:\tmp\DocSite.pdf";
        const string password = "Aspose2020";
        try
        {
            using (var pdfDocument = new Aspose.Pdf.Document(fileName, password))
            {
                Console.WriteLine($"Страницы {pdfDocument.Pages.Count}");
            }
        }
        catch (InvalidPasswordException e)
        {
            Console.WriteLine(e);
        }
    }
```
