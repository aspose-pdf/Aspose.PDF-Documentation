---
title: PDFヘッダーとフッターを追加する
linktitle: ヘッダーとフッターを追加
type: docs
weight: 70
url: /java/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Javaを使用して、PDFファイルにヘッダーとフッターを追加できます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFスタンプは、契約書、レポート、制限された資料などでよく使用され、ドキュメントが「読んだ」「合格」「機密」などとしてレビューおよびマークされたことを証明するために使用されます。この記事では、**Aspose.PDF for Java**を使用してPDFドキュメントに画像スタンプとテキストスタンプを追加する方法を紹介します。

上記のコードスニペットを行ごとに読むと、構文とコードロジックが非常に理解しやすいことがわかります。

## PDFファイルのヘッダーにテキストを追加する

[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)クラスを使用して、PDFファイルのヘッダーにテキストを追加できます。
 TextStampクラスは、フォントサイズ、フォントスタイル、フォントカラーなど、テキストベースのスタンプを作成するために必要なプロパティを提供します。ヘッダーにテキストを追加するには、Documentオブジェクトと必要なプロパティを使用してTextStampオブジェクトを作成する必要があります。その後、PageのAddStampメソッドを呼び出して、PDFのヘッダーにテキストを追加できます。

PDFのヘッダーエリアにテキストが調整されるように、TopMarginプロパティを設定する必要があります。また、HorizontalAlignmentをCenterに、VerticalAlignmentをTopに設定する必要があります。

次のコードスニペットは、JavaでPDFファイルのヘッダーにテキストを追加する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPDFHeaderandFooter {
    // ドキュメントディレクトリへのパス。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddingTextInHeaderOfPDFFile() {

        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "TextinHeader.pdf");

        // ヘッダーを作成
        TextStamp textStamp = new TextStamp("Header Text");

        // スタンプのプロパティを設定
        textStamp.setTopMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Top);

        // すべてのページにヘッダーを追加
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }

        // 更新されたドキュメントを保存
        pdfDocument.save(_dataDir + "TextinHeader_out.pdf");
    }
```

## PDFファイルのフッターにテキストを追加する

TextStampクラスを使用して、PDFファイルのフッターにテキストを追加できます。TextStampクラスは、フォントサイズ、フォントスタイル、フォントカラーなどのテキストベースのスタンプを作成するために必要なプロパティを提供します。フッターにテキストを追加するには、必要なプロパティを使用してDocumentオブジェクトとTextStampオブジェクトを作成する必要があります。その後、ページのAddStampメソッドを呼び出して、PDFのフッターにテキストを追加できます。

以下のコードスニペットは、JavaでPDFファイルのフッターにテキストを追加する方法を示しています。

```java
    public static void AddingTextInFooterOfPDFFile() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "TextinFooter.pdf");
        // フッターを作成
        TextStamp textStamp = new TextStamp("Footer Text");
        // スタンプのプロパティを設定
        textStamp.setBottomMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // すべてのページにフッターを追加
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }
        _dataDir = _dataDir + "TextinFooter_out.pdf";
        // 更新されたPDFファイルを保存
        pdfDocument.save(_dataDir);
    }
```


## PDFファイルのヘッダーに画像を追加する

[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp) クラスを使用して、PDFファイルのヘッダーに画像を追加できます。Image Stampクラスは、フォントサイズ、フォントスタイル、フォントカラーなど、画像ベースのスタンプを作成するために必要なプロパティを提供します。ヘッダーに画像を追加するには、必要なプロパティを使用してDocumentオブジェクトとImage Stampオブジェクトを作成する必要があります。その後、ページの[AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) メソッドを呼び出して、PDFのヘッダーに画像を追加できます。

```java
public static void AddingImageInHeaderOfPDFFile() {

// ドキュメントを開く
Document pdfDocument = new Document(_dataDir + "ImageInHeader.pdf");

// ヘッダーを作成
ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

// スタンプのプロパティを設定
imageStamp.setTopMargin(10);
imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
imageStamp.setVerticalAlignment(VerticalAlignment.Top);
// すべてのページにヘッダーを追加
for (Page page : pdfDocument.getPages()) {
page.addStamp(imageStamp);
}

_dataDir = _dataDir + "ImageInHeader_out.pdf";

// 更新されたPDFファイルを保存
pdfDocument.save(_dataDir);
}
```


以下のコードスニペットは、Javaを使用してPDFファイルのヘッダーに画像を追加する方法を示しています。

## PDFファイルのフッターに画像を追加する

Image Stampクラスを使用して、PDFファイルのフッターに画像を追加できます。Image Stampクラスは、フォントサイズ、フォントスタイル、フォントカラーなど、画像ベースのスタンプの作成に必要なプロパティを提供します。フッターに画像を追加するためには、必要なプロパティを使用してDocumentオブジェクトとImage Stampオブジェクトを作成する必要があります。その後、PageのAddStampメソッドを呼び出して、PDFのフッターに画像を追加できます。

{{% alert color="primary" %}}

PDFのフッターエリアに画像が調整されるように、BottomMarginプロパティを設定する必要があります。また、[HorizontalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment)を`Center`に、[VerticalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment)を`Bottom`に設定する必要があります。

{{% /alert %}}

以下のコードスニペットは、Javaを使用してPDFファイルのフッターに画像を追加する方法を示しています。

```java
    public static void AddingImageInFooterOfPDFFile() {

        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "ImageInFooter.pdf");

        // フッターを作成
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

        // スタンプのプロパティを設定
        imageStamp.setBottomMargin(10);
        imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        imageStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // すべてのページにフッターを追加
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(imageStamp);
        }

        _dataDir = _dataDir + "ImageInFooter_out.pdf";

        // 更新されたPDFファイルを保存
        pdfDocument.save(_dataDir);
    }
