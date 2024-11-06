---
title: 将各种文件格式转换为PDF 
linktitle: 将其他文件格式转换为PDF 
type: docs
weight: 80
url: zh/php-java/convert-other-files-to-pdf/
lastmod: "2024-05-20"
description: 本主题向您展示如何使用Aspose.PDF将其他文件格式转换为PDF文档。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 将EPUB转换为PDF

**Aspose.PDF for PHP** 允许您简单地将EPUB文件转换为PDF格式。

<abbr title="电子出版物">EPUB</abbr> 是由国际数字出版论坛（IDPF）制定的免费开放的电子书标准。文件具有扩展名.epub。EPUB旨在用于可重排内容，这意味着EPUB阅读器可以针对特定显示设备优化文本。

为了将EPUB文件转换为PDF格式，Aspose.PDF for PHP有一个名为[EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions)的类，用于加载源EPUB文件。
 之后，对象作为参数传递给[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)对象初始化，因为它有助于PDF渲染引擎确定源文档的输入格式。

以下代码片段显示了将EPUB文件转换为PDF格式的过程。

1. 创建一个EPUB [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/)。
1. 初始化[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document)对象。
1. 保存输出PDF文档。

```php
// 创建一个新的EpubLoadOptions实例
$loadOption = new EpubLoadOptions();

// 创建一个新的Document对象并加载EPUB文件
$document = new Document($inputFile, $loadOption);

// 将文档保存为PDF文件
$document->save($outputFile);
```

{{% alert color="success" %}}
**尝试在线将EPUB转换为PDF**

