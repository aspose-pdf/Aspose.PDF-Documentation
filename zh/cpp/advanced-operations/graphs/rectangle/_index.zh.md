---
title: 添加矩形对象到PDF文件
linktitle: 添加矩形
type: docs
weight: 50
url: /cpp/add-rectangle/
description: 本文解释了如何使用Aspose.PDF for C++在PDF中创建一个矩形对象。
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 添加矩形对象

Aspose.PDF for C++支持将图形对象（例如图形、线条、矩形等）添加到PDF文档中。您还可以利用添加[矩形](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/)对象的功能，该功能还提供用特定颜色填充矩形对象、控制Z顺序、添加渐变色填充等功能。

首先，让我们看看创建矩形对象的可能性。

请按照以下步骤操作：

1. 创建一个新的PDF [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/)

1. 向PDF文件的页面集合中添加[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/)

1. 将[文本片段](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/)添加到页面实例的段落集合中

1. 创建[图形](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/)实例

1. 为[绘图对象](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing)设置边框

1. 创建矩形实例

1. 将[矩形](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/)对象添加到图形对象的形状集合中

1. 将图形对象添加到页面实例的段落集合中

1. 将[文本片段](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/)添加到页面实例的段落集合中

1. 并保存您的PDF文件

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // 创建与矩形对象指定尺寸相同的图形对象
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // 我们能否改变图形实例的位置
                IsChangePosition = false,
                // 为图形实例设置左侧坐标位置
                Left = x,
                // 为图形对象设置顶部坐标位置
                Top = y
            };
            // 在“图形”中添加一个矩形
            Rectangle rect = new Rectangle(0, 0, width, height);
            // 设置矩形填充颜色
            rect.GraphInfo.FillColor = color;
            // 图形对象的颜色
            rect.GraphInfo.Color = color;
            // 将矩形添加到图形实例的形状集合中
            graph.Shapes.Add(rect);
            // 设置矩形对象的Z指数
            graph.ZIndex = zindex;
            // 将图形添加到页面对象的段落集合中
            page.Paragraphs.Add(graph);
        }
```
![Create Rectangle](create_rectangle.png)

## 创建填充矩形对象

Aspose.PDF for C++ 还提供了用特定颜色填充矩形对象的功能。

下面的代码片段展示了如何添加一个用颜色填充的[矩形](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/)对象。

```csharp
    {
        private const string _dataDir = "C:\\Samples\\";
        public static void RectangleFilled()
        {
            // 创建文档实例
            var doc = new Document();

            // 将页面添加到 PDF 文件的页面集合中
            var page = doc.Pages.Add();
            // 创建图形实例
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // 将图形对象添加到页面实例的段落集合中
            page.Paragraphs.Add(graph);

            // 创建矩形实例
            var rect = new Rectangle(100, 100, 200, 120);

            // 为图形对象指定填充颜色
            rect.GraphInfo.FillColor = Color.Red;

            // 将矩形对象添加到图形对象的形状集合中
            graph.Shapes.Add(rect);

            // 保存 PDF 文件
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

看看填充纯色的矩形结果：

![填充矩形](fill_rectangle.png)

## 添加渐变填充的绘图

Aspose.PDF for C++ 支持将图形对象添加到 PDF 文档的功能，有时需要用渐变色填充图形对象。要用渐变色填充图形对象，我们需要设置 setPatterColorSpace 与 gradientAxialShading 对象，如下所示。

以下代码片段展示了如何添加一个用渐变色填充的[矩形](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/)对象。

```csharp
 public static void CreateFilledRectangletGradientFill()
        {
            // 创建文档实例
            var doc = new Document();

            // 向 PDF 文件的页面集合添加页面
            var page = doc.Pages.Add();
            // 创建图形实例
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // 将图形对象添加到页面实例的段落集合
            page.Paragraphs.Add(graph);
            // 创建矩形实例
            var rect = new Rectangle(0, 0, 300, 300);
            // 为图形对象指定填充颜色
            var gradientColor = new Color();
            var gradientSettings = new GradientAxialShading(Color.Red, Color.Blue)
            {
                Start = new Point(0, 0),
                End = new Point(350, 350)
            };
            gradientColor.PatternColorSpace = gradientSettings;
            rect.GraphInfo.FillColor = gradientColor;

            // 将矩形对象添加到图形对象的形状集合
            graph.Shapes.Add(rect);

            // 保存 PDF 文件
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

![渐变矩形](gradient.png)

## 创建带有 Alpha 颜色通道的矩形

Aspose.PDF for C+++ 支持用特定颜色填充矩形对象。矩形对象还可以具有 Alpha 颜色通道以提供透明外观。以下代码段展示了如何添加具有 Alpha 颜色通道的 [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) 对象。

图像的像素可以存储关于其不透明度的信息以及颜色值。这允许创建具有透明或半透明区域的图像。

每个像素存储其不透明度的信息，而不是使颜色透明。这种不透明度数据称为 alpha 通道，通常存储在像素的颜色通道之后。

```csharp
     public static void RectangleFilled_AlphaChannel()
        {
            // 创建文档实例
            var doc = new Document();

            // 向 PDF 文件的页面集合中添加页面
            var page = doc.Pages.Add();
            // 创建图形实例
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);
            // 将图形对象添加到页面实例的段落集合中
            page.Paragraphs.Add(graph);
            // 创建矩形实例
            var rect = new Rectangle(100, 100, 200, 120);
            // 指定图形对象的填充颜色
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // 将矩形对象添加到图形对象的形状集合中
            graph.Shapes.Add(rect);

            // 创建第二个矩形对象
            var rect1 = new Rectangle(200, 150, 200, 100);
            rect1.GraphInfo.FillColor = Color.FromArgb(160, 120, 0, 120);
            graph.Shapes.Add(rect1);

            // 将图形实例添加到页面对象的段落集合中
            page.Paragraphs.Add(graph);

            // 保存 PDF 文件
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

![矩形 Alpha 通道颜色](rectangle_color.png)

## 控制矩形的 Z-Order

Aspose.PDF for C++ 支持将图形对象（例如图形、线条、矩形等）添加到 PDF 文档的功能。当在 PDF 文件中添加多个相同对象的实例时，我们可以通过指定 Z-Order 来控制它们的渲染。当我们需要将对象相互叠加显示时，也会使用 Z-Order。

以下代码片段展示了如何在相互叠加的情况下渲染[矩形](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/)对象的步骤。

```csharp
 public static void AddRectangleZOrder()
        {
            // 实例化 Document 类对象
            Document doc1 = new Document();
            /// 向 PDF 文件的页面集合中添加页面
            Page page1 = doc1.Pages.Add();
            // 设置 PDF 页面大小
            page1.SetPageSize(375, 300);
            // 将页面对象的左边距设置为 0
            page1.PageInfo.Margin.Left = 0;
            // 将页面对象的上边距设置为 0
            page1.PageInfo.Margin.Top = 0;
            // 创建一个新的矩形，颜色为红色，Z-Order 为 0，并具有特定尺寸
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // 创建一个新的矩形，颜色为蓝色，Z-Order 为 0，并具有特定尺寸
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // 创建一个新的矩形，颜色为绿色，Z-Order 为 0，并具有特定尺寸
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // 保存生成的 PDF 文件
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```

![控制 Z 轴顺序](control.png)