```

## 1つのPDFファイルに異なるヘッダーを追加

TopMarginまたはBottom Marginプロパティを使用して、ドキュメントのヘッダー/フッターセクションにTextStampを追加できることはわかっていますが、場合によっては単一のPDFドキュメントに複数のヘッダー/フッターを追加する必要があるかもしれません。
 **Aspose.PDF for Java**はこれを行う方法を説明します。

この要件を達成するために、個々の[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)オブジェクトを作成し（必要なヘッダー/フッターの数に応じてオブジェクトの数が決まります）、それらをPDFドキュメントに追加します。また、個別のスタンプオブジェクトに対して異なるフォーマット情報を指定することもできます。次の例では、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトと3つの[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)オブジェクトを作成し、その後、ページの[AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp)メソッドを使用して、PDFのヘッダーセクションにテキストを追加しました。次のコードスニペットは、Aspose.PDF for Javaを使用してPDFファイルのフッターに画像を追加する方法を示しています。

```java
public static void AddingDifferentHeadersInOnePDFFile() {

        // ソースドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "AddingDifferentHeaders.pdf");

        // 3つのスタンプを作成
        TextStamp stamp1 = new TextStamp("Header 1");
        TextStamp stamp2 = new TextStamp("Header 2");
        TextStamp stamp3 = new TextStamp("Header 3");

        // スタンプの配置を設定（ページの上部にスタンプを配置し、水平に中央寄せ）
        stamp1.setVerticalAlignment (VerticalAlignment.Top);
        stamp1.setHorizontalAlignment(HorizontalAlignment.Center);
        // フォントスタイルをボールドに指定
        stamp1.getTextState().setFontStyle(FontStyles.Bold);
        // テキストの前景色を赤に設定
        stamp1.getTextState().setForegroundColor(Color.getRed());
        // フォントサイズを14に指定
        stamp1.getTextState().setFontSize(14);

        // 2番目のスタンプオブジェクトの垂直配置を上部に設定する必要があります
        stamp2.setVerticalAlignment(VerticalAlignment.Top);
        // スタンプの水平配置情報を中央揃えに設定
        stamp2.setHorizontalAlignment(HorizontalAlignment.Center);
        // スタンプオブジェクトのズーム係数を設定
        stamp2.setZoom (10);

        // 3番目のスタンプオブジェクトのフォーマットを設定
        // スタンプオブジェクトの垂直配置情報を上部に指定
        stamp3.setVerticalAlignment(VerticalAlignment.Top);
        // スタンプオブジェクトの水平配置情報を中央揃えに設定
        stamp3.setHorizontalAlignment (HorizontalAlignment.Center);
        // スタンプオブジェクトの回転角度を設定
        stamp3.setRotateAngle(35);
        // スタンプの背景色をピンクに設定
        stamp3.getTextState().setBackgroundColor (Color.getPink());
        
        // スタンプのフォント情報をVerdanaに変更
        stamp3.getTextState().setFont (FontRepository.findFont("Verdana"));
        // 最初のスタンプは最初のページに追加されます
        pdfDocument.getPages().get_Item(1).addStamp(stamp1);
        // 2番目のスタンプは2番目のページに追加されます
        pdfDocument.getPages().get_Item(2).addStamp(stamp2);
        // 3番目のスタンプは3番目のページに追加されます
        pdfDocument.getPages().get_Item(3).addStamp(stamp3);

        _dataDir = _dataDir + "multiheader_out.pdf";

        // 更新されたPDFファイルを保存
        pdfDocument.save(_dataDir);
    }

}
```