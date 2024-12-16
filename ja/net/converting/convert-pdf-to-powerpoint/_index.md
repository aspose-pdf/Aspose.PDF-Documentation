---
title: .NETでPDFをPowerPointに変換する
linktitle: PDFをPowerPointに変換
type: docs
weight: 30
url: /ja/net/convert-pdf-to-powerpoint/
lastmod: "2021-11-01"
description: Aspose.PDFを使用して、.NETを使ってPDFをPPT（PowerPoint）形式に変換することができます。PDFをPPTXに変換する方法として、スライドを画像として使用する方法があります。
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 概要

この記事では、**C#を使用してPDFをPowerPointに変換する方法**について説明します。以下のトピックをカバーしています。

_形式_: **PPTX**
- [C# PDFをPPTXに](#csharp-pdf-to-pptx)
- [C#でPDFをPPTXに変換する](#csharp-pdf-to-pptx)
- [C#でPDFファイルをPPTXに変換する方法](#csharp-pdf-to-pptx)

_形式_: **PowerPoint**
- [C# PDFをPowerPointに](#csharp-pdf-to-powerpoint)
- [C#でPDFをPowerPointに変換する](#csharp-pdf-to-powerpoint)
- [C#でPDFファイルをPowerPointに変換する方法](#csharp-pdf-to-powerpoint)

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリでも動作します。

## C# PDFをPowerPointおよびPPTXに変換する
## C# PDFからPowerPointおよびPPTXへの変換

**Aspose.PDF for .NET** はPDFからPPTXへの変換進行状況を追跡できます。

Aspose.SlidesというAPIがあり、PPT/PPTXプレゼンテーションの作成および操作機能を提供しています。このAPIは、PPT/PPTXファイルをPDF形式に変換する機能も提供しています。最近、多くのお客様からPDFをPPTX形式に変換する機能のサポートを求める要望が寄せられました。Aspose.PDF for .NET 10.3.0のリリースを開始して、PDF文書をPPTX形式に変換する機能を導入しました。この変換中に、PDFファイルの個々のページがPPTXファイルの個別のスライドに変換されます。

PDFから<abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>への変換中、テキストはテキストとしてレンダリングされ、選択・更新が可能です。
PDFから<abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>への変換中、テキストは選択/更新可能なテキストとしてレンダリングされます。

## C#およびAspose.PDF .NETを使用したPDFからPowerPointへの簡単な変換

PDFをPPTXに変換するために、Aspose.PDF for .NETは以下のコードステップの使用を推奨します。

<a name="csharp-pdf-to-powerpoint"><strong>手順: C#でPDFをPowerPointに変換する</strong></a> | <a name="csharp-pdf-to-pptx"><strong>手順: C#でPDFをPPTXに変換する</strong></a>

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) クラスのインスタンスを作成します
2. [PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) クラスのインスタンスを作成します
3. **Document** オブジェクトの **Save** メソッドを使用して、PDFをPPTXとして保存します

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// PDFドキュメントをロードします
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// PptxSaveOptions インスタンスをインスタンス化します
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// 出力をPPTX形式で保存します
doc.Save(dataDir + "PDFToPPT_out.pptx", pptx_save);
```
## PDFをPPTXに変換する（スライドを画像として）

{{% alert color="success" %}}
**オンラインでPDFをPowerPointに変換してみる**

Aspose.PDF for .NETは、無料のオンラインアプリケーション["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)を提供しており、その機能性や品質を試すことができます。

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

検索可能なPDFを選択可能なテキストではなく画像としてPPTXに変換する必要がある場合、Aspose.PDFは[Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions)クラスを介してそのような機能を提供します。これを実現するには、以下のコードサンプルに示すように[PptxSaveOptios](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions)クラスの[SlidesAsImages](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/slidesasimages)プロパティを'true'に設定します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// PDFドキュメントをロード
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// PptxSaveOptionsインスタンスをインスタンス化
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// 出力をPPTX形式で保存
pptx_save.SlidesAsImages = true;
doc.Save(dataDir + "PDFToPPT_out_.pptx", pptx_save);
```
## PPTX変換の進捗詳細

Aspose.PDF for .NETは、PDFからPPTXへの変換の進捗を追跡することができます。[Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) クラスは [CustomProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/customprogresshandler) プロパティを提供しており、変換の進捗を追跡するためのカスタムメソッドを指定できます。以下のコードサンプルに示すように。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// PDFドキュメントをロード
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// PptxSaveOptionsインスタンスをインスタンス化
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();

//カスタム進捗ハンドラを指定
pptx_save.CustomProgressHandler = ShowProgressOnConsole;
// 出力をPPTX形式で保存
doc.Save(dataDir + "PDFToPPTWithProgressTracking_out_.pptx", pptx_save);
```
以下は、進行状況の変換を表示するカスタムメソッドです。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
switch (eventInfo.EventType)
{
    case ProgressEventType.TotalProgress:
        Console.WriteLine(String.Format("{0}  - 変換進行状況 : {1}% 。", DateTime.Now.TimeOfDay, eventInfo.Value.ToString()));
        break;
    case ProgressEventType.ResultPageCreated:
        Console.WriteLine(String.Format("{0}  - 結果ページの {1} 枚目の {2} レイアウトが作成されました。", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.ResultPageSaved:
        Console.WriteLine(String.Format("{0}  - 結果ページ {1} 枚目の {2} がエクスポートされました。", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.SourcePageAnalysed:
        Console.WriteLine(String.Format("{0}  - ソースページ {1} 枚目の {2} が分析されました。", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    default:
        break;
}
```
## 関連項目

この記事では、上記と同じコードを使用して以下のトピックもカバーしています。

_形式_: **PowerPoint**
- [C# PDFからPowerPointへのコード](#csharp-pdf-to-powerpoint)
- [C# PDFからPowerPointへのAPI](#csharp-pdf-to-powerpoint)
- [C# PDFからPowerPointへのプログラムによる変換](#csharp-pdf-to-powerpoint)
- [C# PDFからPowerPointへのライブラリ](#csharp-pdf-to-powerpoint)
- [C# PDFをPowerPointとして保存](#csharp-pdf-to-powerpoint)
- [C# PDFからPowerPointを生成](#csharp-pdf-to-powerpoint)
- [C# PDFからPowerPointを作成](#csharp-pdf-to-powerpoint)
- [C# PDFからPowerPointへのコンバーター](#csharp-pdf-to-powerpoint)

_形式_: **PPTX**
- [C# PDFからPPTXへのコード](#csharp-pdf-to-pptx)
- [C# PDFからPPTXへのAPI](#csharp-pdf-to-pptx)
- [C# PDFからPPTXへのプログラムによる変換](#csharp-pdf-to-pptx)
- [C# PDFからPPTXへのライブラリ](#csharp-pdf-to-pptx)
- [C# PDFをPPTXとして保存](#csharp-pdf-to-pptx)
- [C# PDFからPPTXを生成](#csharp-pdf-to-pptx)
- [C# PDFからPPTXを作成](#csharp-pdf-to-pptx)
- [C# PDFからPPTXへのコンバーター](#csharp-pdf-to-pptx)


