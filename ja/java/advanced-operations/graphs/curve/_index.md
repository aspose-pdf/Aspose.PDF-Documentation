---
title: PDFファイルに曲線オブジェクトを追加する
linktitle: 曲線を追加
type: docs
weight: 30
url: /ja/java/add-curve/
description: この記事では、Aspose.PDF for Javaを使用してPDFに曲線オブジェクトを作成する方法について説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 曲線オブジェクトを追加する

グラフ[Curve](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Curve)は、各線が通常の二重点で他の3つと交差する射影線の連結結合です。

Aspose.PDF for Javaは、グラフにベジエ曲線を使用する方法を示しています。ベジエ曲線は、コンピュータグラフィックスで滑らかな曲線をモデル化するために広く使用されています。曲線は制御点の凸包内に完全に含まれており、点はグラフィカルに表示され、直感的に曲線を操作するために使用できます。曲線全体は、四つの与えられた点（その凸包）のコーナーを持つ四辺形内に含まれています。

この記事では、PDFドキュメント内で作成できる単純なグラフ曲線と塗りつぶされた曲線について調査します。

以下の手順に従ってください:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) インスタンスを作成します。

1. 特定の寸法を持つ [Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) を作成します。

1. Drawing オブジェクトに [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) を設定します。

1. ページの段落コレクションに [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) オブジェクトを追加します。

1. PDFファイルを保存します。

```java
    public static void ExampleCurve() {
        // Document インスタンスを作成します
        Document pdfDocument = new Document();
        // PDFファイルのページコレクションにページを追加します
        Page page = pdfDocument.getPages().add();

        // 特定の寸法を持つ Drawing オブジェクトを作成します
        Graph graph = new Graph(400, 200);
        // Drawing オブジェクトにボーダーを設定します
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});

        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // ページの段落コレクションに Graph オブジェクトを追加します
        page.getParagraphs().add(graph);

        // PDFファイルを保存します
        pdfDocument.save(_dataDir + "DrawingCurve1_out.pdf");
    }
```


次の画像は、私たちのコードスニペットで実行された結果を示しています。

![Drawing Curve](drawing_curve.png)

## 塗りつぶされた曲線オブジェクトを作成する

この例は、色で塗りつぶされた曲線オブジェクトを追加する方法を示しています。

```java
    public static void ExampleFilledCurve() {
        // Documentインスタンスを作成する
        Document pdfDocument = new Document();
        // PDFファイルのページコレクションにページを追加する
        Page page = pdfDocument.getPages().add();

        // 特定の寸法でDrawingオブジェクトを作成する
        Graph graph = new Graph(400, 200);
        // Drawingオブジェクトに境界線を設定する
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // ページの段落コレクションにGraphオブジェクトを追加する
        page.getParagraphs().add(graph);

        // PDFファイルを保存する
        pdfDocument.save(_dataDir + "DrawingCurve2_out.pdf");
    }
```


Look at the result of adding a filled Curve:

![塗りつぶされた曲線](filled_curve.png)