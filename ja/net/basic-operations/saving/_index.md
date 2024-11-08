---
title: PDFドキュメントをプログラムで保存
linktitle: PDFを保存
type: docs
weight: 30
url: /ja/net/save-pdf-document/
description: C# Aspose.PDF for .NET PDFライブラリを使ってPDFファイルを保存する方法を学びます。ファイルシステム、ストリーム、WebアプリケーションにPDFドキュメントを保存します。
aliases:
    - /net/saving/
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

次のコードスニペットは、新しいグラフィカルな[Aspose.Drawing](/pdf/ja/net/drawing/)インターフェースでも動作します。

## ファイルシステムにPDFドキュメントを保存

`Document`クラスの`Save`メソッドを使用して、作成または操作したPDFドキュメントをファイルシステムに保存することができます。
形式タイプ（オプション）を指定しない場合、ドキュメントはAspose.PDF v.1.7 (*.pdf)形式で保存されます。

```csharp
public static void SaveDocument()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // 何か操作を行う、例えば新しい空ページを追加
    pdfDocument.Pages.Add();
    pdfDocument.Save(modifiedFileName);
}
```
## ストリームへのPDFドキュメントの保存

作成または操作されたPDFドキュメントをストリームに保存するために、`Save`メソッドのオーバーロードを使用することもできます。

```csharp
public static void SaveDocumentStream()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // 何か操作を行う、例えば新しい空ページを追加
    pdfDocument.Pages.Add();
    pdfDocument.Save(System.IO.File.OpenWrite(modifiedFileName));
}
```

## WebアプリケーションでのPDFドキュメントの保存

Webアプリケーションでドキュメントを保存するには、上記の方法を使用できます。加えて、`Document`クラスは[HttpResponse](https://docs.microsoft.com/en-us/dotnet/api/system.web.httpresponse?view=netframework-4.8)クラスを使用するための`Save`メソッドがオーバーロードされています。

```csharp
var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
var pdfDocument = new Aspose.Pdf.Document(originalFileName);
// 何か操作を行う、例えば新しい空ページを追加
pdfDocument.Pages.Add();
pdfDocument.Save(Response, originalFileName, ContentDisposition.Attachment, new PdfSaveOptions());
```
詳細な説明については、[Showcase](/pdf/ja/net/showcases/)セクションに進んでください。

## PDF/AまたはPDF/X形式で保存

PDF/Aは、電子文書のアーカイブおよび長期保存に使用するために標準化されたポータブルドキュメントフォーマット（PDF）のISO標準版です。
PDF/Aは、フォントリンキング（フォント埋め込みとは対照的）や暗号化など、長期アーカイブに適さない機能を禁止する点でPDFと異なります。PDF/AビューアのISO要件には、カラーマネジメントガイドライン、埋め込みフォントサポート、埋め込み注釈の読み取り用ユーザーインターフェイスが含まれます。

PDF/Xは、PDF ISO標準のサブセットです。PDF/Xの目的はグラフィックス交換を容易にすることであり、そのためには標準のPDFファイルには適用されない一連の印刷関連の要件があります。

どちらの場合も、`Save` メソッドを使用してドキュメントを保存し、ドキュメントは `Convert` メソッドを使用して準備する必要があります。

```csharp
public static void SaveDocumentAsPDFx()
{
    var pdfDocument = new Aspose.Pdf.Document("..\\..\\..\\Samples\\SimpleResume.pdf");
    pdfDocument.Pages.Add();
    pdfDocument.Convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    pdfDocument.Save("..\\..\\..\\Samples\\SimpleResume_X3.pdf");
}
```

