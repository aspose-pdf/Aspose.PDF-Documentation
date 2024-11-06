---
title: 将PDF转换为不同的图像格式
linktitle: 将PDF转换为图像
type: docs
weight: 70
url: zh/net/convert-pdf-to-images-format/
lastmod: "2021-11-01"
description: 本主题展示如何使用Aspose.PDF将PDF转换为各种图像格式，例如TIFF、BMP、EMF、JPEG、PNG、GIF、SVG，只需几行代码。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 概览

本文介绍了如何使用C#将PDF转换为不同的图像格式。它涵盖了以下主题。

_图像格式_：**TIFF**
- [C# PDF到TIFF](#csharp-pdf-to-tiff)
- [C# 将PDF转换为TIFF](#csharp-pdf-to-tiff)
- [C# 将PDF的单页或特定页面转换为TIFF](#csharp-pdf-to-tiff-pages)

_图像格式_：**BMP**
- [C# PDF到BMP](#csharp-pdf-to-bmp)
- [C# 将PDF转换为BMP](#csharp-pdf-to-bmp)
- [C# PDF到BMP转换器](#csharp-pdf-to-bmp)

_图像格式_：**EMF**
- [C# PDF到EMF](#csharp-pdf-to-emf)
- [C# 将PDF转换为EMF](#csharp-pdf-to-emf)
- [C# PDF到EMF转换器](#csharp-pdf-to-emf)
- [C# PDF 转 EMF 转换器](#csharp-pdf-to-emf)

_图像格式_：**JPG**
- [C# PDF 转 JPG](#csharp-pdf-to-jpg)
- [C# 将 PDF 转换为 JPG](#csharp-pdf-to-jpg)
- [C# PDF 转 JPG 转换器](#csharp-pdf-to-jpg)

_图像格式_：**PNG**
- [C# PDF 转 PNG](#csharp-pdf-to-png)
- [C# 将 PDF 转换为 PNG](#csharp-pdf-to-png)
- [C# PDF 转 PNG 转换器](#csharp-pdf-to-png)

_图像格式_：**GIF**
- [C# PDF 转 GIF](#csharp-pdf-to-gif)
- [C# 将 PDF 转换为 GIF](#csharp-pdf-to-gif)
- [C# PDF 转 GIF 转换器](#csharp-pdf-to-gif)

_图像格式_：**SVG**
- [C# PDF 转 SVG](#csharp-pdf-to-svg)
- [C# 将 PDF 转换为 SVG](#csharp-pdf-to-svg)
- [C# PDF 转 SVG 转换器](#csharp-pdf-to-svg)

## C# 将 PDF 转换为图像

以下代码片段也可以与 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库一起使用。

**Aspose.PDF for .NET** 使用多种方法将 PDF 转换为图像。
**Aspose.PDF for .NET** 使用多种方法将 PDF 转换为图像。

库中有几个类允许您使用虚拟设备转换图像。DocumentDevice 面向转换整个文档，而 ImageDevice 则针对特定页面。

## 使用 DocumentDevice 类转换 PDF

**Aspose.PDF for .NET** 可以将 PDF 页面转换为 TIFF 图像。

TiffDevice（基于 DocumentDevice）类允许您将 PDF 页面转换为 TIFF 图像。该类提供了一个名为 `Process` 的方法，允许您将 PDF 文件中的所有页面转换为单个 TIFF 图像。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 TIFF**

Aspose.PDF for .NET 为您提供在线免费应用程序 ["PDF 到 TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)，您可以尝试探索它的功能和工作质量。

{{% /alert %}}

### 将 PDF 页面转换为一个 TIFF 图像

Aspose.PDF for .NET 说明如何将 PDF 文件中的所有页面转换为单个 TIFF 图像：

<a name="csharp-pdf-to-tiff"><strong>步骤：在 C# 中将 PDF 转换为 TIFF</strong></a>

1. 创建 **Document** 类的对象。
2. 创建 **TiffSettings** 和 **TiffDevice** 对象
3. 调用 **TiffDevice.Process()** 方法将 PDF 文档转换为 TIFF。
4. 要设置输出文件的属性，请使用 **TiffSettings** 类。

以下代码片段显示了如何将所有 PDF 页面转换为单个 TIFF 图像。

```csharp
public static void ConvertPDFtoTIFF()
{
    // 打开文档
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // 创建分辨率对象
    Resolution resolution = new Resolution(300);

    // 创建 TiffSettings 对象
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
        SkipBlankPages = false
    };

    // 创建 TIFF 设备
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // 转换特定页面并将图像保存到流中
    tiffDevice.Process(pdfDocument, _dataDir + "AllPagesToTIFF_out.tif");
}
```
### 将一页转换为TIFF图像

Aspose.PDF for .NET 允许将 PDF 文件中的特定页面转换为 TIFF 图像，请使用带有页面编号参数的 Process(..) 方法的重载版本进行转换。以下代码片段展示了如何将 PDF 的第一页转换为 TIFF 格式。

<a name="csharp-pdf-to-tiff-pages"><strong>步骤：在 C# 中将 PDF 的单个或特定页面转换为 TIFF</strong></a>

1. 创建 **Document** 类的对象。
2. 创建 **TiffSettings** 和 **TiffDevice** 对象
3. 使用 **fromPage** 和 **toPage** 参数调用重载的 **TiffDevice.Process()** 方法，将 PDF 文档页面转换为 TIFF。

```csharp
public static void ConvertPDFtoTiffSinglePage()
{
    // 打开文档
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // 创建分辨率对象
    Resolution resolution = new Resolution(300);

    // 创建 TiffSettings 对象
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
    };

    // 创建 TIFF 设备
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // 转换特定页面并将图像保存到流
    tiffDevice.Process(pdfDocument, 1, 1, _dataDir + "PageToTIFF_out.tif");
}
```
### 在转换期间使用布拉德利算法

Aspose.PDF for .NET 已支持将 PDF 转换为使用 LZW 压缩的 TIF，然后可以应用 AForge 的二值化处理。然而，一位客户请求对某些图像使用 Otsu 来获取阈值，所以他们也希望使用布拉德利。

```csharp
  public static void ConvertPDFtoTiffBradleyBinarization()
{
     // 打开文档
     Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    string outputImageFile = _dataDir + "resultant_out.tif";
    string outputBinImageFile = _dataDir + "37116-bin_out.tif";

    // 创建分辨率对象
    Resolution resolution = new Resolution(300);
    // 创建 TiffSettings 对象
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.LZW,
        Depth = Aspose.Pdf.Devices.ColorDepth.Format1bpp
    };
    // 创建 TIFF 设备
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
    // 转换特定页面并将图像保存到流
    tiffDevice.Process(pdfDocument, outputImageFile);

    using (FileStream inStream = new FileStream(outputImageFile, FileMode.Open))
    {
        using (FileStream outStream = new FileStream(outputBinImageFile, FileMode.Create))
        {
            tiffDevice.BinarizeBradley(inStream, outStream, 0.1);
        }
    }
} 
```
## 使用ImageDevice类转换PDF

`ImageDevice` 是 `BmpDevice`、`JpegDevice`、`GifDevice`、`PngDevice` 和 `EmfDevice` 的祖先类。

- [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) 类允许您将PDF页面转换为 <abbr title="Bitmap Image File">BMP</abbr> 图像。
- [EmfDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/emfdevice) 类允许您将PDF页面转换为 <abbr title="Enhanced Meta File">EMF</abbr> 图像。
- [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) 类允许您将PDF页面转换为JPEG图像。
- [PngDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/pngdevice) 类允许您将PDF页面转换为 <abbr title="Portable Network Graphics">PNG</abbr> 图像。
- [GifDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/gifdevice) 类允许您将PDF页面转换为 <abbr title="Graphics Interchange Format">GIF</abbr> 图像。

让我们看看如何将PDF页面转换为图像。
让我们看看如何将PDF页面转换为图像。

`BmpDevice` 类提供了一个名为 [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) 的方法，该方法允许您将PDF文件的特定页面转换为BMP图像格式。其他类也有相同的方法。因此，如果我们需要将PDF页面转换为图像，我们只需实例化所需的类。

<a name="csharp-pdf-to-bmp"></a>
<a name="csharp-pdf-to-emf"></a>
<a name="csharp-pdf-to-jpg"></a>
<a name="csharp-pdf-to-png"></a>
<a name="csharp-pdf-to-gif"></a>
    
以下步骤和C#中的代码片段显示了这种可能性
 
 - [在C#中将PDF转换为BMP](#csharp-pdf-to-image)
 - [在C#中将PDF转换为EMF](#csharp-pdf-to-image)
 - [在C#中将PDF转换为JPG](#csharp-pdf-to-image)
 - [在C#中将PDF转换为PNG](#csharp-pdf-to-image)
 - [在C#中将PDF转换为GIF](#csharp-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>步骤：在C#中将PDF转换为图像（BMP, EMF, JPG, PNG, GIF）</strong></a>

1.
1.
2. 创建一个 **ImageDevice** 子类的实例，例如：
   * **BmpDevice**（将 PDF 转换为 BMP）
   * **EmfDevice**（将 PDF 转换为 Emf）
   * **JpegDevice**（将 PDF 转换为 JPG）
   * **PngDevice**（将 PDF 转换为 PNG）
   * **GifDevice**（将 PDF 转换为 GIF）
3. 调用 **ImageDevice.Process()** 方法来执行 PDF 到图像的转换。

```csharp
public static class ExampleConvertPdfToImage
{
     private static readonly string _dataDir = @"C:\Samples\";
    // BMP, JPEG, GIF, PNG, EMF
    public static void ConvertPDFusingImageDevice()
    {
        // 创建 Resolution 对象            
        Resolution resolution = new Resolution(300);
        BmpDevice bmpDevice = new BmpDevice(resolution);
        JpegDevice jpegDevice = new JpegDevice(resolution);
        GifDevice gifDevice = new GifDevice(resolution);
        PngDevice pngDevice = new PngDevice(resolution);
        EmfDevice emfDevice = new EmfDevice(resolution);

        Document document = new Document(_dataDir + 
            "ConvertAllPagesToBmp.pdf");
            
        ConvertPDFtoImage(bmpDevice, "bmp", document);
        ConvertPDFtoImage(jpegDevice,"jpeg", document);
        ConvertPDFtoImage(gifDevice, "gif", document);
        ConvertPDFtoImage(pngDevice, "png", document);
        ConvertPDFtoImage(emfDevice, "emf", document);
            
    }
}

public static void ConvertPDFtoImage(ImageDevice imageDevice, 
        string ext, Document pdfDocument)
{
    for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
    {
        using (FileStream imageStream = 
        new FileStream($"{_dataDir}image{pageCount}_out.{ext}", 
        FileMode.Create))
        {
            // 转换特定页面并将图像保存到流
            imageDevice.Process(pdfDocument.Pages[pageCount], imageStream);

            // 关闭流
            imageStream.Close();
        }
    }
}
```
{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PNG**

作为我们免费应用程序工作方式的一个示例，请查看下一个功能。

Aspose.PDF for .NET为您提供在线免费应用程序["PDF 到 PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)，您可以在此尝试研究其功能和工作质量。

[![如何使用免费应用程序将 PDF 转换为 PNG](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## 使用 SaveOptions 类转换 PDF

本文部分向您展示如何使用 C# 和 SaveOptions 类将 PDF 转换为 <abbr title="Scalable Vector Graphics">SVG</abbr>。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 SVG**

Aspose.PDF for .NET为您提供在线免费应用程序["PDF 到 SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)，您可以在此尝试研究其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 PDF 转换为 SVG](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
[![Aspose.PDF 转换 PDF 到 SVG 的免费应用](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**可缩放矢量图形 (SVG)** 是一种基于 XML 的文件格式的二维矢量图形规范族，包括静态和动态（交互式或动画）。SVG 规范是一个开放标准，自 1999 年以来一直由万维网联盟 (W3C) 进行开发。

SVG 图像及其行为在 XML 文本文件中定义。这意味着它们可以被搜索、索引、编写脚本，如果需要，还可以被压缩。作为 XML 文件，SVG 图像可以用任何文本编辑器创建和编辑，但使用绘图程序（如 Inkscape）创建通常更方便。

Aspose.PDF for .NET 支持将 SVG 图像转换为 PDF 格式的功能，并且还提供将 PDF 文件转换为 SVG 格式的能力。
Aspose.PDF for .NET 支持将 SVG 图像转换为 PDF 格式的功能，并提供将 PDF 文件转换为 SVG 格式的能力。

以下代码片段展示了使用 .NET 将 PDF 文件转换为 SVG 格式的步骤。

<a name="csharp-pdf-to-svg"><strong>步骤：在 C# 中将 PDF 转换为 SVG</strong></a>

1. 创建 **Document** 类的对象。
2. 创建具有所需设置的 **SvgSaveOptions** 对象。
3. 调用 **Document.Save()** 方法并传递 **SvgSaveOptions** 对象将 PDF 文档转换为 SVG。

```csharp
public static void ConvertPDFtoSVG()
{
    // 加载 PDF 文档
    Document document = new Document(System.IO.Path.Combine(_dataDir, "input.pdf"));
    // 实例化 SvgSaveOptions 对象
    SvgSaveOptions saveOptions = new SvgSaveOptions
    {
        // 不要将 SVG 图像压缩到 Zip 存档中
        CompressOutputToZipArchive = false,
        TreatTargetFileNameAsDirectory = true                
    };
            
    // 保存输出为 SVG 文件
    document.Save(System.IO.Path.Combine(_dataDir, "PDFToSVG_out.svg"), saveOptions);
}
```

