---
title: .NETでPDFをMicrosoft Wordドキュメントに変換する
linktitle: PDFをWordに変換
type: docs
weight: 10
url: ja/net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: Aspose.PDF for .NETを使用してPDFからMicrosoft Word形式への変換を行うC#コードの書き方を学び、PDFからDOC（DOCX）への変換を調整します。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 概要

この記事では、**C#を使用してPDFをMicrosoft Wordドキュメントに変換する方法**について説明します。以下のトピックをカバーしています。

_フォーマット_: **DOC**

- [C# PDFからDOCへ](#csharp-pdf-to-doc)
- [C#でPDFをDOCに変換](#csharp-pdf-to-doc)
- [C# PDFファイルをDOCに変換する方法](#csharp-pdf-to-doc)

_フォーマット_: **DOCX**

- [C# PDFからDOCXへ](#csharp-pdf-to-docx)
- [C#でPDFをDOCXに変換](#csharp-pdf-to-docx)
- [C# PDFファイルをDOCXに変換する方法](#csharp-pdf-to-docx)

_フォーマット_: **Word**

- [C# PDFからWordへ](#csharp-pdf-to-docx)
- [C#でPDFをWordに変換](#csharp-pdf-to-doc)
- [C# PDFファイルをWordに変換する方法](#csharp-pdf-to-docx)

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリでも動作します。
## PDFからDOCおよびDOCXへの変換

最も人気のある機能の1つは、PDFをMicrosoft Word DOCに変換することで、コンテンツ管理をより容易にします。**Aspose.PDF for .NET** は、PDFファイルを迅速かつ効率的にDOCおよびDOCX形式に変換することができます。

## PDFをDOC（Microsoft Word 97-2003）ファイルに変換

PDFファイルをDOC形式に簡単に完全に制御して変換します。Aspose.PDF for .NETは柔軟で、多種多様な変換をサポートしています。たとえば、PDFドキュメントのページを画像に変換する機能は非常に人気があります。

多くのお客様がPDFからDOCへの変換を要求しています。PDFファイルをMicrosoft Wordドキュメントに変換することです。お客様がこれを望む理由は、PDFファイルは簡単に編集できないのに対し、Wordドキュメントは編集が可能だからです。一部の企業では、ユーザーがPDFとして開始したファイルでテキスト、テーブル、画像を操作できるようにしたいと考えています。

物事をシンプルでわかりやすく保つ伝統を守りながら、Aspose.PDF for .NETは、ソースPDFファイルをDOCファイルに変換するために2行のコードで変換できます。
シンプルで理解しやすい伝統を継承し、Aspose.PDF for .NETでは、ソースPDFファイルをDOCファイルに変換するために2行のコードだけで変換できます。

以下のC#コードスニペットは、PDFファイルをDOC形式に変換する方法を示しています。

<a name="csharp-pdf-to-doc"><strong>手順: C#でPDFをDOCに変換する</strong></a>

1. ソースPDFドキュメントを使用して[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/)オブジェクトのインスタンスを作成します。
2. **Document.Save()** メソッドを呼び出して、**SaveFormat.Doc** 形式で保存します。

```csharp
public static void ConvertPDFtoWord()
{
    // ソースPDFドキュメントを開く
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // ファイルをMSドキュメント形式で保存
    pdfDocument.Save(_dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);

}
```

### DocSaveOptionsクラスの使用

[`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) クラスには、PDFファイルをDOC形式に変換する際に役立つ多くのプロパティが用意されています。
[`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) クラスは、PDFファイルをDOC形式に変換する際に多くのプロパティを提供します。

- [`Textbox`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) モードは、PDFファイルのオリジナルの外観を保持するのに適しており、高速ですが、結果として得られるドキュメントの編集性は限定的かもしれません。オリジナルのPDFに視覚的にグループ化されたテキストブロックは、出力ドキュメントでテキストボックスに変換されます。これにより、オリジナルに最大限似せることができるので、出力ドキュメントは見た目が良いですが、全てテキストボックスで構成されており、Microsoft Wordでの編集はかなり困難です。
- [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) は完全認識モードで、エンジンがグルーピングと多層分析を実行して、作者の意図に基づいてオリジナルドキュメントを復元しながら、簡単に編集可能なドキュメントを生成します。
- [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) は完全認識モードで、エンジンがグループ化と多層分析を行い、著者の意図に基づいて元の文書を復元しつつ、編集しやすい文書を生成します。

[`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) プロパティは、テキスト要素間の相対的な近接性を制御するために使用できます。これは、距離がフォントサイズによって標準化されることを意味します。大きなフォントは、音節間に大きな空間があっても単一の全体と見なされる場合があります。例えば、1 = 100% として指定されます。これは、12ptの2つの文字が12pt離れて配置されている場合、近接しているということを意味します。
- [`RecognitionBullets`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/recognizebullets) は変換中に弾丸認識をオンにするために使用されます。

```csharp
public static void ConvertPDFtoWordDocAdvanced()
{
    var pdfFile = Path.Combine(_dataDir, "PDF-to-DOC.pdf");
    var docFile = Path.Combine(_dataDir, "PDF-to-DOC.doc");
    Document pdfDocument = new Document(pdfFile);
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        Format = DocSaveOptions.DocFormat.Doc,
        // フロー認識モードを設定
        Mode = DocSaveOptions.RecognitionMode.Flow,
        // 横方向の近接性を2.5に設定
        RelativeHorizontalProximity = 2.5f,
        // 変換プロセス中に弾丸を認識するための値を有効にする
        RecognizeBullets = true
    };
    pdfDocument.Save(docFile, saveOptions);
}
```
{{% alert color="success" %}}
**オンラインでPDFをDOCに変換してみてください**

Aspose.PDF for .NETは、無料のオンラインアプリケーション["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)を提供しており、その機能と品質を試すことができます。

[![PDFをDOCに変換](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDFをDOCX（Microsoft Word 2007-2021ファイル）に変換

Aspose.PDF for .NET APIを使用すると、C#や.NET言語を使用してPDF文書をDOCXに変換することができます。DOCXは、Microsoft Wordの文書のためのよく知られた形式で、構造がプレーンバイナリからXMLとバイナリファイルの組み合わせに変更されました。DocxファイルはWord 2007以降のバージョンで開くことができますが、以前のバージョンのMS Wordでは開くことができません。これはDOCファイル拡張子をサポートしているからです。

次のC#コードスニペットは、PDFファイルをDOCX形式に変換する方法を示しています。

<a name="csharp-pdf-to-docx"><strong>手順: C#でPDFをDOCXに変換する</strong></a>

1.
1.
2. **SaveFormat.DocX** 形式で保存します。**Document.Save()** メソッドを呼び出してください。

```csharp
public static void ConvertPDFtoWord_DOCX_Format()
{
    // ソースPDFドキュメントを開く
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // 結果のDOCファイルを保存
    pdfDocument.Save(_dataDir + "saveOptionsOutput_out.doc", SaveFormat.DocX);
}
```

### PDFをDOCXに拡張モードで変換

PDFをDOCXに変換する際、より良い結果を得るために `EnhancedFlow` モードを使用できます。
FlowとEnhanced Flowの主な違いは、境界線の有無にかかわらずテーブルが実際のテーブルとして認識されること、背景に画像のあるテキストではないことです。
また、番号付きリストの認識やその他の細かな点もあります。

```csharp
public static void ConvertPDFtoWord_Advanced_DOCX_Format()
{    
    // ソースPDFドキュメントを開く
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");

    // DocSaveOptionsオブジェクトをインスタンス化
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        // 出力形式としてDOCXを指定
        Format = DocSaveOptions.DocFormat.DocX
        // 他のDocSaveOptionsパラメータを設定
        Mode = DocSaveOptions.RecognitionMode.EnhancedFlow
    };
    // docx形式でドキュメントを保存
    pdfDocument.Save("ConvertToDOCX_out.docx", saveOptions);
}
```
{{% alert color="warning" %}}
**オンラインでPDFをDOCXに変換してみてください**

Aspose.PDF for .NETは、無料のオンラインアプリケーション ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx) を提供しています。ここで機能と品質を調査してみることができます。

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 参照

この記事では、上記と同じコードを使用して、以下のトピックもカバーしています。

_Format_: **Word**

- [C# PDFをWordコードに](#csharp-pdf-to-docx)
- [C# PDFをWord APIに](#csharp-pdf-to-docx)
- [C# PDFをプログラムでWordに](#csharp-pdf-to-docx)
- [C# PDFをWordライブラリに](#csharp-pdf-to-docx)
- [C# PDFをWordとして保存](#csharp-pdf-to-docx)
- [C# PDFからWordを生成](#csharp-pdf-to-docx)
- [C# PDFからWordを作成](#csharp-pdf-to-docx)
- [C# PDFをWordコンバーターに](#csharp-pdf-to-docx)

_Format_: **DOC**

- [C# PDFをDOCコードに](#csharp-pdf-to-doc)
- [C# PDFをDOC APIに](#csharp-pdf-to-doc)
- [C# PDFからDOCへのAPI](#csharp-pdf-to-doc)
- [C# PDFからDOCへプログラムで](#csharp-pdf-to-doc)
- [C# PDFからDOCへのライブラリ](#csharp-pdf-to-doc)
- [C# PDFをDOCとして保存](#csharp-pdf-to-doc)
- [C# PDFからDOCを生成](#csharp-pdf-to-doc)
- [C# PDFからDOCを作成](#csharp-pdf-to-doc)
- [C# PDFからDOCへのコンバータ](#csharp-pdf-to-doc)

_Format_: **DOCX**

- [C# PDFからDOCXへのコード](#csharp-pdf-to-docx)
- [C# PDFからDOCXへのAPI](#csharp-pdf-to-docx)
- [C# PDFからDOCXへプログラムで](#csharp-pdf-to-docx)
- [C# PDFからDOCXへのライブラリ](#csharp-pdf-to-docx)
- [C# PDFをDOCXとして保存](#csharp-pdf-to-docx)
- [C# PDFからDOCXを生成](#csharp-pdf-to-docx)
- [C# PDFからDOCXを作成](#csharp-pdf-to-docx)
- [C# PDFからDOCXへのコンバータ](#csharp-pdf-to-docx)

