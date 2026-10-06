---
title: "Java を使用した PDF への画像の追加"
linktitle: "画像の追加"
type: docs
weight: 10
url: /ja/java/add-image-to-existing-pdf-file/
description: "Java を使用して既存の PDF ファイルに画像を追加する方法を学習してください。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での 既存の PDF ファイルへの画像の追加"
Abstract: "このガイドでは、Aspose.PDF for Java を使用して PDF ドキュメントに画像を追加する方法を示します。画像を固定座標に配置する方法、低レベルのページ演算子を使用して画像を追加する方法、アクセシビリティのために代替テキストを設定する方法、および Flate 圧縮で画像データを埋め込む方法について説明します。"
---
Aspose.PDF for Java は、高レベルの画像配置と低レベルの演算子ベースの描画の両方をサポートしています。

## ページ座標による画像の追加

PDF ページ上の固定位置に画像を配置する必要がある場合は、このサンプルを使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページを追加してください。
1. `page.addImage()` を呼び出して、ソース画像のパスとターゲット矩形を指定してください。
1. 生成された PDF ファイルを保存してください。

```java
public static void addImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));
        document.save(outputFile.toString());
    }
}
```

## ページ演算子を使用した画像の追加

ページ演算子を通じて画像の配置とスケーリングを低レベルで制御する必要がある場合は、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ソース画像ストリームを開いてください。
1. 画像をページリソースに追加し、ターゲット矩形を計算してください。
1. 必要なグラフィック演算子を書き込み、ドキュメントを保存してください。

```java
public static void addImageUsingOperators(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream);
        XImage xImage = resourcesImages.get_Item(resourcesImages.size());

        Rectangle rectangle = new Rectangle(
                0,
                0,
                page.getMediaBox().getWidth(),
                (page.getMediaBox().getWidth() * xImage.getHeight()) / xImage.getWidth(),
                true);

        page.getContents().add(new GSave());

        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLX() + (page.getMediaBox().getHeight() - rectangle.getHeight()) / 2);
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```

## 画像の追加と代替テキストの設定

画像にスクリーンリーダー用のアクセシビリティメタデータを含める必要がある場合は、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、画像をページに追加してください。
1. 挿入された [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) をページリソースから取得してください。
1. 代替テキストを設定し、PDF を保存してください。

```java
public static void addImageSetAlternativeTextForImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        page.addImage(imageFile.toString(), new Rectangle(0, 0, 842, 595, true));

        XImage xImage = page.getResources().getImages().get_Item(1);
        boolean result = xImage.trySetAlternativeText("Alternative text for image", page);
        if (result) {
            System.out.println("Text has been added successfuly");
        }
        document.save(outputFile.toString());
    }
}
```

## Flate 圧縮で画像の追加

Flate 圧縮を使用して画像データを埋め込みたい場合は、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、画像ストリームを開いてください。
1. 画像をページリソースに `ImageFilterType.Flate` で追加してください。
1. ページ演算子を使用して画像を描画し、結果を保存してください。

```java
public static void addImageToPdfWithFlateCompression(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream, ImageFilterType.Flate);

        page.getContents().add(new GSave());

        Rectangle rectangle = new Rectangle(0, 0, 600, 600, true);
        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY());

        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```