Aspose.PDF for PHP为您提供免费的在线应用程序["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)，您可以通过它尝试研究其功能和工作质量。
[![Aspose.PDF 转换 EPUB 到 PDF 免费应用](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## 将 Markdown 转换为 PDF

{{% alert color="success" %}}
**尝试在线将 Markdown 转换为 PDF**

Aspose.PDF for PHP 为您提供一个在线免费应用程序 ["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf)，您可以在其中尝试探究其功能和质量。

[![Aspose.PDF 转换 Markdown 到 PDF 免费应用](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdown 是一个供网页作者使用的文本到 HTML 转换工具。Markdown 允许您以易于阅读和编写的纯文本格式编写内容，然后将其转换为结构上有效的 XHTML（或 HTML）。

以下代码片段展示了如何使用 Aspose.PDF for PHP 实现此功能：

```php
// 创建一个新的 MdLoadOptions 实例
$loadOption = new MdLoadOptions();

// 创建一个新的 Document 实例并加载输入的 Markdown 文件
$document = new Document($inputFile, $loadOption);

// 将文档保存为 PDF 文件
$document->save($outputFile);
```


## 将 PCL 转换为 PDF

<abbr title="Printer Command Language">PCL</abbr> （打印机命令语言）是由惠普开发的一种打印机语言，用于访问标准打印机功能。PCL 1 到 5e/5c 级别是基于命令的语言，使用控制序列按接收顺序进行处理和解释。在消费者层面，PCL 数据流由打印驱动程序生成。PCL 输出也可以通过自定义应用程序轻松生成。

{{% alert color="success" %}}
**尝试在线将 PCL 转换为 PDF**

Aspose.PDF for PHP 为您提供在线免费应用程序["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf)，您可以尝试研究其功能性和工作质量。

[![Aspose.PDF 使用免费应用程序将 PCL 转换为 PDF](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**目前，仅支持 PCL5 和更早版本。**

|**命令集**|**支持**|**例外**|**描述**|

| :- | :- | :- | :- |
|作业控制命令|+|双面打印模式|控制打印过程：副本数量，输出纸盒，单面/双面打印，左边和顶部偏移等。|
|页面控制命令|+|跳过打孔命令|指定页面大小，边距，页面方向，行间距，字符间距等。|
|光标定位命令|+| |指定光标位置，从而确定文本、光栅或矢量图像的原点和详细信息。|

|字体选择命令|+|<p>1. 透明打印数据命令。</p><p>2. 嵌入软字体。在当前版本中，我们的库不再创建软字体，而是从目标机器上安装的现有“硬”TrueType字体中选择合适的字体。<br>   合适性由宽高比定义。<br>   该功能仅适用于位图和TrueType字体，并不保证用软字体打印的文本与源文件中的一致。<br>   因为软字体中的字符代码可能与默认的不匹配。</p><p>3. 用户定义符号集。</p>|允许从PCL文件中加载软（嵌入）字体，并在内存中管理它们。|
|光栅图形命令|+|只支持黑白|允许从PCL文件中加载光栅图像到内存，指定光栅参数<br>如宽度、高度、压缩类型、分辨率等。|
|颜色命令|+| |允许为所有可打印对象着色。|
|打印模型命令|+| |允许使用光栅预定义和用户定义的图案填充文本、光栅图像和矩形区域，指定图案和源光栅图像的透明模式。
 <br>预定义的图案包括阴影线、交叉阴影线和填充阴影线。|
|矩形区域填充命令|+| |允许使用图案创建和填充矩形区域。|
|HP-GL/2 矢量图形命令|+|屏蔽矢量命令 (SV)、透明模式命令 (TR)、透明数据命令 (TD)、RO（旋转坐标系）、可缩放或位图字体命令 (SB)、字符倾斜命令 (SL) 和额外空格 (ES) 未实现，DV（定义变量文本路径）命令在测试版中实现。|<p>- 允许将 PCL 文件中的 HP-GL/2 矢量图像加载到内存中。 矢量图像的原点位于可打印区域的左下角，可以进行缩放、平移、旋转和剪裁。</p><p>- 矢量图像可以包含文本，作为标签，以及几何图形，如矩形、圆形、椭圆、线条、弧线、贝塞尔曲线和由简单图形组成的复杂图形。</p><p>- 闭合图形（包括标签的字母）可以使用实心填充或矢量图案填充。</p><p>- 图案可以是阴影、交叉阴影、渐变、光栅用户定义、PCL阴影或交叉阴影及PCL用户定义。PCL图案是光栅的。标签可以单独旋转、缩放，并在四个方向上定向：上、下、左和右。左右方向涉及一个接一个的字母排列。上下方向涉及一个在另一个下面的字母排列。</p>|
|Macross|―| |允许将一系列PCL命令加载到内存中，并多次使用此序列，例如，用于打印页面标题或为一组页面设置一种格式。|
|Unicode text|―| |允许打印非ASCII字符。 未实现，因为缺少带有Unicode文本的示例文件

PCL6 (PCL-XL) | 仅在Beta版中实现，因为缺少测试文件。嵌入字体也不支持。JetReady扩展不支持，因为不可能拥有JetReady规范。二进制文件格式。

### 将PCL文件转换为PDF格式

为了允许从PCL转换为PDF，[Aspose.PDF for PHP](https://products.aspose.com/pdf/php-java)提供了类[PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions)，用于初始化[LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions)对象。然后在[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)对象初始化时，将此对象作为参数传递，并帮助PDF渲染引擎确定源文档的输入格式。

以下代码片段显示了将PCL文件转换为PDF格式的过程。

```php
// 创建PclLoadOptions的新实例
$loadOption = new PclLoadOptions();

// 创建Document的新实例并加载PCL文件
$document = new Document($inputFile, $loadOption);

// 将文档保存为PDF文件
$document->save($outputFile);
```

### 已知问题

1. 如果打印方向不是0º，文本字符串和图像的起源可能与源PCL文件中的略有不同。如果矢量图的坐标系旋转（之前有RO命令），矢量图像的情况也是如此。
2. 如果矢量图像中的标签受到一系列命令的影响：标签起源（LO）、定义变量文本路径（DV）、绝对方向（DI）或相对方向（DR），则标签的起源可能与源PCL文件中的不同。
3. 如果文本必须使用位图或TrueType软（嵌入式）字体渲染，则可能会被错误读取，因为当前这些字体仅部分支持（参见“支持功能表”中的例外）。在这种情况下，只有当软字体中的字符代码与默认字符代码对应时，文本才能被正确读取。读取文本的样式也可能与源PCL文件中的不同，因为不需要在软字体头中设置样式。

1. 如果解析的 PCL 文件包含 Intellifont 或 Universal 软字体，将会抛出异常，因为完全不支持 Intellifont 和 Universal 字体。
1. 如果解析的 PCL 文件包含宏命令，解析结果将与源文件有很大不同，因为不支持宏命令。

## 将文本转换为 PDF

**Aspose.PDF for PHP** 提供了将文本文件转换为 PDF 格式的功能。在本文中，我们演示了如何轻松高效地使用 Aspose.PDF 将文本文件转换为 PDF。

当您需要将文本文件转换为 PDF 时，首先使用某种读取器读取源文本文件。我们使用 StringBuilder 来读取文本文件内容。实例化 Document 对象并在 Pages 集合中添加新页面。创建一个新的 TextFragment 对象，并将 StringBuilder 对象传递给它的构造函数。使用 TextFragment 对象在 Paragraphs 集合中添加一个新段落，并使用 Document 类的 Save 方法保存生成的 PDF 文件。
**尝试在线将文本转换为PDF**

{{% alert color="primary" %}}

[![Aspose.PDF 转换文本为PDF的免费应用程序](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### 将纯文本文件转换为PDF

```php
// 创建一个新的 Document 对象。
$document = new Document();

// 向文档添加一个新页面。
$page = $document->getPages()->add();

// 读取输入文本文件的内容。
$text = file_get_contents($inputFile);

// 创建一个新的 FontRepository 对象。
$fontRepository = new FontRepository();

// 在资源库中查找 "Courier" 字体。
$font = $fontRepository->findFont("Courier");

// 使用输入文本创建一个新的 TextFragment 对象。
$textFragment = new TextFragment($text);

// 将文本片段的字体设置为 "Courier"。
$textFragment->getTextState()->setFont($font);

// 将文本片段添加到页面。
$page->getParagraphs()->add($textFragment);

// 将文档保存到输出文件。
$document->save($outputFile);
```


## 将 XPS 转换为 PDF

**Aspose.PDF for PHP** 支持将 <abbr title="XML Paper Specification">XPS</abbr> 文件转换为 PDF 格式的功能。查看本文以解决您的任务。

XPS，XML 纸张规范，是一种 Microsoft 文件格式，用于将文档创建和查看集成到 Windows 中。使用 Aspose.PDF for PHP，可以将 XPS 文件转换为 Adobe 的便携式文件格式 PDF。

该文件格式基本上是一个压缩的 XML 文件，主要用于分发和存储。它非常难以编辑，并且主要由 Microsoft 实现。

要使用 [Aspose.PDF for PHP](https://products.aspose.com/pdf/php-java) 将 XPS 文件转换为 PDF，请使用 [XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions) 类。
 这是用于初始化一个 [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions) 对象。之后，这个对象作为参数在 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 对象初始化时传递，并帮助 PDF 渲染引擎确定源文档的输入格式。

以下代码片段展示了将 XPS 文件转换为 PDF 格式的过程。

```php
// 创建 XpsLoadOptions 类的新实例
$loadOption = new XpsLoadOptions();

// 创建 Document 类的新实例并加载 XPS 文件
$document = new Document($inputFile, $loadOption);

// 将文档保存为 PDF 文件
$document->save($outputFile);
```

{{% alert color="success" %}}
**尝试在线将 XPS 格式转换为 PDF**

Aspose.PDF for PHP 为您提供在线免费应用程序 ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 转换 XPS 为 PDF 免费应用](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/){{% /alert %}}

## 将 PostScript 转换为 PDF

**Aspose.PDF for PHP** 支持将 PostScript 文件转换为 PDF 格式。Aspose.PDF 的一个功能是，您可以设置一组字体文件夹，以在转换过程中使用。

为了将 PostScript 文件转换为 PDF 格式，Aspose.PDF for PHP 提供了 [PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions) 类，该类用于初始化 LoadOptions 对象。稍后可以将此对象作为参数传递给 Document 对象构造函数，这将帮助 PDF 渲染引擎确定源文档的格式。

以下代码片段可用于将 PostScript 文件转换为 PDF 格式：

```php
// 创建一个新的 PsLoadOptions 对象。
$loadOption = new PsLoadOptions();

// 创建一个新的 Document 对象并加载输入的 PS 文件。
$document = new Document($inputFile, $loadOption);

// 将文档保存为 PDF 文件。
$document->save($outputFile);
```

## 将 XML 转换为 PDF

XML 格式用于存储结构化数据。
 有几种方法可以在 Aspose.PDF 中将 <abbr title="Extensible Markup Language">XML</abbr> 转换为 PDF。

{{% alert color="success" %}}
**尝试在线将 XML 转换为 PDF**

Aspose.PDF for PHP 为您提供在线免费应用程序 ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 转换 XML 到 PDF 使用免费应用程序](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

考虑使用基于 XSL-FO 标准的 XML 文档的选项。

### 将 XSL-FO 转换为 PDF

可以使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) 对象和 [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions) 实现 XSL-FO 文件到 PDF 的转换。

```php
// 设置示例文件的路径
$dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
$inputFoFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xslt";
$inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xml";
$outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . 'result-xmlfo-to-pdf.pdf';

// 创建 XslFoLoadOptions 类的新实例并传递输入 XSL-FO 文件路径
$loadOption = new XslFoLoadOptions($inputFoFile);

// 创建 Document 类的新实例并传递输入 XML 文件和 XSL-FO 加载选项
$document = new Document($inputFile, $loadOption);

// 将转换后的 PDF 文档保存到输出文件路径
$document->save($outputFile);
```

## 将 LaTeX/TeX 转换为 PDF

LaTeX 文件格式是一种文本文件格式，带有 LaTeX 语言家族的标记，而 LaTeX 是 TeX 系统的派生格式。LaTeX（ˈleɪtɛk/ lay-tek 或 lah-tek）是一种文档准备系统和文档标记语言。它广泛用于许多领域的科学文档的交流和出版，包括数学、物理和计算机科学。它在包含复杂多语言材料（如梵文和阿拉伯语，包括校勘版）的书籍和文章的准备和出版中也具有重要作用。LaTeX 使用 TeX 排版程序来格式化其输出，并且其本身是用 TeX 宏语言编写的。

**Aspose.PDF for PHP** 支持将 TeX 文件转换为 PDF 格式的功能，为了实现此要求，com.aspose.pdf 包中有一个名为 [LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions) 的类，它提供加载 LaTeX 文件的功能，并使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 类将输出渲染为 PDF 格式。
 以下代码片段显示了将LaTex文件转换为PDF格式的过程。

```php
// 创建一个新的LatexLoadOptions类的实例
$loadOption = new LatexLoadOptions();

// 创建一个新的Document类实例，并使用TeXLoadOptions加载TeX文件
$document = new Document($inputFile, $loadOption);

// 将文档保存为PDF文件
$document->save($outputFile);
```

{{% alert color="success" %}}
**尝试在线将LaTeX/TeX转换为PDF**

Aspose.PDF for PHP 为您提供在线免费应用程序 ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)，您可以尝试调查其功能和质量。

[![Aspose.PDF Convertion LaTeX/TeX to PDF with Free App](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}