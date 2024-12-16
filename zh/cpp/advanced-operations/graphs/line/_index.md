---
title: 将线对象添加到PDF文件
linktitle: 添加线
type: docs
weight: 40
url: /zh/cpp/add-line/
description: 本文解释了如何使用Aspose.PDF for C++在PDF中创建线对象。
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 添加线对象

Aspose.PDF for C++支持在PDF文档中添加图形对象（例如图形、线、矩形等）的功能。您还可以添加[线](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.line/)对象，并可以为线元素指定虚线模式、颜色和其他格式。

请按照以下步骤操作：

1. 创建一个新的PDF[文档](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/)

1. 将[页面](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/)添加到PDF文件的页面集合中

1. 创建[图形](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/)实例。

1. 将图形对象添加到页面实例的段落集合中。

1. 创建[Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/)实例。

1. 设置线宽。

1. 将[Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/)对象添加到Graph对象的形状集合中。

1. 保存您的PDF文件。

以下代码片段显示了如何添加一个填充颜色的[Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/)对象。

```cpp

void AddLineObjectToPDF()
{

String _dataDir("C:\\Samples\\");

// 创建Document实例

auto document = MakeObject<Document>();


// 将页面添加到PDF文件的页面集合中

auto page = document->get_Pages()->Add();


// 创建Graph实例

auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);


// 将图形对象添加到页面实例的段落集合中

page->get_Paragraphs()->Add(graph);


// 创建Rectangle实例

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(new float[] { 100, 100, 200, 100 });



// 为Graph对象指定填充颜色

line->get_GraphInfo()->set_DashArray (MakeArray<int>({ 0, 1, 0 }));

line->get_GraphInfo()->set_DashPhase (1);



// 将矩形对象添加到Graph对象的形状集合中

graph->get_Shapes()->Add(line);



// 保存PDF文件

document->Save(_dataDir + u"AddLineObject_out.pdf");
}

```
![添加线](add_line.png)

## 如何在您的 PDF 文档中添加虚线

```cpp
void DashLengthInBlackAndDashLengthInWhite()
{

String _dataDir("C:\\Samples\\");

// 创建 Document 实例

auto document = MakeObject<Document>();


// 将页面添加到 PDF 文件的页面集合中

auto page = document->get_Pages()->Add();


// 创建具有特定尺寸的 Drawing 对象

auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

// 将绘图对象添加到页面实例的段落集合中

page->get_Paragraphs()->Add(canvas);



// 创建 Line 对象

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<float>({ 100, 100, 200, 100 }));

// 设置 Line 对象的颜色

line->get_GraphInfo()->set_Color (Aspose::Pdf::Color::get_Red());

// 为线对象指定虚线数组

line->get_GraphInfo()->set_DashArray(MakeArray<int>({ 0, 1, 0 }));

// 设置 Line 实例的虚线相位

line->get_GraphInfo()->set_DashPhase(1);

// 将线条添加到绘图对象的形状集合中

canvas->get_Shapes()->Add(line);


// 保存 PDF 文件

document->Save(_dataDir + u"DashLength_out.pdf");
}
```

让我们检查结果：

![Dashed Line](dash_line.png)

## 绘制横跨页面的线

我们还可以使用线对象绘制从左下角到右上角和从左上角到右下角的交叉线。

请查看以下代码片段以完成此需求。

```cpp
void ExampleLineAcrossPage() {

    // 创建文档实例
    String _dataDir("C:\\Samples\\");
    // 创建文档实例
    auto document = MakeObject<Document>();
   
    // 向PDF文件的页面集合添加页面
    auto page = document->get_Pages()->Add();
    // 将页面边距设置为四边为0

    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);

    // 创建宽度和高度等于页面尺寸的图形对象
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(
        page->get_PageInfo()->get_Width(), 
        page->get_PageInfo()->get_Height());

    // 创建从左下角到右上角的第一个线对象
    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(
        MakeArray<double>({ 
                      page->get_Rect()->get_LLX(), 0, 
                      page->get_PageInfo()->get_Width(),
                      page->get_Rect()->get_URY() }));

    // 将线添加到图形对象的形状集合中
    graph->get_Shapes()->Add(line);
    // 绘制从左上角到右下角的线
    auto line2 = MakeObject<Aspose::Pdf::Drawing::Line>( MakeArray<double>({0, 
        page->get_Rect()->get_URY(), page->get_PageInfo()->get_Width(), page->get_Rect()->get_LLX() }));

    // 将线添加到图形对象的形状集合中
    graph->get_Shapes()->Add(line2);
    // 将图形对象添加到页面的段落集合中
    page->get_Paragraphs()->Add(graph);

    // 保存PDF文件
    document->Save(_dataDir + u"DrawingLine_out.pdf");
}
```

```
![绘制线条](draw_line.png)
```