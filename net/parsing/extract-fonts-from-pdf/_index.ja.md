---
title: PDFからフォントを抽出する C#
linktitle: PDFからフォントを抽出する
type: docs
weight: 30
url: /net/extract-fonts-from-pdf/
description: Aspose.PDF for .NET ライブラリを使用して、PDF文書からすべての埋め込みフォントを抽出します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF文書からすべてのフォントを取得したい場合は、Documentクラスで提供されているFontUtilities.GetAllFonts()メソッドを使用できます。以下のコードスニペットを確認して、既存のPDF文書からすべてのフォントを取得してください：

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリとも動作します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// 文書ディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

