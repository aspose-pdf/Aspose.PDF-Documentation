---
title: "Java での PDFに画像スタンプの追加"
linktitle: PDFファイルの画像スタンプ
type: docs
weight: 10
url: /ja/java/image-stamps-in-pdf-page/
description: JavaでPDFページに画像スタンプを追加する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaを使用してPDFページに画像スタンプと画像背景を追加する
Abstract: このドキュメントでは、Aspose.PDF for Java を使用して PDF ファイルに画像スタンプを追加する方法を解説します。位置指定、回転、透明度、品質管理を伴う画像スタンプと、画像を浮動ボックスの背景として使用する方法について説明します。
---
Aspose.PDF for Java は、オーバーレイとしての画像スタンプおよび画像を背景としたレイアウト要素をサポートしています。

## 画像スタンプの追加

ページにカスタム配置と透明度を持つ画像スタンプを表示する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) を作成し、外観を構成してください。
1. ページにスタンプを追加し、ドキュメントを保存してください。

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(300);
        imageStamp.setWidth(300);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## 品質管理付きで画像スタンプの追加

ImageStamp のレンダリング品質を調整する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 作成する [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) 品質値を設定してください。
1. ページにスタンプを追加し、結果を保存してください。

```java
public static void addImageStampWithQualityControl(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setQuality(10);
        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## 画像をフローティングボックスの背景として使用する

画像をスタイル付きレイアウトコンテナの背景として使用する場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、対象ページにアクセスしてください。
1. 作成する [FloatingBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/floatingbox/) テキストと枠設定で。
1. 背景画像を設定し、ボックスをページに追加し、ドキュメントを保存してください。

```java
public static void addImageAsBackgroundInFloatingBox(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        FloatingBox box = new FloatingBox(200.0f, 100.0f);
        box.setLeft(40);
        box.setTop(80);
        box.setHorizontalAlignment(HorizontalAlignment.Center);
        box.getParagraphs().add(new TextFragment("Text in Floating Box"));
        box.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Image image = new Image();
        image.setFile(imageFile.toString());
        box.setBackgroundImage(image);
        box.setBackgroundColor(Color.getYellow());
        page.getParagraphs().add(box);

        document.save(outputFile.toString());
    }
}
```
