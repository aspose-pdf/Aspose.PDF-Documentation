---
title: 将其他文件格式转换为PDF
linktitle: 将其他文件格式转换为PDF
type: docs
weight: 80
url: /net/convert-other-files-to-pdf/
lastmod: "2021-11-01"
description: 本主题展示如何使用Aspose.PDF将其他文件格式如EPUB、MD、PCL、XPS、PS、XML和LaTeX转换为PDF文档。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 概览

本文解释了如何**使用C#将各种其他类型的文件格式转换为PDF**。它涵盖以下主题。

以下代码片段也可以与[Aspose.PDF.Drawing](/pdf/net/drawing/)库一起使用。

_格式_: **EPUB**
- [C# EPUB转PDF](#csharp-convert-epub-to-pdf)
- [C# 转换EPUB为PDF](#csharp-convert-epub-to-pdf)
- [C# 如何将EPUB文件转换为PDF](#csharp-convert-epub-to-pdf)

_格式_: **Markdown**
- [C# Markdown转PDF](#csharp-convert-markdown-to-pdf)
- [C# 转换Markdown为PDF](#csharp-convert-markdown-to-pdf)
- [C# 如何将Markdown文件转换为PDF](#csharp-convert-markdown-to-pdf)
- [C# 如何将 Markdown 文件转换为 PDF](#csharp-convert-markdown-to-pdf)

_格式_: **MD**
- [C# MD 转 PDF](#csharp-convert-md-to-pdf)
- [C# 转换 MD 为 PDF](#csharp-convert-md-to-pdf)
- [C# 如何将 MD 文件转换为 PDF](#csharp-convert-md-to-pdf)

_格式_: **PCL**
- [C# PCL 转 PDF](#csharp-convert-pcl-to-pdf)
- [C# 转换 PCL 为 PDF](#csharp-convert-pcl-to-pdf)
- [C# 如何将 PCL 文件转换为 PDF](#csharp-convert-pcl-to-pdf)

_格式_: **Text**
- [C# 文本转 PDF](#csharp-convert-text-to-pdf)
- [C# 转换文本为 PDF](#csharp-convert-text-to-pdf)
- [C# 如何将文本文件转换为 PDF](#csharp-convert-text-to-pdf)

_格式_: **TXT**
- [C# TXT 转 PDF](#csharp-convert-txt-to-pdf)
- [C# 转换 TXT 为 PDF](#csharp-convert-txt-to-pdf)
- [C# 如何将 TXT 文件转换为 PDF](#csharp-convert-txt-to-pdf)

_格式_: **Plain Text**
- [C# 纯文本转 PDF](#csharp-convert-plain-text-to-pdf)
- [C# 转换纯文本为 PDF](#csharp-convert-plain-text-to-pdf)
- [C# 如何将纯文本文件转换为 PDF](#csharp-convert-plain-text-to-pdf)
- [C# 如何将纯文本文件转换为PDF](#csharp-convert-plain-text-to-pdf)

_格式_: **预格式化的TXT**
- [C# 将预格式化文本转换为PDF](#csharp-convert-pre-formatted-txt-to-pdf)
- [C# 转换预格式化文本为PDF](#csharp-convert-pre-formatted-txt-to-pdf)
- [C# 如何将预格式化文本文件转换为PDF](#csharp-convert-pre-formatted-txt-to-pdf)

_格式_: **预文本**
- [C# 将预文本转换为PDF](#csharp-convert-pre-text-to-pdf)
- [C# 转换预文本为PDF](#csharp-convert-pre-text-to-pdf)
- [C# 如何将预文本文件转换为PDF](#csharp-convert-pre-text-to-pdf)

_格式_: **XPS**
- [C# 将XPS转换为PDF](#csharp-convert-xps-to-pdf)
- [C# 转换XPS为PDF](#csharp-convert-xps-to-pdf)
- [C# 如何将XPS文件转换为PDF](#csharp-convert-xps-to-pdf)

## 将EPUB转为PDF

**Aspose.PDF for .NET** 允许您轻松将EPUB文件转换为PDF格式。

<abbr title="电子出版物">EPUB</abbr>（电子出版物的简称）是来自国际数字出版论坛（IDPF）的一个自由开放的电子书标准。
<abbr title="电子出版物">EPUB</abbr>（电子出版物的简称）是国际数字出版论坛（IDPF）的一个自由开放的电子书标准。

EPUB还支持固定布局内容。该格式旨在作为出版商和转换公司内部以及用于发行和销售的单一格式。它取代了开放电子书标准。EPUB 3版本也得到了图书行业研究小组（BISG）的认可，该组织是一个领先的图书行业协会，专门从事标准化最佳实践、研究、信息和事件的打包内容。

{{% alert color="success" %}}
**尝试在线将EPUB转换为PDF**

Aspose.PDF for .NET为您提供在线免费应用程序["EPUB到PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF 转换EPUB到PDF的免费应用](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

<a name="csharp-convert-epub-to-pdf" id="csharp-convert-epub-to-pdf"><strong><em>步骤：</em>在C#中将EPUB转换为PDF</strong></a>
<a name="csharp-convert-epub-to-pdf" id="csharp-convert-epub-to-pdf"><strong><em>步骤：</em> 在C#中将EPUB转换为PDF</strong></a>

1. 创建 [EpubLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/epubloadoptions) 类的实例。
2. 创建 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 类的实例，提及源文件名和选项。
3. 以所需的文件名保存文档。

下面的代码片段向您展示如何使用C#将EPUB文件转换为PDF格式。

```csharp
public static void ConvertEPUBtoPDF()
{
    EpubLoadOptions option = new EpubLoadOptions();
    Document pdfDocument= new Document(_dataDir + "WebAssembly.epub", option);
    pdfDocument.Save(_dataDir + "epub_test.pdf");
}
```

您还可以设置转换的页面大小。要定义新的页面大小，请创建 `SizeF` 对象并将其传递给 [EpubLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/epubloadoptions/constructors/main) 构造函数。

```csharp
public static void ConvertEPUBtoPDFAdv()
{
    EpubLoadOptions option = new EpubLoadOptions(new SizeF(1190, 1684));
    Document pdfDocument= new Document(_dataDir + "WebAssembly.epub", option);
    pdfDocument.Save(_dataDir + "epub_test.pdf");
}
```
## 将 Markdown 转换为 PDF

**此功能支持 19.6 或更高版本。**

{{% alert color="success" %}}
**尝试在线将 Markdown 转换为 PDF**

Aspose.PDF for .NET 为您提供免费的在线应用程序 ["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf)，您可以在此尝试探索其功能和工作质量。

[![Aspose.PDF 免费应用转换 Markdown 到 PDF](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Aspose.PDF for .NET 提供了基于输入[Markdown](https://daringfireball.net/projects/markdown/syntax)数据文件创建 PDF 文档的功能。要将 Markdown 转换为 PDF，您需要使用 [MdLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mdloadoptions) 初始化 [文档](https://reference.aspose.com/pdf/net/aspose.pdf/document)。

以下代码片段展示了如何使用 Aspose.PDF 库实现此功能：

<a name="csharp-convert-markdown-to-pdf" id="csharp-convert-markdown-to-pdf"><strong><em>步骤：</em>在 C# 中将 Markdown 转换为 PDF</strong></a> |
<a name="csharp-convert-markdown-to-pdf" id="csharp-convert-markdown-to-pdf"><strong><em>步骤：</em> 在C#中将Markdown转换为PDF</strong></a> |
<a name="csharp-convert-md-to-pdf" id="csharp-convert-md-to-pdf"><strong><em>步骤：</em> 在C#中将MD转换为PDF</strong></a>

1. 创建 [MdLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mdloadoptions/) 类的实例。
2. 创建 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 类的实例，指定源文件名和选项。
3. 以期望的文件名保存文档。

```csharp
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// 打开Markdown文档
Document pdfDocument= new Document(dataDir + "sample.md", new MdLoadOptions());
// 以PDF格式保存文档
pdfDocument.Save(dataDir + "MarkdownToPDF.pdf");
```

## 将PCL转换为PDF

<abbr title="Printer Command Language">PCL</abbr>（打印机命令语言）是惠普公司开发的用于访问标准打印机功能的打印机语言。
<abbr title="打印机命令语言">PCL</abbr>（打印机命令语言）是惠普开发的打印机语言，用于访问标准打印机功能。

{{% alert color="success" %}}
**尝试在线将PCL转换为PDF**

Aspose.PDF for .NET为您提供在线免费应用程序["PCL到PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF 转换PCL为PDF的免费应用](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**当前仅支持PCL5及更早版本**

<table>
    <thead>
        <tr>
            <th>
                命令集
            </th>
            <th>
                支持
            </th>
            <th>
                异常
            </th>
            <th>
                描述
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                作业控制命令
            </td>

<tr>
    <td>
        作业控制命令
    </td>
    <td>
        +
    </td>
    <td>
        双面打印模式
    </td>
    <td>
        控制打印过程：复印件数量、输出仓、单面/双面打印、左侧和顶部偏移等。
    </td>
</tr>
<tr>
    <td>
        页面控制命令
    </td>
    <td>
        +
    </td>
    <td>
        跳过穿孔命令
    </td>
    <td>
        指定页面大小、边距、页面方向、行间距、字符间距等。
    </td>
</tr>
<tr>
    <td>
        光标定位命令
    </td>
    <td>
        +
    </td>
    <td>
        &nbsp;
    </td>
    <td>
        指定光标位置，从而确定文本、栅格或矢量图像的起点和细节。
    </td>
</tr>
```

<tr>
    <td>
        指定光标位置，从而确定文本、光栅或矢量图像和细节的起点。
    </td>
</tr>
<tr>
    <td>
        字体选择命令
    </td>
    <td>
        +
    </td>
    <td>
        <ol>
            <li>透明打印数据命令。</li>
            <li>嵌入式软字体。在当前版本中，我们的库不是创建软字体，而是从目标机器上已安装的“硬”TrueType字体中选择合适的字体。<br/>
                适用性由宽高比定义。<br/>
                此功能仅适用于Bitmap和TrueType字体，并且不保证使用软字体打印的文本与源文件中的文本相关。<br/>
                因为软字体中的字符代码可能与默认的不匹配。
            </li>
            <li>用户定义的符号集。</li>
        </ol>
    </td>
</tr>
```

<li>用户定义的符号集。</li>
</ol>
</td>
<td>
允许从PCL文件加载软（嵌入式）字体并在内存中管理它们。
</td>
</tr>
<tr>
<td>
光栅图形命令
</td>
<td>
+
</td>
<td>
仅限黑白
</td>
<td>
允许从PCL文件加载光栅图像到内存，指定光栅参数。<br
> 如宽度、高度、压缩类型、分辨率等。
</td>
</tr>
<tr>
<td>
颜色命令
</td>
<td>
+
</td>
<td>
&nbsp;
</td>
<td>
允许对所有可打印对象进行着色。
</td>
</tr>
<tr>
<td>
打印模型命令
```
打印模型命令
允许填充文本、光栅图像和矩形区域，使用预定义的光栅和用户定义的图案，指定图案和源光栅图像的透明度模式。预定义的图案包括剖面线、交叉剖面线和阴影。

矩形区域填充命令
允许创建和填充具有图案的矩形区域。

HP-GL/2 矢量图形命令
Screened Vector Command (SV), Transparency Mode Command (TR), Transparent Data Command (TD), RO
屏蔽矢量指令（SV）、透明模式指令（TR）、透明数据指令（TD）、旋转坐标系统（RO）、可缩放或位图字体命令（SB）、字符倾斜命令（SL）和额外空间（ES）未实现，DV（定义变量文本路径）命令在测试版中实现。

允许从PCL文件加载HP-GL/2矢量图像到内存中。矢量图像原点在可打印区域的左下角，可以缩放、平移、旋转和裁剪。矢量图像可以包含文本，作为标签，以及几何图形，如矩形、圆形、椭圆、线条、弧线、贝塞尔曲线和由简单图形组成的复杂图形。封闭图形包括标签的字母可以用实心填充或矢量图案填充。图案可以是剖面图、十字剖面图、阴影、栅格自定义、PCL剖面图或PCL十字剖面图。

孵化、交叉阴影、阴影、用户定义的光栅，PCL孵化或交叉阴影以及PCL用户定义。PCL图案为光栅。标签可以单独旋转、缩放，并在四个方向上指向：上、下、左、右。左和右方向涉及一个接一个的字母排列。上和下的方向涉及一个在另一个下面的字母排列。

允许将一系列PCL命令加载到内存中并多次使用这些命令，例如，打印页面标题或为一组页面设置一种格式。

Unicode文本
```
允许打印非ASCII字符。由于缺少包含Unicode文本的样本文件，未实施。

PCL6（PCL-XL）

仅在Beta版本中实现，因为缺乏测试文件。嵌入式字体也不支持。由于无法获得JetReady规范，因此不支持JetReady扩展。

二进制文件格式。

### 将PCL文件转换为PDF格式

为了允许从PCL转换为PDF，Aspose.PDF有一个类[`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions)，用于初始化LoadOptions对象。
要实现从PCL转换为PDF，Aspose.PDF提供了[`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions)类，用于初始化LoadOptions对象。

以下代码片段展示了将PCL文件转换为PDF格式的过程。

<a name="csharp-convert-pcl-to-pdf" id="csharp-convert-pcl-to-pdf"><strong><em>步骤：</em> 在C#中将PCL转换为PDF</strong></a>

1. 创建[PclLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions/)类的实例。
2. 使用指定源文件名和选项，创建[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/)类的实例。
3. 使用希望的文件名保存文档。

```csharp
public static void ConvertPCLtoPDF()
{
    PclLoadOptions options = new PclLoadOptions();
    Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
    pdfDocument.Save(_dataDir + "pcl_test.pdf");
}
```

您还可以监控转换过程中的错误检测。
您还可以在转换过程中监控错误的检测。

```csharp
public static void ConvertPCLtoPDFAvdanced()
{
    PclLoadOptions options = new PclLoadOptions { SupressErrors = true };
    Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
    if (options.Exceptions!=null)
        foreach (var ex in options.Exceptions)
        {
            Console.WriteLine(ex.Message);
        }
    pdfDocument.Save(_dataDir + "pcl_test.pdf");
}
```

### 已知问题

1. 如果打印方向不是0°，文本字符串和图像的起源可能与源PCL文件中的略有不同。如果矢量图的坐标系统旋转（前置RO命令），同样适用于矢量图。
1. 如果标签受到一系列命令的影响：标签原点（LO）、定义可变文本路径（DV）、绝对方向（DI）或相对方向（DR），则矢量图中的标签原点可能与源PCL文件中的不同。
1. 如果解析的PCL文件包含Intellifont或通用软字体，将抛出异常，因为完全不支持Intellifont和通用字体。
1. 如果解析的PCL文件包含宏命令，解析的结果将与源文件大相径庭，因为不支持宏命令。

## 将文本转换为PDF

**Aspose.PDF for .NET** 支持将纯文本和预格式化文本文件转换为PDF格式的功能。

将文本转换为PDF意味着将文本片段添加到PDF页面上。对于文本文件，我们处理两种类型的文本：预格式化（例如，每行80个字符的25行）和非格式化文本（纯文本）。根据我们的需求，我们可以自己控制这种添加，或者将其委托给库的算法。

{{% alert color="success" %}}
**尝试在线将TEXT转换为PDF**

Aspose.PDF for .NET为您提供免费在线应用程序["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf)，在此您可以尝试研究其功能和工作质量。
Aspose.PDF for .NET为您提供在线免费应用程序[“文本转PDF”](https://products.aspose.app/pdf/conversion/txt-to-pdf)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF文本转PDF的免费应用转换](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)

### 将纯文本文件转换为PDF

对于纯文本文件，我们可以使用以下技术：

<a name="csharp-convert-text-to-pdf" id="csharp-convert-text-to-pdf"><strong><em>步骤：</em>在C#中将文本转换为PDF</strong></a> |
<a name="csharp-convert-txt-to-pdf" id="csharp-convert-txt-to-pdf"><strong><em>步骤：</em>在C#中将TXT转换为PDF</strong></a> |
<a name="csharp-convert-plain-text-to-pdf" id="csharp-convert-plain-text-to-pdf"><strong><em>步骤：</em>在C#中将纯文本转换为PDF</strong></a>

1. 使用_TextReader_读取整个文本；
2.
2.
3. 创建一个新的[TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment/)对象，并将_TextReader_对象传递给它的构造函数；
4. 将_TextFragment_对象作为段落添加到_Paragraphs_集合中。如果文本量超过页面，库算法会自动添加额外页面；
5. 使用[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/)类的**Save**方法；

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// 读取源文本文件
TextReader tr = new StreamReader(dataDir + "log.txt");

// 通过调用其空构造函数实例化一个Document对象
Document pdfDocument= new Document();

// 在Document的Pages集合中添加一个新页面
Page page = pdfDocument.Pages.Add();

// 创建TextFragmet实例，并将来自reader对象的文本作为参数传递给其构造函数
TextFragment text = new TextFragment(tr.ReadToEnd());

// 在段落集合中添加一个新的文本段落，并传递TextFragment对象
page.Paragraphs.Add(text);

// 保存结果PDF文件
pdfDocument.Save(dataDir + "TexttoPDF_out.pdf");
```
### 将预格式化文本文件转换为PDF

转换预格式化文本就像转换普通文本，但您需要执行一些额外的操作，例如设置边距、字体类型和大小。显然，字体应该是等宽字体（例如Courier New）。

按照以下步骤使用C#将预格式化文本转换为PDF：

<a name="csharp-convert-pre-text-to-pdf" id="csharp-convert-pre-text-to-pdf"><strong><em>步骤：</em>在C#中将预文本转换为PDF</strong></a> |
<a name="csharp-convert-pre-formatted-txt-to-pdf" id="csharp-convert-pre-formatted-txt-to-pdf"><strong><em>步骤：</em>在C#中将预格式化TXT转换为PDF</strong></a>

1. 将整个文本读取为字符串数组；
2. 实例化 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) 对象并在 [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/pages/) 集合中添加新页面；
在这种情况下，库的算法也会添加额外的页面，但我们可以自己控制这个过程。以下示例展示了如何将预格式化的文本文件（80x25）转换为A4大小的PDF文档。

```csharp
public static void ConvertPreFormattedTextToPdf()
{
    // 将文本文件读取为字符串数组
    var lines = System.IO.File.ReadAllLines(_dataDir + "rfc822.txt");

    // 通过调用其空构造函数实例化一个Document对象
    Document pdfDocument= new Document();

    // 在Document的Pages集合中添加新页面
    Page page = pdfDocument.Pages.Add();

    // 设置左右边距以获得更好的展示效果
    page.PageInfo.Margin.Left = 20;
    page.PageInfo.Margin.Right = 10;
    page.PageInfo.DefaultTextState.Font = FontRepository.FindFont("Courier New");
    page.PageInfo.DefaultTextState.FontSize = 12;

    foreach (var line in lines)
    {
        // 检查行是否包含“换页”字符
        // 见 https://en.wikipedia.org/wiki/Page_break
        if (line.StartsWith("\x0c"))
        {
            page = pdfDocument.Pages.Add();
            page.PageInfo.Margin.Left = 20;
            page.PageInfo.Margin.Right = 10;
            page.PageInfo.DefaultTextState.Font = FontRepository.FindFont("Courier New");
            page.PageInfo.DefaultTextState.FontSize = 12;
        }
        else
        {
            // 创建TextFragment的实例并
            // 将行作为参数传递给其
            // 构造函数
            TextFragment text = new TextFragment(line);

            // 在段落集合中添加一个新的文本段落并传递TextFragment对象
            page.Paragraphs.Add(text);
        }
    }

    // 保存结果PDF文件
    pdfDocument.Save(_dataDir + "TexttoPDF_out.pdf");
}
```
## 将XPS转换为PDF

**Aspose.PDF for .NET** 支持将 <abbr title="XML Paper Specification">XPS</abbr> 文件转换为PDF格式。查阅本文以解决您的任务。

XPS文件类型主要与微软公司的XML纸张规范相关联。XML纸张规范（XPS），之前的代号为Metro，包含了下一代打印路径（NGPP）的营销概念，是微软将文档创建和查看集成到其Windows操作系统中的倡议。

{{% alert color="primary" %}}

该文件格式基本上是一个被压缩的XML文件，主要用于分发和存储。它非常难以编辑，且主要由微软实现。

{{% /alert %}}

为了使用Aspose.PDF for .NET将XPS转换为PDF，我们引入了一个名为 [XpsLoadOption](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions) 的类，用于初始化 [LoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions) 对象。
为了使用 Aspose.PDF for .NET 将 XPS 转换为 PDF，我们引入了一个名为 [XpsLoadOption](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions) 的类，用于初始化 [LoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions) 对象。

{{% alert color="primary" %}}

在 XP 和 Windows 7 中，如果你在控制面板然后打印机中查找，应该可以找到预安装的 XPS 打印机。你可以使用该打印机作为输出设备来创建这些文件。在 Windows 7 中，你应该可以双击文件在 XPS 查看器中打开它。你也可以从微软的网站下载 XPS 查看器。

{{% /alert %}}

以下代码片段展示了使用 C# 将 XPS 文件转换为 PDF 格式的过程。

<a name="csharp-convert-xps-to-pdf" id="csharp-convert-xps-to-pdf"><strong><em>步骤：</em> 在 C# 中将 XPS 转换为 PDF</strong></a>

1. 创建一个 [XpsLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions/) 类的实例。
2.
2.
3. 将文档保存为PDF格式，并指定文件名。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// 使用XPS加载选项实例化LoadOption对象
Aspose.Pdf.LoadOptions options = new XpsLoadOptions();

// 创建文档对象
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "XPSToPDF.xps", options);

// 保存结果PDF文档
document.Save(dataDir + "XPSToPDF_out.pdf");
```

{{% alert color="success" %}}
**尝试在线将XPS格式转换为PDF**

Aspose.PDF for .NET为您提供在线免费应用程序["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)，您可以在此尝试探索其功能和工作质量。

[![Aspose.PDF Convertion XPS to PDF with Free App](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}
{{% /alert %}}

## 将PostScript转换为PDF

**Aspose.PDF for .NET** 支持将PostScript文件转换为PDF格式的功能。Aspose.PDF的一个特点是您可以设置一组在转换过程中使用的字体文件夹。

为了将PostScript文件转换为PDF格式，Aspose.PDF for .NET 提供了[PsLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/psloadoptions) 类来初始化LoadOptions对象。之后，这个对象可以作为参数传递给Document对象的构造器，这将帮助PDF渲染引擎确定源文档的格式。

以下代码片段可用于使用Aspose.PDF for .NET将PostScript文件转换为PDF格式：

```csharp
// 完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string _dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// 创建一个新的PsLoadOptions实例
PsLoadOptions options = new PsLoadOptions();
// 使用创建的加载选项打开.ps文档
Document pdfDocument = new Document(_dataDir + "input.ps", options);
// 保存文档
pdfDocument.Save(dataDir + "PSToPDF.pdf");
```
Additionally, you can set a set of font folders that will be used during conversion:

```csharp
public static void ConvertPostscriptToPDFAvdanced()
{
    PsLoadOptions options = new PsLoadOptions
    {
        FontsFolders = new [] { @"c:\tmp\fonts1", @"c:\tmp\fonts2"}
    };
    Document pdfDocument = new Document(_dataDir + "input.ps", options);
    pdfDocument.Save(_dataDir + "ps_test.pdf");
}
```

## 将 XML 转换为 PDF

XML 格式用于存储结构化数据。有几种方法可以在 Aspose.PDF 中将 XML 转换为 PDF：

1. 使用 XSLT 将任何 XML 数据转换为 HTML，然后按下面描述将 HTML 转换为 PDF
1. 使用 Aspose.PDF XSD Schema 生成 XML 文档
1. 使用基于 XSL-FO 标准的 XML 文档

{{% alert color="success" %}}
**尝试在线将 XML 转换为 PDF**

Aspose.PDF for .NET 为您提供免费的在线应用程序 ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)，您可以尝试探索其功能和工作质量。
Aspose.PDF for .NET 为您呈现在线免费应用程序[“XML 转 PDF”](https://products.aspose.app/pdf/conversion/xml-to-pdf)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF 转换 XML 至 PDF 的免费应用](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}


## 将 XSL-FO 转换为 PDF

使用传统的 Aspose.PDF 技术将 XSL-FO 文件转换为 PDF - 使用 [Document](https://reference.aspose.com/page/net/aspose.page/document) 对象和 [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions) 实例化。但有时您可能会遇到文件结构不正确的情况。对于这种情况，XSL-FO 转换器允许设置错误处理策略。您可以选择 `ThrowExceptionImmediately`、`TryIgnore` 或 `InvokeCustomHandler`。

```csharp
public static void Convert_XSLFO_to_PDF()
{
    // 实例化 XslFoLoadOption 对象
    var options = new XslFoLoadOptions(".\\samples\\employees.xslt");
    // 设置错误处理策略
    options.ParsingErrorsHandlingType = XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately;
    // 创建 Document 对象
    var pdfDocument = new Aspose.Pdf.Document(".\\samples\\employees.xml", options);
    pdfDocument.Save(_dataDir + "data_xml.pdf");
}
```
## 将LaTeX/TeX转换为PDF

LaTeX文件格式是一种带有标记的文本文件格式，它使用的是TeX家族语言的LaTeX衍生物，而LaTeX是TeX系统的派生格式。LaTeX（ˈleɪtɛk/lay-tek或lah-tek）是一个文档准备系统和文档标记语言。它广泛用于许多领域科学文件的交流和出版，包括数学、物理和计算机科学。它在准备和出版包含复杂多语言材料的书籍和文章中也扮演着重要角色，例如梵文和阿拉伯文，包括关键版本。LaTeX使用TeX排版程序来格式化其输出，并且本身是用TeX宏语言编写的。

{{% alert color="success" %}}
**尝试在线将LaTeX/TeX转换为PDF**

Aspose.PDF for .NET为您提供在线免费应用程序["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)，您可以在此尝试探索其功能和工作质量。

{{% /alert %}}


Aspose.PDF for .NET 支持将 TeX 文件转换为 PDF 格式的功能，为了实现这一需求，Aspose.Pdf 命名空间中有一个名为 [LatexLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexloadoptions) 的类，它提供了加载 LaTex 文件并使用 [Document 类](https://reference.aspose.com/pdf/net/aspose.pdf/document) 渲染输出为 PDF 格式的功能。以下代码片段显示了使用 C# 将 LaTex 文件转换为 PDF 格式的过程。

```csharp
public static void ConvertTeXtoPDF()
{
    // 实例化 Latex 加载选项对象
    TeXLoadOptions options = new TeXLoadOptions();
    // 创建 Document 对象
    Aspose.Pdf.Document pdfDocument= new Aspose.Pdf.Document(_dataDir + "samplefile.tex", options);
    // 将输出保存为 PDF 文件
    pdfDocument.Save(_dataDir + "TeXToPDF_out.pdf");
}
```
