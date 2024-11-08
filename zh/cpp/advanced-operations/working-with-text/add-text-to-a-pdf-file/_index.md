---
title: 使用 C++ 向 PDF 添加文本
linktitle: 向 PDF 添加文本
type: docs
weight: 10
url: /zh/cpp/add-text-to-pdf-file/
description: 本文描述了在 Aspose.PDF 中处理文本的各个方面。了解如何向 PDF 添加文本、添加 HTML 片段或使用自定义 OTF 字体。
lastmod: "2021-12-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 添加文本

要向现有 PDF 文件添加文本：

1. 使用 Document 对象打开输入 PDF。
2. 获取要添加文本的特定页面。
3. 使用输入文本和其他文本属性创建 TextFragment 对象。从该特定页面创建的 TextBuilder 对象允许您使用 AppendText 方法将 TextFragment 对象添加到页面。
4. 调用 Document 对象的 Save 方法并保存输出 PDF 文件。

以下代码片段展示了如何在现有 PDF 文件中添加文本。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddingText() {
    
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("sample.pdf");
    // String for output file name
    String outputFileName("AddingText_out.pdf");

    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // get particular page
    auto pdfPage = document->get_Pages()->idx_get(1);

    // create text fragment
    auto textFragment = MakeObject<TextFragment>("Aspose.PDF");
    textFragment->set_Position(MakeObject<Position>(80, 700));

    // set text properties
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
    textFragment->get_TextState()->set_FontSize(14);
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());

    // create TextBuilder object
    auto textBuilder = MakeObject<TextBuilder>(pdfPage);
    // append the text fragment to the PDF page
    textBuilder->AppendText(textFragment);

    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}
```

## 从流加载字体

以下代码片段显示了如何在向 PDF 文档添加文本时从流对象加载字体。

```cpp
void LoadingFontFromStream() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("sample.pdf");
    String outputFileName("LoadingFontFromStream_out.pdf");

    String fontFile("C:\\Windows\\Fonts\\Arial.ttf");

    // 加载输入 PDF 文件
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 为文档的第一页创建文本构建器对象
    auto textBuilder = MakeObject<TextBuilder>(document->get_Pages()->idx_get(1));
    // 创建带有示例字符串的文本片段
    auto textFragment = MakeObject<TextFragment>("Hello world");

    if (!fontFile.IsNullOrEmpty()) {
        // 将 TrueType 字体加载到流对象中
        auto fontStream = System::IO::File::OpenRead(fontFile);
        // 设置文本字符串的字体名称
        textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
        // 指定文本片段的位置
        textFragment->set_Position(MakeObject<Position>(10, 10));
        // 将文本添加到 TextBuilder，以便可以将其放置在 PDF 文件上
        textBuilder->AppendText(textFragment);

        // 保存生成的 PDF 文档。
        document->Save(_dataDir + outputFileName);
    }
}
```

## 使用 TextParagraph 添加文本

以下代码片段演示了如何使用 [TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph) 类在 PDF 文档中添加文本。

```cpp
void AddTextUsingTextParagraph() {

    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto document = MakeObject<Document>();

    String outputFileName("AddTextUsingTextParagraph_out.pdf");

    // 向 Document 对象的页面集合中添加页面
    auto page = document->get_Pages()->Add();
    auto builder = MakeObject<TextBuilder>(page);

    // 创建文本段落
    auto paragraph = MakeObject<TextParagraph>();

    // 设置随后的行缩进
    paragraph->set_SubsequentLinesIndent(20);

    // 指定添加 TextParagraph 的位置
    paragraph->set_Rectangle(MakeObject<Rectangle>(100, 300, 200, 700));

    // 指定自动换行模式
    paragraph->get_FormattingOptions()->set_WrapMode(TextFormattingOptions::WordWrapMode::ByWords);

    // 创建文本片段
    auto fragment1 = MakeObject<TextFragment>("the quick brown fox jumps over the lazy dog");
    fragment1->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    fragment1->get_TextState()->set_FontSize(12);
    // 将片段添加到段落中
    paragraph->AppendLine(fragment1);
    // 添加段落
    builder->AppendParagraph(paragraph);

    // 保存生成的 PDF 文档。
    document->Save(_dataDir + outputFileName);
}

