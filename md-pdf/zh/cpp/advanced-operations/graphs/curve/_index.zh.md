---
title: 将曲线对象添加到PDF文件
linktitle: 添加曲线
type: docs
weight: 30
url: /cpp/add-curve/
description: 本文解释了如何使用Aspose.PDF for C++在PDF中创建曲线对象。
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 添加曲线对象

图形[曲线](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.curve/)是射影线的连接联合，每条线在普通双点处与另外三条线相交。

Bézier曲线广泛用于计算机图形学中以建模平滑曲线。曲线完全包含在其控制点的凸包内，控制点可以以图形方式显示并用于直观地操纵曲线。
整个曲线包含在由四个给定点（它们的凸包）构成的四边形中。

在本文中，我们将研究简单图形曲线和填充曲线，您可以在PDF文档中创建这些曲线。

请按照以下步骤操作：

1. 创建 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 实例

1. 使用特定尺寸创建 [Drawing object](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing)

1. 为 Drawing object 设置 [Border](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd)

1. 将 [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) 对象添加到页面的段落集合中

1. 保存我们的 PDF 文件

```cpp
void ExampleCurve() {

    // 创建 Document 实例
    String _dataDir("C:\\Samples\\");
    // 创建 Document 实例
    auto document = MakeObject<Document>();

    // 将页面添加到 PDF 文件的页面集合中
    auto page = document->get_Pages()->Add();

    // 使用特定尺寸创建 Drawing object
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // 为 Drawing object 设置 border
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double> ({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // 将 Graph 对象添加到页面的段落集合中
    page->get_Paragraphs()->Add(graph);

    // 保存 PDF 文件
    document->Save(_dataDir + u"DrawingCurve1_out.pdf");
}
```
以下图片展示了使用我们的代码片段执行的结果：

![Drawing Curve](drawing_curve.png)

## 创建填充曲线对象

此示例展示了如何添加一个填充颜色的曲线对象。

```cpp
void ExampleFilledCurve() {

    // 创建文档实例
    String _dataDir("C:\\Samples\\");
    // 创建文档实例
    auto document = MakeObject<Document>();

    // 添加页面到PDF文件的页面集合
    auto page = document->get_Pages()->Add();

    // 创建具有一定尺寸的绘图对象
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // 设置绘图对象的边框
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double>({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // 添加图形对象到页面的段落集合
    page->get_Paragraphs()->Add(graph);

    // 保存PDF文件
    document->Save(_dataDir + u"DrawingCurve2_out.pdf");
}
```

Look at the result of adding a filled Curve:

![填充曲线](filled_curve.png)