---
title: 在PDF文件中添加文字印章
linktitle: 在PDF文件中添加文字印章
type: docs
weight: 20
url: /cpp/text-stamps-in-the-pdf-file/
description: 使用C++的TextStamp类向PDF文件添加文字印章。
lastmod: "2021-12-95"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 使用C++添加文字印章

您可以使用[TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp)类在PDF文件中添加文字印章。TextStamp类提供了创建基于文本的印章所需的属性，如字体大小、字体样式和字体颜色等。为了添加文字印章，您需要使用所需的属性创建一个Document对象和一个TextStamp对象。之后，您可以调用Page的AddStamp方法在PDF中添加印章。以下代码片段向您展示如何在PDF文件中添加文字印章。

```cpp
void AddTextStampToPDFFile() {
   
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    
    // 创建文字印章
    auto textStamp = MakeObject<TextStamp>(u"Sample Stamp");

    // 设置印章是否为背景
    textStamp->set_Background(true);
    // 设置起始位置
    textStamp->set_XIndent(100);
    textStamp->set_YIndent(100);
    // 旋转印章
    textStamp->set_Rotate(Rotation::on90);

    // 设置文本属性
    textStamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    textStamp->get_TextState()->set_FontSize(14.0F);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Bold);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Italic);
    textStamp->get_TextState()->set_ForegroundColor(Color::get_Green());
    // 将印章添加到特定页面
    document->get_Pages()->idx_get(1)->AddStamp(textStamp);

    // 保存输出文档
    document->Save(_dataDir + outputFileName);
}
```

## 定义 TextStamp 对象的对齐方式

向 PDF 文档添加水印是一项经常被要求的功能，Aspose.PDF for C++ 完全能够添加图像和文本水印。我们有一个名为 [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) 的类，它提供了在 PDF 文件上添加文本印章的功能。最近，有一个需求需要支持在使用 TextStamp 对象时指定文本的对齐方式。因此，为了满足这一需求，我们在 TextStamp 类中引入了 TextAlignment 属性。使用此属性，我们可以指定水平文本对齐方式。

以下代码片段显示了如何加载现有 PDF 文档并在其上添加 TextStamp 的示例。

```cpp
void DefineAlignmentTextStamp() {

    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    
    // 使用示例字符串实例化 FormattedText 对象
    auto text = MakeObject<Aspose::Pdf::Facades::FormattedText>("This");

    // 向 FormattedText 添加新文本行
    text->AddNewLineText(u"is sample");
    text->AddNewLineText(u"Center Aligned");
    text->AddNewLineText(u"TextStamp");
    text->AddNewLineText(u"Object");

    // 使用 FormattedText 创建 TextStamp 对象
    auto stamp = MakeObject<TextStamp>(text);
    // 指定文本印章的水平对齐方式为居中对齐
    stamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    // 指定文本印章的垂直对齐方式为居中对齐
    stamp->set_VerticalAlignment(VerticalAlignment::Center);
    // 指定 TextStamp 的文本水平对齐方式为居中对齐
    stamp->set_TextAlignment(HorizontalAlignment::Center);
    // 设置印章对象的上边距
    stamp->set_TopMargin(20);
    // 将印章添加到 PDF 文件的所有页面
    document->get_Pages()->idx_get(1)->AddStamp(stamp);

    // 保存输出文档
    document->Save(_dataDir + outputFileName);
}
```

## 在 PDF 文件中将填充描边文本作为印章

我们已经实现了文本添加和编辑场景的渲染模式设置。要渲染描边文本，请创建 TextState 对象并将 RenderingMode 设置为 TextRenderingMode.StrokeText，同时选择 StrokingColor 属性的颜色。之后，使用 BindTextState() 方法将 TextState 绑定到印章。

以下代码示例演示了如何添加填充描边文本：

```cpp
void FillStrokeTextAsStampInPDFFile() {

    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // 创建 TextState 对象以传输高级属性
    auto ts = MakeObject<TextState>();

    // 设置描边颜色
    ts->set_StrokingColor(Color::get_Gray());

    // 设置文本渲染模式
    ts->set_RenderingMode(TextRenderingMode::StrokeText);

    // 加载输入 PDF 文档
    auto fileStamp = MakeObject<Aspose::Pdf::Facades::PdfFileStamp>(MakeObject<Document>(_dataDir + inputFileName));

    auto stamp = MakeObject<Aspose::Pdf::Facades::Stamp>();

    auto formattedText = MakeObject<Aspose::Pdf::Facades::FormattedText>(u"PAID IN FULL", Color::get_Gray(), Aspose::Pdf::Facades::EncodingType::Winansi, true, 78);
    stamp->BindLogo(formattedText);

    // 绑定 TextState
    stamp->BindTextState(ts);

    // 设置 X,Y 原点
    stamp->SetOrigin(100, 100);
    stamp->set_Opacity(5);
    stamp->set_BlendingSpace(Aspose::Pdf::Facades::BlendingColorSpace::DeviceRGB);
    stamp->set_Rotation(45.0F);
    stamp->set_IsBackground(false);

    // 添加印章
    fileStamp->AddStamp(stamp);
    fileStamp->Save(_dataDir + outputFileName);
    fileStamp->Close();
}
```