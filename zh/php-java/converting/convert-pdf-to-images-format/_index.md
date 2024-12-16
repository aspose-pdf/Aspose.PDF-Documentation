---
title: 将PDF转换为图像格式 
linktitle: 将PDF转换为图像
type: docs
weight: 70
url: /zh/php-java/convert-pdf-to-images-format/
lastmod: "2024-05-20"
description: 本主题向您展示如何使用Aspose.PDF将PDF转换为各种图像格式。通过几行代码将PDF页面转换为PNG、JPEG、BMP图像。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for PHP** 允许您将PDF文档转换为图像格式，如BMP、JPEG、GIF、PNG、EMF、TIFF和SVG，使用两种方法。转换是通过`Device`和`SaveOption`完成的。

库中有几个类允许您使用虚拟设备来转换图像。`DocumentDevice` 适用于整个文档的转换，而`ImageDevice` 适用于特定页面。

## 使用DocumentDevice类转换PDF

**Aspose.PDF for PHP** 使得将PDF页面转换为TIFF图像成为可能。

[TiffDevice类](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) 允许您将PDF页面转换为TIFF图像。
 这个类提供一个名为 Process 的方法，允许您将 PDF 文件中的所有页面转换为单个 TIFF 图像。

### 将 PDF 页面转换为一个 TIFF 图像

Aspose.PDF for PHP 解释了如何将 PDF 文件中的所有页面转换为单个 TIFF 图像：

1. 创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类的对象。
2. 调用 [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/DocumentDevice#process-com.aspose.pdf.IDocument-int-int-java.io.OutputStream-) 方法来转换文档。
3. 要设置输出文件的属性，请使用 [TiffSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/TiffSettings) 类。

以下代码片段展示了如何将所有 PDF 页面转换为单个 TIFF 图像。

```php
// 加载 PDF 文档
$document = new Document($inputFile);

// 创建一个新的 TiffSettings 对象
$tiffSettings = new devices_TiffSettings();

// 取消注释以下行以自定义 TIFF 设置
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// 设置 TIFF 图像的分辨率
$resolution = new devices_Resolution(300);

// 使用指定的分辨率和设置创建一个新的 TiffDevice 对象
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// 使用 TiffDevice 将 PDF 文档转换为 TIFF
$tiffDevice->process($document, $outputFile);
```

### 将单页转换为 TIFF 图像

Aspose.PDF for PHP 允许将 PDF 文件中的特定页面转换为 TIFF 图像，使用 Process(..) 方法的重载版本，该版本将页码作为参数进行转换。以下代码片段显示了如何将 PDF 的第一页转换为 TIFF 格式。

```php
// 加载 PDF 文档
$document = new Document($inputFile);

// 创建一个新的 TiffSettings 对象
$tiffSettings = new devices_TiffSettings();

// 取消注释以下行以自定义 TIFF 设置
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// 设置 TIFF 图像的分辨率
$resolution = new devices_Resolution(300);

// 使用指定的分辨率和设置创建一个新的 TiffDevice 对象
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// 使用 TiffDevice 将 PDF 文档转换为 TIFF
$tiffDevice->process($document, 1, 1, $outputFile);
```


### 在转换过程中使用Bradley算法

Aspose.PDF for PHP 已经支持使用 LZW 压缩将 PDF 转换为 TIFF，然后通过使用 AForge 可以应用二值化。然而，有一位客户要求对于某些图像，他们需要使用 Otsu 获取阈值，因此他们也希望使用 Bradley。

```php
// 创建一个新的 TiffSettings 对象
$tiffSettings = new devices_TiffSettings();

// 取消注释以下行以自定义 TIFF 设置
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// 设置 TIFF 图像的分辨率
$resolution = new devices_Resolution(300);

// 使用指定的分辨率和设置创建一个新的 TiffDevice 对象
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// 使用 TiffDevice 将 PDF 文档转换为 TIFF
$tiffDevice->process($document, 1, 1, $outputFile);

// 创建流对象以保存输出图像
$inStream = new java("java.io.FileInputStream",$outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


### 将 PDF 页面转换为像素化的 TIFF 图像

要将 PDF 文件中的所有页面转换为像素化的 TIFF 格式，请使用 IndexedConversionType 的 Pixelated 选项

```php
// 创建一个新的 TiffSettings 对象
$tiffSettings = new devices_TiffSettings();

// 取消注释以下行以自定义 TIFF 设置
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);
// 设置图像亮度
$tiffSettings->setBrightness(0.5f);
// 设置 IndexedConversion 类型，默认值为 simple
$tiffSettings->setIndexedConversionType(IndexedConversionType::Pixelated);

