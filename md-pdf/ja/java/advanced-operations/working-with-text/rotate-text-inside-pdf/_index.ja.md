---
title: PDF内のテキストを回転 
linktitle: PDF内のテキストを回転
type: docs
weight: 50
url: /java/rotate-text-inside-pdf/
description: PDFにテキストを回転させるさまざまな方法を学びます。Aspose.PDFを使用すると、テキストを任意の角度に回転させたり、テキストフラグメントや段落全体を回転させることができます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 回転プロパティを使用してPDF内のテキストを回転

[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)クラスの[setRotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#setRotation-double-)メソッドを使用することにより、テキストをさまざまな角度で回転させることができます。テキストの回転は、ドキュメント生成のさまざまなシナリオで使用できます。要件に応じてテキストを回転させるために、回転角度を度で指定できます。以下のさまざまなシナリオをご確認ください。これらでテキストの回転を実装できます。

## TextFragmentとTextBuilderを使用して回転を実装

```java
public class ExampleRotateText {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ImplementRotationUsingTextFragmentAndTextBuilder() {

        // ドキュメントオブジェクトを初期化
        Document pdfDocument = new Document();
        // 特定のページを取得
        Page pdfPage = pdfDocument.getPages().add();
        // テキストフラグメントを作成
        TextFragment textFragment1 = new TextFragment("main text");
        textFragment1.setPosition(new Position(100, 600));

        // テキストプロパティを設定
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        // 回転したテキストフラグメントを作成
        TextFragment textFragment2 = new TextFragment("rotated text");
        textFragment2.setPosition(new Position(200, 600));
        // テキストプロパティを設定
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setRotation(45);

        // 回転したテキストフラグメントを作成
        TextFragment textFragment3 = new TextFragment("rotated text");
        textFragment3.setPosition(new Position(300, 600));

        // テキストプロパティを設定
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(90);

        // TextBuilderオブジェクトを作成
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // PDFページにテキストフラグメントを追加
        textBuilder.appendText(textFragment1);
        textBuilder.appendText(textFragment2);
        textBuilder.appendText(textFragment3);

        // ドキュメントを保存
        pdfDocument.save(_dataDir + "TextFragmentTests_Rotated1_out.pdf");
    }
}
```


## TextParagraph と TextBuilder を使用した回転の実装 (回転されたフラグメント)

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    // ドキュメントオブジェクトを初期化
    Document pdfDocument = new Document();
    // 特定のページを取得
    Page pdfPage = (Page) pdfDocument.getPages().add();
    TextParagraph paragraph = new TextParagraph();
    paragraph.setPosition(new Position(200, 600));
    // テキストフラグメントを作成
    TextFragment textFragment1 = new TextFragment("rotated text");
    // テキストプロパティを設定
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // 回転を設定
    textFragment1.getTextState().setRotation(45);

    // テキストフラグメントを作成
    TextFragment textFragment2 = new TextFragment("main text");
    // テキストプロパティを設定
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // テキストフラグメントを作成
    TextFragment textFragment3 = new TextFragment("another rotated text");
    // テキストプロパティを設定
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // 回転を設定
    textFragment3.getTextState().setRotation(-45);

    // テキストフラグメントを段落に追加
    paragraph.appendLine(textFragment1);
    paragraph.appendLine(textFragment2);
    paragraph.appendLine(textFragment3);
    // TextBuilder オブジェクトを作成
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // PDF ページにテキスト段落を追加
    textBuilder.appendParagraph(paragraph);
    // ドキュメントを保存
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated2_out.pdf");
}
```


## TextFragmentとPage.Paragraphsを使用した回転の実装

```csharp
public static void ImplementRotationUsingTextFragmentAndPageParagraphs() {
    // ドキュメントオブジェクトを初期化
    Document pdfDocument = new Document();
    // 特定のページを取得
    Page pdfPage = (Page) pdfDocument.getPages().add();
    // テキストフラグメントを作成
    TextFragment textFragment1 = new TextFragment("main text");
    // テキストプロパティを設定
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // テキストフラグメントを作成
    TextFragment textFragment2 = new TextFragment("rotated text");

    // テキストプロパティを設定
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // 回転を設定
    textFragment2.getTextState().setRotation(315);

    // テキストフラグメントを作成
    TextFragment textFragment3 = new TextFragment("rotated text");
    // テキストプロパティを設定
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // 回転を設定
    textFragment3.getTextState().setRotation(270);
    pdfPage.getParagraphs().add(textFragment1);
    pdfPage.getParagraphs().add(textFragment2);
    pdfPage.getParagraphs().add(textFragment3);

    // ドキュメントを保存
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated3_out.pdf");
    }
```


## TextParagraphとTextBuilderを使用した回転の実装（段落全体の回転）

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder() {

    // ドキュメントオブジェクトを初期化
    Document pdfDocument = new Document();
    // 特定のページを取得
    Page pdfPage = pdfDocument.getPages().add();
    for (int i = 0; i < 4; i++) {
        TextParagraph paragraph = new TextParagraph();
        paragraph.setPosition(new Position(200, 600));
        // 回転を指定
        paragraph.setRotation(i * 90 + 45);
        // テキストフラグメントを作成
        TextFragment textFragment1 = new TextFragment("段落テキスト");
        // テキストプロパティを設定
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment1.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment1.getTextState().setForegroundColor(Color.getBlue());

        // テキストフラグメントを作成
        TextFragment textFragment2 = new TextFragment("テキストの2行目");
        // テキストプロパティを設定
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment2.getTextState().setForegroundColor(Color.getBlue());

        // テキストフラグメントを作成
        TextFragment textFragment3 = new TextFragment("さらにいくつかのテキスト...");
        // テキストプロパティを設定
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment3.getTextState().setForegroundColor(Color.getBlue());
        textFragment3.getTextState().setUnderline(true);

        paragraph.appendLine(textFragment1);
        paragraph.appendLine(textFragment2);
        paragraph.appendLine(textFragment3);
        // TextBuilderオブジェクトを作成
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // テキストフラグメントをPDFページに追加
        textBuilder.appendParagraph(paragraph);
    }
    // ドキュメントを保存
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated4_out.pdf");
}
```