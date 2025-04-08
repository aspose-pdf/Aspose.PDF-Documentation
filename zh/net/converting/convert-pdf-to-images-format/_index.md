---
title: 在C#中将PDF转换为不同的图像格式
linktitle: 将PDF转换为图像
type: docs
weight: 70
url: /zh/net/convert-pdf-to-images-format/
lastmod: "2021-11-01"
description: 本文将向您展示如何使用 Aspose.PDF 通过几行代码将 PDF 转换为各种图像格式，例如 TIFF、BMP、EMF、JPEG、PNG、GIF 和 SVG。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Different Image Formats in C#",
    "alternativeHeadline": "Convert PDF Files to Multiple Image Formats in C#",
    "abstract": "Aspose.PDF for .NET中的功能允许用户无缝地将PDF文件转换为多种图像格式，如TIFF、BMP、EMF、JPEG、PNG、GIF和SVG。此功能通过仅需几行C#代码即可实现转换，从而简化了文档处理，使其成为希望通过多功能PDF处理能力增强应用程序的开发人员的重要工具。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1585",
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
    "url": "/net/convert-pdf-to-images-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-images-format/"
    },
    "dateModified": "2025-04-08",
    "description": "Aspose.PDF不仅可以执行简单易行的任务，还能应对更复杂的目标。请查看下一部分以获取高级用户和开发者的信息。"
}
</script>

## 概览

本文介绍了如何使用 C# 将 PDF 转换为不同的图像格式。它涵盖了以下主题。

