---
title: "Java での PDF への円弧形状の追加"
linktitle: "円弧の追加"
type: docs
weight: 10
url: /ja/java/add-arc/
description: "Java で PDF ファイルに円弧形状を描画および塗りつぶす方法を学習します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用した PDF ファイルへの円弧形状の描画"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF ドキュメントに円弧形状を追加する方法を説明します。異なる色の輪郭付き円弧を複数描画する方法や、円弧と閉じる線を組み合わせて塗りつぶし円弧セグメントを作成する方法をカバーしています。"
---
Aspose.PDF for Java では、`Graph` クラスと `Arc`、`Line` などのシェイプオブジェクトを組み合わせてベクトルグラフィックを描画します。

## 弧のアウトラインの追加

1. 新しい PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) として作成してください。
1. ドキュメントに [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加してください。
1. [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナを作成し、ページに追加してください。
1. [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) オブジェクトを作成し、ジオメトリを設定してください。
1. [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) を [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナに追加してください。
1. 例で必要な形状プロパティを設定し、[Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) を含めてください。
1. 出力 PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) として保存してください。

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

1. 新しい PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) として作成してください。
1. ドキュメントに [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加してください。
1. [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナを作成し、ページに追加してください。
1. [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) 形状を作成し、座標を設定してください。
1. [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) オブジェクトを作成し、ジオメトリを設定してください。
1. [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) および [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) を [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナに追加してください。
1. 出力 PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) として保存してください。

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
