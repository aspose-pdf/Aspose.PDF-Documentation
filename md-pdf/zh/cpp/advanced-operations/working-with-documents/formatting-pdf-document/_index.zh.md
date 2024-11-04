---
title: 格式化 PDF 文档使用 C++
linktitle: 格式化 PDF 文档
type: docs
weight: 20
url: /cpp/formatting-pdf-document/
description: 使用 Aspose.PDF for C++ 创建和格式化 PDF 文档。使用下面的代码片段来解决您的任务。
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 格式化 PDF 文档

### 获取文档窗口和页面显示属性

本主题帮助您了解如何获取文档窗口、查看器应用程序的属性，以及如何显示页面。要设置这些属性，请使用 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 类打开 PDF 文件。现在您可以设置 Document 对象的属性，例如：

- CenterWindow – 在屏幕上居中显示文档窗口。默认值：false。
- Direction – 阅读顺序。这决定了当页面并排显示时如何布局。默认值：从左到右。
- DisplayDocTitle – 在文档窗口标题栏中显示文档标题。 默认: false (标题显示)。
- HideMenuBar – 隐藏或显示文档窗口的菜单栏。默认: false (菜单栏显示)。
- HideToolBar – 隐藏或显示文档窗口的工具栏。默认: false (工具栏显示)。
- HideWindowUI – 隐藏或显示文档窗口元素，如滚动条。默认: false (UI元素显示)。
- NonFullScreenPageMode – 文档在非全屏模式下的显示方式。
- PageLayout – 页面布局。
- PageMode – 文档首次打开时的显示方式。选项包括显示缩略图、全屏、显示附件面板。

以下代码片段展示了如何使用[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)类获取属性。

```cpp
void GetDocumentWindowAndPageDisplayProperties()
{
    // 路径名称的字符串。
    String _dataDir("C:\\Samples\\");
    // 文件名的字符串。
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // 获取不同的文档属性
    // 文档窗口的位置 - 默认: false
    Console::WriteLine(u"CenterWindow : {0}", document->get_CenterWindow());

    // 主要阅读顺序；确定页面的位置
    // 并排显示时 - 默认: L2R
    Console::WriteLine(u"Direction : {0}", document->get_Direction());

    // 窗口标题栏是否显示文档标题
    // 如果为false，标题栏显示PDF文件名 - 默认: false
    Console::WriteLine(u"DisplayDocTitle : {0}", document->get_DisplayDocTitle());

    // 是否调整文档窗口大小以适应
    // 首次显示的页面大小 - 默认: false
    Console::WriteLine(u"FitWindow : {0}", document->get_FitWindow());

    // 是否隐藏查看器应用程序的菜单栏 - 默认: false
    Console::WriteLine(u"HideMenuBar : {0}", document->get_HideMenubar());

    // 是否隐藏查看器应用程序的工具栏 - 默认: false
    Console::WriteLine(u"HideToolBar : {0}", document->get_HideToolBar());

    // 是否隐藏UI元素，如滚动条
    // 仅显示页面内容 - 默认: false
    Console::WriteLine(u"HideWindowUI : {0}", document->get_HideWindowUI());

    // 文档的页面模式。退出全屏模式时如何显示文档。
    Console::WriteLine(u"NonFullScreenPageMode : {0}", document->get_NonFullScreenPageMode());

    // 页面布局，即单页、一列
    Console::WriteLine(u"PageLayout : {0}", document->get_PageLayout());

    // 文档打开时的显示方式
    // 即显示缩略图、全屏、显示附件面板
    Console::WriteLine(u"pageMode : {0}", document->get_PageMode());
}
```
### 设置文档窗口和页面显示属性

本主题介绍如何设置文档窗口、查看器应用程序和页面显示的属性。要设置这些不同的属性：

1. 使用 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 类打开 PDF 文件。
1. 设置不同的文档属性：

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

1. 使用 Save 方法 [保存](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) 更新后的 PDF 文件。

可用的属性有：

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

每个属性在下面的代码中使用和描述。 以下代码片段向您展示如何使用[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)类设置属性。

