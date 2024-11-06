---
title: 将 PDF 转换为图像格式
linktitle: 将 PDF 转换为图像
type: docs
weight: 70
url: zh/cpp/convert-pdf-to-images-format/
lastmod: "2021-11-19"
description: 本主题向您展示如何使用 Aspose.PDF 将 PDF 转换为各种图像格式。通过几行代码将 PDF 页面转换为 PNG、JPEG、BMP 图像。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for C++** 使用几种方法将 PDF 转换为图像。一般来说，我们使用两种方法：使用 Device 方法进行转换和使用 SaveOption 进行转换。本节将向您展示如何使用这些方法之一将 PDF 文档转换为图像格式，如 BMP、JPEG、PNG、TIFF 和 SVG 格式。

库中有几个类允许您使用虚拟设备来转换图像。DocumentDevice 适用于转换整个文档，而 ImageDevice 适用于特定页面。

## 使用 DocumentDevice 类转换 PDF

**Aspose.PDF for C++** 可以将 PDF 页面转换为 TIFF 图像。

The [TiffDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/)（基于 DocumentDevice）类允许您将 PDF 页面转换为 TIFF 图像。此类提供了一个名为 [Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device#a0790daa96125c5638a645647e9678f0c) 的方法，该方法允许您将 PDF 文件中的所有页面转换为单个 TIFF 图像。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 TIFF**

Aspose.PDF for C++ 为您提供在线免费应用程序 ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### 将 PDF 页面转换为一个 TIFF 图像

Aspose.PDF for C++ 解释如何将 PDF 文件中的所有页面转换为单个 TIFF 图像：

1. 打开 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) 与 MakeObject。
1. 创建 Resolution 对象。
1. 创建 [TIffSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_settings/) 对象。
1. 使用指定的属性创建 [Tiff device](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/)。
1. 转换特定页面并将图像保存到流。

以下代码片段显示了如何将所有 PDF 页面转换为单个 TIFF 图像。

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTIFF()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 用于路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 用于文件名的字符串
    String infilename("PageToTiff.pdf");
    String outfilename("PagesToTIFF_out.tif");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // 创建 Resolution 对象
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // 创建 TiffSettings 对象
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::None);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Default);
    tiffSettings->set_Shape(Aspose::Pdf::Devices::ShapeType::Landscape);
    tiffSettings->set_SkipBlankPages(false);

    // 创建 TIFF 设备
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);

    // 转换页面并将图像保存到流
    tiffDevice->Process(document, 1, 2, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
### 将单页转换为 TIFF 图像

Aspose.PDF for C++ 允许您将 PDF 文件中的特定页面转换为 TIFF 图像，使用 Process(..) 方法的重载版本，该版本接受页码作为转换参数。以下代码片段演示如何将 PDF 的第一页转换为 TIFF 格式。

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名的字符串
    String infilename("PageToTiff.pdf");
    String outfilename("PageToTiff_out.tif");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // 创建 Resolution 对象
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // 创建 TIFF 设备
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution);

    // 转换特定页面并将图像保存到流
    tiffDevice->Process(document, 1, 1, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### 在转换过程中使用Bradley算法

Aspose.PDF for C++已经支持使用LZW压缩将PDF转换为TIF，然后可以使用AForge应用二值化。然而，有客户要求对于某些图像，他们需要使用Otsu获取阈值，因此他们也希望使用Bradley。

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffBradleyBinarization()
{
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 打开文档
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PageToTIFF.pdf");

    String outputImageFile = _dataDir + u"resultant_out.tif";
    String outputBinImageFile = _dataDir + u"37116-bin_out.tif";

    // 创建Resolution对象
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // 创建TiffSettings对象
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::LZW);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Format1bpp);

    // 创建TIFF设备
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);
    auto imageStream = System::IO::File::OpenWrite(_dataDir + outputImageFile);

    // 转换特定页面并将图像保存到流中
    tiffDevice->Process(pdfDocument, 1, 2, imageStream);

    imageStream->Close();

    auto inStream = System::IO::File::OpenRead(outputImageFile);
    auto outStream = System::IO::File::OpenWrite(outputBinImageFile);

    tiffDevice->BinarizeBradley(inStream, outStream, 0.1);
}
```

## 使用 ImageDevice 类转换 PDF

`ImageDevice` 是 `BmpDevice`、`JpegDevice`、`GifDevice`、`PngDevice` 和 `EmfDevice` 的祖先。

- [BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device/) 类允许您将 PDF 页面转换为<abbr title="Bitmap Image File">BMP</abbr> 图像。
- [EmfDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.emf_device/) 类允许您将 PDF 页面转换为<abbr title="Enhanced Meta File">EMF</abbr> 图像。
- [JpegDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.jpeg_device/) 类允许您将 PDF 页面转换为 JPEG 图像。
- [PngDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.png_device/) 类允许您将 PDF 页面转换为<abbr title="Portable Network Graphics">PNG</abbr> 图像。

- [GifDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.gif_device/) 类允许您将 PDF 页面转换为<abbr title="Graphics Interchange Format">GIF</abbr> 图像。

让我们看看如何将 PDF 页面转换为图像。

[BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device) 类提供了一个名为 [Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device#a22cefdb47b7c762320fa7973aa4f1f93) 的方法，该方法允许您将 PDF 文件的特定页面转换为 BMP 图像格式。其他类具有相同的方法。因此，如果我们需要将 PDF 页面转换为图像，我们只需实例化所需的类。

以下代码片段展示了这种可能性：

```cpp
void Convert_PDF_To_Images::ConvertPDFusingImageDevice()
{
    std::clog << __func__ << ": Start" << std::endl;

    // 路径名称字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 创建分辨率对象            
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300); // 300 dpi

    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    bmpDevice = MakeObject<Aspose::Pdf::Devices::BmpDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    jpegDevice = MakeObject<Aspose::Pdf::Devices::JpegDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    gifDevice = MakeObject<Aspose::Pdf::Devices::GifDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    pngDevice = MakeObject<Aspose::Pdf::Devices::PngDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    emfDevice = MakeObject<Aspose::Pdf::Devices::EmfDevice>(resolution);

    auto document = MakeObject<Document>(_dataDir + u"ConvertAllPagesToBmp.pdf");

    ConvertPDFtoImage(bmpDevice, u"bmp", document);
    ConvertPDFtoImage(jpegDevice, u"jpeg", document);
    ConvertPDFtoImage(gifDevice, u"gif", document);
    ConvertPDFtoImage(pngDevice, u"png", document);
    ConvertPDFtoImage(emfDevice, u"emf", document);

    std::clog << __func__ << ": Finish" << std::endl;

}

