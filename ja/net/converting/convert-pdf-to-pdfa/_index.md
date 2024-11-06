---
title: PDFをPDF/A形式に変換する
linktitle: PDFをPDF/A形式に変換する
type: docs
weight: 100
url: ja/net/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: このトピックでは、Aspose.PDFを使用してPDFファイルをPDF/A準拠のPDFファイルに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for .NET** は、PDFファイルを<abbr title="Portable Document Format / A">PDF/A</abbr>準拠のPDFファイルに変換することができます。その前に、ファイルを検証する必要があります。このトピックではその方法を説明します。

{{% alert color="primary" %}}

PDF/Aの適合性を検証するために、Adobe Preflightを使用していることに注意してください。市場に出ているすべてのツールは、PDF/Aの適合性について独自の「表現」を持っています。PDF/A検証ツールに関するこの記事を参照してください。Aspose.PDFがPDFファイルをどのように生成するかを検証するために、Adobe製品を選択しました。AdobeはPDFに関連するすべての中心にあります。

{{% /alert %}}

Document クラスの Convert メソッドを使用してファイルを変換します。
{{% alert color="success" %}}
**PDFをPDF/Aオンラインに変換してみる**

Aspose.PDF for .NETは無料のオンラインアプリケーション["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)を提供しています。ここで機能性や品質を調査することができます。

[![Aspose.PDF 変換 PDF to PDF/A 無料アプリ](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

次のコードスニペットも [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリで動作します。

## PDFファイルをPDF/A-1bに変換する

以下のコードスニペットは、PDFファイルをPDF/A-1b準拠のPDFに変換する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "PDFToPDFA.pdf");
           
// PDF/A準拠ドキュメントに変換
// 変換プロセス中に検証も実行されます
pdfDocument.Convert(dataDir + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA_out.pdf";
// 出力ドキュメントを保存
pdfDocument.Save(dataDir);
```
検証のみを行う場合は、以下のコード行を使用してください：

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// 文書ディレクトリへのパス
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// PDFをPDF/A-1aで検証
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```

## PDFファイルをPDF/A-3bに変換

Aspose.PDF for .NETは、PDFファイルをPDF/A-3b形式に変換する機能もサポートしています。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// 文書ディレクトリへのパス
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "input.pdf");           

pdfDocument.Convert(new MemoryStream(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA3b_out.pdf";
// 出力ドキュメントを保存
pdfDocument.Save(dataDir);
```
## PDFファイルをPDF/A-2uに変換

Aspose.PDF for .NETは、PDFファイルをPDF/A-2u形式に変換する機能もサポートしています。

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_2U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## PDFファイルをPDF/A-3uに変換

Aspose.PDF for .NETは、PDFファイルをPDF/A-3u形式に変換する機能もサポートしています。

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## PDF/Aファイルに添付ファイルを追加

PDF/A準拠形式にファイルを添付する必要がある場合、Aspose.PDF.PdfFormat列挙型からPDF_A_3A値の使用を推奨します。
PDF/A_3aは、PDF/A準拠ファイルに任意のファイル形式を添付として追加する機能を提供する形式です。

```csharp
```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// 既存のファイルをロードするためにDocumentインスタンスをインスタンス化します
Aspose.Pdf.Document doc = new Document(dataDir + "input.pdf");
// 添付ファイルとして追加する新しいファイルを設定します
FileSpecification fileSpecification = new FileSpecification(dataDir + "aspose-logo.jpg", "大きなイメージファイル");
// ドキュメントの添付ファイルコレクションに添付ファイルを追加します
doc.EmbeddedFiles.Add(fileSpecification);
// PDF/A_3aへの変換を実行して、結果のファイルに添付ファイルが含まれるようにします
doc.Convert(dataDir + "log.txt", Aspose.Pdf.PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
// 結果のファイルを保存します
doc.Save(dataDir + "AddAttachmentToPDFA_out.pdf");
```

## 代替フォントで欠けているフォントを置き換える

PDFA規格に従い、PDFAドキュメントにはフォントが埋め込まれている必要があります。
PDFA基準に従って、フォントはPDFAドキュメントに埋め込む必要があります。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Aspose.Pdf.Text.Font originalFont = null;
try
{
    originalFont = FontRepository.FindFont("AgencyFB");
}
catch (Exception)
{
    // 対象のマシンにフォントがありません
    FontRepository.Substitutions.Add(new SimpleFontSubstitution("AgencyFB", "Arial"));
}
var fileNew = new FileInfo(dataDir + "newfile_out.pdf");
var pdf = new Document(dataDir + "input.pdf");
pdf.Convert(dataDir + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
pdf.Save(fileNew.FullName);
```