```cpp
void SetDocumentWindowAndPageDisplayProperties()
{
    // 路径名称的字符串。
    String _dataDir("C:\\Samples\\");
    // 文件名的字符串。
    String inputFileName("sample.pdf");
    String outputFileName("sample_page_display_properties.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // 设置不同的文档属性
    // 指定文档窗口的位置 - 默认值: false
    document->set_CenterWindow(true);

    // 主要阅读顺序；决定页面的位置
    // 并排显示时 - 默认值: L2R
    document->set_Direction(Direction::R2L);

    // 指定窗口的标题栏是否应显示文档标题
    // 如果为false，标题栏显示PDF文件名 - 默认值: false
    document->set_DisplayDocTitle(true);

    // 指定是否调整文档窗口的大小以适应
    // 首次显示的页面的大小 - 默认值: false
    document->set_FitWindow(true);

    // 指定是否隐藏查看器应用程序的菜单栏 - 默认值: false
    document->set_HideMenubar(true);

    // 指定是否隐藏查看器应用程序的工具栏 - 默认值: false
    document->set_HideToolBar(true);

    // 指定是否隐藏UI元素如滚动条
    // 仅显示页面内容 - 默认值: false
    document->set_HideWindowUI(true);

    // 文档的页面模式。指定在退出全屏模式时如何显示文档。
    document->set_NonFullScreenPageMode(PageMode::UseOC);

    // 指定页面布局，即单页，一列
    document->set_PageLayout(PageLayout::TwoColumnLeft);

    // 指定文档打开时应如何显示
    // 即显示缩略图，全屏，显示附件面板
    document->set_PageMode(PageMode::UseThumbs);

    // 保存更新后的PDF文件
    document->Save(_dataDir + outputFileName);
}
```
### 嵌入字体到现有的PDF文件中

