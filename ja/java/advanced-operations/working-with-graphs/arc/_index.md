---
title: "Java での PDF に円弧形状の追加"
linktitle: "円弧の追加"
type: docs
weight: 10
url: /ja/java/add-arc/
description: Java で PDF ファイルに円弧形状を描画および塗りつぶす方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して PDF ファイルに円弧形状を描画する
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントに円弧形状を追加する方法を示します。異なる色の輪郭付き円弧を複数描画し、円弧と閉じる線を組み合わせて塗りつぶし円弧セグメントを作成する方法をカバーしています。
---
Aspose.PDF for Java を使用します `Graph` 次のようなシェイプオブジェクトと共に `Arc` そして `Line` ベクトルグラフィックをレンダリングするために。

## 弧のアウトラインの追加

1. 新しいPDFを作成 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 追加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ドキュメントへ。
1. 作成する [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナをページに追加してください。
1. 作成する [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) 形状を作成し、ジオメトリを構成してください。
1. 追加する [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) へ [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナ。
1. 例で必要な形状プロパティを設定し、次のものを含む [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/)。
1. 出力PDFを保存する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void addArc(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

完全な例では、異なる半径、角度、色を持つ3つの弧を同じグラフに追加します。

## 塗りつぶされた円弧セグメントの追加

1. 新しいPDFを作成 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 追加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ドキュメントへ。
1. 作成する [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナをページに追加してください。
1. 作成する [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) 形状を作成し、座標を設定してください。
1. 作成する [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) 形状を作成し、ジオメトリを構成してください。
1. 追加する [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) そして [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) へ [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナ。
1. 出力PDFを保存する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void addArcFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc);

        Line line = new Line(new float[]{195, 100, 100, 100, 100, 195});
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(line);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
