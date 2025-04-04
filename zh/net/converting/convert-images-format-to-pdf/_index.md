---
title: 将各种图像格式转换为PDF在.NET中
linktitle: 将图像转换为PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /zh/net/convert-images-format-to-pdf/
lastmod: "2021-11-01"
description: 使用C# .NET将各种图像格式（如CDR、DJVU、BMP、CGM、JPEG、DICOM、PNG、TIFF、EMF和SVG）转换为PDF。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert various Images formats to PDF in .NET",
    "alternativeHeadline": "Convert Multiple Image Formats to PDF with C#",
    "abstract": "介绍Aspose.PDF for .NET中的一个强大功能，可以无缝转换各种图像格式，包括BMP、CGM、DICOM、EMF、JPG、PNG、SVG、TIFF、CDR和DJVU，生成高质量的PDF文档。此功能提供了一种简单的方法，将图像到PDF的转换集成到您的.NET应用程序中，确保高效处理多样的图形内容。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "3215",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/convert-images-format-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-images-format-to-pdf/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 概述

本文解释了如何使用C#将各种图像格式转换为PDF。它涵盖了以下主题。

以下代码片段也适用于[Aspose.PDF.Drawing](/pdf/zh/net/drawing/)库。

- [将BMP转换为PDF](#csharp-bmp-to-pdf)
- [将CGM转换为PDF](#csharp-cgm-to-pdf)
- [将DICOM转换为PDF](#csharp-dicom-to-pdf)
- [将EMF转换为PDF](#csharp-emf-to-pdf)
- [将GIF转换为PDF](#csharp-gif-to-pdf)
- [将JPG转换为PDF](#csharp-jpg-to-pdf)
- [将PNG转换为PDF](#csharp-png-to-pdf)
- [将SVG转换为PDF](#csharp-svg-to-pdf)
- [将TIFF转换为PDF](#csharp-tiff-to-pdf)
- [将CDR转换为PDF](#csharp-cdr-to-pdf)
- [将DJVU转换为PDF](#csharp-djvu-to-pdf)
- [将HEIC转换为PDF](#csharp-heic-to-pdf)

## C#图像到PDF转换

**Aspose.PDF for .NET**允许您将不同格式的图像转换为PDF文件。我们的库演示了将最流行的图像格式（如BMP、CGM、DICOM、EMF、JPG、PNG、SVG、CDR、HEIC和TIFF格式）转换的代码片段。

## 将BMP转换为PDF

使用**Aspose.PDF for .NET**库将BMP文件转换为PDF文档。

<abbr title="位图图像文件">BMP</abbr>图像是具有扩展名的文件。BMP表示用于存储位图数字图像的位图图像文件。这些图像独立于图形适配器，也称为设备独立位图（DIB）文件格式。
您可以使用Aspose.PDF for .NET API将BMP转换为PDF文件。因此，您可以按照以下步骤转换BMP图像：

<a name="csharp-bmp-to-pdf" id="csharp-bmp-to-pdf"><strong>将BMP转换为PDF</strong></a>

1. 初始化一个新的[Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document)类对象。
2. 加载输入的**BMP**图像。
3. 最后，保存输出的PDF文件。

因此，以下代码片段遵循这些步骤，并展示如何使用C#将BMP转换为PDF：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertBMPtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        
        // Load BMP file
        image.File = dataDir + "BMPtoPDF.bmp";
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "BMPtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**尝试在线将BMP转换为PDF**

Aspose为您提供在线免费应用程序["BMP到PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF将BMP转换为PDF的免费应用](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## 将CGM转换为PDF

<abbr title="计算机图形元文件">CGM</abbr>是计算机图形元文件格式的文件扩展名，通常用于CAD（计算机辅助设计）和演示图形应用程序。CGM是一种矢量图形格式，支持三种不同的编码方法：二进制（最佳程序读取速度）、基于字符（生成最小文件大小并允许更快的数据传输）或明文编码（允许用户使用文本编辑器读取和修改文件）。

请查看下一个代码片段以将CGM文件转换为PDF格式。

<a name="csharp-cgm-to-pdf" id="csharp-cgm-to-pdf"><strong>将CGM转换为PDF</strong></a>

1. 创建[CgmLoadOptions](https://reference.aspose.com/pdf/zh/net/aspose.pdf/cgmloadoptions)类的实例。
2. 创建一个[Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document)类的实例，并提及源文件名和选项。
3. 使用所需的文件名保存文档。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertCGMtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    var option = new Aspose.Pdf.CgmLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CGMtoPDF.cgm", option))
    {
        // Save PDF document
        document.Save(dataDir + "CGMtoPDF_out.pdf");
    }
}
```

## 将DICOM转换为PDF

<abbr title="医学中的数字成像和通信">DICOM</abbr>格式是医疗行业标准，用于创建、存储、传输和可视化数字医学图像和被检查患者的文档。

**Aspose.PDF for .NET**允许您转换DICOM和SVG图像，但由于技术原因，添加图像时需要指定要添加到PDF的文件类型：

<a name="csharp-dicom-to-pdf" id="csharp-dicom-to-pdf"><strong>将DICOM转换为PDF</strong></a>

1. 创建Image类的对象。
2. 将图像添加到页面的段落集合中。
3. 指定[FileType](https://reference.aspose.com/pdf/zh/net/aspose.pdf/image/properties/filetype)属性。
4. 指定文件的路径或来源。
    - 如果图像位于硬盘上的某个位置，请使用Image.File属性指定路径位置。
    - 如果图像放置在MemoryStream中，请将持有图像的对象传递给Image.ImageStream属性。

以下代码片段展示了如何使用Aspose.PDF将DICOM文件转换为PDF格式。您应该加载DICOM图像，将图像放置在PDF文件的页面上，并将输出保存为PDF。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDICOMtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document 
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        
        var image = new Aspose.Pdf.Image
        {
            FileType = ImageFileType.Dicom,
            File = dataDir + "DICOMtoPDF.dcm"
        };
        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "DICOMtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**尝试在线将DICOM转换为PDF**

Aspose为您提供在线免费应用程序["DICOM到PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF将DICOM转换为PDF的免费应用](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## 将EMF转换为PDF

<abbr title="增强型元文件格式">EMF</abbr>以设备无关的方式存储图形图像。EMF的元文件由按时间顺序排列的可变长度记录组成，可以在任何输出设备上解析后呈现存储的图像。此外，您可以使用以下步骤将EMF转换为PDF图像：

<a name="csharp-emf-to-pdf" id="csharp-emf-to-pdf"><strong>将EMF转换为PDF</strong></a>

1. 首先，初始化[Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document)类对象。
2. 加载**EMF**图像文件。
3. 将加载的EMF图像添加到页面。
4. 保存PDF文档。

此外，以下代码片段展示了如何在您的.NET代码片段中使用C#将EMF转换为PDF：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertEMFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document 
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load EMF file
        image.File = dataDir + "EMFtoPDF.emf";

        // Specify page dimension properties
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;
        page.PageInfo.Margin.Left = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Width = image.BitmapSize.Width;
        page.PageInfo.Height = image.BitmapSize.Height;

        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "EMFtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**尝试在线将EMF转换为PDF**

Aspose为您提供在线免费应用程序["EMF到PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF将EMF转换为PDF的免费应用](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## 将GIF转换为PDF

使用**Aspose.PDF for .NET**库将GIF文件转换为PDF文档。

<abbr title="图形交换格式">GIF</abbr>能够以不超过256种颜色的格式存储无损压缩的数据。硬件无关的GIF格式由CompuServe于1987年（GIF87a）开发，用于通过网络传输位图图像。
您可以使用Aspose.PDF for .NET API将GIF转换为PDF文件。因此，您可以按照以下步骤转换GIF图像：

<a name="csharp-gif-to-pdf" id="csharp-gif-to-pdf"><strong>将GIF转换为PDF</strong></a>

1. 初始化一个新的[Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document)类对象。
2. 加载输入的**GIF**图像。
3. 最后，保存输出的PDF文件。

因此，以下代码片段遵循这些步骤，并展示如何使用C#将GIF转换为PDF：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertGIFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        
        // Load sample GIF image file
        image.File = dataDir + "GIFtoPDF.gif";
        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "GIFtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**尝试在线将GIF转换为PDF**

Aspose为您提供在线免费应用程序["GIF到PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF将GIF转换为PDF的免费应用](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## 将JPG转换为PDF

不必担心如何将JPG转换为PDF，因为**Apose.PDF for .NET**库提供了最佳解决方案。

您可以通过以下步骤非常轻松地将JPG图像转换为PDF：

<a name="csharp-jpg-to-pdf" id="csharp-jpg-to-pdf"><strong>将JPG转换为PDF</strong></a>

1. 初始化[Document](https://reference.aspose.com/page/net/aspose.page/document)类对象。
2. 向PDF文档添加一个新页面。
3. 加载**JPG**图像并添加到段落中。
4. 保存输出PDF。

下面的代码片段展示了如何使用C#将JPG图像转换为PDF：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertJPGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document 
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load input JPG file
        image.File = dataDir + "JPGtoPDF.jpg";
        
        // Add image on a page
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "JPGtoPDF_out.pdf");
    }
}
```

然后，您可以看到如何将图像转换为PDF，**页面的高度和宽度相同**。我们将获取图像的尺寸，并相应地设置PDF文档的页面尺寸，步骤如下：

1. 加载输入图像文件。
1. 设置页面的高度、宽度和边距。
1. 保存输出PDF文件。

以下代码片段展示了如何使用C#将图像转换为PDF，页面高度和宽度相同：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertJPGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load JPEG file
        image.File = dataDir + "JPGtoPDF.jpg";
        
        // Read Height of input image
        page.PageInfo.Height = image.BitmapSize.Height;
        // Read Width of input image
        page.PageInfo.Width = image.BitmapSize.Width;
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Margin.Left = 0;
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "JPGtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**尝试在线将JPG转换为PDF**

Aspose为您提供在线免费应用程序["JPG到PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF将JPG转换为PDF的免费应用](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## 将PNG转换为PDF

**Aspose.PDF for .NET**支持将PNG图像转换为PDF格式的功能。请查看下一个代码片段以实现您的任务。

<abbr title="可移植网络图形">PNG</abbr>指的是一种使用无损压缩的光栅图像文件格式，这使得它在用户中非常受欢迎。

您可以使用以下步骤将PNG转换为PDF图像：

<a name="csharp-png-to-pdf" id="csharp-png-to-pdf"><strong>将PNG转换为PDF</strong></a>

1. 加载输入的**PNG**图像。
2. 读取高度和宽度值。
3. 创建新的[Document](https://reference.aspose.com/page/net/aspose.page/document)对象并添加页面。
4. 设置页面尺寸。
5. 保存输出文件。

此外，下面的代码片段展示了如何在您的.NET应用程序中使用C#将PNG转换为PDF：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPNGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load PNG file
        image.File = dataDir + "PNGtoPDF.png";
        
        // Read Height of input image
        page.PageInfo.Height = image.BitmapSize.Height;
        // Read Width of input image
        page.PageInfo.Width = image.BitmapSize.Width;
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Margin.Left = 0;
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "PNGtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**尝试在线将PNG转换为PDF**

Aspose为您提供在线免费应用程序["PNG到PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF将PNG转换为PDF的免费应用](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## 将SVG转换为PDF

**Aspose.PDF for .NET**解释了如何将SVG图像转换为PDF格式，以及如何获取源<abbr title="可缩放矢量图形">SVG</abbr>文件的尺寸。

可缩放矢量图形（SVG）是一系列基于XML的文件格式规范，用于二维矢量图形，包括静态和动态（交互式或动画）。SVG规范是一个开放标准，自1999年以来一直由万维网联盟（W3C）开发。

SVG图像及其行为在XML文本文件中定义。这意味着它们可以被搜索、索引、脚本化，并在需要时进行压缩。作为XML文件，SVG图像可以使用任何文本编辑器创建和编辑，但通常使用绘图程序（如Inkscape）创建更方便。

{{% alert color="success" %}}
**尝试在线将SVG格式转换为PDF**

Aspose.PDF for .NET为您提供在线免费应用程序["SVG到PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf/)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF将SVG转换为PDF的免费应用](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

要将SVG文件转换为PDF，请使用名为[SvgLoadOptions](https://reference.aspose.com/pdf/zh/net/aspose.pdf/svgloadoptions)的类，该类用于初始化[`LoadOptions`](https://reference.aspose.com/pdf/zh/net/aspose.pdf/loadoptions)对象。稍后，此对象作为参数传递给Document对象的初始化，并帮助PDF渲染引擎确定源文档的输入格式。

<a name="csharp-svg-to-pdf" id="csharp-svg-to-pdf"><strong>将SVG转换为PDF</strong></a>

1. 创建[`SvgLoadOptions`](https://reference.aspose.com/pdf/zh/net/aspose.pdf/loadoptions)类的实例。
2. 创建一个[Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document)类的实例，并提及源文件名和选项。
3. 使用所需的文件名保存文档。

以下代码片段展示了将SVG文件转换为PDF格式的过程，使用Aspose.PDF for .NET。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertSVGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    var option = new Aspose.Pdf.SvgLoadOptions();
    // Open SVG file 
    using (var document = new Aspose.Pdf.Document(dataDir + "SVGtoPDF.svg", option))
    {
        // Save PDF document
        document.Save(dataDir + "SVGtoPDF_out.pdf");
    }
}
```

## 获取SVG尺寸

还可以获取源SVG文件的尺寸。如果我们希望SVG覆盖输出PDF的整个页面，这些信息可能会很有用。SvgLoadOption类的AdjustPageSize属性满足此要求。此属性的默认值为false。如果将值设置为true，则输出PDF将具有与源SVG相同的大小（尺寸）。

以下代码片段展示了获取源SVG文件的尺寸并生成PDF文件的过程。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertSVGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    var loadopt = new Aspose.Pdf.SvgLoadOptions();
    loadopt.AdjustPageSize = true;
    // Open SVG file
    using (var document = new Aspose.Pdf.Document(dataDir + "SVGtoPDF.svg", loadopt))
    {
        document.Pages[1].PageInfo.Margin.Top = 0;
        document.Pages[1].PageInfo.Margin.Left = 0;
        document.Pages[1].PageInfo.Margin.Bottom = 0;
        document.Pages[1].PageInfo.Margin.Right = 0;

        // Save PDF document
        document.Save(dataDir + "SVGtoPDF_out.pdf");
    }
    
}
```

### SVG支持的特性

<table>
    <thead>
        <tr>
            <th>
                <p>SVG标签</p>
            </th>
            <th>
                <p>示例用法</p>
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <p>circle</p>
            </td>
            <td>
                <code><pre>&lt circle id="r2" cx="10" cy="10" r="10" stroke="blue" stroke-width="2"&gt </pre></code>
            </td>
        </tr>
        <tr>
            <td>
                <p>defs</p>
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
                    text-anchor="middle" &gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    被遮罩的文本&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;/text&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;use xlink:href="#Text" fill="blue"&nbsp; /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ellipse&nbsp;</p>
            </td>
            <td>
                <p>&lt;ellipse cx="2.5" cy="1.5" rx="2" ry="1" fill="red" /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>g&nbsp;</p>
            </td>
            <td>
                <p>&lt;g fill="none" stroke="dimgray" stroke-width="1.5" &gt;&nbsp; <br>
                    &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="-7"
                    y1="-7" x2="-3" y2="-3"/&gt;&nbsp; <br> &nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="7" x2="3"
                    y2="3"/&gt;&nbsp; <br> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="-7" y1="7" x2="-3" y2="3"/&gt;&nbsp;
                    <br> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="-7" x2="3" y2="-3"/&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;/g&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>image</p>
            </td>
            <td>
                <p>&lt;image id="ShadedRelief" x="24" y="4" width="64" height="82" xlink:href="relief.jpg"
                    /&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>line</p>
            </td>
            <td>
                <p>&lt;line style="stroke:#eea;stroke-width:8" x1="10" y1="30" x2="260" y2="100"/&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>path</p>
            </td>
            <td>
                <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
                    "/&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>style</p>
            </td>
            <td>
                <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
                    "/&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>polygon</p>
            </td>
            <td>
                <p>&lt;polygon style="stroke:#24a;stroke-width:1.5;fill:#eefefe" points="10,10 180,10 10,250 10,10"
                    /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>polyline</p>
            </td>
            <td>
                <p>&lt;polyline fill="none" stroke="dimgray" stroke-width="1" points="-3,-6 3,-6 3,1 5,1 0,7 -5,1
                    -3,1 -3,-5"/&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>rect&nbsp;</p>
            </td>
            <td>
                <p>&lt;rect x="0" y="0" width="400" height="600" stroke="none" fill="aliceblue" /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>svg</p>
            </td>
            <td>
                <p>&lt;svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="10cm" height="5cm" &gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>text</p>
            </td>
            <td>
                <p>&lt;text font-family="sans-serif" fill="dimgray" font-size="22px" font-weight="bold" x="58"
                    y="30" pointer-events="none"&gt;地图标题&lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>font</p>
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
                <p>&lt;tspan dy="25" x="25"&gt;六种墨水颜色输入值。在这里它将 &lt;/tspan&gt;</p>
            </td>
        </tr>
    </tbody>
</table>

## 将TIFF转换为PDF

**Aspose.PDF**文件格式支持，无论是单帧还是多帧<abbr title="标签图像文件格式">TIFF</abbr>图像。这意味着您可以在您的.NET应用程序中将TIFF图像转换为PDF。

TIFF或TIF，标签图像文件格式，表示用于在符合此文件格式标准的各种设备上使用的光栅图像。TIFF图像可以包含多个帧，具有不同的图像。Aspose.PDF文件格式也支持，无论是单帧还是多帧TIFF图像。

您可以以与其他光栅文件格式图形相同的方式将TIFF转换为PDF：

<a name="csharp-tiff-to-pdf" id="csharp-tiff-to-pdf"><strong>将TIFF转换为PDF</strong></a>

1. 创建新的[Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document)类对象并添加页面。
2. 加载输入的**TIFF**图像。
3. 保存PDF文档。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertTIFFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        
        // Load sample Tiff image file
        image.File = dataDir + "TIFFtoPDF.tiff";
        document.Pages[1].Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "TIFFtoPDF_out.pdf");
    }
}
```

如果您需要将多页TIFF图像转换为多页PDF文档并控制一些参数，例如宽度或纵横比，请按照以下步骤操作：

1. 实例化Document类的实例。
1. 加载输入的TIFF图像。
1. 获取帧的FrameDimension。
1. 为每个帧添加新页面。
1. 最后，将图像保存到PDF页面。

以下代码片段展示了如何使用C#将多页或多帧TIFF图像转换为PDF：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertTIFFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        using (var bitmap = new System.Drawing.Bitmap(File.OpenRead(dataDir + "TIFFtoPDF.tif")))
        {
            // Convert multi page or multi frame TIFF to PDF
            var dimension = new FrameDimension(bitmap.FrameDimensionsList[0]);
            var frameCount = bitmap.GetFrameCount(dimension);

            // Iterate through each frame
            for (int frameIdx = 0; frameIdx <= frameCount - 1; frameIdx++)
            {
                var page = document.Pages.Add();

                bitmap.SelectActiveFrame(dimension, frameIdx);

                using (var currentImage = new MemoryStream())
                {
                    bitmap.Save(currentImage, ImageFormat.Tiff);

                    var imageht = new Aspose.Pdf.Image
                    {
                        ImageStream = currentImage,
                        //Apply some other options
                        //ImageScale = 0.5
                    };
                    page.Paragraphs.Add(imageht);
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "TIFFtoPDF_out.pdf");
    }
}
```

## 将CDR转换为PDF

<abbr title="CDR">CDR</abbr>是一种文件格式，由Corel公司开发，主要用于矢量图形图像和绘图。CDR文件格式被大多数图像编辑程序识别。CDR格式是Corel Draw应用程序的默认格式。

请查看下一个代码片段以将CDR文件转换为PDF格式。

<a name="csharp-cdr-to-pdf" id="csharp-cdr-to-pdf"><strong>将CDR转换为PDF</strong></a>

1. 创建[CdrLoadOptions](https://reference.aspose.com/pdf/zh/net/aspose.pdf/cdrloadoptions/)类的实例。
2. 创建一个[Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document)类的实例，并提及源文件名和选项。
3. 使用所需的文件名保存文档。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertCDRtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open CDR file
    using (var document = new Aspose.Pdf.Document(dataDir + "CDRtoPDF.cdr", new CdrLoadOptions()))
    {
        // Save PDF document
        document.Save(dataDir + "CDRtoPDF_out.pdf");
    }
}
```

## 将DJVU转换为PDF

<abbr title="DJVU">DjVu</abbr>是一种压缩图像格式，由LizardTech开发。该文件格式主要用于存储不同类型的扫描文档；特别是包含文本、图片、索引彩色图像和线条图的文档。

请查看下一个代码片段以将DJVU文件转换为PDF格式。

<a name="csharp-djvu-to-pdf" id="csharp-djvu-to-pdf"><strong>将DJVU转换为PDF</strong></a>

1. 创建[DjvuLoadOptions](https://reference.aspose.com/pdf/zh/net/aspose.pdf/djvuloadoptions/)类的实例。
2. 创建一个[Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document)类的实例，并提及源文件名和选项。
3. 使用所需的文件名保存文档。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDJVUtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    
    // Open DJVU file
    using (var document = new Aspose.Pdf.Document(dataDir + "CDRtoPDF.djvu", new DjvuLoadOptions()))
    {
        // Save PDF document
        document.Save(dataDir + "CDRtoPDF_out.pdf");
    }
}
```

## 将HEIC转换为PDF

<a name="csharp-heic-to-pdf" id="csharp-heic-to-pdf"><strong>将HEIC转换为PDF</strong></a>

HEIC文件是一种高效容器图像文件格式，可以将多个图像作为集合存储在一个文件中。
要加载heic图像，您需要添加对https://www.nuget.org/packages/FileFormat.Heic/ nuget包的引用。
使用Aspose.PDF将HEIC图像转换为PDF：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHEICtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open HEIC file
    using (var fs = new FileStream(dataDir + "HEICtoPDF.heic", FileMode.Open))
    {
        var image = FileFormat.Heic.Decoder.HeicImage.Load(fs);
        var pixels = image.GetByteArray(PixelFormat.Rgb24);
        var width = (int)image.Width;
        var height = (int)image.Height;

        using (var document = new Aspose.Pdf.Document())
        {
            var page = document.Pages.Add();
            var asposeImage = new Aspose.Pdf.Image();
            asposeImage.BitmapInfo = new Aspose.Pdf.BitmapInfo(pixels, width, height, Aspose.Pdf.BitmapInfo.PixelFormat.Rgb24);
            page.PageInfo.Height = height;
            page.PageInfo.Width = width;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Left = 0;

            page.Paragraphs.Add(asposeImage);

            // Save PDF document
            document.Save(dataDir + "HEICtoPDF_out.pdf");
        }
    }
}
```