---
title: 将弧形对象添加到PDF文件
linktitle: 添加弧形
type: docs
weight: 10
url: /zh/cpp/add-arc/
description: 本文介绍如何使用Aspose.PDF for C++在PDF中创建弧形对象。
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 添加弧形对象

Aspose.PDF for C++ 支持向PDF文档添加图形对象（例如图形、线条、矩形等）的功能。它还提供了用特定颜色填充[弧形](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc)对象的功能。

请按照以下步骤操作：

1. 创建[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)实例

1. 创建具有特定尺寸的[Drawing object](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing)

1. 为Drawing对象设置[Border](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) 将[Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph)对象添加到页面的段落集合中

1. 保存我们的PDF文件

以下代码片段显示了如何添加[Arc](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc/)对象。

```cpp
void ExampleArc() {
    // 创建文档实例
    String _dataDir("C:\\Samples\\");
    // 创建文档实例
    auto document = MakeObject<Document>();

    // 向PDF文件的页面集合中添加页面
    auto page = document->get_Pages()->Add();

    // 创建具有特定尺寸的Drawing对象
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // 为Drawing对象设置边框
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto arc1 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 95, 0, 90);
    arc1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc1);

    auto arc2 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 90, 70, 180);
    arc2->get_GraphInfo()->set_Color(Color::get_DarkBlue());
    graph->get_Shapes()->Add(arc2);

    auto arc3 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 85, 120, 210);
    arc3->get_GraphInfo()->set_Color(Color::get_Red());
    graph->get_Shapes()->Add(arc3);

    // 将Graph对象添加到页面的段落集合中
    page->get_Paragraphs()->Add(graph);

    // 保存PDF文件
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```
## 创建填充弧对象

下一个示例展示了如何添加一个填充颜色和特定尺寸的弧对象。

```cpp
void ExampleFilledArc() {

    // 创建 Document 实例
    String _dataDir("C:\\Samples\\");
    // 创建 Document 实例
    auto document = MakeObject<Document>();

    // 向 PDF 文件的页面集合添加页面
    auto page = document->get_Pages()->Add();

    // 创建具有特定尺寸的绘图对象
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // 为绘图对象设置边框
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto arc = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 95, 0, 90);
    arc->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc);

    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<double>({ 195, 100, 100, 100, 100, 195 }));
    line->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(line);

    // 将图形对象添加到页面的段落集合中
    page->get_Paragraphs()->Add(graph);

    // 保存 PDF 文件
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```

```
让我们看看添加一个填充弧的结果：

![Filled Arc](filled_arc.png)
```