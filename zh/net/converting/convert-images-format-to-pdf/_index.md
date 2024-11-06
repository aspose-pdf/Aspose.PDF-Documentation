---
title: 将各种图片格式转换为 .NET 中的 PDF
linktitle: 将图片转换为 PDF
type: docs
weight: 60
url: zh/net/convert-images-format-to-pdf/
lastmod: "2021-11-01"
description: 使用 C# .NET 将各种图片格式（如 BMP、CGM、JPEG、DICOM、PNG、TIFF、EMF 和 SVG）转换为 PDF。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 概览

本文介绍了如何使用 C# 将各种图片格式转换为 PDF。它涵盖了以下主题。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

_格式_: **BMP**
- [C# BMP 转 PDF](#csharp-bmp-to-pdf)
- [C# 将 BMP 转换为 PDF](#csharp-bmp-to-pdf)
- [C# 如何将 BMP 图像转换为 PDF](#csharp-bmp-to-pdf)

_格式_: **CGM**
- [C# CGM 转 PDF](#csharp-cgm-to-pdf)
- [C# 将 CGM 转换为 PDF](#csharp-cgm-to-pdf)
- [C# 如何将 CGM 图像转换为 PDF](#csharp-cgm-to-pdf)

_格式_: **DICOM**
- [C# DICOM 转 PDF](#csharp-dicom-to-pdf)
- [C# 将 DICOM 转换为 PDF](#csharp-dicom-to-pdf)
- [C# 如何将 DICOM 图像转换为 PDF](#csharp-dicom-to-pdf)
- [C# 如何将DICOM图像转换为PDF](#csharp-dicom-to-pdf)

_格式_: **EMF**
- [C# EMF转PDF](#csharp-emf-to-pdf)
- [C# 将EMF转换为PDF](#csharp-emf-to-pdf)
- [C# 如何将EMF图像转换为PDF](#csharp-emf-to-pdf)

_格式_: **GIF**
- [C# GIF转PDF](#csharp-gif-to-pdf)
- [C# 将GIF转换为PDF](#csharp-gif-to-pdf)
- [C# 如何将GIF图像转换为PDF](#csharp-gif-to-pdf)

_格式_: **JPG**
- [C# JPG转PDF](#csharp-jpg-to-pdf)
- [C# 将JPG转换为PDF](#csharp-jpg-to-pdf)
- [C# 如何将JPG图像转换为PDF](#csharp-jpg-to-pdf)

_格式_: **PNG**
- [C# PNG转PDF](#csharp-png-to-pdf)
- [C# 将PNG转换为PDF](#csharp-png-to-pdf)
- [C# 如何将PNG图像转换为PDF](#csharp-png-to-pdf)

_格式_: **SVG**
- [C# SVG转PDF](#csharp-svg-to-pdf)
- [C# 将SVG转换为PDF](#csharp-svg-to-pdf)
- [C# 如何将SVG图像转换为PDF](#csharp-svg-to-pdf)

_格式_: **TIFF**
- [C# TIFF转PDF](#csharp-tiff-to-pdf)
- [C# 将TIFF转换为PDF](#csharp-tiff-to-pdf)
- [C# 如何将TIFF图像转换为PDF](#csharp-tiff-to-pdf)
 - [C# 如何将 TIFF 图像转换为 PDF](#csharp-tiff-to-pdf)

其他本文涵盖的主题
- [另请参阅](#see-also)


## C# 图像转 PDF 转换

**Aspose.PDF for .NET** 允许您将不同格式的图像转换为 PDF 文件。我们的库展示了将最流行的图像格式转换为 PDF 的代码片段，如 - BMP、CGM、DICOM、EMF、JPG、PNG、SVG 和 TIFF 格式。

## 转换 BMP 为 PDF

使用 **Aspose.PDF for .NET** 库将 BMP 文件转换为 PDF 文档。

<abbr title="位图图像文件">BMP</abbr> 图像是具有扩展名 .BMP 的文件，代表位图图像文件，用于存储位图数字图像。这些图像独立于图形适配器，也称为设备独立位图（DIB）文件格式。
您可以使用 Aspose.PDF for .NET API 将 BMP 转换为 PDF 文件。因此，您可以按照以下步骤将 BMP 图像转换为 PDF：

<a name="csharp-bmp-to-pdf" id="csharp-bmp-to-pdf"><strong>步骤：在 C# 中将 BMP 转换为 PDF</strong></a>

1.
1.
2. 载入输入的**BMP**图片。
3. 最终保存输出的PDF文件。

以下代码片段遵循这些步骤，并展示如何使用C#将BMP转换为PDF：

```csharp
//初始化空的PDF文档
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // 载入示例BMP图片文件
    image.File = dataDir + "Sample.bmp";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // 保存输出的PDF文档
    pdfDocument.Save(dataDir + "BMPtoPDF.pdf");
}
```

{{% alert color="success" %}}
**尝试在线转换BMP为PDF**

Aspose为您提供在线免费应用程序["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF Convertion BMP to PDF using Free App](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## 转换CGM为PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> 是计算机图形元文件格式的文件扩展名，常用于CAD（计算机辅助设计）和演示图形应用程序。
<abbr title="计算机图形元文件">CGM</abbr>是一个常用于CAD（计算机辅助设计）和演示图形应用程序中的计算机图形元文件格式的文件扩展名。

查看下面的代码片段，了解如何将CGM文件转换为PDF格式。

<a name="csharp-cgm-to-pdf" id="csharp-cgm-to-pdf"><strong>步骤：在C#中将CGM转换为PDF</strong></a>

1. 创建[CgmLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/cgmloadoptions)类的实例。
2. 使用指定的源文件名和选项创建[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)类的实例。
3. 使用所需的文件名保存文档。

```csharp
public static void ConvertCGMtoPDF()
{
    CgmLoadOptions option = new CgmLoadOptions();
    Document pdfDocument= new Document(_dataDir+"corvette.cgm", option);
    pdfDocument.Save(_dataDir+"CGMtoPDF.pdf");
}
```

## 将DICOM转换为PDF

<abbr title="医学数字成像和通讯">DICOM</abbr>格式是医疗行业用于创建、存储、传输和可视化检查过的患者的数字医学图像和文档的标准。
<abbr title="数字成像和通信医学">DICOM</abbr>格式是医疗行业用于创建、存储、传输和可视化已检查患者的数字医学图像和文件的行业标准。

**Aspsoe.PDF for .NET** 允许您转换 DICOM 和 SVG 图像，但由于技术原因，添加图像时需要指定要添加到 PDF 的文件类型：

<a name="csharp-dicom-to-pdf" id="csharp-dicom-to-pdf"><strong>步骤：在 C# 中将 DICOM 转换为 PDF</strong></a>

1. 创建 Image 类的对象。
2. 将图像添加到页面的 Paragraphs 集合中。
3. 指定 [FileType](https://reference.aspose.com/pdf/net/aspose.pdf/image/properties/filetype) 属性。
4. 指定文件的路径或来源。
    - 如果图像位于硬盘上的位置，请使用 Image.File 属性指定路径位置。
    - 如果图像放置在 MemoryStream 中，请将保存图像的对象传递给 Image.ImageStream 属性。

以下代码片段显示了如何使用 Aspose.PDF 将 DICOM 文件转换为 PDF 格式。
以下代码片段显示了如何使用 Aspose.PDF 将 DICOM 文件转换为 PDF 格式。

```csharp
private const string _dataDir = "..\\..\\..\\..\\Samples";
// 使用 Image 类将 DICOM 图像转换为 PDF
public static void ConvertDICOMtoPDF()
{
    // 实例化 Document 对象
    Document pdfDocument = new Document();

    // 向文档的页面集合中添加一页
    Page page = pdfDocument.Pages.Add();

    Image image = new Image
    {
        FileType = ImageFileType.Dicom,
        File = System.IO.Path.Combine(_dataDir,"bmode.dcm")
    };
    pdfDocument.Pages[1].Paragraphs.Add(image);
    // 保存输出为 PDF 格式
    pdfDocument.Save(System.IO.Path.Combine(_dataDir,"PDFWithDicomImage_out.pdf"));
}
```

{{% alert color="success" %}}
**尝试在线将 DICOM 转换为 PDF**

Aspose 为您提供在线免费应用程序 ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)，您可以在此尝试探索其功能和工作质量。
{{% /alert %}}

## 将EMF转换为PDF

<abbr title="增强型元文件格式">EMF</abbr>EMF独立于设备地存储图形图像。EMF的元文件包括按时间顺序的可变长度记录，可以在任何输出设备上解析后呈现存储的图像。此外，您可以使用以下步骤将EMF转换为PDF图像：

<a name="csharp-emf-to-pdf" id="csharp-emf-to-pdf"><strong>步骤：在C#中将EMF转换为PDF</strong></a>

1. 首先，初始化[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)类对象。
2. 加载**EMF**图像文件。
3. 将加载的EMF图像添加到页面。
4. 保存PDF文档。

此外，以下代码片段显示了如何在您的.NET代码片段中使用C#将EMF转换为PDF：

```csharp
// 初始化新的PDF文档
var doc = new Document();

// 指定输入EMF图像文件的路径
var imageFile = dataDir + "drawing.emf";
var page = doc.Pages.Add();
string file = imageFile;
FileStream filestream = new FileStream(file, FileMode.Open, FileAccess.Read);
BinaryReader reader = new BinaryReader(filestream);
long numBytes = new FileInfo(file).Length;
byte[] bytearray = reader.ReadBytes((int)numBytes);
Stream stream = new MemoryStream(bytearray);
var b = new Bitmap(stream);

// 指定页面尺寸属性
page.PageInfo.Margin.Bottom = 0;
page.PageInfo.Margin.Top = 0;
page.PageInfo.Margin.Left = 0;
page.PageInfo.Margin.Right = 0;
page.PageInfo.Width = b.Width;
page.PageInfo.Height = b.Height;
var image = new Aspose.Pdf.Image();
image.File = imageFile;
page.Paragraphs.Add(image);

//保存输出PDF文档
doc.Save(dataDir + "EMFtoPDF.pdf");
```
{{% alert color="success" %}}
**尝试在线将EMF转换为PDF**

Aspose为您提供免费在线应用程序[“EMF转PDF”](https://products.aspose.app/pdf/conversion/emf-to-pdf/)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF 转换 EMF 为 PDF 使用免费应用](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## 将GIF转换为PDF

使用 **Aspose.PDF for .NET** 库将GIF文件转换为PDF文档。

<abbr title="Graphics Interchange Format">GIF</abbr> 能够在不超过256色的格式中存储无损压缩数据。GIF格式是1987年（GIF87a）由CompuServe开发的，用于通过网络传输位图图像。
您可以使用Aspose.PDF for .NET API将GIF转换为PDF文件。因此，您可以按照以下步骤将GIF图像转换为PDF：

<a name="csharp-gif-to-pdf" id="csharp-gif-to-pdf"><strong>步骤：在C#中将GIF转换为PDF</strong></a>

1.
1.
2. 加载输入的 **GIF** 图像。
3. 最后，保存输出的 PDF 文件。

因此，以下代码片段遵循这些步骤，并展示如何使用 C# 将 BMP 转换为 PDF：

```csharp
//初始化空白 PDF 文档
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // 加载示例 GIF 图像文件
    image.File = dataDir + "Sample.gif";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // 保存输出 PDF 文档
    pdfDocument.Save(dataDir + "GIFtoPDF.pdf");
}
```

{{% alert color="success" %}}
**尝试在线将 GIF 转换为 PDF**

Aspose 为您提供在线免费应用程序 ["GIF to PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF 转换 GIF 到 PDF 使用免费应用](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## 将 JPG 转换为 PDF

无需纠结如何将 JPG 转换为 PDF，因为 **Apose.PDF for .NET** 库提供了最佳解决方案。
不需要纠结如何将JPG转换为PDF，因为 **Apose.PDF for .NET** 库提供了最佳解决方案。

您可以通过以下步骤使用Aspose.PDF for .NET轻松将JPG图片转换为PDF：

<a name="csharp-jpg-to-pdf" id="csharp-jpg-to-pdf"><strong>步骤：在C#中将JPG转换为PDF</strong></a>

1. 初始化 [Document](https://reference.aspose.com/page/net/aspose.page/document) 类的对象。
2. 向PDF文档添加新页面。
3. 加载 **JPG** 图片并添加到段落。
4. 保存输出的PDF。

以下代码片段展示了如何使用C#将JPG图像转换为PDF：

```csharp
// 加载输入的JPG文件
String path = dataDir + "Aspose.jpg";

// 初始化新的PDF文档
Document doc = new Document();

// 在空文档中添加空白页
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// 在页面上添加图片
page.Paragraphs.Add(image);

// 保存输出的PDF文件
doc.Save(dataDir + "ImagetoPDF.pdf");
```

然后您可以看到如何将图像转换为PDF，**与页面的高度和宽度相同**。
然后您可以看到如何将图像转换为具有**页面相同高度和宽度**的 PDF。

1. 加载输入图像文件
1. 获取图像的高度和宽度
1. 设置页面的高度、宽度和边距
1. 保存输出 PDF 文件

以下代码片段显示了如何使用 C# 将图像转换为具有相同页面高度和宽度的 PDF：

```csharp
// 加载输入 JPG 图像文件
String path = dataDir + "Aspose.jpg";
System.Drawing.Image srcImage = System.Drawing.Image.FromFile(path);

// 读取输入图像的高度
int h = srcImage.Height;

// 读取输入图像的宽度
int w = srcImage.Width;

// 初始化一个新的 PDF 文档
Document doc = new Document();

// 添加一个空白页
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// 设置页面尺寸和边距
page.PageInfo.Height = (h);
page.PageInfo.Width = (w);
page.PageInfo.Margin.Bottom = (0);
page.PageInfo.Margin.Top = (0);
page.PageInfo.Margin.Right = (0);
page.PageInfo.Margin.Left = (0);
page.Paragraphs.Add(image);

// 保存输出 PDF 文件
doc.Save(dataDir + "ImagetoPDF_HeightWidth.pdf");
```
{{% alert color="success" %}}
**尝试在线将JPG转换为PDF**

Aspose为您提供在线免费应用程序["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将JPG转换为PDF](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## 将PNG转换为PDF

**Aspose.PDF for .NET** 支持将PNG图像转换为PDF格式的功能。查看下一个代码片段，以实现您的任务。

<abbr title="Portable Network Graphics">PNG</abbr> 指的是一种光栅图像文件格式，它使用无损压缩，这使得它在用户中很受欢迎。

您可以使用以下步骤将PNG转换为PDF图像：

<a name="csharp-png-to-pdf" id="csharp-png-to-pdf"><strong>步骤：在C#中将PNG转换为PDF</strong></a>

1. 加载输入**PNG**图像。
2. 读取高度和宽度值。
3.
设置页面尺寸。
保存输出文件。

此外，以下代码片段显示了如何在您的.NET应用程序中使用C#将PNG转换为PDF：

```csharp
// 加载输入的PNG文件
String path = dataDir + "Aspose.png";
System.Drawing.Image srcImage = System.Drawing.Image.FromFile(path);
int h = srcImage.Height;
int w = srcImage.Width;

// 初始化新文档
Document doc = new Document();
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// 设置页面尺寸
page.PageInfo.Height = (h);
page.PageInfo.Width = (w);
page.PageInfo.Margin.Bottom = (0);
page.PageInfo.Margin.Top = (0);
page.PageInfo.Margin.Right = (0);
page.PageInfo.Margin.Left = (0);
page.Paragraphs.Add(image);

// 保存输出的PDF
doc.Save(dataDir + "ImagetoPDF.pdf");
```

{{% alert color="success" %}}
**尝试在线将PNG转换为PDF**

Aspose为您提供在线免费应用程序["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)，您可以尝试探索其功能和工作质量。

{{% /alert %}}

## 将 SVG 转换为 PDF

**Aspose.PDF for .NET** 介绍如何将 SVG 图像转换为 PDF 格式以及如何获取源 SVG 文件的尺寸。

可缩放矢量图形（SVG）是一个基于 XML 的文件格式的二维矢量图形规范系列，包括静态和动态（交互式或动画）。SVG 规范是一个开放标准，自 1999 年以来一直在由万维网联盟（W3C）开发。

SVG 图像及其行为在 XML 文本文件中定义。
SVG 图像及其行为在 XML 文本文件中定义。

{{% alert color="success" %}}
**尝试在线将 SVG 格式转换为 PDF**

Aspose.PDF for .NET 为您提供在线免费应用程序 ["SVG 到 PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF 转换 SVG 到 PDF 的免费应用](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

要将 SVG 文件转换为 PDF，使用名为 [SvgLoadOptions](https://reference.aspose.com/net/pdf/aspose.pdf/svgloadoptions) 的类，该类用于初始化 [`LoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions) 对象。稍后，在文档对象初始化期间将此对象作为参数传递，帮助 PDF 渲染引擎确定源文档的输入格式。

<a name="csharp-svg-to-pdf" id="csharp-svg-to-pdf"><strong>步骤：在 C# 中将 SVG 转换为 PDF</strong></a>

1.
1.
2. 创建一个[`Document`](https://reference.aspose.com/pdf/net/aspose.pdf/document)类的实例，提及源文件名和选项。
3. 使用所需的文件名保存文档。

以下代码片段显示了使用Aspose.PDF for .NET将SVG文件转换为PDF格式的过程。

```csharp
public static void ConvertSVGtoPDF()
{
    SvgLoadOptions option = new SvgLoadOptions();
    Document pdfDocument= new Document(_dataDir + "car.svg", option);
    pdfDocument.Save(_dataDir + "svgtest.pdf");
}
```

## 获取SVG尺寸

还可以获取源SVG文件的尺寸。如果我们希望SVG覆盖输出PDF的整个页面，这些信息可能很有用。ScgLoadOption类的AdjustPageSize属性满足了这一需求。此属性的默认值为false。如果该值设置为true，输出的PDF将与源SVG的尺寸相同。

以下代码片段显示了获取源SVG文件尺寸并生成PDF文件的过程。
以下代码片段展示了获取源 SVG 文件尺寸和生成 PDF 文件的过程。

```csharp
public static void ConvertSVGtoPDF_Advanced()
{
    // 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // 文档目录的路径。
    string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    var loadopt = new SvgLoadOptions();
    loadopt.AdjustPageSize = true;
    var svgDoc = new Document(dataDir + "GetSVGDimensions.svg", loadopt);
    svgDoc.Pages[1].PageInfo.Margin.Top = 0;
    svgDoc.Pages[1].PageInfo.Margin.Left = 0;
    svgDoc.Pages[1].PageInfo.Margin.Bottom = 0;
    svgDoc.Pages[1].PageInfo.Margin.Right = 0;
    svgDoc.Save(dataDir + "GetSVGDimensions_out.pdf");
}
```

### 支持的 SVG 功能

<table>
    <thead>
        <tr>
            <th>
                <p>SVG 标签</p>
            </th>
            <th>
                <p>示例用途</p>
            </th>
        </tr>
    </thead>
    <tbody>

<tbody>
   <tr>
       <td>
           <p>圆圈</p>
       </td>
       <td>
           <code><pre>&lt;circle id="r2" cx="10" cy="10" r="10" stroke="blue" stroke-width="2"&gt;</pre></code>
       </td>
   </tr>
   <tr>
       <td>
           <p>定义</p>
       </td>
       <td>
           <code>&lt;defs&gt;&nbsp; <br> &lt;rect id="r1" width="15" height="15"
               stroke="blue" stroke-width="2" /&gt;&nbsp; <br> &lt;circle id="r2"
               cx="10" cy="10" r="10" stroke="blue" stroke-width="2"/&gt;&nbsp; <br>
               &lt;circle id="r3" cx="10" cy="10" r="10" stroke="blue" stroke-width="3"/&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br> &lt;use
               x="25" y="40" xlink:href="#r1" fill="red"/&gt;&nbsp; <br> &lt;use
               x="35" y="15" xlink:href="#r2" fill="green"/&gt;&nbsp; <br> &lt;use
               x="58" y="50" xlink:href="#r3" fill="blue"/&gt;</code>
       </td>
   </tr>
</tbody>
```

         </tr>
        <tr>
            <td>
                <p>tref</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text
                    id="ReferencedText"&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    引用的字符数据&nbsp; <br> &nbsp;&nbsp;&nbsp;
                    &lt;/text&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;text x="10" y="100" font-size="15" fill="red" &gt;&nbsp; <br
                        class="atl-forced-newline"> &nbsp;&nbsp;&nbsp; &lt;tref
                    xlink:href="#ReferencedText"/&gt;&nbsp; <br> &lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>use</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text id="Text" x="400"
                    y="200"&nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; font-family="Verdana" font-size="100"
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; font-family="Verdana" font-size="100"
文本锚点="中间" &gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
蒙版文本 <br> &nbsp;&nbsp;&nbsp; &lt;/文本&gt;&nbsp; <br
    class="atl-forced-newline"> &lt;use xlink:href="#Text" fill="blue"&nbsp; /&gt;</p>
</td>
</tr>
<tr>
<td>
<p>椭圆</p>
</td>
<td>
<p>&lt;ellipse cx="2.5" cy="1.5" rx="2" ry="1" fill="red" /&gt;</p>
</td>
</tr>
<tr>
<td>
<p>g</p>
</td>
<td>
<p>&lt;g fill="none" stroke="暗灰色" stroke-width="1.5" &gt;&nbsp; <br>
    &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="-7"
    y1="-7" x2="-3" y2="-3"/&gt;&nbsp; <br> &nbsp;&nbsp;
    &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="7" x2="3"
```

<tr>
    <td>
        <p>线</p>
    </td>
    <td>
        <p>&lt;line x1="7" y1="7" x2="3" y2="3"/&gt; <br> &lt;line x1="-7" y1="7" x2="-3" y2="3"/&gt; <br> &lt;line x1="7" y1="-7" x2="3" y2="-3"/&gt; <br class="atl-forced-newline"> &lt;/g&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>图像</p>
    </td>
    <td>
        <p>&lt;image id="ShadedRelief" x="24" y="4" width="64" height="82" xlink:href="relief.jpg"/&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>线</p>
    </td>
    <td>
        <p>&lt;line style="stroke:#eea;stroke-width:8" x1="10" y1="30" x2="260" y2="100"/&gt;</p>
    </td>
</tr>
```

<tr>
    <td>
        <p>线</p>
    </td>
    <td>
        <p>&lt;line style="stroke:#eea;stroke-width:8" x1="10" y1="30" x2="260" y2="100"/&gt;&nbsp;</p>
    </td>
</tr>
<tr>
    <td>
        <p>路径</p>
    </td>
    <td>
        <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
            "/&gt;&nbsp;</p>
    </td>
</tr>
<tr>
    <td>
        <p>样式</p>
    </td>
    <td>
        <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
            "/&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>多边形</p>
    </td>
    <td>
        <p>&lt;polygon style="stroke:#24a;stroke-width:1.5;fill:#eefefe" points="10,10 180,10 10,250 10,10"
            /&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>折线</p>
    </td>
```

<tr>
    <td>
        <p>折线</p>
    </td>
    <td>
        <p>&lt;polyline fill="none" stroke="dimgray" stroke-width="1" points="-3,-6 3,-6 3,1 5,1 0,7 -5,1
            -3,1 -3,-5"/&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>矩形</p>
    </td>
    <td>
        <p>&lt;rect x="0" y="0" width="400" height="600" stroke="none" fill="aliceblue" /&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>SVG</p>
    </td>
    <td>
        <p>&lt;svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="10cm" height="5cm" &gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>文本</p>
    </td>
    <td>
        <p>&lt;text font-family="sans-serif" fill="dimgray" font-size="22px" font-weight="bold" x="58"
            y="30" pointer-events="none"&gt;地图标题&lt;/text&gt;</p>
    </td>
</tr>
```

<table>
    <tbody>
        <tr>
            <td>
                <p>字体</p>
            </td>
            <td>
                <p>&lt;text x="10" y="100" font-size="15" fill="red" &gt;&nbsp; <br>
                    &nbsp;&nbsp;&nbsp; 示例文本&nbsp; <br> &lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>tspan</p>
            </td>
            <td>
                <p>&lt;tspan dy="25" x="25"&gt;六种墨水颜色输入值。在这里将 &lt;/tspan&gt;</p>
            </td>
        </tr>
    </tbody>
</table>

## 将TIFF转换为PDF

**Aspose.PDF** 支持文件格式，无论是单帧还是多帧 <abbr title="标签图像文件格式">TIFF</abbr> 图像。这意味着您可以在 .NET 应用程序中将 TIFF 图像转换为 PDF。

TIFF 或 TIF，标签图像文件格式，代表旨在用于符合此文件格式标准的各种设备的栅格图像。
```
TIFF或TIF，标签图像文件格式，代表了旨在用于符合此文件格式标准的各种设备上的光栅图像。

您可以像转换其他光栅文件格式的图形一样将TIFF转换为PDF：

<a name="csharp-tiff-to-pdf" id="csharp-tiff-to-pdf"><strong>步骤：在C#中将TIFF转换为PDF</strong></a>

1. 创建新的[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)类对象并添加页面。
2. 加载输入**TIFF**图像。
3. 保存PDF文档。

```csharp
初始化空白PDF文档
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // 加载示例Tiff图像文件
    image.File = dataDir + "sample.tiff";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // 保存输出PDF文档
    pdfDocument.Save(dataDir + "TIFFtoPDF.pdf");
}
```

如果您需要将多页TIFF图像转换为多页PDF文档并控制一些参数，例如
如果您需要将多页TIFF图像转换为多页PDF文档并控制一些参数，例如：

1. 实例化Document类的实例
1. 加载输入TIFF图像
1. 获取帧的FrameDimension
1. 为每个帧添加新页面
1. 最后，将图像保存到PDF页面

以下代码片段显示了如何使用C#将多页或多帧TIFF图像转换为PDF：

```csharp
public static void TiffToPDF2()
{
    // 初始化新文档
    Document pdf = new Document();

    //将TIFF图像加载到流中
    Bitmap bitmap = new Bitmap(File.OpenRead(_dataDir+"multipage.tif"));
    // 将多页或多帧TIFF转换为PDF
    FrameDimension dimension = new FrameDimension(bitmap.FrameDimensionsList[0]);
    int frameCount = bitmap.GetFrameCount(dimension);

    // 遍历每个帧
    for (int frameIdx = 0; frameIdx <= frameCount - 1; frameIdx++)
    {
        Page page = pdf.Pages.Add();

        bitmap.SelectActiveFrame(dimension, frameIdx);

        MemoryStream currentImage = new MemoryStream();
        bitmap.Save(currentImage, ImageFormat.Tiff);

        Aspose.Pdf.Image imageht = new Aspose.Pdf.Image
        {
            ImageStream = currentImage,
            //应用其他选项
            //ImageScale = 0.5
        };
        page.Paragraphs.Add(imageht);
    }

    // 保存输出PDF文件
    pdf.Save(_dataDir + "TifftoPDF.pdf");
}
```
## 适用于

|**平台**|**支持**|**评论**|
| :- | :- |:- |
|Windows .NET Framework|2.0-4.6| |
|Windows .NET Core |2.0-3.1| |
|.NET 5 Windows| |
|Linux .NET Core|2.0-3.1 | |
|.NET 5 Linux | |

## 另见

本文还涵盖了以下主题。代码与上面相同。

_格式_：**BMP**
- [C# BMP 转 PDF 代码](#csharp-bmp-to-pdf)
- [C# BMP 转 PDF API](#csharp-bmp-to-pdf)
- [C# BMP 转 PDF 编程方式](#csharp-bmp-to-pdf)
- [C# BMP 转 PDF 库](#csharp-bmp-to-pdf)
- [C# 保存 BMP 为 PDF](#csharp-bmp-to-pdf)
- [C# 从 BMP 生成 PDF](#csharp-bmp-to-pdf)
- [C# 从 BMP 创建 PDF](#csharp-bmp-to-pdf)
- [C# BMP 转 PDF 转换器](#csharp-bmp-to-pdf)

_格式_：**CGM**
- [C# CGM 转 PDF 代码](#csharp-cgm-to-pdf)
- [C# CGM 转 PDF API](#csharp-cgm-to-pdf)
- [C# CGM 转 PDF 编程方式](#csharp-cgm-to-pdf)
- [C# CGM 转 PDF 库](#csharp-cgm-to-pdf)
- [C# 保存 CGM 为 PDF](#csharp-cgm-to-pdf)
- [C# 从 CGM 生成 PDF](#csharp-cgm-to-pdf)
- [C# 从 CGM 创建 PDF](#csharp-cgm-to-pdf)
- [C# CGM 转 PDF 转换器](#csharp-cgm-to-pdf)
- [C# CGM to PDF Converter](#csharp-cgm-to-pdf)

_Format_: **DICOM**
- [C# DICOM 转 PDF 代码](#csharp-dicom-to-pdf)
- [C# DICOM 转 PDF API](#csharp-dicom-to-pdf)
- [C# DICOM 转 PDF 编程](#csharp-dicom-to-pdf)
- [C# DICOM 转 PDF 库](#csharp-dicom-to-pdf)
- [C# 将 DICOM 保存为 PDF](#csharp-dicom-to-pdf)
- [C# 从 DICOM 生成 PDF](#csharp-dicom-to-pdf)
- [C# 从 DICOM 创建 PDF](#csharp-dicom-to-pdf)
- [C# DICOM 转 PDF 转换器](#csharp-dicom-to-pdf)

_Format_: **EMF**
- [C# EMF 转 PDF 代码](#csharp-emf-to-pdf)
- [C# EMF 转 PDF API](#csharp-emf-to-pdf)
- [C# EMF 转 PDF 编程](#csharp-emf-to-pdf)
- [C# EMF 转 PDF 库](#csharp-emf-to-pdf)
- [C# 将 EMF 保存为 PDF](#csharp-emf-to-pdf)
- [C# 从 EMF 生成 PDF](#csharp-emf-to-pdf)
- [C# 从 EMF 创建 PDF](#csharp-emf-to-pdf)
- [C# EMF 转 PDF 转换器](#csharp-emf-to-pdf)