```

## 向 TextSegment 添加超链接

一个 PDF 页面可能包含一个或多个 TextFragment 对象，其中每个 TextFragment 对象可以有一个或多个 TextSegment 实例。为了为 TextSegment 设置超链接，可以在提供 Aspose.Pdf.WebHyperlink 实例的对象时使用 [TextSegment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_segment) 类的 Hyperlink 属性。请尝试使用以下代码片段来完成此需求。

```cpp
void AddHyperlinkToTextSegment() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("AddHyperlinkToTextSegment_out.pdf");

    // 创建文档实例
    auto document = MakeObject<Document>();

    // 向 PDF 文件的页面集合添加页面
    auto page1 = document->get_Pages()->Add();

    // 创建 TextFragment 实例
    auto tf = MakeObject<TextFragment>("Sample Text Fragment");
    // 设置 TextFragment 的水平对齐
    tf->set_HorizontalAlignment(HorizontalAlignment::Right);

    // 创建带有示例文本的 textsegment
    auto segment = MakeObject<TextSegment>(" ... Text Segment 1...");
    // 将 segment 添加到 TextFragment 的 segments 集合中
    tf->get_Segments()->Add(segment);

    // 创建一个新的 TextSegment
    segment = MakeObject<TextSegment>("Link to Google");
    // 将 segment 添加到 TextFragment 的 segments 集合中

    tf->get_Segments()->Add(segment);

    // 为 TextSegment 设置超链接
    segment->set_Hyperlink(MakeObject<Aspose::Pdf::WebHyperlink>("www.aspose.com"));

    // 设置文本段的前景色
    segment->get_TextState()->set_ForegroundColor(Color::get_Blue());

    // 将文本格式设置为斜体
    segment->get_TextState()->set_FontStyle(FontStyles::Italic);

    // 创建另一个 TextSegment 对象
    segment = MakeObject<TextSegment>(u"TextSegment without hyperlink");

    // 将 segment 添加到 TextFragment 的 segments 集合中
    tf->get_Segments()->Add(segment);

    // 将 TextFragment 添加到页面对象的段落集合中
    page1->get_Paragraphs()->Add(tf);

    // 保存生成的 PDF 文档。
    document->Save(_dataDir + outputFileName);

}
```

## 使用 OTF 字体

Aspose.PDF for C++ 提供了在创建/操作 PDF 文件内容时使用自定义/TrueType 字体的功能，以便文件内容使用非默认系统字体显示。

```cpp
void UseOTFFont() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("OTFFont_out.pdf");

    // 创建新文档实例    
    auto document = MakeObject<Document>();

    // 将页面添加到 PDF 文件的页面集合
    auto page = document->get_Pages()->Add();

    // 创建带有示例文本的 TextFragment 实例
    auto fragment = MakeObject<TextFragment>("Sample Text in OTF font");

    // 或者您甚至可以指定系统目录中 OTF 字体的路径
    fragment->get_TextState()->set_Font(FontRepository::OpenFont(u"C:\\Samples\\Fonts\\Montserrat-Black.otf"));
    // 指定将字体嵌入 PDF 文件中，以便其正确显示，
    // 即使目标机器上未安装/存在特定字体
    fragment->get_TextState()->get_Font()->set_IsEmbedded(true);
    // 将 TextFragment 添加到页面实例的段落集合中
    page->get_Paragraphs()->Add(fragment);
    // 保存生成的 PDF 文档。
    document->Save(_dataDir + outputFileName);
}
```

## 使用 DOM 添加 HTML 字符串

Aspose.Pdf.Generator.Text 类包含一个名为 IsHtmlTagSupported 的属性，使得可以在 PDF 文件中添加 HTML 标签/内容。添加的内容以原生 HTML 标签形式呈现，而不是简单的文本字符串。为了在 Aspose.Pdf 命名空间的新文档对象模型 (DOM) 中支持类似功能，引入了 HtmlFragment 类。

[HtmlFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_fragment) 实例可用于指定应放置在 PDF 文件中的 HTML 内容。类似于 TextFragment，HtmlFragment 是一个段落级对象，可以添加到 Page 对象的段落集合中。以下代码片段展示了使用 DOM 方法在 PDF 文件中放置 HTML 内容的步骤。

```cpp
void AddingHtmlString() {
    
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String inputFileName("sample.pdf");

    // 输出文件名的字符串
    String outputFileName("sample_html_out.pdf");

    // 创建 Document 实例
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 向 PDF 文件的页面集合中添加一个页面
    auto page = document->get_Pages()->Add();

    // 使用 HTML 内容实例化 HtmlFragment
    auto title = MakeObject<HtmlFragment>("<h1 style=\"color:blue\"><strong>HTML String Demo</strong></h1>");

    // 设置 MarginInfo 以获取边距详细信息
    auto margin = MakeObject<MarginInfo>();
    margin->set_Bottom(10);
    margin->set_Top(200);
    // 设置边距信息
    title->set_Margin(margin);

    // 将 HTML Fragment 添加到页面的段落集合中
    page->get_Paragraphs()->Add(title);
    // 保存 PDF 文件
    document->Save(_dataDir + outputFileName);
}
```

以下代码片段演示了如何将HTML有序列表添加到文档中的步骤：

```cpp
void AddHTMLOrderedListIntoDocuments() {
    
    String _dataDir("C:\\Samples\\");

    // 输出文件名的字符串
    String outputFileName("AddHTMLOrderedListIntoDocuments_out.pdf");

    // 实例化Document对象    
    auto document = MakeObject<Document>();

    // 用对应的HTML片段实例化HtmlFragment对象
    auto htmlFragment = MakeObject<HtmlFragment>(
        "<div style=\"font-family: sans-serif\"><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul><p>Text after the list.</p><p>Next line<br/>Last line</p></div>");
    // 在Pages集合中添加页面
    auto page = document->get_Pages()->Add();

    // 在页面中添加HtmlFragment
    page->get_Paragraphs()->Add(htmlFragment);

    // 保存生成的PDF文件
    document->Save(_dataDir + outputFileName);
}
```

您还可以使用TextState对象设置HTML字符串格式，如下所示：

```cpp
void AddHTMLStringFormatting() {
    
    String _dataDir("C:\\Samples\\");

    // 输出文件名的字符串
    String outputFileName("sample_html_out.pdf");

    // 实例化Document对象    
    auto document = MakeObject<Document>();

    // 在Pages集合中添加页面
    auto page = document->get_Pages()->Add();

    // 用HTML内容实例化HtmlFragment
    auto title = MakeObject<HtmlFragment>("<h1><strong>HTML String Demo</strong></h1>");

    auto textState = MakeObject<TextState>(12);

    textState->set_Font(FontRepository::FindFont(u"Calibri"));
    textState->set_ForegroundColor(Color::get_Green());
    textState->set_BackgroundColor(Color::get_Coral());
    title->set_TextState(textState);

    // 将HTML片段添加到页面的段落集合中
    page->get_Paragraphs()->Add(title);
    // 保存PDF文件
    document->Save(_dataDir + outputFileName);
}

