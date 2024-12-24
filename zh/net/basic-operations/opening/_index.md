---
title: 以编程方式打开 PDF 文档
linktitle: 打开 PDF
type: docs
weight: 20
url: /zh/net/open-pdf-document/
description: 学习如何在 C# Aspose.PDF for .NET PDF 库中打开 PDF 文件。您可以打开现有的 PDF 文件、流中的文档以及加密的 PDF 文档。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## 打开现有的 PDF 文档

打开文档有几种方法。最简单的是指定文件名。

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

## 从流中打开现有的 PDF 文档

```csharp
public static void OpenDocumentStream()
{
    const string fileName = "SJPR0033_Folder_Utland_16sid_ENG_web3.pdf";
    var remoteUri = "https://www.sj.se/content/dam/SJ/pdf/Engelska/";
    // 创建一个新的 WebClient 实例。
    var webClient = new WebClient();
    // 将域与 Web 资源文件名连接起来。
    var strWebResource = remoteUri + fileName;
    Console.WriteLine("正在从 \"{1}\" 下载文件 \"{0}\" .......\n\n", fileName, strWebResource);

    var stream = new MemoryStream();
    webClient.OpenRead(strWebResource)?.CopyTo(stream);

    using (var pdfDocument = new Aspose.Pdf.Document(stream))
    {
        Console.WriteLine($"Pages {pdfDocument.Pages.Count}");
    }
}
```
## 打开加密的PDF文档

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
