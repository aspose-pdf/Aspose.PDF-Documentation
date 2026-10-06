---
title: "Java での PDF への長方形シェイプの追加"
linktitle: "長方形の追加"
type: docs
weight: 50
url: /ja/java/add-rectangle/
description: "Java で PDF ファイルに長方形シェイプを描画および塗りつぶす方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用した PDF ファイルへの長方形シェイプの描画"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントに長方形シェイプを追加する方法を示します。アウトライン付き長方形、実色塗り、グラデーション塗り、アルファ透明度、および重なり合うシェイプの Z オーダー制御について説明します。
---
## 長方形のアウトラインの追加

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) をドキュメントに追加してください。
1. [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナを作成し、ページに追加してください。
1. [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) オブジェクトを作成し、ジオメトリを設定してください。
1. [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) を [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナに追加してください。
1. 出力 PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) として保存してください。

```java
public static void addRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 300.0);
        page.getParagraphs().add(graph);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Rectangle rectangle = new Rectangle(20, 20, 350, 250);
        graph.getShapes().addItem(rectangle);

        document.save(outputFile.toString());
    }
}
```

## 矩形の単色またはグラデーション色による塗りつぶし

矩形の例には次が含まれます：

- `createRectangleFilled` は、`Color.getRed()` を使用した単色塗りつぶし用です。
- `addDrawingWithGradientFill` は、`GradientAxialShading` 埋め込み用です。

## アルファ透明度の使用

`createRectangleWithAlphaColorChannel` は、`Color.fromArgb(...)` を使用して半透明の色を適用し、重なり合った矩形が表示されたままになるようにします。

## 矩形の Z 順序の制御

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) をドキュメントに追加してください。
1. 必要な [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) サイズを設定してください。
1. 構成した [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) シェイプを、必要な Z 順序で対象ページに追加してください。
1. 出力 PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) として保存してください。

```java
public static void controlZOrderOfRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(375, 300);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setTop(0);

        addRectangleToPage(page, 50, 40, 60, 40, Color.getRed(), 2);
        addRectangleToPage(page, 20, 20, 30, 30, Color.getBlue(), 1);
        addRectangleToPage(page, 40, 40, 60, 30, Color.getGreen(), 0);

        document.save(outputFile.toString());
    }
}
```