```

如果您通过HTML标记设置了一些文本属性值，然后在TextState属性中提供相同的值，它们将通过TextState实例的属性覆盖HTML参数。以下代码片段显示了描述的行为。

```cpp
void AddHTMLUsingDOMAndOverwrite() {

    String _dataDir("C:\\Samples\\");
    // 输出文件名的字符串
    String outputFileName("AddHTMLUsingDOMAndOverwrite_out.pdf");

    // 实例化Document对象    
    auto document = MakeObject<Document>();

    // 在Pages集合中添加页面
    auto page = document->get_Pages()->Add();

    // 使用HTML内容实例化HtmlFragment
    auto title = MakeObject<HtmlFragment>("<p style='font-family: Verdana'><b><i>表格包含文本</i></b></p>");

    // 字体族从'Verdana'将被重置为'Arial'
    title->set_TextState(new TextState(u"Arial Black"));
    title->set_TextState(new TextState(20));

    // 设置底部边距信息
    title->get_Margin()->set_Bottom(10);
    // 设置顶部边距信息
    title->get_Margin()->set_Top(400);
    // 将HTML片段添加到页面的段落集合中
    page->get_Paragraphs()->Add(title);
    // 保存PDF文件
    document->Save(_dataDir + outputFileName);
}
```

## FootNotes and EndNotes (DOM)

脚注通过使用连续的上标数字在论文的文本中指示注释。实际的注释是缩进的，可以作为脚注出现在页面底部。

### Adding FootNote

在脚注引用系统中，指示引用的方法是：

- 在源材料后直接在行上方放置一个小数字。这个数字称为注释标识符。它稍微高于文本行。
- 在页面底部放置相同的数字，后跟您的来源引用。脚注应该是按数字和时间顺序的：第一个引用是1，第二个是2，依此类推。

脚注的优点是读者可以简单地扫视页面底部，以发现他们感兴趣的引用来源。

按照以下步骤：

- 创建一个 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 实例
- 创建一个 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 对象

- 创建一个 [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) 对象
- 创建一个 Note 实例并将其值传递给 TextFragment [FootNote](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#abe1663009fbceed84a0a392527463219) 属性
- 将 TextFragment 添加到页面实例的段落集合中

```cpp
void AddFootNote() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name
    String inputFileName("sample.pdf");
    String outputFileName("sample_footnote_out.pdf");

    // Instantiate Document object    
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Add Page in Pages Collection
    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>();
    note->set_Text(u"Demo");
    t->set_FootNote(note);

    // create TextFragment instance
    auto text = MakeObject<TextFragment>("Hello World");
    // set FootNote value for TextFragment
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    // add TextFragment to paragraphs collection of first page of document
    page->get_Paragraphs()->Add(text);
    // create second TextFragment
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // set FootNote for second text fragment
    text->set_FootNote(MakeObject<Note>("foot note for test text 2"));
    // add second text fragment to paragraphs collection of PDF file
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### 自定义脚注的线条样式

