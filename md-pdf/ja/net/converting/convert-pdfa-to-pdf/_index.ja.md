---
title: PDF/AをPDF形式に変換
linktitle: PDF/AをPDF形式に変換
type: docs
weight: 110
url: /net/convert-pdfa-to-pdf/
lastmod: "2021-11-01"
description: このトピックでは、Aspose.PDFを使用してPDF/Aファイルを.NETライブラリを用いてPDFドキュメントに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

次のコードスニペットは[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

## PDF/AドキュメントをPDFに変換

PDF/AドキュメントをPDFに変換するとは、元のドキュメントから<abbr title="Portable Document Format Archive">PDF/A</abbr>の制限を取り除くことを意味します。
クラス[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)には、入力/ソースファイルからPDF準拠情報を削除する[RemovePdfaCompliance(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/removepdfacompliance)メソッドがあります。

```csharp
public static void ConvertPDFAtoPDF()
{
    // 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // PDF/A準拠情報を削除
    pdfDocument.RemovePdfaCompliance();
    // 更新されたドキュメントを保存
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
この情報は、文書に変更を加えると削除されます（例：ページを追加する場合）。次の例では、ページを追加した後、出力文書がPDF/A準拠を失います。

```csharp
public static void ConvertPDFAtoPDFAdvanced()
{
    // 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // 新しい（空の）ページを追加すると、PDF/A準拠情報が削除されます。
    pdfDocument.Pages.Add();
    // 更新されたドキュメントを保存
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
