---
title: 向PDF文件添加椭圆对象
linktitle: 添加椭圆
type: docs
weight: 60
url: zh/cpp/add-ellipse/
description: 本文解释了如何使用Aspose.PDF for C++在PDF中创建椭圆对象。
lastmod: "2021-12-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 添加椭圆对象

Aspose.PDF for C++支持向PDF文档添加[椭圆](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.ellipse/)对象。它还提供了用特定颜色填充椭圆对象的功能。

```cpp
void ExampleEllipse() {
    // 创建文档实例
    String _dataDir("C:\\Samples\\");
    // 创建文档实例
    auto document = MakeObject<Document>();

    // 向PDF文件的页面集合添加页面
    auto page = document->get_Pages()->Add();

    // 创建具有特定尺寸的绘图对象
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // 为绘图对象设置边框
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(150, 100, 120, 60);
    ellipse1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    ellipse1->set_Text(MakeObject<Aspose::Pdf::Text::TextFragment>("Ellipse"));
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(50, 50, 18, 300);
    ellipse2->get_GraphInfo()->set_Color(Color::get_DarkRed());

    graph->get_Shapes()->Add(ellipse2);

    // 将图形对象添加到页面的段落集合中
    page->get_Paragraphs()->Add(graph);

    // 保存PDF文件
    document->Save(_dataDir + u"DrawingEllipse_out.pdf");

}
```

![添加椭圆](ellipse.png)

## 创建填充椭圆对象

以下代码片段展示了如何添加一个用颜色填充的[椭圆](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.ellipse/)对象。

```csharp
void ExampleFilledEllipse() {
    // 创建文档实例
    String _dataDir("C:\\Samples\\");
    // 创建文档实例
    auto document = MakeObject<Document>();

    // 添加页面到PDF文件的页面集合中
    auto page = document->get_Pages()->Add();

    // 创建具有特定尺寸的绘图对象
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // 为绘图对象设置边框
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(100, 100, 120, 180);
    ellipse1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(200, 150, 180, 120);
    ellipse2->get_GraphInfo()->set_FillColor(Color::get_DarkRed());
    graph->get_Shapes()->Add(ellipse2);

    // 添加图形对象到页面的段落集合中
    page->get_Paragraphs()->Add(graph);

    // 保存PDF文件
    document->Save(_dataDir + u"DrawingEllipse_out.pdf");
}
```

![填充椭圆](fill_ellipse.png)

## 在椭圆内添加文本

Aspose.PDF for C++支持在图形对象内添加文本。图形对象的文本属性提供了设置图形对象文本的选项。

以下代码片段显示了如何在矩形对象内添加文本。

```cpp
void ExampleEllipseWithText() {
    // 创建文档实例
    String _dataDir("C:\\Samples\\");
    // 创建文档实例
    auto document = MakeObject<Document>();

    // 将页面添加到PDF文件的页面集合中
    auto page = document->get_Pages()->Add();

    // 创建具有一定尺寸的绘图对象
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // 设置绘图对象的边框
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto textFragment = MakeObject<Aspose::Pdf::Text::TextFragment>("Ellipse");
    textFragment->get_TextState()->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Helvetica"));
    textFragment->get_TextState()->set_FontSize(24);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(100, 100, 120, 180);
    ellipse1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    ellipse1->set_Text(textFragment);
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(200, 150, 180, 120);
    ellipse2->get_GraphInfo()->set_FillColor(Color::get_DarkRed());
    ellipse2->set_Text(textFragment);
    graph->get_Shapes()->Add(ellipse2);

    // 将图形对象添加到页面的段落集合中
    page->get_Paragraphs()->Add(graph);

    // 保存PDF文件
    document->Save(_dataDir + u"DrawingEllipseText_out.pdf");

}
```

抱歉，我无法查看或翻译图片内容。请提供文本内容，我将乐于帮助您进行翻译。