以下示例演示如何在 Pdf 页面底部添加脚注并定义自定义线条样式。

```cpp
void CustomFootNote_Line() {
    
    String _dataDir("C:\\Samples\\");

    // 输出文件名的字符串    
    String outputFileName("customFootNote_Line.pdf");

    // 创建文档实例
    auto document = MakeObject<Document>();

    // 向 PDF 的页面集合中添加页面
    auto page = document->get_Pages()->Add();
    
    // 创建 GraphInfo 对象
    auto graph = MakeObject<GraphInfo>();
    // 设置线宽为 2
    graph->set_LineWidth(2);
    // 设置图形对象的颜色
    graph->set_Color(Color::get_Red());
    // 将虚线数组值设置为 3
    graph->set_DashArray(MakeArray<int>(3));
    // 将虚线相位值设置为 1
    graph->set_DashPhase(1);
    // 将页面的脚注线样式设置为图形
    page->set_NoteLineStyle(graph);

    // 创建 TextFragment 实例
    auto text = MakeObject<TextFragment>("Hello World");
    // 为 TextFragment 设置脚注值
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    // 将 TextFragment 添加到文档第一页的段落集合中
    page->get_Paragraphs()->Add(text);
    // 创建第二个 TextFragment
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // 为第二个文本片段设置脚注
    text->set_FootNote(MakeObject<Note>("foot note for test text 2"));
    // 将第二个文本片段添加到 PDF 文件的段落集合中
    page->get_Paragraphs()->Add(text);
    // 保存 PDF 文件
    document->Save(_dataDir + outputFileName);
}
```

我们可以使用 TextState 对象设置脚注标签（注释标识符）格式，如下所示：