PDF阅读器支持[14种核心字体](https://en.wikipedia.org/wiki/PDF#Text)，以便无论文件在哪个平台上显示，文档都可以以相同的方式显示。当PDF包含的字体不是14种核心字体之一时，需要将字体嵌入到PDF文件中以避免字体替换。

Aspose.PDF for C++支持在现有PDF文件中嵌入字体。您可以嵌入完整字体或字体的子集。要嵌入字体，请使用[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)类打开PDF文件。然后使用[Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.font)类将字体嵌入到PDF文件中。要嵌入完整字体，使用Font类的IsEmbeded属性；要使用字体的子集，使用IsSubset属性。

{{% alert color="primary" %}}

字体子集仅嵌入使用到的字符，在字体用于短句或标语时非常有用，例如企业字体用于标志但不是正文时。 使用子集可以减少输出 PDF 的文件大小。然而，如果为正文使用自定义字体，请将其完整嵌入。

以下代码片段展示了如何在 PDF 文件中嵌入字体。
{{% /alert %}}

### 嵌入标准 Type 1 字体

有些 PDF 文档使用来自一个特殊集合的字体，这些字体被称为“标准 Type 1 字体”。这个集合包含 14 种字体，嵌入这种类型的字体需要使用特殊的标志，即 [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a8f1a88eef22e05ee9ee22a79db9cb9f6)。

以下是可以用来获得包含所有嵌入字体的文档的代码片段，包括标准 Type 1 字体：

```cpp
void EmbeddingStandardType1Fonts()
{

    // 用于路径名称的字符串。
    String _dataDir("C:\\Samples\\");
    // 用于文件名的字符串。
    String inputFileName("sample.pdf");
    String outputFileName("embedded-fonts-updated_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // 设置文档的 EmbedStandardFonts 属性
    document->set_EmbedStandardFonts(true);
    for (auto page : document->get_Pages())
    {
        auto fonts = page->get_Resources()->get_Fonts();
        if (fonts != nullptr)
        {
            for (auto pageFont : fonts)
            {
                // 检查字体是否已嵌入
                if (!pageFont->get_IsEmbedded())
                {
                    pageFont->set_IsEmbedded(true);
                }
            }
        }
    }
    document->Save(_dataDir + outputFileName);
}
```
### 创建 PDF 时嵌入字体

如果您需要使用 Adobe Reader 支持的 14 种核心字体以外的任何字体，则必须在生成 Pdf 文件时嵌入字体描述。如果字体信息没有嵌入，Adobe Reader 会从操作系统中获取它（如果它已安装在系统上），或者根据 Pdf 中的字体描述构造一个替代字体。

>请注意，嵌入的字体必须安装在主机上，即在以下代码中 'Univers Condensed' 字体已安装在系统上。

我们使用 Font 类的 IsEmbedded 属性将字体信息嵌入到 Pdf 文件中。将此属性的值设置为 ‘True’ 会将完整的字体文件嵌入到 Pdf 中，知道这会增加 Pdf 文件的大小。以下是可用于将字体信息嵌入到 Pdf 的代码片段。

```cpp
void EmbeddingFontsWhileCreatingPDF()
{
    // 路径名称的字符串。
    String _dataDir("C:\\Samples\\");
    // 文件名称的字符串。
    String inputFileName("sample.pdf");
    String outputFileName("EmbedFontWhileDocCreation_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // 在 Pdf 对象中创建一个部分
    auto page = document->get_Pages()->Add();

    auto fragment = MakeObject<TextFragment>("");
    auto segment = MakeObject <TextSegment>(u"This is a sample text using Custom font.");

    auto ts = MakeObject<TextState>();

    ts->set_Font(FontRepository::FindFont(u"Arial"));
    ts->get_Font()->set_IsEmbedded(true);
    segment->set_TextState(ts);
    fragment->get_Segments()->Add(segment);
    page->get_Paragraphs()->Add(fragment);

    // 保存 PDF 文档
    document->Save(_dataDir);
}
```

### 保存 PDF 时设置默认字体名称

当 PDF 文档中包含的字体在文档本身和设备上不可用时，API 会将这些字体替换为默认字体。当字体可用时（已安装在设备上或嵌入到文档中），输出 PDF 应该具有相同的字体（不应替换为默认字体）。默认字体的值应包含字体的名称（而不是字体文件的路径）。Apose.PDF for C++ 实现了一个功能，可以在将文档保存为 PDF 时设置默认字体名称。以下代码片段可以用来设置默认字体：

```cpp
void SetDefaultFontNameWhileSavingPDF()
{
    // 路径名的字符串。
    String _dataDir("C:\\Samples\\");
    // 文件名的字符串。
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);

    auto pdfSaveOptions = MakeObject<PdfSaveOptions>();

    // 指定默认字体名称
    pdfSaveOptions->set_DefaultFontName(newName);
    document->Save(_dataDir + outputFileName, pdfSaveOptions);
}
```

### 获取 PDF 文档中的所有字体

如果您想从 PDF 文档中获取所有字体，可以使用 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 类中提供的 [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a2e22a508e8baef176dfc34734cf0def9).GetAllFonts() 方法。

请查看以下代码片段，以从现有 PDF 文档中获取所有字体：

```cpp
void GetAllFontsFromPDFdocument()
{
    // 路径名称的字符串。
    String _dataDir("C:\\Samples\\");
    // 文件名称的字符串。
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);
    auto fonts = document->get_FontUtilities()->GetAllFonts();
    for (auto font : fonts)
    {
        std::cerr << font->get_FontName() << std::endl;
    }
}
```

### 获取字体替代警告

Aspose.PDF for C++ 提供了一些方法来获取有关字体替代的通知，以处理字体替代情况。 代码片段如下所示如何使用相应的功能。

```cpp
void GetWarningsForFontSubstitution()
{
    // 路径名称的字符串。
    String _dataDir("C:\\Samples\\");

    // 文件名的字符串。
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    document->FontSubstitution = Aspose::Pdf::Document::FontSubstitutionHandler(OnFontSubstitution);
}
```

[OnFontSubstitution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac776d8736d430532bdaa530a36eb51a0) 方法如下所示。

```cpp
void OnFontSubstitution(Aspose::Pdf::Text::Font &font, Aspose::Pdf::Text::Font& newFont) {
    std::cout << "Warning: Font " << font.get_FontName() 
            << " was substituted with another font -> " 
            << newFont.get_FontName() << std::endl;
}
```

### 使用 FontSubsetStrategy 改进字体嵌入

可以使用 IsSubset 属性将字体作为子集嵌入，但有时您希望将完全嵌入的字体集减少到仅在文档中使用的子集。 [Aspose.Pdf.Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 具有属性 [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.i_document_font_utilities/)，其中包含方法 SubsetFonts(FontSubsetStrategy subsetStrategy)。在方法 SubsetFonts() 中，参数 subsetStrategy 有助于调整子集策略。FontSubsetStrategy 支持以下两种字体子集变体。

- SubsetAllFonts - 这将对子集中使用的所有字体。
- SubsetEmbeddedFontsOnly - 这将仅对子集中完全嵌入到文档中的字体。

以下代码片段显示了如何设置 FontSubsetStrategy：

```cpp
void ImproveFontsEmbeddingUsingFontSubsetStrategy()
{
    // 用于路径名称的字符串。
    String _dataDir("C:\\Samples\\");

    // 用于文件名的字符串。
    String inputFileName("sample.pdf");
    // 用于文件名的字符串。
    String outputFileName("sample_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    // 在 SubsetAllFonts 的情况下，所有字体都将作为子集嵌入到文档中。
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetAllFonts);
    // 将为完全嵌入的字体嵌入字体子集，但未嵌入到文档中的字体将不受影响。
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetEmbeddedFontsOnly);
    document->Save(_dataDir + outputFileName);
}
```
### 获取和设置 PDF 文件的缩放因子

有时候，你可能需要设置 PDF 文档的缩放因子。使用 Aspose.PDF for C++，你可以通过 Document 类的 [set_OpenAction(…) 方法](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#abb5c84979077034d06a673409b666e21) 来设置缩放因子的值。

[GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action/) 类的 Destination 属性允许你获取与 PDF 文件关联的缩放值。同样，它也可以用于设置文件的缩放因子。

#### 设置缩放因子

以下代码片段展示了如何设置 PDF 文件的缩放因子。

```cpp
void SetZoomFactor() {
    // 路径名称的字符串。
    String _dataDir("C:\\Samples\\");

    // 文件名的字符串。
    String inputFileName("sample.pdf");
    // 文件名的字符串。
    String outputFileName("Zoomed_pdf_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 0, 0, .5));

    document->set_OpenAction(action);
    // 保存文档
    document->Save(_dataDir + outputFileName);
}
```

#### 获取缩放因子

使用 Aspose.PDF for C++ 获取 PDF 文件的缩放因子。

以下代码片段显示了如何获取 PDF 文件的缩放因子：

```cpp
void GetZoomFactor() 
{
    // 路径名称的字符串。
    String _dataDir("C:\\Samples\\");

    // 文件名称的字符串。
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // 创建 GoToAction 对象
    auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(document->get_OpenAction());

    // 获取 PDF 文件的缩放因子
    auto zoom = System::DynamicCast<Aspose::Pdf::Annotations::XYZExplicitDestination>(action->get_Destination());
    Console::WriteLine(zoom->get_Zoom()); // 文档缩放值；
}
```

### 设置打印对话框预设属性

Aspose.PDF for C++ 允许设置 PDF 文档的打印对话框预设属性。 它允许您更改PDF文档的DuplexMode属性，该属性默认设置为单面。这可以通过以下两种不同的方法来实现。

```cpp
void SettingPrintDialogPresetProperties()
{
    // 路径名称的字符串。
    String _dataDir("C:\\Samples\\");
    // 文件名的字符串。
    String outputFileName("SettingPrintDialogPresetProperties.pdf");

    auto document = MakeObject<Document>();
    document->get_Pages()->Add();
    document->set_Duplex(PrintDuplex::DuplexFlipLongEdge);
    document->Save(_dataDir + outputFileName);
}
```

### 使用PDF内容编辑器设置打印对话框预设属性

```cpp
void SettingPrintDialogPresetPropertiesUsingContentEditor() {
    // 路径名称的字符串。
    String _dataDir("C:\\Samples\\");

    // 文件名的字符串。
    String inputFileName("sample.pdf");
    String outputFileName("SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto contentEditor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    contentEditor->BindPdf(outputFileName);
    if ((contentEditor->GetViewerPreference() & Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge) > 0)
    {
    std::cout << "The file has duplex flip short edge" << std::endl;
    }

    contentEditor->ChangeViewerPreference(Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge);
    contentEditor->Save(_dataDir + outputFileName);
}
```