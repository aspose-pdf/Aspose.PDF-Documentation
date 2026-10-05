---
title: JavaでPDFページをトリミング
linktitle: PDFページのトリミング
type: docs
weight: 70
url: /ja/java/crop-pages/
description: JavaでPDFページをトリミングし、crop、trim、bleed、mediaボックスを調整する方法を学びます。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Javaを使用してPDFファイルのページをトリミングし、ページボックスの調整"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF ページをトリミングする方法を説明します。crop、trim、art、bleed ボックスに新しいトリム矩形を割り当てる方法と、検出された画像コンテンツに基づいてページを自動的にトリミングする方法について説明します。"
---
Aspose.PDF for Java は、明示的なボックス座標または検出されたコンテンツに基づいてページをトリミングできます。

## ページボックスの設定によるページのトリミング

メインページボックスに同じトリミング領域を適用する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 新しいトリミング用の [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) を作成してください。
1. 矩形をトリミング関連のページボックスに適用し、ドキュメントを保存してください。

```java
public static void cropPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520, true);
        document.getPages().get_Item(1).setCropBox(newBox);
        document.getPages().get_Item(1).setTrimBox(newBox);
        document.getPages().get_Item(1).setArtBox(newBox);
        document.getPages().get_Item(1).setBleedBox(newBox);
        document.save(outputFile.toString());
    }
}
```

## 検出したコンテンツに合わせたページのトリミング

ページ上で最初に検出された画像からトリミング領域を取得する場合に、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) を使用して画像配置を検出してください。
1. 画像の矩形が見つかった場合は、クロップボックスをその矩形に設定し、ドキュメントを保存してください。

```java
public static void cropPageByContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        if (absorber.getImagePlacements().size() > 0) {
            document.getPages().get_Item(1).setCropBox(absorber.getImagePlacements().get_Item(1).getRectangle());
        } else {
            System.out.println("No images found on the first page");
        }
        document.save(outputFile.toString());
    }
}
```