_图像格式_: **TIFF**
- [C# PDF to TIFF](#csharp-pdf-to-tiff)
- [C# Convert PDF to TIFF](#csharp-pdf-to-tiff)
- [C# Convert Single or Particular Pages of PDF to TIFF](#csharp-pdf-to-tiff-pages)


_图像格式_: **BMP**
- [C# PDF to BMP](#csharp-pdf-to-bmp)
- [C# Convert PDF to BMP](#csharp-pdf-to-bmp)
- [C# PDF to BMP Converter](#csharp-pdf-to-bmp)

_图像格式_: **EMF**
- [C# PDF to EMF](#csharp-pdf-to-emf)
- [C# Convert PDF to EMF](#csharp-pdf-to-emf)
- [C# PDF to EMF Converter](#csharp-pdf-to-emf)


_图像格式_: **JPG**
- [C# PDF to JPG](#csharp-pdf-to-jpg)
- [C# Convert PDF to JPG](#csharp-pdf-to-jpg)
- [C# PDF to JPG Converter](#csharp-pdf-to-jpg)


_图像格式_: **PNG**
- [C# PDF to PNG](#csharp-pdf-to-png)
- [C# Convert PDF to PNG](#csharp-pdf-to-png)
- [C# PDF to PNG Converter](#csharp-pdf-to-png)


_图像格式_: **GIF**
- [C# PDF to GIF](#csharp-pdf-to-gif)
- [C# Convert PDF to GIF](#csharp-pdf-to-gif)
- [C# PDF to GIF Converter](#csharp-pdf-to-gif)

_图像格式_: **SVG**
- [C# PDF to SVG](#csharp-pdf-to-svg)
- [C# Convert PDF to SVG](#csharp-pdf-to-svg)
- [C# PDF to SVG Converter](#csharp-pdf-to-svg)

## 使用 C# 将 PDF 转换为图像

下面的代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

**Aspose.PDF for .NET** 使用了几种 PDF 转图像的转换方法。一般而言，我们使用两种方法：使用 Device 方法转换和使用 SaveOption 转换。本节将向您展示如何使用这些方法之一将 PDF 文档转换为 BMP、JPEG、GIF、PNG、EMF、TIFF 和 SVG 等图像格式。

该库中有多个类允许您使用虚拟设备来转换图像。DocumentDevice 适用于整个文档的转换，而 ImageDevice 则适用于特定页面的转换。

## 使用 DocumentDevice 类转换 PDF

**Aspose.PDF for .NET** 使将 PDF 页面转换为 TIFF 图像成为可能。

TiffDevice 类（基于 DocumentDevice）允许您将 PDF 页面转换为 TIFF 图像。该类提供了一个名为 `Process` 的方法，该方法允许您将 PDF 文件中的所有页面转换为单个 TIFF 图像。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 TIFF**

Aspose.PDF for .NET 为您提供在线免费应用程序 ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)，您可以尝试了解其功能和工作质量。

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### 将 PDF 页面转换为单个 TIFF 图像

Aspose.PDF for .NET 解释了如何将 PDF 文件中的所有页面转换为单个 TIFF 图像：

<a name="csharp-pdf-to-tiff"><strong>步骤：在 C# 中将 PDF 转换为 TIFF</strong></a>

1. 创建一个 **Document** 类的对象。
2. 创建 **TiffSettings** 和 **TiffDevice** 对象。
3. 调用 **TiffDevice.Process()** 方法将 PDF 文档转换为 TIFF。
4. 使用 **TiffSettings** 类设置输出文件的属性。

```csharp
public static void ConvertPDFtoTIFF()
{
    // Open document
    Document document = new Document(dataDir + "PageToTIFF.pdf");

    // Create Resolution object
    Resolution resolution = new Resolution(300);

    // Create TiffSettings object
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
        SkipBlankPages = false
    };

    // Create TIFF device
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // Convert a particular page and save the image to stream
    tiffDevice.Process(document, dataDir + "AllPagesToTIFF_out.tif");
}
```

### 将单个页面转换为 TIFF 图像

Aspose.PDF for .NET 允许将 PDF 文件中的特定页面转换为 TIFF 图像，使用重载的 Process(..) 方法，该方法接受页面编号作为转换参数。下面的代码片段演示了如何将 PDF 的第一页转换为 TIFF 格式。

<a name="csharp-pdf-to-tiff-pages"><strong>步骤：在 C# 中将单个或特定页面的 PDF 转换为 TIFF</strong></a>

1. 创建一个 **Document** 类的对象。
2. 创建 **TiffSettings** 和 **TiffDevice** 对象。
3. 调用重载的 **TiffDevice.Process()** 方法并传入 **fromPage** 和 **toPage** 参数，将 PDF 文档的页面转换为 TIFF。

```csharp
public static void ConvertPDFtoTiffSinglePage()
{
    // Open document
    Document document = new Document(dataDir + "PageToTIFF.pdf");

    // Create Resolution object
    Resolution resolution = new Resolution(300);

    // Create TiffSettings object
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
    };

    // Create TIFF device
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // Convert a particular page and save the image to stream
    tiffDevice.Process(document, 1, 1, dataDir + "PageToTIFF_out.tif");
}
```

### 转换过程中使用 Bradley 算法

Aspose.PDF for .NET 支持使用 LZW 压缩将 PDF 转换为 TIF，然后借助 AForge 应用二值化处理。但是有客户要求对某些图像通过 Otsu 获取阈值，因此他们也希望使用 Bradley。

```csharp
public static void ConvertPDFtoTiffBradleyBinarization()
{
    // Open document
    Document document = new Document(dataDir + "PageToTIFF.pdf");

    string outputImageFile = dataDir + "resultant_out.tif";
    string outputBinImageFile = dataDir + "37116-bin_out.tif";

    // Create Resolution object
    Resolution resolution = new Resolution(300);
    // Create TiffSettings object
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.LZW,
        Depth = Aspose.Pdf.Devices.ColorDepth.Format1bpp
    };
    // Create TIFF device
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
    // Convert a particular page and save the image to stream
    tiffDevice.Process(document, outputImageFile);

    using (FileStream inStream = new FileStream(outputImageFile, FileMode.Open))
    {
        using (FileStream outStream = new FileStream(outputBinImageFile, FileMode.Create))
        {
            tiffDevice.BinarizeBradley(inStream, outStream, 0.1);
        }
    }
} 
```


## 使用 ImageDevice 类转换 PDF

`ImageDevice` 是 `BmpDevice`、`JpegDevice`、`GifDevice`、`PngDevice` 和 `EmfDevice` 的基类。

- [BmpDevice](https://reference.aspose.com/pdf/zh/net/aspose.pdf.devices/bmpdevice) 类允许您将 PDF 页面转换为 <abbr title="Bitmap Image File">BMP</abbr> 图像。
- [EmfDevice](https://reference.aspose.com/pdf/zh/net/aspose.pdf.devices/emfdevice) 类允许您将 PDF 页面转换为 <abbr title="Enhanced Meta File">EMF</abbr> 图像。
- [JpegDevice](https://reference.aspose.com/pdf/zh/net/aspose.pdf.devices/jpegdevice) 类允许您将 PDF 页面转换为 JPEG 图像。
- [PngDevice](https://reference.aspose.com/pdf/zh/net/aspose.pdf.devices/pngdevice) 类允许您将 PDF 页面转换为 <abbr title="Portable Network Graphics">PNG</abbr> 图像。
- [GifDevice](https://reference.aspose.com/pdf/zh/net/aspose.pdf.devices/gifdevice) 类允许您将 PDF 页面转换为 <abbr title="Graphics Interchange Format">GIF</abbr> 图像。

让我们看看如何将 PDF 页面转换为图像。

`BmpDevice` 类提供了一个名为 [Process](https://reference.aspose.com/pdf/zh/net/aspose.pdf.devices/bmpdevice/methods/process) 的方法，该方法允许您将 PDF 文件的某个特定页面转换为 BMP 图像格式。其他类具有相同的方法。因此，如果我们需要将 PDF 页面转换为图像，只需实例化所需的类即可。

<a name="csharp-pdf-to-bmp"></a>
<a name="csharp-pdf-to-emf"></a>
<a name="csharp-pdf-to-jpg"></a>
<a name="csharp-pdf-to-png"></a>
<a name="csharp-pdf-to-gif"></a>
    
下面的步骤和 C# 代码片段展示了这一可能性：
 
 - [Convert PDF to BMP in C#](#csharp-pdf-to-image)
 - [Convert PDF to EMF in C#](#csharp-pdf-to-image)
 - [Convert PDF to JPG in C#](#csharp-pdf-to-image)
 - [Convert PDF to PNG in C#](#csharp-pdf-to-image)
 - [Convert PDF to GIF in C#](#csharp-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>步骤：在 C# 中将 PDF 转换为图像（BMP、EMF、JPG、PNG、GIF）</strong></a>

1. 使用 **Document** 类加载 PDF 文件。
2. 创建 **ImageDevice** 子类的实例，即  
   * **BmpDevice**（用于将 PDF 转换为 BMP）。  
   * **EmfDevice**（用于将 PDF 转换为 Emf）。  
   * **JpegDevice**（用于将 PDF 转换为 JPG）。  
   * **PngDevice**（用于将 PDF 转换为 PNG）。  
   * **GifDevice**（用于将 PDF 转换为 GIF）。
3. 调用 **ImageDevice.Process()** 方法执行 PDF 到图像的转换。

```csharp
public static class ExampleConvertPdfToImage
{
     private static readonly string dataDir = @"C:\Samples\";
    // BMP, JPEG, GIF, PNG, EMF
    public static void ConvertPDFusingImageDevice()
    {
        // Create Resolution object            
        Resolution resolution = new Resolution(300);
        BmpDevice bmpDevice = new BmpDevice(resolution);
        JpegDevice jpegDevice = new JpegDevice(resolution);
        GifDevice gifDevice = new GifDevice(resolution);
        PngDevice pngDevice = new PngDevice(resolution);
        EmfDevice emfDevice = new EmfDevice(resolution);

        Document document = new Document(dataDir + 
            "ConvertAllPagesToBmp.pdf");
            
        ConvertPDFtoImage(bmpDevice, "bmp", document);
        ConvertPDFtoImage(jpegDevice,"jpeg", document);
        ConvertPDFtoImage(gifDevice, "gif", document);
        ConvertPDFtoImage(pngDevice, "png", document);
        ConvertPDFtoImage(emfDevice, "emf", document);
            
    }
}

public static void ConvertPDFtoImage(ImageDevice imageDevice, 
        string ext, Document document)
{
    for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
    {
        using (FileStream imageStream = 
            new FileStream($"{dataDir}image{pageCount}_out.{ext}", 
            FileMode.Create))
        {
            // Convert a particular page and save the image to stream
            imageDevice.Process(document.Pages[pageCount], imageStream);
        }
    }
}
```

### 以透明背景转换 PDF 为图像

PDF 页面可以转换为带有透明背景而非白色背景的 PNG 图像。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoImageWithTransparentBackground()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertPDFtoImageWithTransparentBackground.pdf"))
    {
        var pngDevice = new Aspose.Pdf.Devices.PngDevice();
        pngDevice.TransparentBackground = true;
        using (var pngStream = new FileStream(dataDir + "ConvertPDFtoImageWithTransparentBackground.png", FileMode.Create))
        {
            // Convert page to PNG image
            pngDevice.Process(document.Pages[1], pngStream);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoImageWithTransparentBackground()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "ConvertPDFtoImageWithTransparentBackground.pdf");
    var pngDevice = new Aspose.Pdf.Devices.PngDevice()
    {
        TransparentBackground = true
    };
    using var pngStream = new FileStream(dataDir + "ConvertPDFtoImageWithTransparentBackground.png", FileMode.Create);
    // Convert page to PNG image
    pngDevice.Process(document.Pages[1], pngStream);
}
```
{{< /tab >}}
{{< /tabs >}}

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PNG**

作为免费应用程序如何工作的示例，请查看下一个功能。

Aspose.PDF for .NET 为您在线提供免费应用程序 ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)，您可以尝试了解其功能和工作质量。

[![How to convert PDF to PNG using Free App](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## 使用 SaveOptions 类转换 PDF

本文的这一部分向您展示了如何使用 C# 和 SaveOptions 类将 PDF 转换为 <abbr title="Scalable Vector Graphics">SVG</abbr>。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 SVG**

Aspose.PDF for .NET 为您在线提供免费应用程序 ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)，您可以尝试了解其功能和工作质量。

[![Aspose.PDF Convertion PDF to SVG with Free App](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**可缩放矢量图形 (SVG)** 是一系列基于 XML 的二维矢量图形文件格式规范，既适用于静态也适用于动态（交互式或动画）图形。SVG 规范是一个开放标准，自 1999 年以来由万维网联盟 (W3C) 进行开发。

SVG 图像及其行为在 XML 文本文件中定义。这意味着它们可以被搜索、索引、脚本化，并在需要时进行压缩。作为 XML 文件，SVG 图像可以用任何文本编辑器创建和编辑，但通常使用 Inkscape 等绘图程序会更方便。

Aspose.PDF for .NET 支持将 SVG 图像转换为 PDF 格式的功能，并提供了将 PDF 文件转换为 SVG 格式的能力。为实现这一需求，[`SvgSaveOptions`](https://reference.aspose.com/pdf/zh/net/aspose.pdf/svgsaveoptions/methods/index) 类已被引入到 Aspose.PDF 命名空间中。实例化一个 SvgSaveOptions 对象，并将其作为第二个参数传递给 [`Document.Save(..)`](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/methods/save/index) 方法。

下面的代码片段展示了使用 .NET 将 PDF 文件转换为 SVG 格式的步骤。

<a name="csharp-pdf-to-svg"><strong>步骤：在 C# 中将 PDF 转换为 SVG</strong></a>

1. 创建一个 **Document** 类的对象。
2. 创建具有所需设置的 **SvgSaveOptions** 对象。
3. 调用 **Document.Save()** 方法，并传入 **SvgSaveOptions** 对象，将 PDF 文档转换为 SVG。

```csharp
public static void ConvertPDFtoSVG()
{
    // Load PDF document
    Document document = new Document(dataDir + "input.pdf");
    // Instantiate an object of SvgSaveOptions
    SvgSaveOptions saveOptions = new SvgSaveOptions
    {
        // Do not compress SVG image to Zip archive
        CompressOutputToZipArchive = false,
        TreatTargetFileNameAsDirectory = true                
    };
            
    // Save the output in SVG files
    document.Save(dataDir + "PDFToSVG_out.svg", saveOptions);
}
```