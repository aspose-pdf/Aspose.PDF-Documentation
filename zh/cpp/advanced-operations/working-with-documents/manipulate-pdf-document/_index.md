---
title: Manipulate PDF Document 
linktitle: Manipulate PDF Document
type: docs
weight: 30
url: /zh/cpp/manipulate-pdf-document/
lastmod: "2021-11-11"
description: 本节解释了关于验证 PDF A 标准的 PDF 文档，如何使用目录，如何设置 PDF 到期日期，以及如何确定 PDF 文件生成的进度。
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 验证 PDF A 标准 (A 1A 和 A 1B) 的 PDF 文档

要验证 PDF/A-1a 或 PDF/A-1b 兼容性的 PDF 文档，请使用 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 类的 [Validate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aa1ac4565b320807c718c44eeee7cda8c) 方法。此方法允许您指定结果要保存的文件名和所需的验证类型 [PdfFormat](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ac83739fd7c818167c2fdc4dd554de763) 枚举：PDF_A_1A 或 PDF_A_1B。

{{% alert color="primary" %}}

输出的XML格式是自定义的Aspose格式。XML包含一组名为Problem的标签；每个标签包含特定问题的详细信息。Problem标签的ObjectID属性表示与此问题相关的特定对象的ID。Clause属性表示PDF规范中的相应规则。

{{% /alert %}}

以下代码片段展示了如何验证PDF文档的PDF/A-1A标准。

```cpp
void ExampleValidate01() {
    // 路径名的字符串。
    String _dataDir("C:\\Samples\\");

    // 文件名的字符串。
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1A.xml");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // 验证PDF的PDF/A-1a
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1A);
}
```

以下代码片段展示了如何验证PDF文档的PDF/A-1B标准。

```cpp
void ExampleValidate02() {
    // 路径名的字符串。
    String _dataDir("C:\\Samples\\");

    // 文件名的字符串。
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1B.xml");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // 验证PDF的PDF/A-1a
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1B);
}
```

## 目录操作

### 向现有 PDF 添加目录

Aspose.PDF API 允许您在创建 PDF 时或对现有文件添加目录。

要向现有 PDF 文件添加目录，请使用 Aspose.Pdf 命名空间中的 [Heading](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.heading) 类。Aspose.Pdf 命名空间允许您创建新的 PDF 文件并操作现有的 PDF 文件。要向现有 PDF 添加目录，请使用 Aspose.Pdf 命名空间。

以下代码片段展示了如何在现有 PDF 文件中创建目录。

```cpp
void ExampleToc01() {
    // 路径名的字符串。
    String _dataDir("C:\\Samples\\");

    // 文件名的字符串
    String inputFileName("AddTOC.pdf");
    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 获取 PDF 文件的第一页
    auto tocPage = document->get_Pages()->Insert(1);

    // 创建对象以表示目录信息
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("目录");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // 设置目录的标题
    tocInfo->set_Title(title);
    tocPage->set_TocInfo(tocInfo);

    // 创建将用作目录元素的字符串对象
    auto titles = MakeArray<String>(4);
    titles->SetValue(u"第一页", 0);
    titles->SetValue(u"第二页", 1);
    titles->SetValue(u"第三页", 2);
    titles->SetValue(u"第四页", 3);

    for (int i = 0; i < 2; i++)
    {
        // 创建标题对象
        auto heading2 = MakeObject<Heading>(1);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);

        // 指定标题对象的目标页面

        heading2->set_DestinationPage(document->get_Pages()->idx_get(i + 2));

        // 目标页面
        heading2->set_Top(document->get_Pages()->idx_get(i + 2)->get_Rect()->get_Height());

        // 目标坐标
        segment2->set_Text(titles[i]);

        // 将标题添加到包含目录的页面
        tocPage->get_Paragraphs()->Add(heading2);
    }

    // 保存更新后的文档
    document->Save(_dataDir + outputFileName);
}
```

### 为不同的目录级别设置不同的TabLeaderType

Aspose.PDF for C++还允许为不同的目录级别设置不同的TabLeaderType。您需要为FormatArray的LineDash属性设置TabLeaderType的适当值。接下来，您可以将列表部分添加到Pdf文档的部分集合中。之后，在Pdf文档中创建一个部分并保存PDF文件。

```cpp
void ExampleToc02() {
    // 路径名的字符串。
    String _dataDir("C:\\Samples\\");

    // 文件名的字符串。
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto tocPage = document->get_Pages()->Add();
    auto tocInfo = MakeObject<TocInfo>();

    //设置LeaderType
    tocInfo->set_LineDash(TabLeaderType::Solid);

    // 创建对象以表示目录信息
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // 设置目录的标题
    tocInfo->set_Title(title);

    //将列表部分添加到Pdf文档的部分集合中
    tocPage->set_TocInfo(tocInfo);

    //通过设置左边距和
    //每个级别的文本格式设置定义四级列表的格式

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Left(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(0)->set_LineDash(TabLeaderType::Dot);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(10);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(1)->set_LineDash(TabLeaderType::None);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Left(20);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->set_LineDash(TabLeaderType::Solid);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    //在Pdf文档中创建一个部分
    auto page = document->get_Pages()->Add();

    //在该部分添加四个标题
    for (int Level = 1; Level <= 4; Level++)
    {
    auto heading2 = MakeObject<Heading>(Level);
    auto segment2 = MakeObject<TextSegment>();

    heading2->get_Segments()->Add(segment2);
    heading2->set_IsAutoSequence(true);
    heading2->set_TocPage(tocPage);
    segment2->set_Text(u"Sample Heading" + Level);
    heading2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial Unicode MS"));

    //将标题添加到目录中。
    heading2->set_IsInList(true);
    page->get_Paragraphs()->Add(heading2);
    }

    // 保存Pdf
    document->Save(_dataDir + outputFileName);
}
```

