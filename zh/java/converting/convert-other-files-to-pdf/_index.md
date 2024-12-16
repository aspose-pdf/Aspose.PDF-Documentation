---
title: 将各种文件格式转换为PDF
linktitle: 将其他文件格式转换为PDF
type: docs
weight: 80
url: /zh/java/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: 本主题向您展示如何使用Aspose.PDF将其他文件格式转换为PDF文档。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 将EPUB转换为PDF

**Aspose.PDF for Java** 允许您简单地将EPUB文件转换为PDF格式。

<abbr title="electronic publication">EPUB</abbr>（电子出版物的缩写）是国际数字出版论坛（IDPF）制定的一个免费开放的电子书标准。文件扩展名为.epub。EPUB设计用于可重排内容，这意味着EPUB阅读器可以为特定的显示设备优化文本。

为了将EPUB文件转换为PDF格式，Aspose.PDF for Java提供了一个名为[EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions)的类，用于加载源EPUB文件。
 在此之后，对象作为参数传递给[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)对象初始化，因为它帮助PDF渲染引擎确定源文档的输入格式。

以下代码片段显示了将EPUB文件转换为PDF格式的过程。

1. 创建一个EPUB [`LoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/loadoptions)。
1. 初始化[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document)对象。
1. 保存输出的PDF文档。

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertEPUBtoPDF {

    private ConvertEPUBtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // 创建一个EPUB LoadOptions
        EpubLoadOptions options = new EpubLoadOptions();

        // 初始化document对象
        String epubFileName = Paths.get(_dataDir.toString(), "aliceDynamic.epub").toString();
        Document document = new Document(epubFileName, options);

        // 保存输出的PDF文档
        document.save(Paths.get(_dataDir.toString(),"EPUBtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**尝试在线将EPUB转换为PDF**

Aspose.PDF for Java为您提供免费的在线应用程序["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF Convertion EPUB to PDF with Free App](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## 将Markdown转换为PDF

**此功能在版本19.6或更高版本中支持。**

{{% alert color="success" %}}
**尝试在线将Markdown转换为PDF**

Aspose.PDF for Java为您提供免费的在线应用程序["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF Convertion Markdown to PDF with Free App](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdown是为网页作者提供的一种文本到HTML转换工具。
 Markdown 允许您以易于阅读和书写的纯文本格式编写内容，然后将其转换为结构上有效的 XHTML（或 HTML）。

以下代码片段展示了如何在 Java 中使用 Aspose.PDF 实现此功能：

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertMDtoPDF {

    private ConvertMDtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // 实例化 Latex 加载选项对象
        MdLoadOptions options = new MdLoadOptions();
        
        // 创建文档对象
        String markdownFileName = Paths.get(_dataDir.toString(), "samplefile.md").toString();
        Document document = new Document(markdownFileName, options);

        // 保存输出 PDF 文档
        document.save(Paths.get(_dataDir.toString(),"MarkdownToPDF.pdf").toString());
    }
}

```

## 将 PCL 转换为 PDF

<abbr title="Printer Command Language">PCL</abbr>（打印机命令语言）是惠普公司开发的一种打印机语言，用于访问标准打印机功能。PCL 1 至 5e/5c 是基于命令的语言，使用控制序列，这些序列按照接收的顺序进行处理和解释。在消费者层面，PCL 数据流由打印驱动程序生成。PCL 输出也可以通过自定义应用程序轻松生成。

{{% alert color="success" %}}
**尝试在线将 PCL 转换为 PDF**

Aspose.PDF for Java 提供了一个免费的在线应用程序 ["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf)，您可以在此尝试调查功能和工作的质量。

[![Aspose.PDF 转换 PCL 为 PDF 免费应用](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**目前，仅支持 PCL5 及更早版本。**

|**命令集**|**支持**|**例外**|**描述**|

| :- | :- | :- | :- |
|Job control commands|+|双面打印模式|控制打印过程：份数、输出纸盒、单面/双面打印、左侧和顶部偏移等。|
|Page control commands|+|跳过穿孔命令|指定页面大小、边距、页面方向、行间距、字符间距等。|
|Cursor Positioning Commands|+| |指定光标位置，因此，文本、栅格或矢量图像和细节的起点。|

|字体选择命令|+|<p>1. 透明打印数据命令。</p><p>2. 嵌入式软字体。在当前版本中，我们的库不创建软字体，而是从目标机器上安装的现有“硬”TrueType字体中选择合适的字体。<br>   合适性由宽高比定义。<br>   此功能仅适用于位图和TrueType字体，并不保证使用软字体打印的文本与源文件中的一致。<br>   因为软字体中的字符代码可能与默认的不匹配。</p><p>3. 用户定义的符号集。</p>|允许从PCL文件加载软（嵌入式）字体并在内存中管理它们。|
|光栅图形命令|+|仅黑白|允许从PCL文件加载光栅图像到内存中，指定光栅参数<br>如宽度、高度、压缩类型、分辨率等。|
|颜色命令|+| |允许为所有可打印对象着色。|
|打印模型命令|+| |允许用光栅预定义和用户定义的图案填充文本、光栅图像和矩形区域，指定图案和源光栅图像的透明模式。
 <br>预定义图案包括阴影、十字阴影和着色图案。|
|矩形区域填充命令|+| |允许使用图案创建和填充矩形区域。|
|HP-GL/2 矢量图形命令|+|屏幕矢量命令 (SV)、透明模式命令 (TR)、透明数据命令 (TD)、RO（旋转坐标系）、可缩放或位图字体命令 (SB)、字符倾斜命令 (SL) 和额外空间 (ES) 未实现，DV（定义变量文本路径）命令在测试版中实现。|<p>- 允许将 PCL 文件中的 HP-GL/2 矢量图像加载到内存中。 Vector 图像的起点位于可打印区域的左下角，可以缩放、平移、旋转和裁剪。</p><p>- 矢量图像可以包含文本，作为标签，以及几何图形，如矩形、圆形、椭圆、线条、弧线、贝塞尔曲线和由简单图形组成的复杂图形。</p><p>- 封闭图形，包括标签的字母，可以用实心填充或矢量图案填充。</p><p>- 图案可以是影线、交叉影线、阴影、用户定义的栅格、PCL 影线或交叉影线以及 PCL 用户定义。PCL 图案是栅格的。标签可以单独旋转、缩放，并可以在四个方向上定向：上、下、左和右。左右方向涉及一个接一个的字母排列。上下方向涉及一个在另一个下方的字母排列。</p>|  
|宏|―| |允许将一系列 PCL 命令加载到内存中，并多次使用此序列，例如，用于打印页面页眉或为一组页面设置一种格式。|  
|Unicode 文本|―| |允许打印非 ASCII 字符。 未实现，因为缺少包含Unicode文本的示例文件|
|PCL6 (PCL-XL)| |仅在Beta版本中实现，因为缺少测试文件。不支持嵌入字体。JetReady扩展不支持，因为不可能拥有JetReady规范。|二进制文件格式。|

### 将PCL文件转换为PDF格式

为了允许从PCL转换为PDF， [Aspose.PDF for Java](https://products.aspose.com/pdf/java) 提供了类 [PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions)，用于初始化 [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions) 对象。然后在 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 对象初始化期间将此对象作为参数传递，并帮助PDF渲染引擎确定源文档的输入格式。

以下代码片段展示了将PCL文件转换为PDF格式的过程。

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPCLtoPDF {

    private ConvertPCLtoPDF() {
        
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {        
        ConvertPCLtoPDF_Simple();
        ConvertPCLtoPDF_Advanced();
    }

    public static void ConvertPCLtoPDF_Simple() {
        PclLoadOptions options = new PclLoadOptions();
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        pdfDocument.save(_dataDir + "epub_test.pdf");        
    }

    public static void ConvertPCLtoPDF_Advanced() {
        PclLoadOptions options = new PclLoadOptions();
        options.SupressErrors=true;
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        if (options.Exceptions!=null)
            for (Exception ex : options.Exceptions)
            {
                System.out.println(ex.getMessage());
            }
        pdfDocument.save(_dataDir + "pcl_test.pdf");        
    }
}
```

### 已知问题

1. 如果打印方向不是0º，文本字符串和图像的起始位置可能与源PCL文件中的略有不同。如果矢量图的坐标系旋转了（前面有RO命令），矢量图像的起始位置也同样如此。
2. 如果标签受到一系列命令的影响，矢量图像中的标签起始位置可能与源PCL文件中的不同：标签起始位置（LO）、定义变量文本路径（DV）、绝对方向（DI）或相对方向（DR）。
3. 如果文本必须使用位图或TrueType软（嵌入）字体呈现，则可能无法正确读取文本，因为目前这些字体仅部分支持（参见“支持的功能表”中的例外情况）。在这种情况下，只有当软字体中的字符代码与默认代码相对应时，文本才能正确读取。读取文本的样式也可能与源PCL文件中的样式不同，因为不需要在软字体头中设置样式。

1. 如果解析的 PCL 文件包含 Intellifont 或 Universal 软字体，将抛出异常，因为完全不支持 Intellifont 和 Universal 字体。
1. 如果解析的 PCL 文件包含宏命令，解析结果将与源文件有很大不同，因为不支持宏命令。

## 将文本转换为 PDF

**Aspose.PDF for Java** 提供了将文本文件转换为 PDF 格式的功能。在本文中，我们演示了如何使用 Aspose.PDF 轻松高效地将文本文件转换为 PDF。

当您需要将文本文件转换为 PDF 时，首先在某个阅读器中读取源文本文件。我们使用 StringBuilder 来读取文本文件内容。实例化 Document 对象，并在 Pages 集合中添加新页面。创建一个新的 TextFragment 对象，并将 StringBuilder 对象传递给其构造函数。使用 TextFragment 对象在 Paragraphs 集合中添加一个新段落，并使用 Document 类的 Save 方法保存生成的 PDF 文件。
 **尝试在线将文本转换为PDF**
{{% alert color="primary" %}}

Aspose.PDF for Java 为您提供在线免费应用程序 ["文本到PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf)，您可以在其中尝试研究其功能和工作质量。

[![Aspose.PDF 转换文本到PDF的免费应用程序](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### 将纯文本文件转换为PDF

```java
package com.aspose.pdf.examples;
/**
 * 将TXT转换为PDF
 */

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertTextToPDF {

    private ConvertTextToPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    final static Charset ENCODING = StandardCharsets.UTF_8;

    public static void main(String[] args) throws IOException {
        ConvertTXT_to_PDF_Simple();
    }

    public static void ConvertTXT_to_PDF_Simple() throws IOException {
        // 初始化文档对象

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");

        // 通过调用其空构造函数实例化一个Document对象
        Document pdfDocument = new Document();

        // 在Document的Pages集合中添加一个新页面
        Page page = pdfDocument.getPages().add();

        // 创建一个TextFragmet实例并将reader对象中的文本作为参数传递给其构造函数
        TextFragment text = new TextFragment(Files.readString(txtDocumentFileName, ENCODING));

        // 在段落集合中添加一个新的文本段落并传递TextFragment对象
        page.getParagraphs().add(text);

        // 保存结果PDF文件
        pdfDocument.save(pdfDocumentFileName);
    }
```


### 将预格式化文本文件转换为PDF

```java
    public static void ConvertPreFormattedTextToPdf() throws IOException {

        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();

        // 将文本文件读取为字符串数组
        java.util.List<String> lines = Files.readAllLines(txtDocumentFileName, ENCODING);

        // 通过调用其空构造函数实例化一个Document对象
        Document pdfDocument = new Document();

        // 在Document的Pages集合中添加一个新页面
        Page page = pdfDocument.getPages().add();

        // 设置左边距和右边距以获得更好的展示效果
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // 检查行是否包含“换页符”字符
            // 参见 https://en.wikipedia.org/wiki/Page_break
            if (line.startsWith("\f")) {
                page = pdfDocument.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // 创建一个TextFragment实例并
                // 将该行传递给其
                // 构造函数作为参数
                TextFragment text = new TextFragment(line);

                // 在段落集合中添加一个新的文本段落，并传递TextFragment对象
                page.getParagraphs().add(text);
            }

            pdfDocument.save(pdfDocumentFileName);
        }
    }
}
```


## 将 XPS 转换为 PDF

**Aspose.PDF for Java** 支持将 <abbr title="XML Paper Specification">XPS</abbr> 文件转换为 PDF 格式的功能。查看本文以解决您的任务。

XPS，全称 XML Paper Specification，是一种 Microsoft 文件格式，用于将文档创建和查看集成到 Windows 中。通过 Aspose.PDF for Java，可以将 XPS 文件转换为 Adobe 的便携式文件格式 PDF。

这种文件格式基本上是一个压缩的 XML 文件，主要用于分发和存储。它很难编辑，并且主要由 Microsoft 实现。

要使用 [Aspose.PDF for Java](https://products.aspose.com/pdf/java) 将 XPS 文件转换为 PDF，请使用 [XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions) 类。
 这用于初始化一个 [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions) 对象。之后，该对象在 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 对象初始化时作为参数传递，并帮助 PDF 渲染引擎确定源文档的输入格式。

在 XP 和 Windows 7 中，如果您查看控制面板然后查看打印机，您应该会发现预安装的 XPS 打印机。要创建 XPS 文件，您可以将该打印机用作输出设备。在 Windows 7 中，您应该可以直接双击文件以在 XPS 查看器中打开它。您还可以从微软网站下载 [XPS 查看器](http://windows.microsoft.com/en-US/windows-vista/what-is-the-xps-viewer)。

以下代码片段展示了将 XPS 文件转换为 PDF 格式的过程。

```java
public final class ConvertXPStoPDF {

    private ConvertXPStoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // 初始化文档对象

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xpsDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();

        // 使用 XPS 加载选项实例化 LoadOption 对象
        LoadOptions options = new XpsLoadOptions();

        // 通过调用其空构造函数实例化 Document 对象
        Document pdfDocument = new Document(xpsDocumentFileName, options);

        // 保存生成的 PDF 文件
        pdfDocument.save(pdfDocumentFileName);
    }
}
```

{{% alert color="success" %}}
**尝试在线将 XPS 格式转换为 PDF**

Aspose.PDF for Java 为您提供免费的在线应用程序 ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)，您可以在其中尝试调查其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 XPS 转换为 PDF](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## 将 PostScript 转换为 PDF

**Aspose.PDF for Java** 支持将 PostScript 文件转换为 PDF 格式的功能。Aspose.PDF 的其中一个功能是您可以设置一组在转换过程中使用的字体文件夹。

为了将 PostScript 文件转换为 PDF 格式，Aspose.PDF for Java 提供了 [PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions) 类，该类用于初始化 LoadOptions 对象。稍后可以将此对象作为参数传递给 Document 对象的构造函数，这将帮助 PDF 渲染引擎确定源文档的格式。


以下代码片段可用于将 PostScript 文件转换为 PDF 格式：

```java
public static void ConvertPostScriptToPDF_Simple(){
        // 初始化文档对象

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();

        // 创建文档对象
        Document document = new Document(psDocumentFileName, options);

        // 保存输出 PDF 文档
        document.save(pdfDocumentFileName);
    }
```

此外，您可以设置一组将在转换过程中使用的字体文件夹：

```java
public static void ConvertPostscriptToPDFAvdanced() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();
        
        options.setFontsFolders(new String[] { "c:\tmp\fonts1", "c:\tmp\fonts2" });

        // 创建文档对象
        Document document = new Document(psDocumentFileName, options);

        // 保存输出 PDF 文档
        document.save(pdfDocumentFileName);
    }
```


## 将 XML 转换为 PDF

XML 格式用于存储结构化数据。在 Aspose.PDF 中有几种方法可以将 <abbr title="Extensible Markup Language">XML</abbr> 转换为 PDF。

{{% alert color="success" %}}
**尝试在线将 XML 转换为 PDF**

Aspose.PDF for Java 为您提供在线免费应用程序 ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)，您可以尝试研究其功能和质量。

[![Aspose.PDF 转换 XML 到 PDF 免费应用](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

考虑使用基于 XSL-FO 标准的 XML 文档的选项。

### 将 XSL-FO 转换为 PDF

可以使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) 对象和 [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions) 实现 XSL-FO 文件到 PDF 的转换。

```java
package com.aspose.pdf.examples;
/**
 * 将 XML 转换为 PDF
 */

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertXMLtoPDF {

    private ConvertXMLtoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
        Convert_XSLFO_to_PDF_Adv();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // 初始化文档对象

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xmlDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();
        String xsltDocumentFileName = Paths.get(_dataDir.toString(), "employees.xslt").toString();

        XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

        // 使用其空构造函数实例化一个 Document 对象
        Document pdfDocument = new Document(xmlDocumentFileName,options);

        // 保存生成的 PDF 文件
        pdfDocument.save(pdfDocumentFileName);
    }
}
```


### 将 XSL-FO 转换为 PDF 并设置错误处理策略

```java
// 初始化文档对象

String documentFileName = Paths.get(DATA_DIR.toString(), "demo_txt.pdf").toString();
String xmlDocumentFileName = Paths.get(DATA_DIR.toString(), "demo.xml").toString();
String xsltDocumentFileName = Paths.get(DATA_DIR.toString(), "employees.xslt").toString();

XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

// 设置错误处理策略
options.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);

// 通过调用空构造函数实例化 Document 对象
Document document = new Document(xmlDocumentFileName, options);

// 保存生成的 PDF 文件
document.save(documentFileName);
document.close();
```

## 将 LaTeX/TeX 转换为 PDF

LaTeX 文件格式是一种文本文件格式，使用 LaTeX 衍生自 TeX 语言家族的标记语言，LaTeX 是 TeX 系统的衍生格式。
 LaTeX (ˈleɪtɛk/ lay-tek 或 lah-tek) 是一种文档准备系统和文档标记语言。它广泛用于许多领域的科学文档的交流和出版，包括数学、物理和计算机科学。它在包含复杂多语言材料（如梵文和阿拉伯文，包括重要版本）的书籍和文章的准备和出版中也起着重要作用。LaTeX 使用 TeX 排版程序来格式化其输出，并且它本身是用 TeX 宏语言编写的。

**Aspose.PDF for Java** 支持将 TeX 文件转换为 PDF 格式的功能。为了实现这一要求，com.aspose.pdf 包中有一个名为 [LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions) 的类，该类提供加载 LaTex 文件的功能，并使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 类以 PDF 格式呈现输出。 以下代码片段展示了将LaTex文件转换为PDF格式的过程。

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertLATEXtoPDF {

    private ConvertLATEXtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // 实例化Latex加载选项对象
        TeXLoadOptions options = new TeXLoadOptions();
        
        // 创建文档对象
        String latexFileName = Paths.get(_dataDir.toString(), "samplefile.tex").toString();
        Document document = new Document(latexFileName, options);

        // 保存输出PDF文档
        document.save(Paths.get(_dataDir.toString(),"TEXtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**尝试在线将LaTeX/TeX转换为PDF**

Aspose.PDF for Java 为您提供了一个免费的在线应用程序 ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)，您可以尝试调查其功能和工作质量。
[![Aspose.PDF 将 LaTeX/TeX 转换为 PDF 的免费应用程序](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)  
{{% /alert %}}