$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// 设置 TIFF 图像的分辨率
$resolution = new devices_Resolution(300);

// 使用指定的分辨率和设置创建一个新的 TiffDevice 对象
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// 使用 TiffDevice 将 PDF 文档转换为 TIFF
$tiffDevice->process($document, 1, 1, $outputFile);

// 创建流对象以保存输出图像
$inStream = new java("java.io.FileInputStream",$outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


{{% alert color="success" %}}
**尝试在线将 PDF 转换为 TIFF**

Aspose.PDF for PHP 为您提供在线免费应用程序 ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 到 TIFF 免费应用](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## 使用 ImageDevice 类转换 PDF

`ImageDevice` 是 `BmpDevice`、`JpegDevice`、`GifDevice`、`PngDevice` 和 `EmfDevice` 的祖先。

- [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) 类允许您将 PDF 页面转换为 <abbr title="位图图像文件">BMP</abbr> 图像。
- [EmfDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/EmfDevice) 类允许您将 PDF 页面转换为 <abbr title="增强型图元文件">EMF</abbr> 图像。

- [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) 类允许您将 PDF 页面转换为 JPEG 图像。
- [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/PngDevice) 类允许您将 PDF 页面转换为 <abbr title="便携式网络图形">PNG</abbr> 图像。
- [GifDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/GifDevice) 类允许您将 PDF 页面转换为 <abbr title="图形交换格式">GIF</abbr> 图像。

让我们看看如何将 PDF 页面转换为图像。

[BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) 类提供了一个名为 [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice#process-com.aspose.pdf.Page-com.aspose.ms.System.Drawing.Graphics-) 的方法，该方法允许您将 PDF 文件的特定页面转换为 BMP 图像格式。其他类也有相同的方法。因此，如果我们需要将 PDF 页面转换为图像，我们只需实例化所需的类。

以下代码片段展示了这种可能性：

```php
// 加载 PDF 文档
$document = new Document($inputFile);

// 获取文档中的页面集合
$pages = $document->getPages();

// 获取文档中的总页数
$count = $pages->size();

// 设置 PNG 图像的分辨率
$resolution = new devices_Resolution(300);

// 创建具有指定分辨率的新 PNG 设备
$imageDevice = new devices_PngDevice($resolution);

// 遍历文档中的每一页
for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {
    // 为当前页面设置输出图像文件名
    $imageFileName = $imageFileNameTemplate . $pageCount . '.png';

    // 从集合中获取当前页面
    $page = $document->getPages()->get_Item($pageCount);

    // 处理当前页面并将其保存为 PNG 图像
    $imageDevice->process($page, $imageFileName);
}
```


{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PNG**

作为我们免费应用程序如何工作的示例，请查看下一个功能。

Aspose.PDF for PHP 为您提供在线免费应用程序 ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)，您可以在其中尝试调查其功能和质量。

[![如何使用免费应用程序将 PDF 转换为 PNG](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## 使用 SaveOptions 类转换 PDF

本文的这一部分向您展示如何使用 Java 和 SaveOptions 类将 PDF 转换为 <abbr title="可缩放矢量图形">SVG</abbr>。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 SVG**

Aspose.PDF for PHP 为您提供在线免费应用程序 ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)，您可以在其中尝试调查其功能和质量。

[![Aspose.PDF 使用免费应用程序将 PDF 转换为 SVG](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**可伸缩矢量图形 (SVG)** 是基于 XML 的二维矢量图形文件格式的规范家族，包括静态和动态（交互式或动画）图形。SVG 规范是一个开放标准，自 1999 年以来由万维网联盟 (W3C) 开发。

SVG 图像及其行为在 XML 文本文件中定义。这意味着它们可以被搜索、索引、脚本化，并且在需要时可以被压缩。作为 XML 文件，SVG 图像可以用任何文本编辑器创建和编辑，但用 Inkscape 等绘图程序创建它们通常更方便。

### 将 PDF 页面转换为 SVG 图像

Aspose.PDF for PHP 支持将 PDF 文件转换为 SVG 格式的功能。
 为了实现此要求，已将 [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) 类引入到 com.aspose.pdf 包中。实例化一个 [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) 对象，并将其作为第二个参数传递给 [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 方法。

以下代码片段展示了将 PDF 文件转换为 SVG 格式的步骤。

```php
// 加载 PDF 文档
$document = new Document($inputFile);

// 创建 SvgSaveOptions 类的实例
$saveOption = new SvgSaveOptions();

// 将 PDF 文档保存为 SVG
$document->save($outputFile, $saveOption);
```