---
title: "Java での PDFに長方形シェイプの追加"
linktitle: "長方形の追加"
type: docs
weight: 50
url: /ja/java/add-rectangle/
description: JavaでPDFファイルに長方形シェイプを描画および塗りつぶす方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaを使用してPDFファイルに長方形シェイプを描画する
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントに長方形シェイプを追加する方法を示します。アウトライン付き長方形、実色塗り、グラデーション塗り、アルファ透明度、および重なり合うシェイプの Z オーダー制御について説明します。
---
## 長方形のアウトラインの追加

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. 追加する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ドキュメントへ。
1. 作成する [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナを作成し、ページに追加してください。
1. 作成 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) 形状を作成し、ジオメトリを設定してください。
1. 追加 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) 〜へ [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナ。
1. 出力 PDF を保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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

## 矩形を単色またはグラデーションの色で塗りつぶす

矩形の例には次が含まれます：

- `createRectangleFilled` 実体塗りつぶし用 `Color.getRed()`
- `addDrawingWithGradientFill` のための `GradientAxialShading` 埋める

## アルファ透明度の使用

`createRectangleWithAlphaColorChannel` 半透明の色を適用する `Color.fromArgb(...)` その結果、重なり合った矩形は表示されたままです。

## 矩形の Z 順序を制御する

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. 追加する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ドキュメントへ。
1. 必要なものを設定する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) サイズ。
1. 構成されたものを追加する [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) 必要な Z 順序で対象ページにシェイプを追加してください。
1. 出力 PDF を保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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
