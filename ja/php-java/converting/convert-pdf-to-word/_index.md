---
title: PDFをMicrosoft Wordに変換
linktitle: PDFをWordに変換
type: docs
weight: 10
url: ja/php-java/convert-pdf-to-word/
lastmod: "2024-05-20"
description: Aspose.PDF for PHPを使用して、PDFファイルをDOCおよびDOCX形式に簡単かつ完全に制御して変換します。Microsoft WordドキュメントへのPDF変換を調整する方法を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 概要

この記事では、PHPを使用してPDFをWordに変換する方法を説明します。コードは非常にシンプルで、PDFをDocumentクラスにロードして、出力としてMicrosoft WordのDOCまたはDOCX形式として保存するだけです。次のトピックをカバーします

- [PHP PDFをWordに変換](#convert-pdf-to-doc)
- [PHP PDFをDOCに変換](#convert-pdf-to-doc)
- [PHP PDFをDOCXに変換](#convert-pdf-to-docx)
- [PHP PDFをWordに変換](#convert-pdf-to-docx)
- [PHP PDFをDOCに変換](#convert-pdf-to-doc)
- [PHP PDFをDOCXに変換](#convert-pdf-to-docx)
- [PHP PDFファイルをWord DOC](#convert-pdf-to-doc) または [Word DOCXに変換する方法](#convert-pdf-to-docx)

- [PHP PDFをWordライブラリ、APIまたはコードを使用して、プログラムでPDFからWordドキュメントを保存、生成または作成](#convert-pdf-to-docx)

## PDFをDOCに変換

最も人気のある機能の一つは、PDFをMicrosoft Word DOCに変換することで、これによりコンテンツの操作が容易になります。Aspose.PDF for PHPを使用すると、PDFファイルをDOCに変換できます。

**Aspose.PDF for PHP**は、ゼロからPDFドキュメントを作成でき、既存のPDFドキュメントを更新、編集、操作するための優れたツールキットです。重要な機能の一つは、ページやPDF全体を画像に変換する能力です。もう一つの人気機能は、PDFをMicrosoft Word DOCに変換することで、これによりコンテンツの操作が容易になります。（ほとんどのユーザーはPDFドキュメントを編集できませんが、Microsoft Wordでテーブル、テキスト、画像を簡単に操作できます。）

シンプルで理解しやすくするために、Aspose.PDF for PHPは、PDFファイルをDOCファイルに変換するための2行のコードを提供しています。

以下のJavaコードスニペットは、PDFファイルをDOC形式に変換するプロセスを示しています。

1. ソースPDFドキュメントで[Document](https://reference.aspose.com/page/java/com.aspose.page/document)オブジェクトのインスタンスを作成します。

2. **Document.save()** メソッドを呼び出して、**SaveFormat.Doc** 形式で保存します。

```php
// PDF ドキュメントを読み込む
$document = new Document($inputFile);

// 新しい DocSaveOptions オブジェクトを作成する
$saveOption = new DocSaveOptions();

// 出力形式を DOC に設定する
$saveOption->setFormat(DocSaveOptions_DocFormat::$Doc);

// ドキュメントを DOC として保存する
$document->save($outputFile, $saveOption);
```

## DocSaveOptions クラスの使用

[DocSaveOptions クラス](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions) は、PDF ファイルを DOC 形式に変換するプロセスを改善する多くのプロパティを提供します。これらのプロパティの中で、Mode は PDF コンテンツの認識モードを指定することができます。このプロパティには RecognitionMode 列挙から任意の値を指定できます。これらの値それぞれには特定の利点と制限があります：

- [Textbox](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) モードは高速で、PDF ファイルの元の外観を保持するのに適していますが、結果として得られるドキュメントの編集可能性が制限される可能性があります。
 元のPDFで視覚的にグループ化されたすべてのテキストブロックは、出力ドキュメントでテキストボックスに変換されます。これにより、元のドキュメントに最大限に似せることができ、出力ドキュメントは見た目が良くなりますが、完全にテキストボックスで構成されているため、Microsoft Wordでの編集が難しくなる可能性があります。

- Flowは完全認識モードであり、エンジンがグループ化および多層分析を行って、著者の意図に従って元のドキュメントを復元し、簡単に編集可能なドキュメントを生成します。制限として、出力ドキュメントは元のものと異なる場合があります。

- RelativeHorizontalProximityプロパティは、テキスト要素間の相対的な近接性を制御するために使用され、距離がフォントサイズによって正規化されることを意味します。大きなフォントでは音節間の距離が大きくても、1つの全体として考えられる場合があります。これはフォントサイズのパーセンテージで指定され、例えば、1 = 100%です。これは、12ptの文字が12pt離れて配置されているとき、それらが近接していることを意味します。

- RecognitionBulletsは、変換中に箇条書き認識をオンにするために使用されます。
```php
// PDFドキュメントを読み込む
$document = new Document($inputFile);

// 新しいDocSaveOptionsオブジェクトを作成
$saveOption = new DocSaveOptions();

// 認識モードをEnhancedFlowに設定
$saveOption->setMode(DocSaveOptions_RecognitionMode::$EnhancedFlow);

// 出力形式をDOCに設定
$saveOption->setFormat(DocSaveOptions_DocFormat::$Doc);

// 認識モードをFlowとして設定
saveOptions->setMode(DocSaveOptions_RecognitionMode::$Flow);

// 水平方向の近接性を2.5に設定
saveOptions->setRelativeHorizontalProximity(2.5f);

// 変換プロセス中に箇条書きを認識するように値を有効化
saveOptions->setRecognizeBullets(true);

// ドキュメントをDOCXとして保存
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**PDFをオンラインでDOCに変換してみてください**

Aspose.PDF for PHPは、オンラインで無料のアプリケーション["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-doc)を提供しており、そこで機能と品質を調査することができます。
{{% /alert %}}


[![Convert PDF to DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
## PDFをDOCXに変換する

DocFormat列挙型は、Word文書の出力形式としてDOCXを選択するオプションも提供します。ソースPDFファイルをDOCX形式にレンダリングするには、以下のコードスニペットを使用します。

## PDFをDOCXに変換する方法

以下のJavaコードスニペットは、PDFファイルをDOCX形式に変換するプロセスを示しています。

1. ソースPDF文書を使用して[Document](https://reference.aspose.com/page/java/com.aspose.page/document)オブジェクトのインスタンスを作成します。
2. **Document.save()** メソッドを呼び出して、**SaveFormat.DocX** 形式で保存します。

```php
    // PDFドキュメントをロードする
    $document = new Document($inputFile);
    
    // ドキュメントをDOCXとして保存する
    $document->save($outputFile, SaveFormat::$DocX);
```

[DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions) クラスには、結果のドキュメントの形式を指定する機能を提供するFormatというプロパティがあります。つまり、DOCまたはDOCXです。
 PDFファイルをDOCX形式に変換するには、DocSaveOptions.DocFormat列挙からDocx値を渡してください。

以下のコードスニペットをご覧ください。これは、JavaでPDFファイルをDOCX形式に変換する機能を提供します。

```php
// PDFドキュメントを読み込む
$document = new Document($inputFile);

// 新しいDocSaveOptionsオブジェクトを作成
$saveOption = new DocSaveOptions();

// 認識モードをEnhancedFlowに設定
$saveOption->setMode(DocSaveOptions_RecognitionMode::$EnhancedFlow);

// 出力形式をDOCXに設定
$saveOption->setFormat(DocSaveOptions_DocFormat::$DocX);

// ドキュメントをDOCXとして保存
$document->save($outputFile, $saveOption);
```

{{% alert color="warning" %}}
**PDFをDOCXにオンラインで変換してみてください**

Aspose.PDF for PHPは、オンラインの無料アプリケーション["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx)を提供しており、その機能と品質を試して調査することができます。


[![Aspose.PDF Convertion PDF to DOCX Free App](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)
{{% /alert %}}