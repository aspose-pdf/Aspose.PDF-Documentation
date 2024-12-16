---
title: 在 PDF 中使用 C++ 格式化文本
linktitle: 在 PDF 中格式化文本
type: docs
weight: 30
url: /zh/cpp/text-formatting-inside-pdf/
description: 本页解释了如何在 PDF 文件中格式化文本。包括添加行缩进、添加文本边框、添加下划线文本、在添加的文本周围添加边框、浮动框内容的文本对齐等。
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 如何在 PDF 中添加行缩进

要在 PDF 中添加行缩进，Aspose.PDF for C++ 使用 [SubsequentLinesIndent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a89b064ab1f39d56040625d7d98194ad3) 属性在 [TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options/) 类中，并且还利用 [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) 和 [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs) 集合。

请使用以下代码片段来使用该属性：

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLineIndent() {

    String _dataDir("C:\\Samples\\");

    // 输出文件名的字符串
    String outputFileName("SubsequentIndent_out.pdf");


    // 创建新的文档对象
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto text = MakeObject<TextFragment>("A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog.");

    // 初始化文本片段的TextFormattingOptions并指定SubsequentLinesIndent值

    text->get_TextState()->set_FormattingOptions(MakeObject<Aspose::Pdf::Text::TextFormattingOptions>());
    text->get_TextState()->get_FormattingOptions()->set_SubsequentLinesIndent(20);

    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line2");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line3");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line4");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line5");
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);

}
```

## 如何添加文本边框

以下代码片段展示了如何使用 TextBuilder 并设置 [TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) 的 DrawTextRectangleBorder 属性为文本添加边框

```cpp
void AddTextBorder() {

    String _dataDir("C:\\Samples\\");

    // 输出文件名的字符串
    String outputFileName("PDFWithTextBorder_out.pdf");

    // 创建新的文档对象
    auto document = MakeObject<Document>();
    // 获取特定页面
    auto page = document->get_Pages()->Add();

    // 创建文本片段
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // 设置文本属性
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // 设置 StrokingColor 属性以在文本周围绘制边框（描边）
    // 矩形
    textFragment->get_TextState()->set_StrokingColor(Color::get_DarkRed());
    // 将 DrawTextRectangleBorder 属性值设置为 true
    textFragment->get_TextState()->set_DrawTextRectangleBorder(true);
    auto tb = MakeObject<TextBuilder>(page);
    tb->AppendText(textFragment);
    // 保存文档
    document->Save(_dataDir + outputFileName);
}
```

## 如何添加下划线文本

以下代码片段向您展示了如何在创建新 PDF 文件时添加下划线文本。

```cpp
void AddUnderlineText() {
    String _dataDir("C:\\Samples\\");

    // 输出文件名的字符串
    String outputFileName("AddUnderlineText_out.pdf");

    // 创建新的文档对象
    auto document = MakeObject<Document>();
    // 获取特定页面
    auto page = document->get_Pages()->Add();

    // 带有示例文本的 TextFragment
    auto fragment = MakeObject<TextFragment>("Text with underline decoration");
    // 设置 TextFragment 的字体
    fragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    fragment->get_TextState()->set_FontSize(10);

    // 设置文本格式为下划线
    fragment->get_TextState()->set_Underline(true);

    // 指定 TextFragment 需要放置的位置
    fragment->set_Position(MakeObject<Position>(10, 800));

    auto tb = MakeObject<TextBuilder>(page);
    // 将 TextFragment 添加到 PDF 文件
    tb->AppendText(fragment);

    // 保存生成的 PDF 文档。
    document->Save(_dataDir + outputFileName);
}
```

## 如何为添加的文本添加边框

您可以控制所添加文本的外观和感觉。下面的示例展示了如何通过在添加的文本周围绘制一个矩形来添加边框。了解更多关于 [PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor/) 类的信息。

```cpp
void AddBorderAroundAddedText() {

    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String inputFileName("sample.pdf");

    // 输出文件名的字符串
    String outputFileName("AddingBorderAroundAddedText_out.pdf");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    editor->BindPdf(_dataDir + inputFileName);
    auto lineInfo = MakeObject<Aspose::Pdf::Facades::LineInfo>();

    lineInfo->set_LineWidth(2);
    lineInfo->set_VerticeCoordinate(MakeArray<float>({ 0, 0, 100, 100, 50, 100 }));
    lineInfo->set_Visibility(true);
    auto rect = MakeObject<System::Drawing::Rectangle>(0, 0, 0, 0);
    editor->CreatePolygon(lineInfo, 1, System::Drawing::Rectangle(0, 0, 0, 0), String::Empty);

    // 保存生成的 PDF 文档。
    editor->Save(_dataDir + outputFileName);
}
```

## 如何添加换行符

要添加带换行符的文本，请使用 [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) 与 [TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph)。

以下代码片段展示了如何在您的 PDF 文件中添加换行符：

```cpp
void AddNewLineFeed() {
    String _dataDir("C:\\Samples\\");

    // 输出文件名的字符串
    String outputFileName("AddNewLineFeed_out.pdf");

    // 创建新的文档对象
    auto document = MakeObject<Document>();
    // 获取特定页面
    auto page = document->get_Pages()->Add();

    // 使用包含所需换行符的文本初始化新的 TextFragment
    auto textFragment = MakeObject<TextFragment>("Applicant Name: \r\n Joe Smoe");

    // 如有必要，设置文本片段属性
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());

    // 创建 TextParagraph 对象
    auto par = MakeObject<TextParagraph>();

    // 将新的 TextFragment 添加到段落
    par->AppendLine(textFragment);

    // 设置段落位置
    par->set_Position(MakeObject<Position>(100, 600));

    // 创建 TextBuilder 对象
    auto textBuilder = new TextBuilder(page);
    // 使用 TextBuilder 添加 TextParagraph
    textBuilder->AppendParagraph(par);

    // 保存生成的 PDF 文档。
    document->Save(_dataDir + outputFileName);
}
```

## 如何添加删除线文本

您可以使用 [TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) 类来设置文本格式，如粗体、斜体、下划线，并且 API 还提供了将文本格式标记为删除线的功能。

请尝试使用以下代码片段来添加具有删除线格式的 TextFragment。

```cpp
void AddStrikeOutText() {
    String _dataDir("C:\\Samples\\");

    // 输出文件名字符串
    String outputFileName("AddStrikeOutText_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>();
    // 获取特定页面
    auto page = document->get_Pages()->Add();

    // 创建文本片段
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // 设置文本属性
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // 设置删除线属性
    textFragment->get_TextState()->set_StrikeOut(true);
    // 将文本标记为粗体
    textFragment->get_TextState()->set_FontStyle(FontStyles::Bold);

    // 创建 TextBuilder 对象
    auto textBuilder = MakeObject<TextBuilder>(page);
    // 将文本片段附加到 PDF 页面
    textBuilder->AppendText(textFragment);

    // 保存生成的 PDF 文档。
    document->Save(_dataDir + outputFileName);
}
```

## 应用梯度阴影到文本

[Aspose.Pdf.Color](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color) 类通过引入 [PatternColorSpace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color#a8be6d8ab626d2ba6935a13a9c5b0de54) 的新属性得到了进一步增强，可以用于为文本指定阴影颜色。这个新属性为文本添加不同的梯度阴影，例如轴向阴影、径向（类型3）阴影，如以下代码片段所示：

```cpp
void ApplyGradientShading() {

    String _dataDir("C:\\Samples\\");

    // 输入文件名字符串
    String inputFileName("sample.pdf");

    // 输出文件名字符串
    String outputFileName("ApplyGradientShading_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>("always print correctly");

    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientAxialShading>(Color::get_Red(), Color::get_Blue()));

    // 使用模式颜色空间创建新颜色
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);

}
```

>为了应用径向渐变，您可以在上述代码片段中将‘PatternColorSpace’属性设置为‘Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)’。

## 如何对齐浮动内容的文本

Aspose.PDF支持为Floating Box元素中的内容设置文本对齐。[Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box)实例的对齐属性可用于实现这一点，如以下代码示例所示。

```cpp
void ApplyGradientShadingRadial() {

    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String inputFileName("sample.pdf");

    // 输出文件名的字符串
    String outputFileName("ApplyGradientShadingRadial_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>(u"always print correctly");
    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientRadialShading>(Color::get_Red(), Color::get_Blue()));

    // 创建具有图案颜色空间的新颜色
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);
}
```