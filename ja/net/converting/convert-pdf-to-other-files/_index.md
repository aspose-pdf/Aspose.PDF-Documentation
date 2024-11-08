---
title: PDFをEPUB、LaTeX、テキスト、XPSに変換するC#
linktitle: PDFを他のフォーマットに変換
type: docs
weight: 90
url: /ja/net/convert-pdf-to-other-files/
lastmod: "2021-11-01"
keywords: 変換, PDF, EPUB, LaTeX, テキスト, XPS, C#
description: このトピックでは、C#または.NETを使用してPDFファイルをEPUB、LaTeX、テキスト、XPSなどの他のファイル形式に変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDFをEPUBに変換

{{% alert color="success" %}}
**オンラインでPDFをEPUBに変換してみる**

Aspose.PDF for .NETは、無料のアプリケーション["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)を提供しています。ここで機能と品質を試すことができます。

[![Aspose.PDF で無料アプリでのPDFからEPUBへの変換](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>**は、国際デジタル出版フォーラム（IDPF）からの無料かつオープンな電子書籍標準です。
**<abbr title="Electronic Publication">EPUB</abbr>** は、国際デジタル出版フォーラム（IDPF）から提供されている無料でオープンな電子ブック標準です。
EPUBはリフロー可能なコンテンツ用に設計されており、EPUBリーダーは特定のディスプレイデバイス用にテキストを最適化することができます。EPUBは固定レイアウトコンテンツもサポートしています。このフォーマットは、出版社および変換ハウスが社内で使用するため、または配布および販売用に単一のフォーマットとして意図されています。これはOpen eBook標準を置き換えるものです。

次のコードスニペットも [Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリで動作します。

Aspose.PDF for .NET はPDFドキュメントをEPUBフォーマットに変換する機能もサポートしています。Aspose.PDF for .NETには、EpubSaveOptionsというクラスがあり、これを[`Document.Save(..)`](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index)メソッドの第二引数として使用することで、EPUBファイルを生成できます。
以下のC#コードスニペットを使用して、この要件を達成してください。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET へアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// PDFドキュメントをロード
Document pdfDocument = new Document(dataDir + "PDFToEPUB.pdf");
// Epub保存オプションのインスタンスを作成
EpubSaveOptions options = new EpubSaveOptions();
// 内容のレイアウトを指定
options.ContentRecognitionMode = EpubSaveOptions.RecognitionMode.Flow;
// ePUBドキュメントを保存
pdfDocument.Save(dataDir + "PDFToEPUB_out.epub", options);
```
## PDFをLaTeX/TeXに変換

**Aspose.PDF for .NET** はPDFをLaTeX/TeXに変換する機能をサポートしています。
LaTeXファイル形式は、特別なマークアップを含むテキストファイル形式であり、高品質な組版のためのTeXベースのドキュメント準備システムで使用されます。

{{% alert color="success" %}}
**オンラインでPDFをLaTeX/TeXに変換してみる**

Aspose.PDF for .NETでは、無料のオンラインアプリケーション["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)を提供しており、機能と品質を調査することができます。

[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

PDFファイルをTeXに変換するために、Aspose.PDFは[LaTeXSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexsaveoptions)クラスを提供しており、変換プロセス中に一時画像を保存するためのプロパティOutDirectoryPathを提供しています。

次のコードスニペットは、C#を使用してPDFファイルをTEX形式に変換するプロセスを示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Documentオブジェクトを作成
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "PDFToTeX.pdf");

// LaTex保存オプションをインスタンス化          
LaTeXSaveOptions saveOptions = new LaTeXSaveOptions();

// 出力ディレクトリを指定
string pathToOutputDirectory = dataDir;

// 保存オプションオブジェクトに出力ディレクトリパスを設定
saveOptions.OutDirectoryPath = pathToOutputDirectory;

// PDFファイルをLaTex形式に保存           
doc.Save(dataDir + "PDFToTeX_out.tex", saveOptions);
```
## PDFをテキストに変換

**Aspose.PDF for .NET** は、PDF文書全体と単一ページをテキストファイルに変換することをサポートします。

### PDF文書全体をテキストファイルに変換

[TextAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber) クラスの [Visit](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber/methods/visit/index) メソッドを使用して、PDF文書をTXTファイルに変換することができます。

次のコードスニペットは、すべてのページからテキストを抽出する方法を説明しています。

```csharp
public static void ConvertPDFDocToTXT()
{
    // 文書を開く
    Document pdfDocument = new Document(_dataDir + "demo.pdf");
    TextAbsorber ta = new TextAbsorber();
    ta.Visit(pdfDocument);
    // 抽出したテキストをテキストファイルに保存する
    File.WriteAllText(_dataDir + "input_Text_Extracted_out.txt",ta.Text);
}
```

{{% alert color="success" %}}
**オンラインでPDFをテキストに変換してみる**

Aspose.PDF for .NETは、無料のオンラインアプリケーション["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)を提供しています。ここで機能と品質を試すことができます。
Aspose.PDF for .NETは、無料のオンラインアプリケーション ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt) を提供しており、その機能と品質を試すことができます。
{{% /alert %}}

[![Aspose.PDF 変換 PDF to Text 無料アプリ](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)

### PDFページをテキストファイルに変換

Aspose.PDF for .NETを使用して、PDFドキュメントをTXTファイルに変換できます。このタスクを解決するには、`TextAbsorber` クラスの `Visit` メソッドを使用する必要があります。

以下のコードスニペットは、特定のページからテキストを抽出する方法を説明しています。

```csharp
public static void ConvertPDFPagestoTXT()
{
    Document pdfDocument = new Document(System.IO.Path.Combine(_dataDir, "demo.pdf"));
    TextAbsorber ta = new TextAbsorber();
    var pages = new [] {1, 3, 4};
    foreach (var page in pages)
    {
        ta.Visit(pdfDocument.Pages[page]);
    }
   
    // 抽出されたテキストをテキストファイルに保存
    File.WriteAllText(System.IO.Path.Combine(_dataDir, "input_Text_Extracted_out.txt"), ta.Text);
}
```
## PDFをXPSに変換する

**Aspose.PDF for .NET** はPDFファイルを<abbr title="XML Paper Specification">XPS</abbr>形式に変換する機能を提供します。以下のコードスニペットを使用して、C#でPDFファイルをXPS形式に変換してみましょう。

{{% alert color="success" %}}
**オンラインでPDFをXPSに変換してみる**

Aspose.PDF for .NETは、無料のオンラインアプリケーション["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)を提供しています。ここで機能の動作と品質を試すことができます。

[![Aspose.PDF Convertion PDF to XPS with Free App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPSファイルタイプは、主にMicrosoft CorporationによるXML Paper Specificationと関連しています。XML Paper Specification (XPS)は、以前にMetroとコードネームされ、Next Generation Print Path (NGPP)のマーケティングコンセプトを取り込んだもので、MicrosoftがWindowsオペレーティングシステムに文書の作成と表示を統合しようとしている取り組みです。

PDFファイルをXPSに変換するために、Aspose.PDFには[XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions)クラスがあり、[Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index)メソッドの第二引数として使用され、XPSファイルを生成します。
PDFファイルをXPSに変換するために、Aspose.PDFは[XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions)クラスを使用し、[Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index)メソッドの第二引数としてXPSファイルを生成します。

以下のコードスニペットは、PDFファイルをXPS形式に変換するプロセスを示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// PDFドキュメントをロード
Document pdfDocument = new Document(dataDir + "input.pdf");

// XPS保存オプションをインスタンス化
Aspose.Pdf.XpsSaveOptions saveOptions = new Aspose.Pdf.XpsSaveOptions();
// XPSドキュメントを保存
pdfDocument.Save("PDFToXPS_out.xps", saveOptions)
```
