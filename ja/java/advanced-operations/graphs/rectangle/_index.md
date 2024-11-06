---

title: PDFファイルに長方形オブジェクトを追加する  
linktitle: 長方形を追加  
type: docs  
weight: 50  
url: ja/java/add-rectangle/  
description: この記事では、Aspose.PDF for Javaを使用してPDFに長方形オブジェクトを作成する方法を説明します。  
lastmod: "2021-06-05"  
sitemap:  
    changefreq: "monthly"  
    priority: 0.7  
---
## 長方形オブジェクトを追加する

Aspose.PDF for Javaは、PDFドキュメントにグラフオブジェクト（例えば、グラフ、線、長方形など）を追加する機能をサポートしています。また、[Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Rectangle) オブジェクトを追加する機能を提供しており、特定の色で長方形オブジェクトを塗りつぶしたり、Zオーダーを制御したり、グラデーションカラーで塗りつぶしたりする機能もあります。

まず、長方形オブジェクトを作成する可能性を見てみましょう。

以下の手順に従ってください：

1. 新しいPDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) を作成する

1. PDFファイルのページコレクションに [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) を追加する

1. ページインスタンスの段落コレクションに[Text fragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)を追加

1. [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph)インスタンスを作成

1. [Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame)の境界を設定

1. Rectangleインスタンスを作成

1. Graphオブジェクトのシェイプコレクションに[Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Rectangle)オブジェクトを追加

1. Graphオブジェクトをページインスタンスの段落コレクションに追加

1. ページインスタンスの段落コレクションに[Text fragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)を追加

1. そして、PDFファイルを保存

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.BorderInfo;
import com.aspose.pdf.BorderSide;
import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;
import com.aspose.pdf.Point;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.drawing.*;

public class WorkingWithGraphs {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void ExampleRectangle() {

        // 新しいPDFドキュメントを作成
        Document pdfDocument = new Document();

        // PDFファイルのページコレクションにページを追加
        Page page = pdfDocument.getPages().add();

        // ページインスタンスの段落コレクションにテキストフラグメントを追加
        page.getParagraphs().add(new TextFragment("Graphオブジェクトの前のテキスト"));

        // Graphインスタンスを作成
        Graph graph = new Graph(400, 200);

        // Drawingオブジェクトの境界を設定
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getRed());
        graph.setBorder(borderInfo);

        // Rectangleインスタンスを作成
        Rectangle rect = new Rectangle(10, 10, 380, 180);

        // Graphオブジェクトのシェイプコレクションに長方形オブジェクトを追加
        graph.getShapes().add(rect);

        // ページインスタンスの段落コレクションにGraphオブジェクトを追加
        page.getParagraphs().add(graph);

        // ページインスタンスの段落コレクションにテキストフラグメントを追加
        page.getParagraphs().add(new TextFragment("Graphオブジェクトの後のテキスト"));

        // PDFファイルを保存
        pdfDocument.save(_dataDir + "CreateRectangle_out.pdf");
    }
```


![Create Rectangle](create_rectangle.png)

## 塗りつぶしされた長方形オブジェクトを作成する

Aspose.PDF for Javaは、特定の色で長方形オブジェクトを塗りつぶす機能も提供しています。

次のコードスニペットは、色で塗りつぶされた[Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle)オブジェクトを追加する方法を示しています。

```java
   public static void ExampleRectangleFilledSolidColor() {

        Document pdfDocument = new Document();

        // PDFファイルのページコレクションにページを追加
        Page page = pdfDocument.getPages().add();
        // Graphインスタンスを作成
        Graph graph = new Graph(100, 400);

        // ページインスタンスの段落コレクションにグラフオブジェクトを追加
        page.getParagraphs().add(graph);

        // Rectangleインスタンスを作成
        Rectangle rect = new Rectangle(100, 100, 200, 120);

        // Graphオブジェクトの塗りつぶしの色を指定
        rect.getGraphInfo().setFillColor(Color.getRed());

        // Graphオブジェクトの図形コレクションに長方形オブジェクトを追加
        graph.getShapes().add(rect);

        // PDFファイルを保存
        pdfDocument.save(_dataDir + "CreateFilledRectangle_out.pdf");
    }
