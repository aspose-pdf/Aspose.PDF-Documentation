---
title: "Java での PDF へのラインシェイプの追加"
linktitle: "ラインの追加"
type: docs
weight: 40
url: /ja/java/add-line/
description: "Java で PDF ファイルにラインシェイプやスタイル付きラインを描画する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用した PDF ファイルへのラインシェイプの描画"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF 文書にラインシェイプを追加する方法を示します。座標配列からラインを作成し、破線のスタイルと色を適用し、ページ全体にわたってラインを描画する方法をカバーしています。
---
## 破線の追加

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) をドキュメントに追加してください。
1. [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナを作成し、ページに追加してください。
1. [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) シェイプを作成し、座標を設定してください。
1. [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) を [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナに追加してください。
1. 出力 PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) に保存してください。

```java
public static void addLine(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(100.0, 400.0);
        page.getParagraphs().add(graph);

        Line line = new Line(new float[]{100, 100, 200, 100});
        line.getGraphInfo().setDashArray(new int[]{0, 1, 0});
        line.getGraphInfo().setDashPhase(1);
        graph.getShapes().addItem(line);

        document.save(outputFile.toString());
    }
}
```

## 色付きの点線または破線の追加

`addDottedDashedLine` は同じ座標とダッシュ設定を使用しますが、さらに `Color.getRed()` を適用します。

## ページ全体に線を描く

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) をドキュメントに追加してください。
1. [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナを作成し、ページに追加してください。
1. [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) シェイプを作成し、座標を設定してください。
1. [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) を [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナに追加してください。
1. 出力 PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) に保存してください。

```java
public static void drawLineAcrossPage(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        Graph graph = new Graph(page.getPageInfo().getWidth(), page.getPageInfo().getHeight());
        Line line = new Line(new float[]{
                (float) page.getRect().getLLX(),
                0,
                (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY()
        });
        graph.getShapes().addItem(line);
        page.getParagraphs().add(graph);

        document.save(outputFile.toString());
    }
}
```
