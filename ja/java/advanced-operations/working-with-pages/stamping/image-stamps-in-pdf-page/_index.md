---
title: PDFに画像スタンプをプログラムで追加する
linktitle: PDFファイルに画像スタンプ
type: docs
weight: 10
url: /ja/java/image-stamps-in-pdf-page/
description: Aspose.PDF for Javaライブラリを使用してImageStampクラスを使用してPDFドキュメントに画像スタンプを追加します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイルに画像スタンプを追加する

[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) クラスを使用して、PDFドキュメントに画像をスタンプとして追加できます。[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) クラスは、高さ、幅、不透明度などを指定するメソッドを提供します。

画像スタンプを追加するには:

1. 必要なプロパティを使用して[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトとImageStampオブジェクトを作成します。

1. PDFにスタンプを追加するには、[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)クラスの[addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-)メソッドを呼び出します。

次のコードスニペットは、PDFファイルに画像スタンプを追加する方法を示しています。

```java
public static void AddImageStampInPDFFile() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // 画像スタンプを作成
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(48);
        imageStamp.setWidth(225);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        // 特定のページにスタンプを追加
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        // 出力ドキュメントを保存
        pdfDocument.save(_dataDir + "AddImageStamp_out.pdf");

    }
```


## スタンプ追加時の画像品質の制御

[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) クラスを使用すると、PDFドキュメントに画像をスタンプとして追加できます。また、PDFファイルに画像を透かしとして追加する際の画像品質を制御することもできます。これを可能にするために、[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) クラスに setQuality(...) というメソッドが追加されています。類似のメソッドは com.aspose.pdf.facades パッケージの [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) クラスにも存在します。

以下のコードスニペットは、PDFファイルにスタンプとして追加する際に画像の品質を制御する方法を示しています。

```java
 public static void ControlImageQualityWhenAddingStamp() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // 画像スタンプを作成
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setQuality(10);
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        pdfDocument.save(_dataDir + "ControlImageQuality_out.pdf");
    }
```


## 浮動ボックス内の背景としての画像スタンプ

Aspose.PDF APIを使用すると、浮動ボックス内の背景として画像スタンプを追加できます。FloatingBoxクラスのBackgroundImageプロパティを使用して、次のコードサンプルに示すように浮動ボックスの背景画像スタンプを設定できます。

```java
public static void ImageStampAsBackgroundInFloatingBox() {
        // Documentオブジェクトをインスタンス化
        Document doc = new Document();
        // PDFドキュメントにページを追加
        Page page = doc.getPages().add();

        // FloatingBoxオブジェクトを作成
        FloatingBox aBox = new FloatingBox(200, 100);

        // FloatingBoxの左位置を設定
        aBox.setLeft(40);
        // FloatingBoxの上位置を設定
        aBox.setTop(80);
        // FloatingBoxの水平位置を設定
        aBox.setHorizontalAlignment(HorizontalAlignment.Center);
        // FloatingBoxの段落コレクションにテキストフラグメントを追加
        aBox.getParagraphs().add(new TextFragment("メインテキスト"));
        // FloatingBoxの境界線を設定
        aBox.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        // 背景画像を追加
        Image img = new Image();
        img.setFile(_dataDir + "aspose-logo.png");
        aBox.setBackgroundImage(img);

        // FloatingBoxの背景色を設定
        aBox.setBackgroundColor(Color.getYellow());

        // ページオブジェクトの段落コレクションにFloatingBoxを追加
        page.getParagraphs().add(aBox);
        // PDFドキュメントを保存
        doc.save(_dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
    }
}
```