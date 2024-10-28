---
title: 将PDF文件转换为HTML格式
linktitle: 将PDF文件转换为HTML格式
type: docs
weight: 50
url: /java/convert-pdf-to-html/
lastmod: "2021-11-19"
description: 本主题向您展示如何使用Aspose.PDF通过Java库将PDF文件转换为HTML格式。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Aspose.PDF for Java提供了许多功能，可以将各种文件格式转换为PDF文档，并将PDF文件转换为各种输出格式。本文讨论如何将PDF文件转换为HTML格式，并将PDF文件中的图像保存在特定文件夹中。

{{% alert color="success" %}}
**尝试在线将PDF转换为HTML**

Aspose.PDF for Java为您提供在线免费应用程序["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将PDF转换为HTML](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

当将包含多个页面的大型 PDF 文件转换为 HTML 格式时，输出显示为单个 HTML 页面。它可能会变得非常长。为了控制页面大小，可以在 PDF 到 HTML 转换过程中将输出拆分为多个页面。

## 将 PDF 页面转换为 HTML

Aspose.PDF for Java 提供了许多功能，用于将各种文件格式转换为 PDF 文档，并将 PDF 文件转换为各种输出格式。本文讨论如何将 PDF 文件转换为 HTML 格式，并将 PDF 文件中的图像保存到特定文件夹中。

以下代码片段展示了在将 PDF 转换为 HTML 时可以使用的所有可能选项。

```java
// 打开源 PDF 文档
Document pdfDocument = new Document(_dataDir + "PDFToHTML.pdf");

// 将文件保存为 MS 文档格式
pdfDocument.save(_dataDir + "output_out.html", SaveFormat.Html);
```

## 将 PDF 转换为 HTML - 将输出拆分为多页 HTML

Aspose.PDF for Java 支持将 PDF 文档转换为包括 HTML 在内的各种输出格式的功能。
 然而，当转换由多页组成的大型 PDF 文件时，您可能需要将每个 PDF 页保存为单独的 HTML 文件。

当将包含多页的大型 PDF 文件转换为 HTML 格式时，输出显示为单个 HTML 页面。它可能会变得非常长。为了控制页面大小，可以在 PDF 转 HTML 转换过程中将输出拆分为多个页面。请尝试使用以下代码片段。

```java
// 打开源 PDF 文档
Document document = new Document(_dataDir + "PDFToHTML.pdf");

// 实例化 HTML SaveOptions 对象
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// 指定将输出拆分为多个页面
htmlOptions.setSplitIntoPages(true);

// 保存文档
document.save(_dataDir + "MultiPageHTML_out.html", htmlOptions);    
```

## PDF 转 HTML - 避免将图像保存为 SVG 格式

从 PDF 转换为 HTML 时，保存图像的默认输出格式是 SVG。 在转换过程中，PDF中的一些图像会被转换为SVG矢量图像。这可能会很慢。相反，图像可以转换为PNG。为了实现这一点，Aspose.PDF提供了使用SVG矢量图像或创建PNG的选项。

为了在将PDF文件转换为HTML格式时完全移除图像的SVG格式渲染，请尝试使用以下代码片段。

```java
// 加载PDF文件
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// 实例化HTML保存选项对象
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// 指定在PDF到HTML转换过程中保存SVG图像的文件夹
saveOptions.setSpecialFolderForSvgImages(DATA_DIR.toString());

// 保存输出文件
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
```

## 在转换过程中压缩SVG图像

要在PDF到HTML转换过程中压缩SVG图像，请尝试使用以下代码：

```java
// 加载PDF文件
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// 创建带有测试功能的HtmlSaveOption
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// 如果有SVG图像则压缩
saveOptions.setCompressSvgGraphicsIfAny(true);
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```

## 转换 PDF 为 HTML - 指定图像文件夹

默认情况下，当将 PDF 文件转换为 HTML 时，PDF 中的图像会保存在与输出 HTML 创建的相同目录中创建的单独文件夹中。但有时，有必要在生成 HTML 文件时指定一个不同的文件夹来保存图像。为此，我们引入了 [SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions)。[SpecialFolderForAllImages 方法](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForAllImages-java.lang.String-) 用于指定存储图像的目标文件夹。

```java
// 加载 PDF 文件
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// 指定用于保存图像的单独文件夹
saveOptions.setSpecialFolderForAllImages(DATA_DIR.toString());
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```

## 创建仅包含正文内容的后续文件

通过以下简单的代码片段，您可以将输出HTML拆分为多个页面。在输出页面中，所有HTML对象必须准确地放置在它们现在的位置（字体处理和输出、CSS创建和输出、图像创建和输出），除了输出HTML将包含当前放置在标签内的内容（现在将省略“body”标签）。

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

HtmlSaveOptions saveOptions = new HtmlSaveOptions();

saveOptions.setHtmlMarkupGenerationMode(HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
saveOptions.setSplitIntoPages(true);

document.save(DATA_DIR + "CreateSubsequentFiles_out.html", saveOptions);
document.close();
```

## 透明文本渲染

如果源/输入PDF文件包含被前景图像遮挡的透明文本，则可能会出现文本渲染问题。因此，为了处理这种情况，可以使用`setSaveShadowedTextsAsTransparentTexts`和`setSaveTransparentTexts`方法。

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// 实例化HTML保存选项对象
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setSaveTransparentTexts(true);

// 保存文档
document.save(DATA_DIR + "TransparentTextRendering_out.html", htmlsaveOptions);
document.close();
```


## PDF 文档层渲染

我们可以在将 PDF 转换为 HTML 的过程中，在单独的层类型元素中渲染 PDF 文档层：

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
// 实例化 HTML SaveOptions 对象

HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// 指定在输出 HTML 中单独渲染 PDF 文档层
htmlsaveOptions.setConvertMarkedContentToLayers(true);

// 保存文档
document.save(DATA_DIR + "LayersRendering_out.html", htmlsaveOptions);
document.close();
```

PDF 到 HTML 转换是 Aspose.PDF 最受欢迎的功能之一，因为它可以在各种平台上查看 PDF 文件的内容，而无需使用 PDF 文档查看器。输出的 HTML 符合 WWW 标准，可以轻松地在所有网页浏览器中显示。使用此功能，可以在手持设备上查看 PDF 文件，因为您不需要安装任何 PDF 查看应用程序，只需使用一个简单的网页浏览器即可。

## PDF 到 HTML - 排除字体资源

如果您打算在将 PDF 转换为 HTML 的过程中排除所有或部分字体资源，Aspose.PDF for Java API 可以通过 HtmlSaveOptions 类帮助您实现此目的。该 API 提供了两个选项来实现此目的。

- `htmlOptions.FontSavingMode = HTmlSaveOptions.FontSavingModes.DontSave` - 防止导出所有字体
- `htmlOptions.ExcludeFontNameList = (new String[] { "ArialMT", "SymbolMT" });` - 用于防止导出特定字体（字体名称应指定为不带井号）

为了在转换 PDF 为 HTML 时排除字体资源，请使用以下步骤：

1. 定义一个新的 HtmlSaveOptions 类对象
1. 定义并设置要防止导出的字体名称在 HtmlSaveOptions.ExcludeFontNameList 中
1. 使用 save 方法将 PDF 转换为 HTML

```java
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setExplicitListOfSavedPages(
        new int[]{
                1
        }
);
htmlsaveOptions.setFixedLayout(true);
htmlsaveOptions.setCompressSvgGraphicsIfAny(false);
htmlsaveOptions.setSaveTransparentTexts(true);
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setExcludeFontNameList(new String[]{"ArialMT", "SymbolMT"});
htmlsaveOptions.setFontSavingMode(HtmlSaveOptions.FontSavingModes.DontSave);
htmlsaveOptions.setDefaultFontName("Comic Sans MS");
htmlsaveOptions.setUseZOrder(true);
htmlsaveOptions
        .setLettersPositioningMethod(LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss);
htmlsaveOptions
        .setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.NoEmbedding);
htmlsaveOptions
        .setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
htmlsaveOptions.setSplitIntoPages(false);

Document document = new Document(DATA_DIR + "sample.pdf");
document.save(DATA_DIR + "output_out.html", htmlsaveOptions);
document.close();
```