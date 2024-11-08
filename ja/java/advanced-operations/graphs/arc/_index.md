---
title: PDFファイルにアークオブジェクトを追加
linktitle: アークを追加
type: docs
weight: 10
url: /ja/java/add-arc/
description: この記事では、Aspose.PDF for Javaを使用してPDFにアークオブジェクトを作成する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## アークオブジェクトを追加

Aspose.PDF for Javaは、PDFドキュメントにグラフオブジェクト（例えばグラフ、ライン、長方形など）を追加する機能をサポートしています。また、特定の色でアークオブジェクトを塗りつぶす機能も提供しています。

以下の手順に従ってください：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) インスタンスを作成

1. 特定の寸法で [Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) を作成

1. Drawingオブジェクトに [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) を設定

1. ページの段落コレクションに [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) オブジェクトを追加

1. PDFファイルを保存

以下のコードスニペットは、[Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Arc) オブジェクトを追加する方法を示しています。

```java
    public static void ExampleArc() {
        // Documentインスタンスを作成
        Document pdfDocument = new Document();
        // PDFファイルのページコレクションにページを追加
        Page page = pdfDocument.getPages().add();

        // 特定の寸法でDrawingオブジェクトを作成
        Graph graph = new Graph(400, 400);
        // Drawingオブジェクトに境界線を設定
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(arc1);

        Arc arc2 = new Arc(100, 100, 90, 70, 180);
        arc2.getGraphInfo().setColor(Color.getDarkBlue());
        graph.getShapes().add(arc2);

        Arc arc3 = new Arc(100, 100, 85, 120, 210);
        arc3.getGraphInfo().setColor(Color.getRed());
        graph.getShapes().add(arc3);

        // Graphオブジェクトをページの段落コレクションに追加
        page.getParagraphs().add(graph);

        // PDFファイルを保存
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


## 塗りつぶされた弧オブジェクトを作成

次の例は、色で塗りつぶされた特定の寸法を持つ弧オブジェクトを追加する方法を示します。

```java
    public static void ExampleFilledArc() {
        // Documentインスタンスを作成
        Document pdfDocument = new Document();
        // PDFファイルのページコレクションにページを追加
        Page page = pdfDocument.getPages().add();

        // 特定の寸法を持つDrawingオブジェクトを作成
        Graph graph = new Graph(400, 400);
        // Drawingオブジェクトの境界を設定
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(arc);

        Line line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(line);

        // ページの段落コレクションにGraphオブジェクトを追加
        page.getParagraphs().add(graph);

        // PDFファイルを保存
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


Let's see the result of adding a filled Arс:

![塗りつぶされたアーク](filled_arc.png)