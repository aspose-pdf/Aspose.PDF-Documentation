---
title: PDFファイルに長方形オブジェクトを追加
linktitle: 長方形を追加
type: docs
weight: 50
url: ja/cpp/add-rectangle/
description: Aspose.PDF for C++を使用してPDFに長方形オブジェクトを作成する方法を説明します。
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 長方形オブジェクトを追加

Aspose.PDF for C++は、グラフオブジェクト（例えばグラフ、線、長方形など）をPDFドキュメントに追加する機能をサポートしています。また、特定の色で長方形オブジェクトを塗りつぶしたり、Zオーダーを制御したり、グラデーションカラーで塗りつぶしたりする機能も提供しています。

まず、長方形オブジェクトを作成する可能性を見てみましょう。

以下の手順に従ってください：

1. 新しいPDF [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) を作成します

1. PDFファイルのページコレクションに [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) を追加します

1.  [Text fragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) をページインスタンスの段落コレクションに追加

1. [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/) インスタンスを作成

1. [Drawing object](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) の境界線を設定

1. Rectangle インスタンスを作成

1. [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) オブジェクトを Graph オブジェクトのシェイプコレクションに追加

1. グラフオブジェクトをページインスタンスの段落コレクションに追加

1. [Text fragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) をページインスタンスの段落コレクションに追加

1. そして PDF ファイルを保存

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // Rectangle オブジェクトに指定されたのと同じ寸法でグラフオブジェクトを作成
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // グラフインスタンスの位置を変更できますか
                IsChangePosition = false,
                // グラフインスタンスの左座標位置を設定
                Left = x,
                // グラフオブジェクトの上座標位置を設定
                Top = y
            };
            // "graph" 内に長方形を追加
            Rectangle rect = new Rectangle(0, 0, width, height);
            // 長方形の塗りつぶし色を設定
            rect.GraphInfo.FillColor = color;
            // グラフオブジェクトの色
            rect.GraphInfo.Color = color;
            // 長方形をグラフインスタンスのシェイプコレクションに追加
            graph.Shapes.Add(rect);
            // 長方形オブジェクトの Z-Index を設定
            graph.ZIndex = zindex;
            // グラフをページオブジェクトの段落コレクションに追加
            page.Paragraphs.Add(graph);
        }