```csharp
void AddCustomFootNoteLabel() {
    
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串    
    String inputFileName("sample.pdf");

    // 输出文件名的字符串    
    String outputFileName("sample_footnote.pdf");

    // 创建 Document 实例
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>("Demo");
    t->set_FootNote(note);

    // 创建 TextFragment 实例
    auto text = MakeObject<TextFragment>("Hello World");
    // 为 TextFragment 设置脚注值
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    text->get_FootNote()->set_Text(u"21");

    auto ts = MakeObject<TextState>();
    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_FontStyle(FontStyles::Italic);
    text->get_FootNote()->set_TextState(ts);

    // 将 TextFragment 添加到文档第一页的段落集合中
    page->get_Paragraphs()->Add(text);
    // 创建第二个 TextFragment
    text = MakeObject<TextFragment>(u"Aspose.Pdf for C++");
    // 为第二个文本片段设置脚注
    text->set_FootNote(MakeObject<Note>("foot note for test text 2"));
    // 将第二个文本片段添加到 PDF 文件的段落集合中
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### 自定义脚注标签

默认情况下，脚注编号从1开始递增。然而，我们可能需要设置一个自定义的脚注标签。为了实现这个需求，请尝试使用以下代码片段

```cpp
void CustomFootNote_Label() {

    String _dataDir("C:\\Samples\\");
    // 输出文件名的字符串    
    String outputFileName("CustomizeFootNoteLabel_out.pdf");

    // 创建Document实例
    auto document = MakeObject<Document>();

    // 向PDF的页面集合添加页面
    auto page = document->get_Pages()->Add();

    // 创建GraphInfo对象
    auto graph = MakeObject<GraphInfo>();

    // 设置线宽为2
    graph->set_LineWidth(2);

    // 为图形对象设置颜色
    graph->set_Color(Color::get_Red());

    // 设置虚线数组值为3
    graph->set_DashArray(MakeArray<int>(3));

    // 设置虚线相位值为1
    graph->set_DashPhase(1);

    // 将页面的脚注线样式设置为图形
    page->set_NoteLineStyle(graph);

    // 创建TextFragment实例
    auto text = MakeObject<TextFragment>("Hello World");
    // 为TextFragment设置脚注值
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    // 为脚注指定自定义标签
    text->get_FootNote()->set_Text(u" Aspose(2021)");
    // 将TextFragment添加到文档第一页的段落集合中
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## 添加图像和表格到脚注

以下代码片段展示了将[脚注](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#a017ff999979d9f799b8e3cd32ab95722)添加到[TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment)对象的步骤，然后将图像和表格对象添加到脚注部分的段落集合中。

```cpp

void AddingImageAndTableToFootnote() {
    
    String _dataDir("C:\\Samples\\");

    // 输出文件名的字符串
    String outputFileName("AddImageAndTableToFootNote_out.pdf");

    // 创建文档实例
    auto document = new Document();
    // 添加页面到PDF的页面集合中
    auto page = document->get_Pages()->Add();

    // 创建TextFragment实例
    auto text = MakeObject<TextFragment>("Hello World");

    page->get_Paragraphs()->Add(text);

    text->set_FootNote(MakeObject<Note>());
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.jpg");
    image->set_FixHeight(20);

    text->get_FootNote()->get_Paragraphs()->Add(image);

    auto footNote = MakeObject<TextFragment>("footnote text");
    footNote->get_TextState()->set_FontSize(20);
    footNote->set_IsInLineParagraph(true);
    text->get_FootNote()->get_Paragraphs()->Add(footNote);
    
    auto table = MakeObject<Table>();
    table->get_Rows()->Add()->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Row 1 Cell 1"));
    text->get_FootNote()->get_Paragraphs()->Add(table);

    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## 如何创建尾注

尾注是一种来源引用，指引读者在论文末尾的特定位置找到引用或提到的信息或文字的来源。当使用尾注时，引用或改写的句子或总结材料后面会跟随一个上标编号。

以下示例演示了如何在 Pdf 页面中添加尾注。

```cpp
void HowToCreateEndNotes() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name    
    String outputFileName("endNote_out.pdf");

    // Create Document instance
    auto document = new Document();
    // Add page to pages collection of PDF
    auto page = document->get_Pages()->Add();

    // create TextFragment instance
    auto text = MakeObject<TextFragment>("Hello World");

    // set FootNote value for TextFragment
    text->set_EndNote(MakeObject<Note>("sample End note"));

    // specify custom label for FootNote
    text->get_EndNote()->set_Text(u" Aspose(2021)");
    // add TextFragment to paragraphs collection of first page of document
    page->get_Paragraphs()->Add(text);
    // save the PDF file
    document->Save(_dataDir + outputFileName);
}
```

## 文本和图像作为行内段落

PDF 文件的默认布局是流式布局（从左上到右下）。因此，每个新元素添加到 PDF 文件时，都是在右下方的流中添加。然而，我们可能需要在同一水平（一个接一个）显示各种页面元素，例如图像和文本。一种方法是创建一个表格实例，并将两个元素分别添加到单个单元格对象中。然而，另一种方法可以是行内段落。通过将图像和文本的 IsInLineParagraph 属性设置为 true，这些段落将作为行内显示在其他页面元素中。

以下代码片段展示了如何在 PDF 文件中添加文本和图像作为行内段落。

```cpp
void TextAndImageAsInLineParagraph() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("TextAndImageAsParagraph_out.pdf");

    // 实例化 Document 实例
    auto document = MakeObject<Document>();

    // 向 Document 实例的页面集合添加页面
    auto page = document->get_Pages()->Add();

    // 创建 TextFragmnet
    auto text = MakeObject<TextFragment>("Hello World.. ");
    // 将文本片段添加到页面对象的段落集合中
    page->get_Paragraphs()->Add(text);

    // 创建一个图像实例
    auto image = MakeObject<Image>();

    // 将图像设置为行内段落，以便它出现在
    // 前一个段落对象（TextFragment）之后
    image->set_IsInLineParagraph(true);

    // 指定图像文件路径
    image->set_File(_dataDir + u"aspose-logo.jpg");
    // 设置图像高度（可选）
    image->set_FixHeight(30);
    // 设置图像宽度（可选）
    image->set_FixWidth(100);
    // 将图像添加到页面对象的段落集合中
    page->get_Paragraphs()->Add(image);
    // 使用不同的内容重新初始化 TextFragment 对象
    text = MakeObject<TextFragment>(" Hello Again..");
    // 将 TextFragment 设置为行内段落
    text->set_IsInLineParagraph(true);
    // 将新创建的 TextFragment 添加到页面的段落集合中
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## 指定添加文本时的字符间距

文本可以通过 TextFragment 实例或 TextParagraph 对象添加到 PDF 的段落集合中，甚至可以使用 TextStamp 类在 PDF 中添加文本。当添加文本时，我们可能需要为文本对象指定字符之间的间距。为了满足这一要求，引入了一个名为 Property CharacterSpacing 的新属性。

请考虑以下方法来满足这一要求。

以下方法展示了在 PDF 文档中添加文本时指定字符间距的步骤。

### 使用 TextBuilder 和 TextFragment

```cpp
// 使用 TextBuilder 和 TextFragment 在添加文本时指定字符间距
void CharacterSpacing_TextFragment() {
    
    String _dataDir("C:\\Samples\\");

    // 输出文件名的字符串    
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // 创建 Document 实例
    auto document = MakeObject<Document>();
    // 向 Document 的页面集合中添加页面
    auto page = document->get_Pages()->Add();

    // 创建 TextBuilder 实例
    auto builder = MakeObject<TextBuilder>(page);

    // 使用示例内容创建文本片段实例
    auto wideFragment = MakeObject<TextFragment>("Text with increased character spacing");
    wideFragment->get_TextState()->ApplyChangesFrom(MakeObject<TextState>("Arial", 12));

    // 为 TextFragment 指定字符间距
    wideFragment->get_TextState()->set_CharacterSpacing(2.0f);

    // 指定 TextFragment 的位置
    wideFragment->set_Position(MakeObject<Position>(100, 650));

    // 将 TextFragment 附加到 TextBuilder 实例
    builder->AppendText(wideFragment);

    // 保存生成的 PDF 文档。
    document->Save(_dataDir + outputFileName);
}
```

### 使用 TextParagraph

```cpp
void CharacterSpacing_TextParagraph() {
    
    String _dataDir("C:\\Samples\\");

    // 输出文件名的字符串
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // 创建 Document 实例
    auto document = MakeObject<Document>();

    // 向 Document 的页面集合添加页面
    auto page = document->get_Pages()->Add();

    // 创建 TextBuilder 实例
    auto builder = MakeObject<TextBuilder>(page);

    // 实例化 TextParagraph 实例
    auto paragraph = MakeObject<TextParagraph>();

    // 创建 TextState 实例以指定字体名称和大小
    auto state = MakeObject<TextState>("Arial", 12);

    // 指定字符间距
    state->set_CharacterSpacing(1.5f);

    // 将文本追加到 TextParagraph 对象
    paragraph->AppendLine(u"这是具有字符间距的段落", state);

    // 指定 TextParagraph 的位置
    paragraph->set_Position(MakeObject<Position>(100, 550));

    // 将 TextParagraph 追加到 TextBuilder 实例
    builder->AppendParagraph(paragraph);

    // 保存生成的 PDF 文档。
    document->Save(_dataDir + outputFileName);
}
```

### 使用文字印章

```cpp
void CharacterSpacing_TextStamp() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("CharacterSpacingUsingTextStamp_out.pdf");
    // 创建文档实例
    auto document = MakeObject<Document>();

    // 向文档的页面集合中添加页面    
    auto page = document->get_Pages()->Add();

    // 使用示例文本实例化 TextStamp 实例
    auto stamp = MakeObject<TextStamp>("这是带有字符间距的文字印章");

    // 为印章对象指定字体名称
    stamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    // 为 TextStamp 指定字体大小
    stamp->get_TextState()->set_FontSize(12);
    // 将字符间距指定为 1f
    stamp->get_TextState()->set_CharacterSpacing(1.0f);
    // 设置印章的 XIndent
    stamp->set_XIndent(100);
    // 设置印章的 YIndent
    stamp->set_YIndent(500);
    // 将文本印章添加到页面实例
    stamp->Put(page);
    // 保存生成的 PDF 文档。
    document->Save(_dataDir + outputFileName);
}
```

## 创建多栏 PDF 文档

本主题展示如何使用 Aspose.Pdf for C++ 创建多栏 PDF。

今天，我们经常看到新闻以多栏形式显示在单独的页面上，而不是在书籍中，其中的文本段落大多从左到右打印在所有页面上。许多文档处理应用程序，如 Microsoft Word 和 Adobe Acrobat Writer，允许用户在单个页面上创建多列，然后向其中添加数据。

Aspose.Pdf for C++ 也提供了在 PDF 文档页面中创建多栏的功能。要创建带有多列的 PDF，我们可以使用 [Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box) 类，因为它提供了一个 ColumnInfo.ColumnCount 属性来指定 FloatingBox 内列的数量，我们还可以分别使用 ColumnInfo.ColumnSpacing 和 ColumnInfo.ColumnWidths 指定列间距和列宽度。

下面给出了一个示例，展示了如何创建包含图形对象（线条）的两列，并将它们添加到 FloatingBox 的段落集合中，然后添加到 Page 实例的段落集合中。

```cpp
void CreateMultiColumn() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("CreateMultiColumnPdf_out.pdf");

    // 创建新的文档实例
    auto document = MakeObject<Document>();

    // 指定PDF文件的左边距信息
    document->get_PageInfo()->get_Margin()->set_Left(40);

    // 指定PDF文件的右边距信息
    document->get_PageInfo()->get_Margin()->set_Right(40);

    // 添加页面到PDF文件的页面集合中
    auto page = document->get_Pages()->Add();

    auto graph1 = MakeObject<Aspose::Pdf::Drawing::Graph>(500, 2);

    // 将线条添加到段落集合中
    page->get_Paragraphs()->Add(graph1);

    // 指定线条的坐标
    auto posArr = MakeArray<float>({ 1, 2, 500, 2 });
    auto l1 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr);
    graph1->get_Shapes()->Add(l1);

    // 创建包含HTML标签的字符串变量
    String s ("<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">\
<strong> 如何避免金钱诈骗</<strong> </span>");

    // 创建包含HTML文本的文本段落

    auto heading_text = MakeObject<HtmlFragment>(s);
    page->get_Paragraphs()->Add(heading_text);

    auto box = MakeObject<FloatingBox>();

    // 在节中添加四列
    box->get_ColumnInfo()->set_ColumnCount(2);
    // 设置列之间的间距
    box->get_ColumnInfo()->set_ColumnSpacing(u"5");

    box->get_ColumnInfo()->set_ColumnWidths(u"105 105");
    auto text1 = MakeObject<TextFragment>("By A Googler (The Official Google Blog)");
    text1->get_TextState()->set_FontSize(8);
    text1->get_TextState()->set_LineSpacing(2);
    text1->get_TextState()->set_FontSize(10);
    text1->get_TextState()->set_FontStyle(FontStyles::Italic);

    box->get_Paragraphs()->Add(text1);

    // 创建图形对象以绘制线条
    auto graph2 = MakeObject<Aspose::Pdf::Drawing::Graph>(50, 10);
    // 指定线条的坐标
    auto posArr2 = MakeArray<float>({ 1, 10, 100, 10 });

    auto l2 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr2);
    graph2->get_Shapes()->Add(l2);

    // 将线条添加到段落集合中
    box->get_Paragraphs()->Add(graph2);

    auto text2 = MakeObject<TextFragment>(
        "Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. \
        Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue.\
        Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur \
        ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean \
        posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. \
        Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, \
        risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam \
        luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, \
        sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, \
        pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut,\
        iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus \
        mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla.\
        Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam,\
        iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique\
        ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\
        Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. \
        Praesent porttitor turpis eleifend ante. Morbi sodales.");
    box->get_Paragraphs()->Add(text2);

    page->get_Paragraphs()->Add(box);

    // 保存PDF文件
    document->Save(_dataDir + outputFileName);
}
```

## 使用自定义制表位

制表位是一个用于制表的停止点。在文字处理过程中，每行包含若干个以固定间隔放置的制表位（例如，每半英寸）。然而，它们可以被更改，因为大多数文字处理器允许您在任何需要的地方设置制表位。当您按下 Tab 键时，光标或插入点跳到下一个制表位，这个制表位本身是不可见的。虽然制表位不存在于文本文件中，但文字处理器会跟踪它们，以便能够对 Tab 键做出正确的反应。

以下是设置自定义制表位的示例。

```cpp
void CustomTabStops() {
    String _dataDir("C:\\Samples\\");
    String outputFileName("CustomTabStops_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto ts = MakeObject<TabStops>();
    auto ts1 = ts->Add(100);

    ts1->set_AlignmentType(TabAlignmentType::Right);
    ts1->set_LeaderType(TabLeaderType::Solid);

    auto ts2 = ts->Add(200);
    ts2->set_AlignmentType(TabAlignmentType::Center);
    ts2->set_LeaderType(TabLeaderType::Dash);

    auto ts3 = ts->Add(300);
    ts3->set_AlignmentType(TabAlignmentType::Left);
    ts3->set_LeaderType(TabLeaderType::Dot);

    auto header = MakeObject<TextFragment>("这是一个使用制表位形成表格的示例", ts);
    auto text0 =  MakeObject<TextFragment>("#$TABHead1 #$TABHead2 #$TABHead3", ts);

    auto text1 = MakeObject<TextFragment>("#$TABdata11 #$TABdata12 #$TABdata13", ts);
    auto text2 = MakeObject<TextFragment>("#$TABdata21 ", ts);
    text2->get_Segments()->Add(MakeObject<TextSegment>("#$TAB"));
    text2->get_Segments()->Add(MakeObject<TextSegment>("data22 "));
    text2->get_Segments()->Add(MakeObject<TextSegment>("#$TAB"));
    text2->get_Segments()->Add(MakeObject<TextSegment>("data23"));
              
    page->get_Paragraphs()->Add(header);
    page->get_Paragraphs()->Add(text0);
    page->get_Paragraphs()->Add(text1);
    page->get_Paragraphs()->Add(text2);

    document->Save(_dataDir + outputFileName);
}
```

## 如何在 PDF 中添加透明文本

PDF 1.4（Acrobat 5 支持的文件格式）是第一个支持透明度的 PDF 版本。这个 PDF 大约在 Adobe Illustrator 9 推出时进入市场。

一个 PDF 文件包含图像、文本、图形、附件、注释对象，在创建 TextFragment 时，可以设置前景色、背景色信息以及文本格式。Aspose.PDF for C++ 支持添加具有 Alpha 颜色通道的文本功能。以下代码片段显示了如何添加具有透明颜色的文本。

```cpp
void AddTransparentText() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("AddTransparentText_out.pdf");

    // 创建 Document 实例
    auto document = MakeObject<Document>();    
    // 创建 PDF 文件的页面集合
    auto page = document->get_Pages()->Add();

    // 创建 Graph 对象
    auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

    // 创建具有特定尺寸的矩形实例
    auto rect = MakeObject<Aspose::Pdf::Drawing::Rectangle>(100, 100, 400, 400);
    // 从 Alpha 颜色通道创建颜色对象
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;

    auto alphaColor = Color::FromArgb(alpha, red, green, blue);

    rect->get_GraphInfo()->set_FillColor(alphaColor);

    // 将矩形添加到 Graph 对象的形状集合
    canvas->get_Shapes()->Add(rect);

    // 将图形对象添加到页面对象的段落集合
    page->get_Paragraphs()->Add(canvas);

    // 设置值以不更改图形对象的位置
    canvas->set_IsChangePosition(false);

    // 创建具有示例值的 TextFragment 实例
    auto text = MakeObject<TextFragment>(
        "transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text ");
    // 从 Alpha 通道创建颜色对象
    alpha = 30;
    alphaColor = Color::FromArgb(alpha, red, green, blue);
    // 为文本实例设置颜色信息
    text->get_TextState()->set_ForegroundColor(alphaColor);
    // 将文本添加到页面实例的段落集合
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## 为字体指定行间距

[Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) 类有一个枚举 [LineSpacingMode](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91)，这是为特定字体设计的，例如输入字体 "HPSimplified.ttf"。此外，类 [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) 有一个类型为 LineSpacingMode 的属性 [LineSpacing](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91a9e120eead36071a90367e425c96b5eaf)。您只需要将 LineSpacing 设置为 LineSpacingMode.FullSize。为了正确显示字体，代码片段如下所示：

```cpp
void SpecifyLineSpacingForFonts() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("SpecifyLineSpacing_out.pdf");

    String fontFile ("hp-simplified-265.ttf");

    // 加载输入 PDF 文件
    auto document = MakeObject<Document>();
    
    // 创建具有 LineSpacingMode.FullSize 的 TextFormattingOptions
    auto formattingOptions = MakeObject<TextFormattingOptions>();
    formattingOptions->set_LineSpacing(TextFormattingOptions::LineSpacingMode::FullSize);
    
    // 使用示例字符串创建文本片段
    auto textFragment = MakeObject<TextFragment>("Hello world");

    // 将 TrueType 字体加载到流对象中
    auto fontStream = System::IO::File::OpenRead(_dataDir + fontFile);
    
    // 设置文本字符串的字体名称
    textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
    // 指定文本片段的位置
    textFragment->set_Position(MakeObject<Position>(100, 600));
    // 将当前片段的 TextFormattingOptions 设置为预定义的（指向
    // LineSpacingMode.FullSize）
    textFragment->get_TextState()->set_FormattingOptions(formattingOptions);
    
    // 将文本添加到 TextBuilder，以便它可以被放置在 PDF 文件上    
    auto page = document->get_Pages()->Add();
    page->get_Paragraphs()->Add(textFragment);

    // 保存生成的 PDF 文档
    document->Save(_dataDir + outputFileName);
}
```

## 动态获取文本宽度

[Aspose.Pdf.Text.TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) 类展示了如何在 PDF 文档中动态获取文本宽度。

有时候，需要动态获取文本宽度。Aspose.PDF for C++ 包含两种用于测量字符串宽度的方法。您可以调用 Aspose.Pdf.Text.Font 或 Aspose.Pdf.Text.TextState 类（或同时调用）的 [MeasureString](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state#a084c1781028cd3483c82b4fd4cec4967) 方法。下面的代码片段展示了如何使用此功能。

```cpp
void GetTextWidthDynamicaly() {
    auto font = FontRepository::FindFont(u"Arial");
    auto ts = MakeObject<TextState>();

    ts->set_Font(font);
    ts->set_FontSize(14);

    if (Math::Abs(font->MeasureString(u"A", 14) - 9.337) > 0.001)
        Console::WriteLine(u"Unexpected font string measure!");

    if (Math::Abs(ts->MeasureString(u"z") - 7.0) > 0.001)
        Console::WriteLine(u"Unexpected font string measure!");

    for (char c = 'A'; c <= 'z'; c++) {
        String v(c);
        double fnMeasure = font->MeasureString(v, 14);
        double tsMeasure = ts->MeasureString(v);

        if (Math::Abs(fnMeasure - tsMeasure) > 0.001)
            Console::WriteLine(u"Font and state string measuring doesn't match!");
    }
}
```