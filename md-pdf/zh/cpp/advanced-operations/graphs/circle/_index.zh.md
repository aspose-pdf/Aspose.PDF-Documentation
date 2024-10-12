---
title: 向PDF文件添加圆形对象
linktitle: 添加圆形
type: docs
weight: 20
url: /cpp/add-circle/
description: 本文解释了如何使用Aspose.PDF for C++在您的PDF中创建一个圆形对象。
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 添加圆形对象

与条形图一样，圆形图可以用于显示多个独立类别中的数据。然而，与条形图不同的是，圆形图只能在您拥有构成整体的所有类别的数据时使用。那么让我们看看如何使用Aspose.PDF for C++添加一个[Circle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.circle/)对象。

请按照以下步骤操作：

1. 创建[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)实例

1. 创建具有特定尺寸的[Drawing object](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing)

1. 为绘图对象设置[边框](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd)

1. 将[图形](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph)对象添加到页面的段落集合中

1. 保存我们的PDF文件

```cpp
void ExampleCircle() {

    // 创建文档实例
    String _dataDir("C:\\Samples\\");
    // 创建文档实例
    auto document = MakeObject<Document>();

    // 将页面添加到PDF文件的页面集合中
    auto page = document->get_Pages()->Add();

    // 创建具有特定尺寸的绘图对象
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    // 为绘图对象设置边框
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);

    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(circle);

    // 将图形对象添加到页面的段落集合中
    page->get_Paragraphs()->Add(graph);

    // 保存PDF文件
    document->Save(_dataDir + u"DrawingCircle1_out.pdf");
}
```
我们的绘制圆形将如下所示：

![绘制圆形](drawing_circle.png)

## 创建填充圆形对象

此示例展示了如何添加一个填充颜色的圆形对象。

```cpp
void ExampleFilledCircle() {
    // 创建 Document 实例
    String _dataDir("C:\\Samples\\");
    // 创建 Document 实例
    auto document = MakeObject<Document>();

    // 向 PDF 文件的页面集合中添加页面
    auto page = document->get_Pages()->Add();

    // 创建具有特定尺寸的 Drawing 对象
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // 为 Drawing 对象设置边框
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);
    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    circle->get_GraphInfo()->set_FillColor(Color::get_Green());

    circle->set_Text(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Circle"));

    graph->get_Shapes()->Add(circle);

    // 将 Graph 对象添加到页面的段落集合中
    page->get_Paragraphs()->Add(graph);

    // 保存 PDF 文件
    document->Save(_dataDir + u"DrawingCircle2_out.pdf");
}
```

```
让我们看看添加一个填充圆的结果：

![填充圆](filled_circle.png)
```