### 在目录中隐藏页码

如果要在目录中隐藏页码和标题，可以将 [TOCInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info) 类的 [IsShowPageNumbers](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info#ada10e841699bba062dcd0b440c26b832) 属性设置为 false。

请查看以下代码片段以在目录中隐藏页码：

```cpp
void ExampleToc03() {
    // 路径名称的字符串。
    String _dataDir("C:\\Samples\\");

    // 文件名称的字符串。
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto tocPage = document->get_Pages()->Add();

    // 创建对象以表示目录信息
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // 设置目录的标题
    tocInfo->set_Title(title);

    //将列表部分添加到 Pdf 文档的部分集合中
    tocPage->set_TocInfo(tocInfo);

    tocInfo->set_IsShowPageNumbers(false);

    //通过设置左边距和每个级别的文本格式设置来定义四级列表的格式

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_Underline(true);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    auto page = document->get_Pages()->Add();
    //在部分添加四个标题
    for (int Level = 1; Level != 5; Level++)
    {
        auto heading2 = MakeObject<Heading>(Level);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);
        heading2->set_IsAutoSequence(true);
        segment2->set_Text(u"this is heading of level " + Level);
        heading2->set_IsInList(true);
        page->get_Paragraphs()->Add(heading2);
    }
    // 保存 Pdf
    document->Save(_dataDir + outputFileName);
}
```

## 如何设置PDF过期日期

我们在PDF文件上应用访问权限，以便特定用户组可以访问PDF文档的特定功能/对象。为了限制PDF文件访问，我们通常应用加密，并且可能需要设置PDF文件的过期日期，以便用户在访问/查看文档时获得有关PDF文件到期的有效提示。

为了实现上述要求，我们可以使用[JavascriptAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.javascript_action/)对象。请查看以下代码片段。

```cpp
void SetPDFexpiryDate() {

    // 文件路径字符串。
    String _dataDir("C:\\Samples\\");

    // 文件名字符串。
    String outputFileName("SetExpiryDate_out.pdf");

    // 实例化Document对象
    auto document = MakeObject<Document>();

    // 向PDF文件的页面集合添加页面
    document->get_Pages()->Add();

    // 向页面对象的段落集合中添加文本片段
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(new TextFragment(u"Hello World..."));

    String javascriptCode(u"var year=2017;");
    javascriptCode += u"var month=5;";
    javascriptCode += u"today = new Date(); today = new Date(today.getFullYear(), today.getMonth());";
    javascriptCode += u"expiry = new Date(year, month);";
    javascriptCode += u"if (today.getTime() > expiry.getTime())";
    javascriptCode += u"app.alert('The file is expired. You need a new one.');";

    // 创建JavaScript对象以设置PDF过期日期
    auto javaScript = MakeObject<Aspose::Pdf::Annotations::JavascriptAction>(javascriptCode);

    // 设置JavaScript作为PDF打开动作
    document->set_OpenAction(javaScript);

    // 保存PDF文档
    document->Save(_dataDir + outputFileName);
}
```

## 确定 PDF 文件生成的进度

客户要求我们添加一个功能，使开发人员能够确定 PDF 文件生成的进度。以下是对此请求的响应。

[DocSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) 类的 [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb) 字段允许您确定 PDF 生成的进展情况。

下面的代码片段展示了如何使用 [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb)。

```cpp
using ProgressHandler = System::MulticastDelegate<void(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo>)>;
void ConversionProgressCallback(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    String eventType;
    switch (eventInfo->EventType)
    {
    case ProgressEventType::ResultPageCreated:
        eventType = u"ResultPageCreated";
        break;
    case ProgressEventType::ResultPageSaved:
        eventType = u"ResultPageSaved";
        break;
    case ProgressEventType::SourcePageAnalysed:
        eventType = u"SourcePageAnalysed";
        break;
    case ProgressEventType::TotalProgress:
        eventType = u"TotalProgress";
        break;
    }
    Console::WriteLine(String::Format(u"Event type: {0}, Value: {1}, MaxValue: {2}", 
        eventType, eventInfo->Value, eventInfo->MaxValue));
}
```

```cpp
void DetermineProgressOfPDFfileGeneration() {
    // 路径名称的字符串。
    String _dataDir("C:\\Samples\\");

    // 文件名称的字符串。
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // 打开文档
    auto saveOptions = MakeObject<DocSaveOptions>();

    saveOptions->CustomProgressHandler = ProgressHandler(ConversionProgressCallback);

    document->Save(_dataDir + outputFileName, saveOptions);
}
```

## 在C++中扁平化可填写的PDF

PDF文档通常包含具有交互式可填写小部件的表单，如单选按钮、复选框、文本框、列表等。为了使其不可编辑以适应各种应用程序目的，我们需要扁平化PDF文件。
Aspose.PDF for C++ 提供了在C++中仅需几行代码即可扁平化PDF的功能：

```cpp
void FlattenFillablePDF() {
    // 路径名称的字符串。
    String _dataDir("C:\\Samples\\");
    // 文件名称的字符串。
    String inputFileName("sample-form.pdf");
    String outputFileName("FlattenForms_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 扁平化可填写的PDF
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for (auto item : document->get_Form()->get_Fields())
        item->Flatten();
    }

    // 保存更新后的文档
    document->Save(_dataDir + outputFileName);
}
```