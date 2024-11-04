---
title: PDFファイルに円オブジェクトを追加する
linktitle: 円を追加
type: docs
weight: 20
url: /java/add-circle/
description: この記事では、Aspose.PDF for Javaを使用してPDFに円オブジェクトを作成する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 円オブジェクトを追加する

棒グラフのように、円グラフは複数の異なるカテゴリのデータを表示するために使用できます。ただし、棒グラフとは異なり、円グラフは全体を構成するすべてのカテゴリのデータがある場合にのみ使用できます。それでは、Aspose.PDF for Javaを使用して[Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Circle)オブジェクトを追加する方法を見てみましょう。

以下の手順に従ってください：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)インスタンスを作成する

1. 一定の寸法で[Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame)を作成する

1. [Drawing](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) オブジェクトに境界線を設定する

1. ページの段落コレクションに[Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph)オブジェクトを追加する

1. PDFファイルを保存する

```java
public static void ExampleCircle() {
        // Document インスタンスを作成する
        Document pdfDocument = new Document();
        // PDFファイルのページコレクションにページを追加する
        Page page = pdfDocument.getPages().add();

        // 特定の寸法で Drawing オブジェクトを作成する
        Graph graph = new Graph(400, 200);
        // Drawing オブジェクトに境界線を設定する
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);

        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(circle);

        // ページの段落コレクションに Graph オブジェクトを追加する
        page.getParagraphs().add(graph);

        // PDFファイルを保存する
        pdfDocument.save(_dataDir + "DrawingCircle1_out.pdf");
    }
```


私たちが描いた円は次のように見えます：

![Drawing Circle](drawing_circle.png)

## 塗りつぶされた円オブジェクトの作成

この例は、色で塗りつぶされた円オブジェクトを追加する方法を示しています。

```java

    public static void ExampleFilledCircle() {
        // Documentインスタンスを作成
        Document pdfDocument = new Document();
        // PDFファイルのページコレクションにページを追加
        Page page = pdfDocument.getPages().add();

        // 特定の寸法でDrawingオブジェクトを作成
        Graph graph = new Graph(400, 200);
        // Drawingオブジェクトの境界を設定
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());       
        circle.getGraphInfo().setFillColor(Color.getGreenYellow());

        graph.getShapes().add(circle);

        // ページの段落コレクションにGraphオブジェクトを追加
        page.getParagraphs().add(graph);

        // PDFファイルを保存
        pdfDocument.save(_dataDir + "DrawingCircle2_out.pdf");
    }
```


Let's see the result of adding a filled Circle:

![塗りつぶされた円](filled_circle.png)