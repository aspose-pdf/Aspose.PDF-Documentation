---
title: .NETでPDFをHTMLに変換
linktitle: PDFをHTML形式に変換
type: docs
weight: 50
url: /ja/net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: このトピックでは、Aspose.PDF C# ライブラリを使用してPDFファイルをHTML形式に変換する方法を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 概要

この記事では、**C#を使用してPDFをHTMLに変換する方法**について説明します。以下のトピックをカバーしています。

_フォーマット_: **HTML**
- [C# PDFをHTMLに変換](#csharp-pdf-to-html)
- [C# PDFからHTMLに変換](#csharp-pdf-to-html)
- [C# PDFファイルをHTMLに変換する方法](#csharp-pdf-to-html)

次のコードスニペットも [Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリで動作します。

## PDFをHTMLに変換

**Aspose.PDF for .NET** は、さまざまなファイル形式をPDFドキュメントに変換し、PDFファイルをさまざまな出力形式に変換するための多くの機能を提供します。
**Aspose.PDF for .NET** は、さまざまなファイル形式をPDFドキュメントに変換し、PDFファイルをさまざまな出力形式に変換するための多くの機能を提供します。

**Aspose.PDF for .NET** は、PDFファイルをHTMLに変換する機能をサポートしています。Aspose.PDFライブラリで実行できる主なタスクは次のとおりです:

- PDFをHTMLに変換;
- 出力を複数ページのHTMLに分割;
- SVGファイルの保存先フォルダを指定;
- 変換中のSVGイメージの圧縮;
- 画像フォルダを指定;
- 本文のみを含む後続ファイルを作成;
- 透明なテキストレンダリング;
- PDFドキュメントレイヤーのレンダリング。

{{% alert color="success" %}}
**PDFをHTMLにオンラインで変換してみる**

Aspose.PDF for .NETは、無料のアプリケーション["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)をオンラインで提供しています。ここで機能性と品質を試すことができます。

[![Aspose.PDF Convertion PDF to HTML with Free App](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Aspose.PDF for .NETは、ソースPDFファイルをHTMLに変換するための2行のコードを提供します。
Aspose.PDF for .NETは、ソースPDFファイルをHTMLに変換するための2行のコードを提供します。

<a name="csharp-pdf-to-html"><strong>手順: C#でPDFをHTMLに変換する</strong></a>

1. ソースPDFドキュメントを使用して[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/)オブジェクトのインスタンスを作成します。
2. **Document.Save()** メソッドを呼び出して **SaveFormat.Html** フォーマットで保存します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// ソースPDFドキュメントを開く
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// ファイルをMSドキュメント形式で保存
pdfDocument.Save(dataDir + "output_out.html", SaveFormat.Html);
```

### 複数ページのHTMLへの出力分割

複数ページの大きなPDFファイルをHTML形式に変換すると、出力は単一のHTMLページとして表示されます。
複数ページの大きなPDFファイルをHTML形式に変換すると、出力が単一のHTMLページとして表示されます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// ソースPDFドキュメントを開く
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// HTML SaveOptions オブジェクトをインスタンス化
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// 出力を複数のページに分割するよう指定
htmlOptions.SplitIntoPages = true;

// ドキュメントを保存
pdfDocument.Save(@"MultiPageHTML_out.html", htmlOptions);
```

### SVGファイルを保存するフォルダを指定する

PDFからHTMLへの変換中に、SVG画像を保存するフォルダを指定することができます。
PDFからHTMLへの変換中に、SVG画像を保存するフォルダを指定することが可能です。

```csharp
// PDFファイルをロード
Document doc = new Document(dataDir + "PDFToHTML.pdf");

// HTML保存オプションオブジェクトをインスタンス化
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// PDFからHTMLへの変換時にSVG画像を保存するフォルダを指定
newOptions.SpecialFolderForSvgImages = dataDir;

// 出力ファイルを保存
doc.Save(dataDir + "SaveSVGFiles_out.html", newOptions);
```

### 変換中のSVG画像の圧縮

PDFからHTMLへの変換中にSVG画像を圧縮する場合は、以下のコードを使用してみてください：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// テストされた機能を持つHtmlSaveOptionを作成
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// SVG画像があれば圧縮
newOptions.CompressSvgGraphicsIfAny = true;
```

### 画像フォルダの指定

PDFからHTMLへの変換中に、画像を保存するフォルダも指定できます：
PDFからHTMLへの変換中に画像が保存されるフォルダを指定することもできます：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// テストされた機能を持つHtmlSaveOptionを作成
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// 画像を保存する別のフォルダを指定
newOptions.SpecialFolderForAllImages = dataDir;
```

### 本文のみの後続ファイルを作成する

最近、PDFファイルをHTMLに変換し、ユーザーが各ページの`<body>`タグの内容のみを取得できる機能を導入するよう依頼されました。これにより、CSS、`<html>`、`<head>`の詳細を含む1つのファイルと、他のファイルが`<body>`の内容のみで生成されます。

この要件を満たすために、HtmlSaveOptionsクラスにHtmlMarkupGenerationModeという新しいプロパティが導入されました。

次のシンプルなコードスニペットを使用すると、出力HTMLをページに分割できます。
以下のシンプルなコードスニペットを使用して、出力HTMLをページに分割できます。

```csharp
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");

HtmlSaveOptions options = new HtmlSaveOptions();
// これはテストされた設定です。
options.HtmlMarkupGenerationMode = HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent;
options.SplitIntoPages = true;

doc.Save(dataDir + "CreateSubsequentFiles_out.html", options);
```

### 透明テキストのレンダリング

ソース/入力 PDF ファイルに透明テキストが前景画像によって影がついている場合、テキストのレンダリングに問題が発生する可能性があります。そのようなシナリオに対応するために、SaveShadowedTextsAsTransparentTexts と SaveTransparentTexts プロパティが使用できます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.SaveShadowedTextsAsTransparentTexts = true;
htmlOptions.SaveTransparentTexts = true;
doc.Save(dataDir + "TransparentTextRendering_out.html", htmlOptions);
```
### PDF文書のレイヤー描画

PDFをHTML変換中に、別のレイヤータイプの要素でPDF文書のレイヤーを描画できます：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
// HTML SaveOptions オブジェクトのインスタンスを作成します
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// 出力HTMLでPDF文書のレイヤーを個別に描画するように指定します
htmlOptions.ConvertMarkedContentToLayers = true;

// 文書を保存します
doc.Save(dataDir + "LayersRendering_out.html", htmlOptions);
```

## 参照

この記事では、以下のトピックもカバーしています。コードは上記と同じです。

_フォーマット_: **HTML**
- [C# PDFをHTMLにコード](#csharp-pdf-to-html)
- [C# PDFをHTMLにAPI](#csharp-pdf-to-html)
- [C# PDFをプログラムでHTMLに](#csharp-pdf-to-html)
- [C# PDFをHTMLライブラリに](#csharp-pdf-to-html)
- [C# PDFをHTMLとして保存](#csharp-pdf-to-html)
- [C# PDFをHTMLとして保存](#csharp-pdf-to-html)
- [C# PDFからHTMLを生成](#csharp-pdf-to-html)
- [C# PDFからHTMLを作成](#csharp-pdf-to-html)
- [C# PDFからHTMLへのコンバータ](#csharp-pdf-to-html)
