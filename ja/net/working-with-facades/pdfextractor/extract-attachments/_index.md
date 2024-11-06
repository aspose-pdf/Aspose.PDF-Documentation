```
---
title: PDFファイルから添付ファイルを抽出する
type: docs
weight: 10
url: ja/net/extract-attachments/
description: このセクションでは、PdfExtractorクラスを使用してPDFから添付ファイルを抽出する方法について説明します。
lastmod: "2021-06-05"
---

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)の抽出機能の主なカテゴリの1つは、添付ファイルの抽出です。
``` このカテゴリは、一連のメソッドを提供しており、添付ファイルを抽出するのを助けるだけでなく、添付ファイルに関連する情報を提供するメソッドも提供します。つまり、[GetAttachmentInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) および [GetAttachName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) メソッドは、それぞれ添付ファイルの情報と添付ファイル名を提供します。添付ファイルを抽出して取得するために、私たちは [ExtractAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) および [GetAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachment) メソッドを使用します。

次のコードスニペットは、PdfExtractor メソッドの使用方法を示しています:

```csharp
public static void ExtractAttachments()
{
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample-attach.pdf");

    // 添付ファイルを抽出
    pdfExtractor.ExtractAttachment();

    // 添付ファイル名を取得
    if (pdfExtractor.GetAttachNames().Count > 0)
    {
         Console.WriteLine("抽出して保存中...");
         // 抽出された添付ファイルを取得
         pdfExtractor.GetAttachment(_dataDir);
    }
}
```