```


矩形が単色で塗りつぶされた結果を見てください：

![塗りつぶされた長方形](fill_rectangle.png)

## グラデーション塗りつぶしでの描画の追加

Aspose.PDF for Java は、PDF ドキュメントにグラフオブジェクトを追加する機能をサポートしており、時にはグラフオブジェクトをグラデーションカラーで塗りつぶす必要があります。グラフオブジェクトをグラデーションカラーで塗りつぶすには、setPatterColorSpace を gradientAxialShading オブジェクトと共に設定する必要があります。

次のコードスニペットは、グラデーションカラーで塗りつぶされた [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) オブジェクトを追加する方法を示しています。

```java
   public static void ExampleRectangleFilledGradient() {

        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        Graph graph = new Graph(300, 300);
        page.getParagraphs().add(graph);
        Rectangle rect = new Rectangle(0, 0, 300, 300);
        graph.getShapes().add(rect);

        // グラフオブジェクトのグラデーション塗りつぶし色を指定して塗りつぶす
        Color gradientFill = new com.aspose.pdf.Color();
        rect.getGraphInfo().setFillColor(gradientFill);

        GradientAxialShading gradientAxialShading = new GradientAxialShading(Color.getRed(), Color.getBlue());

        gradientAxialShading.setStart(new Point(0, 0));
        gradientAxialShading.setEnd(new Point(300, 300));
        gradientFill.setPatternColorSpace(gradientAxialShading);

        // PDF ファイルを保存
        pdfDocument.save(_dataDir + "AddDrawingWithGradientFill_out.pdf");
    }
```


![Gradient Rectangle](gradient.png)

## アルファカラーチャネルで長方形を作成する

Aspose.PDF for Javaは、特定の色で長方形オブジェクトを塗りつぶすことをサポートしています。長方形オブジェクトは、透明な外観を与えるためにアルファカラーチャネルを持つこともできます。以下のコードスニペットは、アルファカラーチャネルを持つ[Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle)オブジェクトを追加する方法を示しています。

画像のピクセルは、色の値とともに不透明度に関する情報を保存できます。これにより、透明または半透明の領域を持つ画像を作成できます。

色を透明にする代わりに、各ピクセルはその不透明度に関する情報を保存します。この不透明度のデータはアルファチャンネルと呼ばれ、通常はピクセルのカラーチャンネルの後に保存されます。

コードスニペットでは、[com.aspose.pdf.Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/Color) の [fromArgb](https://reference.aspose.com/pdf/java/com.aspose.pdf/Color#fromArgb-int-int-int-) メソッドを使用しました。
 値を指定する必要があります。最初の3つは色の成分で、0から255の範囲で指定され、最後は不透明度（アルファチャンネル）で、0から1の範囲の小数で指定されます。

```java
    public static void ExampleRectangleAlphaChannelColor() {
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // Graphインスタンスを作成
        Graph graph = new Graph(100, 400);

        // 特定の寸法を持つ長方形オブジェクトを作成
        Rectangle rect1 = new Rectangle(100, 100, 200, 100);
        Color color1 = Color.fromArgb(128, 224, 0, 224);
        rect1.getGraphInfo().setFillColor(color1);
        // Graphインスタンスの図形コレクションに長方形オブジェクトを追加
        graph.getShapes().add(rect1);

        // 2つ目の長方形オブジェクトを作成
        Rectangle rect2 = new Rectangle(200, 150, 200, 100);
        Color color2 = Color.fromArgb(64, 0, 224, 224);
        rect2.getGraphInfo().setFillColor(color2);
        graph.getShapes().add(rect2);

        // ページオブジェクトの段落コレクションにGraphインスタンスを追加
        page.getParagraphs().add(graph);

        // PDFファイルを保存
        pdfDocument.save(_dataDir + "CreateRectangleWithAlphaColor_out.pdf");
    }
```

![Rectangle Alpha Channel Color](rectangle_color.png)

## 長方形のZオーダーの制御

Aspose.PDF for Javaは、PDFドキュメントにグラフオブジェクト（グラフ、ライン、長方形など）を追加する機能をサポートしています。PDFファイル内に同じオブジェクトのインスタンスを複数追加する場合、Zオーダーを指定することでその描画を制御できます。Zオーダーは、オブジェクトを互いに重ねて描画する必要がある場合にも使用されます。

以下のコードスニペットは、[Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) オブジェクトを互いに重ねて描画する手順を示しています。

```java
   public static void Controlling_Z_Order() {

        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // 色が赤で、Zオーダーが0、特定のサイズの新しい長方形を作成
        AddRectangle(page, 50, 40, 60, 40, Color.getRed(), 2);
        // 色が青で、Zオーダーが0、特定のサイズの新しい長方形を作成
        AddRectangle(page, 20, 20, 30, 30, Color.getBlue(), 1);
        // 色が緑で、Zオーダーが0、特定のサイズの新しい長方形を作成
        AddRectangle(page, 40, 40, 60, 30, Color.getGreen(), 0);

        // 結果のPDFファイルを保存
        pdfDocument.save(_dataDir + "ControlRectangleZOrder_out.pdf");

    }
```


![Zオーダーの制御](control.png)