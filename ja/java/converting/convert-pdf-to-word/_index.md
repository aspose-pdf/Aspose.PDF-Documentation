---
title: JavaでPDFをMicrosoft Wordドキュメントに変換
linktitle: PDFをWordに変換
type: docs
weight: 10
url: ja/java/convert-pdf-to-word/
lastmod: "2021-11-19"
description: Aspose.PDF for Javaを使用して、PDFファイルをDOCおよびDOCX形式に簡単かつ完全に制御して変換します。Microsoft WordドキュメントへのPDF変換を調整する方法を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 概要

この記事では、Javaを使用してPDFをWordに変換する方法を説明します。コードは非常に簡単で、PDFをDocumentクラスにロードし、それをMicrosoft Word DOCまたはDOCX形式として出力するだけです。以下のトピックをカバーしています

- [Java PDFをWordに変換](#convert-pdf-to-doc)
- [Java PDFをDOCに変換](#convert-pdf-to-doc)
- [Java PDFをDOCXに変換](#convert-pdf-to-docx)
- [Java PDFをWordに変換](#convert-pdf-to-docx)
- [Java PDFをDOCに変換](#convert-pdf-to-doc)
- [Java PDFをDOCXに変換](#convert-pdf-to-docx)
- [Java PDFファイルをWord DOCまたはWord DOCXに変換する方法](#convert-pdf-to-doc) または [Word DOCX](#convert-pdf-to-docx)

- [Java PDFをWordライブラリ、APIまたはコードを使用して、PDFからプログラムでWordドキュメントを保存、生成または作成](#convert-pdf-to-docx)

## PDFをDOCに変換

最も人気のある機能の1つは、PDFをMicrosoft Word DOCに変換することです。これにより、内容を簡単に操作できます。Aspose.PDF for Javaを使用すると、PDFファイルをDOCに変換できます。

**Aspose.PDF for Java**は、PDFドキュメントをゼロから作成することができ、既存のPDFドキュメントを更新、編集、操作するための優れたツールキットです。重要な機能の1つは、ページやPDFドキュメント全体を画像に変換する能力です。もう一つの人気のある機能は、PDFをMicrosoft Word DOCに変換することで、内容を簡単に操作できるようになります。（ほとんどのユーザーはPDFドキュメントを編集できませんが、Microsoft Wordではテーブル、テキスト、画像を簡単に操作できます。）

物事を簡単で理解しやすくするために、Aspose.PDF for Javaは、ソースPDFファイルをDOCファイルに変換するための2行のコードを提供しています。

以下のJavaコードスニペットは、PDFファイルをDOC形式に変換するプロセスを示しています。

1. ソースPDFドキュメントを使用して[Document](https://reference.aspose.com/page/java/com.aspose.page/document)オブジェクトのインスタンスを作成します。
2. **Document.save()**メソッドを呼び出して**SaveFormat.Doc**形式で保存します。

```java
public static void convertPDFtoWord() {
    // ソースPDFドキュメントを開く
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // ファイルをMSドキュメント形式で保存する
    document.save(DATA_DIR + "PDFToDOC_out.doc", SaveFormat.Doc);
    document.close();
}
```

## DocSaveOptionsクラスを使用する

[DocSaveOptionsクラス](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions)は、PDFファイルをDOC形式に変換するプロセスを改善する多くのプロパティを提供します。これらのプロパティの中で、ModeはPDFコンテンツの認識モードを指定することができます。このプロパティには、RecognitionMode列挙から任意の値を指定できます。これらの値のそれぞれには特定の利点と制限があります。

- [Textbox](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField)モードは高速で、PDFファイルの元の外観を保持するのに適していますが、結果のドキュメントの編集可能性は制限される可能性があります。
 元のPDFで視覚的にグループ化されたテキストのブロックは、出力ドキュメントではテキストボックスに変換されます。これにより、出力ドキュメントが元のものと非常によく似たものになり、見た目は良くなりますが、テキストボックスのみで構成されているため、Microsoft Wordでの編集が難しくなる可能性があります。

- Flowは完全認識モードであり、エンジンはグループ化と多層分析を行い、著者の意図に応じて元のドキュメントを復元し、簡単に編集可能なドキュメントを生成します。制限として、出力ドキュメントは元のものとは異なる見た目になる可能性があります。

- RelativeHorizontalProximityプロパティは、テキスト要素間の相対的な近接性を制御するために使用され、距離がフォントサイズによって規格化されることを意味します。大きなフォントは、音節間の距離が大きくても単一の全体とみなされることがあります。これはフォントサイズのパーセンテージとして指定され、例えば、1 = 100%ということです。つまり、12ptの2つの文字が12pt離れて配置されている場合、それらは近接しているとみなされます。

- RecognitionBulletsは、変換中に箇条書きの認識をオンにするために使用されます。
```java
public static void convertPDFtoWordDocAdvanced() {
    Path pdfFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.pdf");
    Path docFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.doc");
    Document document = new Document(pdfFile.toString());
    DocSaveOptions saveOptions = new DocSaveOptions();

    // 出力形式をDOCとして指定
    saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
    // 認識モードをFlowとして設定
    saveOptions.setMode(DocSaveOptions.RecognitionMode.Flow);

    // 水平方向の近接度を2.5に設定
    saveOptions.setRelativeHorizontalProximity(2.5f);

    // 変換プロセス中に箇条書きを認識するように値を有効にする
    saveOptions.setRecognizeBullets(true);

    document.save(docFile.toString(), saveOptions);
    document.close();
}
```

{{% alert color="success" %}}
**PDFをDOCにオンラインで変換してみてください**

Aspose.PDF for Javaは、オンラインで無料のアプリケーション["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-doc)を提供しています。ここでは、その機能と品質を調査することができます。

[![Convert PDF to DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDFをDOCXに変換

DocFormat列挙型は、Wordドキュメントの出力形式としてDOCXを選択するオプションも提供します。ソースPDFファイルをDOCX形式にレンダリングするには、以下のコードスニペットを使用します。

## PDFをDOCXに変換する方法

以下のJavaコードスニペットは、PDFファイルをDOCX形式に変換するプロセスを示しています。

1. ソースPDFドキュメントで[Document](https://reference.aspose.com/page/java/com.aspose.page/document)オブジェクトのインスタンスを作成します。
2. **Document.save()**メソッドを呼び出して**SaveFormat.DocX**形式で保存します。

```java
public static void convertPDFtoWord_DOCX_Format() {
    // ソースPDFドキュメントを開く
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // 結果のDOCファイルを保存する
    document.save(DATA_DIR + "saveOptionsOutput_out.doc", SaveFormat.DocX);
    document.close();
}
```

[DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions)クラスには、結果のドキュメントの形式を指定する機能を提供するFormatというプロパティがあります。すなわち、DOCまたはDOCXです。
 PDFファイルをDOCX形式に変換するには、DocSaveOptions.DocFormat列挙からDocx値を渡してください。

以下のコードスニペットをご覧ください。これはPDFファイルをJavaでDOCX形式に変換する機能を提供します。

```java
public static void convertPDFtoWord_Advanced_DOCX_Format() {
    // ソースPDFドキュメントを開く
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");

    // DocSaveOptionsオブジェクトをインスタンス化
    DocSaveOptions saveOptions = new DocSaveOptions();
    // 出力形式をDOCXとして指定
    saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
    // 他のDocSaveOptionsパラメータを設定
    // ....

    // ドキュメントをdocx形式で保存
    document.save("ConvertToDOCX_out.docx", saveOptions);
    document.close();
}
```

{{% alert color="warning" %}}
**PDFをDOCXにオンラインで変換する**


Aspose.PDF for Javaは、オンライン無料アプリケーション["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx)を提供しており、そこで機能性と品質を調査することができます。
[![Aspose.PDF 変換 PDF から DOCX 無料アプリ](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}