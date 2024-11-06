---
title: PDFファイルに線オブジェクトを追加する
linktitle: 線を追加
type: docs
weight: 40
url: ja/java/add-line/
description: この記事では、Aspose.PDF for Javaを使用してPDFに線オブジェクトを作成する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 線オブジェクトを追加する

Aspose.PDF for Javaは、PDFドキュメントにグラフオブジェクト（例えばグラフ、線、長方形など）を追加する機能をサポートしています。また、[Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Line)オブジェクトを追加し、ダッシュパターン、色、その他のフォーマットを指定することもできます。

以下の手順に従います：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) インスタンスを作成します。

1. PDFファイルのページコレクションに[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)を追加します。

1. [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) インスタンスを作成します。

1. ページインスタンスの段落コレクションにGraphオブジェクトを追加します。

1. [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) インスタンスを作成します。

1. 線幅を設定します。

1. [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) オブジェクトを Graph オブジェクトの形状コレクションに追加します。

1. PDFファイルを保存します。

次のコードスニペットは、色で塗りつぶされた [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) オブジェクトを追加する方法を示しています。

```java
 public static void ExampleLine() {
        // Document インスタンスを作成します
        Document pdfDocument = new Document();
        // PDF ファイルのページ コレクションにページを追加します
        Page page = pdfDocument.getPages().add();
        // Graph インスタンスを作成します
        Graph graph = new Graph(100, 400);

        // グラフ オブジェクトをページ インスタンスの段落コレクションに追加します
        page.getParagraphs().add(graph);

        // Rectangle インスタンスを作成します
        Line line = new Line(new float[] { 100, 100, 200, 100 });
        
        line.getGraphInfo().setLineWidth(5);
        
        // Rectangle オブジェクトを Graph オブジェクトの形状コレクションに追加します
        graph.getShapes().add(line);

        // PDF ファイルを保存します
        pdfDocument.save(_dataDir + "LineAdded.pdf");
    }
```


![Add Line](add_line.png)

## PDFドキュメントに点線を追加する方法

```java
public static void ExampleDashedLine() {
        // Documentインスタンスを作成
        Document pdfDocument = new Document();
        // PDFファイルのページコレクションにページを追加
        Page page = pdfDocument.getPages().add();

        // 特定の寸法でDrawingオブジェクトを作成
        Graph canvas = new Graph(100, 400);
        // ページインスタンスの段落コレクションにDrawingオブジェクトを追加
        page.getParagraphs().add(canvas);

        // Lineオブジェクトを作成
        Line line = new Line(new float[] { 100, 100, 200, 100 });

        // Lineオブジェクトの色を設定
        line.getGraphInfo().setColor(Color.getRed());
        // Lineオブジェクトのダッシュ配列を指定
        line.getGraphInfo().setDashArray(new int[] { 0, 1, 0 });
        // Lineインスタンスのダッシュフェーズを設定
        line.getGraphInfo().setDashPhase(1);
        // Drawingオブジェクトの図形コレクションに線を追加
        canvas.getShapes().add(line);
        // PDFドキュメントを保存
        pdfDocument.save(_dataDir + "DashLength_out.pdf");
    }
```


結果を確認しましょう：

![Dashed Line](dash_line.png)

## ページ全体に線を引く

ラインオブジェクトを使用して、左下から右上の角まで、左上の角から右下の角までのクロスを描くこともできます。

この要件を達成するために、以下のコードスニペットをご覧ください。

```java
    public static void ExampleLineAcrossPage() {
        // Documentインスタンスを作成
        Document pdfDocument = new Document();
        // PDFファイルのページコレクションにページを追加
        Page page = pdfDocument.getPages().add();
        // 全ての側面のページマージンを0に設定

        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        // ページの幅と高さに等しいGraphオブジェクトを作成
        Graph graph = new Graph((float) page.getPageInfo().getWidth(), (float) page.getPageInfo().getHeight());

        // 下左からページの右上の角までの最初のラインオブジェクトを作成
        Line line = new Line(new float[] { (float) page.getRect().getLLX(), 0, (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY() });

        // Graphオブジェクトのシェイプコレクションにラインを追加
        graph.getShapes().add(line);
        // ページの左上の角から右下の角まで線を引く
        Line line2 = new Line(new float[] { 0, (float) page.getRect().getURY(), (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getLLX() });

        // Graphオブジェクトのシェイプコレクションにラインを追加
        graph.getShapes().add(line2);
        // ページの段落コレクションにGraphオブジェクトを追加
        page.getParagraphs().add(graph);

        // PDFファイルを保存
        pdfDocument.save(_dataDir + "DrawingLine_out.pdf");
    }
```


![線を描く](draw_line.png)