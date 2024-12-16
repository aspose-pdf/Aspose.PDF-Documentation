---
title: プログラムによるPDFドキュメントの開始
linktitle: PDFを開く
type: docs
weight: 20
url: /ja/net/open-pdf-document/
description: C# Aspose.PDF for .NET PDFライブラリを使用してPDFファイルを開く方法を学びます。既存のPDF、ストリームからのドキュメント、暗号化されたPDFドキュメントを開くことができます。
aliases:
    - /net/opening-a-pdf-document/
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

次のコードスニペットは [Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリでも動作します。

## 既存のPDFドキュメントを開く

ドキュメントを開く方法はいくつかあります。最も簡単な方法はファイル名を指定することです。

```csharp
public static void OpenDocument()
{
    var fileName = @"C:\tmp\tourguidev2_gb_tags.pdf";
    using (var pdfDocument = new Aspose.Pdf.Document(fileName))
    {
        Console.WriteLine($"ページ数 {pdfDocument.Pages.Count}");
    }
}
```

## ストリームから既存のPDFドキュメントを開く

```csharp
public static void OpenDocumentStream()
{
    const string fileName = "SJPR0033_Folder_Utland_16sid_ENG_web3.pdf";
    var remoteUri = "https://www.sj.se/content/dam/SJ/pdf/Engelska/";
    // 新しいWebClientインスタンスを作成します。
    var webClient = new WebClient();
    // ドメインとWebリソースのファイル名を連結します。
    var strWebResource = remoteUri + fileName;
    Console.WriteLine("ファイル \"{0}\" を \"{1}\" からダウンロードしています.......\n\n", fileName, strWebResource);

    var stream = new MemoryStream();
    webClient.OpenRead(strWebResource)?.CopyTo(stream);

    using (var pdfDocument = new Aspose.Pdf.Document(stream))
    {
        Console.WriteLine($"ページ数 {pdfDocument.Pages.Count}");
    }
}
```
## 暗号化されたPDFドキュメントを開く

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
