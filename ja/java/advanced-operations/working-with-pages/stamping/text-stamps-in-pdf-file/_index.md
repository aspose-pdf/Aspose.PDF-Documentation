---
title: PDFにテキストスタンプをプログラムで追加
linktitle: PDFファイルにおけるテキストスタンプ
type: docs
weight: 20
url: /ja/java/text-stamps-in-the-pdf-file/
description: JavaでTextStampクラスを使用してPDFファイルにテキストスタンプを追加します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Javaでテキストスタンプを追加

Aspose.PDF for Javaは、PDFファイルにテキストスタンプを追加するための[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)クラスを提供します。
 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) クラスは、スタンプオブジェクトのフォントサイズ、フォントスタイル、フォントカラーなどを指定するための必要なメソッドを提供します。テキストスタンプを追加するには、まず [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトと [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) オブジェクトを必要なメソッドを使用して作成する必要があります。その後、[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) クラスの [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) メソッドを呼び出して、PDF ドキュメントにスタンプを追加することができます。

次のコードスニペットは、PDF ファイルにテキストスタンプを追加する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.*;
import com.aspose.pdf.facades.Stamp;

public class ExampleStampingImage {
    // ドキュメントディレクトリへのパス。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddTextStamp() {
        // ドキュメントを開く
        Document pdfDocument = new Document("input.pdf");
        // テキストスタンプを作成
        TextStamp textStamp = new TextStamp("Sample Stamp");
        // スタンプが背景かどうかを設定
        textStamp.setBackground(true);
        // 原点を設定
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        // スタンプを回転
        textStamp.setRotate(Rotation.on90);
        // テキストプロパティを設定
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0F);
        textStamp.getTextState().setFontStyle(FontStyles.Bold);
        textStamp.getTextState().setFontStyle(FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getGreen());
        // 特定のページにスタンプを追加
        pdfDocument.getPages().get_Item(1).addStamp(textStamp);
        // 出力ドキュメントを保存
        pdfDocument.save("TextStamp_output.pdf");
    }
```

## TextStampオブジェクトの配置を定義する

PDFドキュメントに透かしを追加することは頻繁に求められる機能の一つであり、Aspose.PDF for Javaは画像およびテキストの透かしを追加することが完全に可能です。[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)クラスは、PDFファイルにテキストスタンプを追加する機能を提供します。最近、[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)オブジェクトを使用する際にテキストの配置を指定する機能をサポートする必要がありました。そのため、この要件を満たすために、[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)クラスにsetTextAlignment(..)メソッドを導入しました。このメソッドを使用することで、テキストの水平配置を指定できます。

以下のコードスニペットは、既存のPDFドキュメントを読み込み、その上に[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)を追加する方法の例を示しています。

```java
    public static void DefineAlignmentTextStamp() {
        // 入力ファイルでDocumentオブジェクトをインスタンス化する
        Document pdfDocument = new Document("input.pdf");
        // サンプル文字列でFormattedTextオブジェクトをインスタンス化する
        FormattedText text = new FormattedText("This");
        
        // FormattedTextに新しいテキスト行を追加する
        text.addNewLineText("is sample");
        text.addNewLineText("Center Aligned");
        text.addNewLineText("TextStamp");
        text.addNewLineText("Object");
        // FormattedTextを使用してTextStampオブジェクトを作成する
        TextStamp stamp = new TextStamp(text);
        // テキストスタンプの水平配置を中央揃えに指定する
        stamp.setHorizontalAlignment(HorizontalAlignment.Center);
        // テキストスタンプの垂直配置を中央揃えに指定する
        stamp.setVerticalAlignment(VerticalAlignment.Center);
        // TextStampのテキスト水平配置を中央揃えに指定する
        stamp.setTextAlignment(HorizontalAlignment.Center);
        // スタンプオブジェクトの上部マージンを設定する
        stamp.setTopMargin(20);
        // PDFファイルのすべてのページにスタンプを追加する
        pdfDocument.getPages().get_Item(1).addStamp(stamp);
        
        // 出力ドキュメントを保存する
        pdfDocument.save("TextStamp_output.pdf");
    }
```


## PDFファイルにスタンプとしての塗りつぶしストロークテキスト

テキストの追加および編集シナリオに対するレンダリングモードの設定を実装しました。ストロークテキストをレンダリングするには、[TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState)オブジェクトを作成し、RenderingModeをTextRenderingMode.StrokeTextに設定し、さらにStrokingColorプロパティの色を選択してください。その後、BindTextState()メソッドを使用してTextStateをスタンプにバインドします。

以下のコードスニペットは、塗りつぶしストロークテキストを追加する方法を示しています：

```java
   public static void FillStrokeTextAsStampInPDFFile(){
        // 詳細プロパティを転送するためのTextStateオブジェクトを作成
        TextState ts = new TextState();
        
        // ストロークの色を設定
        ts.setStrokingColor(Color.getGray());
        
        // テキストレンダリングモードを設定
        ts.setRenderingMode (TextRenderingMode.StrokeText);
        
        // 入力PDFドキュメントをロード
        PdfFileStamp fileStamp = new PdfFileStamp(new Document(_dataDir + "input.pdf"));

        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("PAID IN FULL", java.awt.Color.GRAY, "Arial", EncodingType.Winansi, true, 78));

        // TextStateをバインド
        stamp.bindTextState(ts);
        // X,Yの原点を設定
        stamp.setOrigin(100, 100);
        stamp.setOpacity (5);
        stamp.setBlendingSpace (BlendingColorSpace.DeviceRGB);
        stamp.setRotation (45.0F);
        stamp.setBackground(false);
        // スタンプを追加
        fileStamp.addStamp(stamp);
        fileStamp.save(_dataDir + "ouput_out.pdf");
        fileStamp.close();
    }
```