void Convert_PDF_To_Images::ConvertPDFtoImage(
 System::SmartPtr<Aspose::Pdf::Devices::ImageDevice> imageDevice,
 String ext, System::SmartPtr<Document> document)
{
    // 路径名称字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    for (int pageCount = 1; pageCount <= document->get_Pages()->get_Count(); pageCount++)
    {
    String outfilename = String::Format(u"{0}PageToBmp{1}_out.{2}",
    _dataDir, pageCount, ext);

    auto imageStream = System::IO::File::OpenWrite(outfilename);

    // 创建分辨率对象
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // 转换特定页面并将图像保存到流中
    imageDevice->Process(document->get_Pages()->idx_get(pageCount), imageStream);

    // 关闭流
    imageStream->Close();
    }
}
```

{{% alert color="success" %}}
**尝试在线将PDF转换为PNG**

作为我们免费应用程序如何工作的示例，请查看下一个功能。

Aspose.PDF for C++ 为您提供在线免费应用程序["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)，您可以尝试调查其功能和工作质量。

[![如何使用免费应用程序将PDF转换为PNG](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## 使用 SaveOptions 类转换PDF

本文的这一部分向您展示如何使用 C++ 和 SaveOptions 类将PDF转换为<abbr title="可缩放矢量图形">SVG</abbr>。

{{% alert color="success" %}}
**尝试在线将PDF转换为SVG**

Aspose.PDF for C++ 为您提供在线免费应用程序["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将PDF转换为SVG](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

为了将 PDF 转换为 SVG，Aspose.PDF for CPP 提供了 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 类的 [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) 方法。您需要传递输出路径和枚举 SaveFormat::svg 给 Save 方法来将 PDF 转换为 SVG。以下代码片段展示了如何将 PDF 转换为 SVG：

本文教您如何使用 C++ 将 PDF 转换为 <abbr title="Scalable Vector Graphics">SVG</abbr>。

**可缩放矢量图形 (SVG)** 是一种基于 XML 的二维矢量图形文件格式的规范家族，可以是静态的，也可以是动态的（交互式或动画）。SVG 规范是一个开放标准，自 1999 年以来一直由万维网联盟 (W3C) 开发。

SVG 图像及其行为是在 XML 文本文件中定义的。 这意味着它们可以被搜索、索引、脚本化，并在需要时压缩。作为XML文件，SVG图像可以用任何文本编辑器创建和编辑，但使用诸如Inkscape之类的绘图程序创建它们通常更为方便。

Aspose.PDF for C++支持将SVG图像转换为PDF格式的功能，还提供将PDF文件转换为SVG格式的功能。为了实现这一要求，`SvgSaveOptions`类已被引入Aspose.PDF命名空间。实例化一个SvgSaveOptions对象并将其作为第二个参数传递给[Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)方法。

以下代码片段展示了使用C++将PDF文件转换为SVG格式的步骤。

```cpp
void Convert_PDF_To_Images::ConvertPDFtoSvgSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名称的字符串
    String infilename("PageToSvg.pdf");
    String outfilename("PageToSvg_out.svg");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 实例化SvgSaveOptions对象
    auto saveOptions = MakeObject<SvgSaveOptions>();
    // 不将SVG图像压缩到Zip存档
    saveOptions->CompressOutputToZipArchive = false;

    try {
    // 将输出保存为SVG文件
    document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```