```
![Create Rectangle](create_rectangle.png)

## 塗りつぶしの長方形オブジェクトを作成する

Aspose.PDF for C++ は、特定の色で長方形オブジェクトを塗りつぶす機能も提供しています。

次のコードスニペットは、色で塗りつぶされた[Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/)オブジェクトを追加する方法を示しています。

```csharp
    {
        private const string _dataDir = "C:\\Samples\\";
        public static void RectangleFilled()
        {
            // Document インスタンスを作成
            var doc = new Document();

            // PDF ファイルの pages コレクションにページを追加
            var page = doc.Pages.Add();
            // Graph インスタンスを作成
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // ページインスタンスの paragraphs コレクションに graph オブジェクトを追加
            page.Paragraphs.Add(graph);

            // Rectangle インスタンスを作成
            var rect = new Rectangle(100, 100, 200, 120);

            // Graph オブジェクトの塗りつぶし色を指定
            rect.GraphInfo.FillColor = Color.Red;

            // Graph オブジェクトの shapes コレクションに rectangle オブジェクトを追加
            graph.Shapes.Add(rect);

            // PDF ファイルを保存
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

長方形の塗りつぶしの結果を見てください：

![塗りつぶされた長方形](fill_rectangle.png)

## グラデーション塗りつぶしを使った描画の追加

Aspose.PDF for C++ は、PDFドキュメントにグラフオブジェクトを追加する機能をサポートしており、時にはグラフオブジェクトをグラデーションカラーで塗りつぶす必要があります。グラフオブジェクトをグラデーションカラーで塗りつぶすには、次のようにgradientAxialShadingオブジェクトでsetPatterColorSpaceを設定する必要があります。

次のコードスニペットは、グラデーションカラーで塗りつぶされた[Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/)オブジェクトを追加する方法を示しています。

```csharp
 public static void CreateFilledRectangletGradientFill()
        {
            // Documentインスタンスを作成
            var doc = new Document();

            // PDFファイルのページコレクションにページを追加
            var page = doc.Pages.Add();
            // Graphインスタンスを作成
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // ページインスタンスの段落コレクションにグラフオブジェクトを追加
            page.Paragraphs.Add(graph);
            // Rectangleインスタンスを作成
            var rect = new Rectangle(0, 0, 300, 300);
            // グラフオブジェクトの塗りつぶし色を指定
            var gradientColor = new Color();
            var gradientSettings = new GradientAxialShading(Color.Red, Color.Blue)
            {
                Start = new Point(0, 0),
                End = new Point(350, 350)
            };
            gradientColor.PatternColorSpace = gradientSettings;
            rect.GraphInfo.FillColor = gradientColor;

            // Graphオブジェクトのシェイプコレクションに長方形オブジェクトを追加
            graph.Shapes.Add(rect);

            // PDFファイルを保存
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

![Gradient Rectangle](gradient.png)

## アルファカラーチャンネルを持つ長方形の作成

Aspose.PDF for C+++ は、特定の色で長方形オブジェクトを塗りつぶすことをサポートしています。長方形オブジェクトは、透明な外観を与えるためにアルファカラーチャンネルを持つこともできます。次のコードスニペットは、アルファカラーチャンネルを持つ[長方形](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/)オブジェクトを追加する方法を示しています。

画像のピクセルは、色の値と共に不透明度に関する情報を保存できます。これにより、透明または半透明の領域を持つ画像を作成することができます。

色を透明にする代わりに、各ピクセルはそれがどれだけ不透明であるかの情報を保存します。この不透明度のデータはアルファチャンネルと呼ばれ、通常はピクセルの色チャンネルの後に保存されます。

```csharp
     public static void RectangleFilled_AlphaChannel()
        {
            // Document インスタンスを作成
            var doc = new Document();

            // PDF ファイルのページコレクションにページを追加
            var page = doc.Pages.Add();
            // Graph インスタンスを作成
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);
            // ページインスタンスの段落コレクションにグラフオブジェクトを追加
            page.Paragraphs.Add(graph);
            // Rectangle インスタンスを作成
            var rect = new Rectangle(100, 100, 200, 120);
            // Graph オブジェクトの塗りつぶし色を指定
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // Graph オブジェクトの形状コレクションに長方形オブジェクトを追加
            graph.Shapes.Add(rect);

            // 2番目の長方形オブジェクトを作成
            var rect1 = new Rectangle(200, 150, 200, 100);
            rect1.GraphInfo.FillColor = Color.FromArgb(160, 120, 0, 120);
            graph.Shapes.Add(rect1);

            // ページオブジェクトの段落コレクションにグラフインスタンスを追加
            page.Paragraphs.Add(graph);

            // PDF ファイルを保存
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

![Rectangle Alpha Channel Color](rectangle_color.png)

## 長方形のZオーダーを制御する

Aspose.PDF for C++は、PDFドキュメントにグラフオブジェクト（例えばグラフ、線、長方形など）を追加する機能をサポートしています。PDFファイル内に同じオブジェクトのインスタンスを複数追加する場合、Zオーダーを指定することでそのレンダリングを制御できます。Zオーダーは、オブジェクトを互いに重ねてレンダリングする必要がある場合にも使用されます。

次のコードスニペットは、[Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) オブジェクトを互いに重ねてレンダリングする手順を示しています。

```csharp
 public static void AddRectangleZOrder()
        {
            // Documentクラスオブジェクトをインスタンス化
            Document doc1 = new Document();
            /// PDFファイルのページコレクションにページを追加
            Page page1 = doc1.Pages.Add();
            // PDFページのサイズを設定
            page1.SetPageSize(375, 300);
            // ページオブジェクトの左マージンを0に設定
            page1.PageInfo.Margin.Left = 0;
            // ページオブジェクトの上マージンを0に設定
            page1.PageInfo.Margin.Top = 0;
            // 色を赤、Zオーダーを0、特定の寸法の新しい長方形を作成
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // 色を青、Zオーダーを0、特定の寸法の新しい長方形を作成
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // 色を緑、Zオーダーを0、特定の寸法の新しい長方形を作成
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // 結果のPDFファイルを保存
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```


![Zオーダーの制御](control.png)
```