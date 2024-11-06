---
title: 将PDF文件转换为HTML格式 
linktitle: 将PDF文件转换为HTML格式
type: docs
weight: 50
url: zh/cpp/convert-pdf-to-html/
lastmod: "2021-11-19"
description: 本主题向您展示如何使用C++库的Aspose.PDF将PDF文件转换为HTML格式。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for C++** 提供了许多功能，可以将各种文件格式转换为PDF文档，并将PDF文件转换为各种输出格式。本文讨论了如何将PDF文件转换为<abbr title="HyperText Markup Language">HTML</abbr>。Aspose.PDF for C++ 提供了使用InLineHtml方法将HTML文件转换为PDF格式的功能。我们收到许多关于将PDF文件转换为HTML格式的功能请求，并提供了此功能。请注意，此功能还支持XHTML 1.0。

**Aspose.PDF for C++** 支持将PDF文件转换为HTML的功能。 主要任务如下，您可以使用 Aspose.PDF 库完成：

- 将 PDF 转换为 HTML；
- 将输出拆分为多页 HTML；
- 指定用于存储 SVG 文件的文件夹；
- 在转换过程中压缩 SVG 图像；
- 指定图像文件夹；
- 仅创建包含正文内容的后续文件；
- 透明文本渲染；
- PDF 文档层渲染。

Aspose.PDF for C++ 提供了一个两行代码，用于将源 PDF 文件转换为 HTML。`SaveFormat enumeration` 包含值 Html，允许您将源文件保存为 HTML。以下代码片段显示了将 PDF 文件转换为 HTML 的过程。

```cpp
void ConvertPDFtoHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名的字符串
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // 以 HTML 格式保存输出
    document->Save(outfilename, SaveFormat::Html);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="success" %}}
**尝试在线将PDF转换为HTML**

Aspose.PDF for C++为您提供在线免费应用程序["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)，您可以在其中尝试研究其功能和工作质量。

[![Aspose.PDF转换PDF到HTML与免费应用程序](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

## 将输出拆分为多页HTML

当将包含多个页面的大型PDF文件转换为HTML格式时，输出显示为单个HTML页面。它可能会变得非常长。为了控制页面大小，可以在PDF到HTML转换过程中将输出拆分为多个页面。请尝试使用以下代码片段。

```cpp
void ConvertPDFtoHTML_SplittingOutputToMultiPageHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名的字符串
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 实例化HTML保存选项对象
    auto htmlOptions = MakeObject<HtmlSaveOptions>();
    // 指定将输出拆分为多个页面
    htmlOptions->set_SplitIntoPages(true);

    try {
    // 以HTML格式保存输出
    document->Save(_dataDir + outfilename, htmlOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 指定存储SVG文件的文件夹

在PDF到HTML的转换过程中，可以指定SVG图像应保存到的文件夹。使用[`HtmlSaveOption class`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options) [`SpecialFolderForSvgImages property`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#ac1bb3905c599118fb3db67fd67a5a06f)来指定一个特殊的SVG图像目录。此属性获取或设置在转换过程中遇到的SVG图像必须保存到的目录路径。如果参数为空或为null，那么任何SVG文件将与其他图像文件一起保存。

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringSVGfiles()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名的字符串
    String infilename("sample.pdf");
    String outfilename("SaveSVGFiles_out.html");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 实例化HTML保存选项对象
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // 指定在PDF到HTML转换过程中保存SVG图像的文件夹
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // 以HTML格式保存输出
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 在转换过程中压缩SVG图像

要在将PDF转换为HTML的过程中压缩SVG图像，请尝试使用以下代码：

```cpp
void ConvertPDFtoHTML_CompressingSVGimages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名称的字符串
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 实例化HTML保存选项对象
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // 指定在PDF到HTML转换过程中保存SVG图像的文件夹
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // 以HTML格式保存输出
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 指定图像文件夹

我们还可以指定在PDF转换为HTML的过程中图像将被保存到的文件夹：

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringAllImages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名称的字符串
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 实例化HTML保存选项对象
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // 指定在PDF到HTML转换期间保存所有图像的文件夹
    htmlOptions->SpecialFolderForAllImages = (_dataDir + String("\\images\\"));

    // 保存输出为HTML格式
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Create Subsequent Files with Body Contents Only

最近，我们被要求引入一个功能，将PDF文件转换为HTML，并且用户可以仅获取每页的`<body>`标签的内容。 这将生成一个包含 CSS、`<html>`、`<head>` 详细信息的文件，以及其他文件中的所有页面仅包含 `<body>` 内容。

为了满足此要求，在 [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options) 类中引入了一个新属性 HtmlMarkupGenerationMode。

使用以下简单代码片段，您可以将输出 HTML 拆分为页面。在输出页面中，所有 HTML 对象必须准确定位在它们当前的位置（字体处理和输出、CSS 创建和输出、图像创建和输出），只是输出 HTML 将包含当前放置在标签内的内容（现在将省略“body”标签）。然而，使用这种方法时，链接到 CSS 是您的代码的责任，因为诸如将被剥离。为此，您可以通过 File.ReadAllText() 读取 CSS 并通过 AJAX 发送到一个网页，在该网页上将由 jQuery 应用。

```cpp
void ConvertPDFtoHTML_CreateSubsequentFilesWithBodyContentsOnly()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 用于路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 用于文件名的字符串
    String infilename("sample.pdf");
    String outfilename("CreateSubsequentFiles_out.html");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 实例化 HTML 保存选项对象
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->set_SplitIntoPages(true);

    // 以 HTML 格式保存输出
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## 透明文本渲染

如果源/输入 PDF 文件包含被前景图像遮挡的透明文本，则可能会出现文本渲染问题。因此，为了应对这种情况，可以使用 [SaveShadowedTextsAsTransparentTexts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#a6269cf414eb8c252f0ba64a0baf2f9ef) 和 SaveTransparentTexts 属性。

```cpp
void ConvertPDFtoHTML_TransparentTextRendering()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名的字符串
    String infilename("sample.pdf");
    String outfilename("TransparentTextRendering_out.html");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 实例化 HTML 保存选项对象
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->SaveShadowedTextsAsTransparentTexts = true;
    htmlOptions->SaveTransparentTexts = true;

    // 以 HTML 格式保存输出
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDF 文档层渲染

我们可以在 PDF 转 HTML 转换过程中，将 PDF 文档层渲染到单独的层类型元素中：

```cpp
void ConvertPDFtoHTML_DocumentLayersRendering()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名称的字符串
    String infilename("sample.pdf");
    String outfilename("LayersRendering_out.html");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 实例化 HTML 保存选项对象
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // 指定在输出 HTML 中单独渲染 PDF 文档层
    htmlOptions->set_ConvertMarkedContentToLayers(true);

    // 将输出保存为 HTML 格式
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```