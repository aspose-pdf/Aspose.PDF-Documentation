---
title: "Java を使用した PDF ファイルから画像の抽出"
linktitle: "画像の抽出"
type: docs
weight: 30
url: /ja/java/extract-images-from-pdf-file/
description: Java で PDF ファイルから埋め込み画像を抽出する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF ファイルから画像を抽出する
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントから画像を抽出する方法を示します。ページから特定の画像リソースを保存する方法と、選択した矩形領域内にある画像をエクスポートする方法について説明します。
---
Aspose.PDF for Java は、直接的な画像リソース抽出および配置ベースのフィルタリングをサポートしています。

## インデックスで埋め込まれた画像の抽出

PDFページから特定の画像リソースを保存する必要がある場合に、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ターゲットにアクセスする [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) ページリソースから。
1. 画像ストリームを出力ファイルに保存してください。

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```

## 特定のページ領域から画像の抽出

選択した矩形内に配置された画像のみをエクスポートする場合にこの例を使用してください。

1. 対象を定義する [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) そしてソースPDFを開いてください。
1. 使用 [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) ページ上の画像配置を検査するために。
1. 選択領域内に配置が収まる画像のみを保存してください。

```java
public static void extractImageFromSpecificRegion(Path inputFile, Path outputFile) throws Exception {
    Rectangle rectangle = new Rectangle(0, 0, 590, 590, true);

    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        int index = 1;
        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            Point point1 = new Point(imagePlacement.getRectangle().getLLX(), imagePlacement.getRectangle().getLLY());
            Point point2 = new Point(imagePlacement.getRectangle().getURX(), imagePlacement.getRectangle().getURX());
            if (rectangle.contains(point1, true) && rectangle.contains(point2, true)) {
                Path indexedOutputFile = Path.of(outputFile.toString().replace("index", String.valueOf(index)));
                try (OutputStream outputImage = Files.newOutputStream(indexedOutputFile)) {
                    imagePlacement.getImage().save(outputImage);
                }
                index++;
            }
        }
    }
}
```
