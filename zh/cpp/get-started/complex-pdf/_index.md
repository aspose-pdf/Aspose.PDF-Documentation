---
title: 创建复杂的PDF
linktitle: 创建复杂的PDF
type: docs
weight: 60
url: /zh/cpp/complex-pdf-example/
description: Aspose.PDF for C++允许您创建包含图像、文本片段和表格的更复杂的文档。
lastmod: "2021-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

[Hello, World](/pdf/zh/cpp/hello-world-example/) 示例展示了使用 C++ 和 Aspose.PDF 创建 PDF 文档的简单步骤。在本文中，我们将看看如何使用 C++ 和 Aspose.PDF for C++ 创建一个更复杂的文档。作为一个例子，我们将使用一家虚构的提供客运渡轮服务的公司的文档。我们的文档将包含一张图片、两个文本片段（标题和段落）以及一个表格。为了构建这样的文档，我们将使用基于DOM的方法。您可以在[DOM API 的基础](/pdf/zh/cpp/basics-of-dom-api/)部分阅读更多内容。

如果我们从头创建一个文档，我们需要遵循某些步骤：

1. Create a [String Class](https://reference.aspose.com/pdf/cpp/class/system.string) 用于路径名和文件名。
1. 实例化一个 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 对象。在这一步中，我们将创建一个带有一些元数据但没有页面的空PDF文档。
1. 向文档对象添加一个 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)。因此，现在我们的文档将有一页。
1. 向页面添加一个 [Image](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image)。
1. 为标题创建一个 [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/)。对于标题，我们将使用Arial字体，字体大小为24pt，并居中对齐。
1. 将标题添加到页面的 [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170)。 创建一个 [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) 用于描述。对于描述，我们将使用 Arial 字体，字体大小为 24pt，居中对齐。
1. 添加（描述）到页面段落。
1. 创建一个表格，添加表格属性。
1. 将（表格）添加到页面 [段落](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170)。
1. 保存文档为 "Complex.pdf"。

```cpp
void ExampleComplex()
{
    String outputFileName;

    // 路径名的字符串。
    String _dataDir("C:\\Samples\\");

    // 文件名的字符串。
    String filename("Complex.pdf");

    // 初始化文档对象
    auto document = MakeObject<Document>();
    // 添加页面
    auto page = document->get_Pages()->Add();

    // 添加图像
    String imageFileName = _dataDir + String(u"logo.png");

    // 将图像添加到页面资源的图像集合中
    auto rectangle = MakeObject<Rectangle>(20, 730, 120, 830);
    page->AddImage(imageFileName, rectangle);

    // 添加标题
    auto header = MakeObject<TextFragment>(u"New ferry routes in Fall 2020");
    auto textFragementState = header->get_TextState();
    textFragementState->set_Font(FontRepository::FindFont(u"Arial"));
    textFragementState->set_FontSize(24);
    header->set_HorizontalAlignment(HorizontalAlignment::Center);
    auto position = MakeObject<Aspose::Pdf::Text::Position>(130, 720);
    header->set_Position(position);
    page->get_Paragraphs()->Add(header);

    // 添加描述
    String descriptionText(u"Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.");
    auto description = MakeObject<TextFragment>(descriptionText);
    description->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    description->get_TextState()->set_FontSize(14);
    description->set_HorizontalAlignment(HorizontalAlignment::Left);
    page->get_Paragraphs()->Add(description);

    // 添加表格
    auto table = MakeObject<Table>();
    table->set_ColumnWidths(u"200");

    table->set_Border(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, 1.0f, Aspose::Pdf::Color::get_DarkSlateGray()));
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, .5f, Aspose::Pdf::Color::get_Black()));
    table->get_Margin()->set_Bottom(10);
    table->get_DefaultCellTextState()->set_Font(FontRepository::FindFont(u"Helvetica"));

    auto headerRow = table->get_Rows()->Add();
    headerRow->get_Cells()->Add(u"Departs City");
    headerRow->get_Cells()->Add(u"Departs Island");

    for (auto headerRowCell : headerRow->get_Cells())
    {
        headerRowCell->set_BackgroundColor(Color::get_Gray());
        headerRowCell->get_DefaultCellTextState()->set_ForegroundColor(Color::get_WhiteSmoke());
    }

    String arrivals[10] = { u"6:00",u"6:45", u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45" };
    String departures[10] = { u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45", u"11:00", u"11:45" };

    for (int i = 0; i < 10; i++)
    {
        auto dataRow = table->get_Rows()->Add();
        dataRow->get_Cells()->Add(arrivals[i]);
        dataRow->get_Cells()->Add(departures[i]);
    }

    page->get_Paragraphs()->Add(table);

    // 保存更新后的 PDF
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```