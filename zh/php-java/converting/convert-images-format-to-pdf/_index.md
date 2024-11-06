---
title: 将各种图像格式转换为PDF 
linktitle: 将图像转换为PDF
type: docs
weight: 60
url: zh/php-java/convert-images-format-to-pdf/
lastmod: "2024-05-20"
description: 本主题展示了如何使用 Aspose.PDF for PHP 库将各种图像格式转换为PDF。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for PHP** 允许您将不同格式的图像转换为PDF文件。我们的库展示了转换最流行图像格式（如 BMP、CGM、DMF、JPG、PNG、SVG 和 TIFF 格式）的代码片段。

## 将 BMP 转换为 PDF

使用 **Aspose.PDF for PHP** 库将 BMP 文件转换为 PDF 文档。

<abbr title="Bitmap Image File">BMP</abbr> 图像是扩展名为 .BMP 的文件，表示用于存储位图数字图像的位图图像文件。这些图像与图形适配器无关，也称为设备无关位图 (DIB) 文件格式。您可以使用 Aspose.PDF for PHP API 将 BMP 转换为 PDF。
 因此，您可以按照以下步骤将 BMP 图像转换为 PDF：

1. 创建一个新的 Document 对象
2. 向文档添加一个新页面
3. 将页面的边距设置为 0（如有需要）
4. 创建一个新的 Image 对象并设置输入 BMP 文件
5. 将图像添加到页面
6. 将文档保存为输出 PDF 文件

因此，以下代码片段遵循这些步骤，并展示了如何使用 PHP 将 BMP 转换为 PDF：

```php
// 创建一个新的 Document 对象
$document = new Document();

// 向文档添加一个新页面
$page = $document->getPages()->add();

// 将页面的边距设置为 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 创建一个新的 Image 对象并设置输入 BMP 文件
$image = new Image();
$image->setFile($inputFile);

// 将图像添加到页面
$page->getParagraphs()->add($image);

// 将文档保存为输出 PDF 文件
$document->save($outputFile);
```

## 将 CGM 转换为 PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> 是一个 ISO 标准，它提供了一种基于矢量的二维图像文件格式，用于存储和检索图形信息。CGM 是一种设备无关的格式。CGM 是一种矢量图形格式，支持三种不同的编码方法：二进制（最适合程序读取速度）、基于字符（生成最小文件大小并允许更快的数据传输）或明文编码（允许用户使用文本编辑器读取和修改文件）。

以下代码片段向您展示了如何使用 Aspose.PDF for PHP 将 CGM 文件转换为 PDF 格式。

1. 创建一个 [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) 实例，以指定加载 CGM 文件的任何特定选项
1. 创建一个 [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) 类的实例，并提及源文件名和选项。
1. 使用所需的文件名保存文档。

```php
$options = new CgmLoadOptions();

// 创建一个 Document 对象，并使用指定的选项加载 CGM 文件
$document = new Document($inputFile, $options);

// 将文档保存为 PDF 文件
$document->save($outputFile);
```


## 将 DICOM 转换为 PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> 是一个用于处理、存储、打印和传输医学影像信息的标准。它包括文件格式定义和网络通信协议。

Aspose.PDF for PHP 允许您将 DICOM 文件转换为 PDF 格式，请查看下一个代码片段：

1. 创建一个新的 Document 对象
1. 向文档添加一个新页面
1. 将页面的边距设置为 0（如果需要）
1. 创建一个新的 Image 对象并设置输入 BMP 文件
1. 将 DICOM 文件设置为图像的源文件
1. 将图像的文件类型设置为 DICOM
1. 将图像添加到页面
1. 将文档保存为输出 PDF 文件

```php
// 创建一个新的 Document 对象
$document = new Document();

// 向文档添加一个新页面
$page = $document->getPages()->add();

// 将页面的边距设置为 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 创建一个新的 Image 对象
$image = new Image();

// 将 DICOM 文件设置为图像的源文件
$image->setFile($inputFile);

// 将图像的文件类型设置为 DICOM
$image->setFileType(ImageFileType::$Dicom);

// 将图像添加到页面
$page->getParagraphs()->add($image);

// 将文档保存为 PDF 文件
$document->save($outputFile);
```


{{% alert color="success" %}}
**尝试在线将DICOM转换为PDF**

Aspose为您提供在线免费应用程序["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)，您可以在此尝试调查其功能和工作质量。

[![Aspose.PDF Convertion DICOM to PDF using Free App](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## 将EMF转换为PDF

增强型图元文件格式（<abbr title="Enhanced metafile format">EMF</abbr>）以设备无关的方式存储图形图像。EMF的图元文件由按时间顺序排列的可变长度记录组成，可以在任何输出设备上解析后渲染存储的图像。

我们有几种方法可以将EMF转换为PDF。

## 使用Image类

PDF文档由页面组成，每个页面包含一个或多个段落对象。段落可以是文本、图像、表格、浮动框、图形、标题、表单字段或附件。

要将图像文件转换为PDF格式，请将其封装在段落中。

可以在本地硬盘的物理位置、在网络URL或在Stream实例中转换图像。

要添加图像：

1. 创建一个com.aspose.pdf.Image类的对象。
1. 将图像添加到页面实例的[Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs)集合中。
1. 指定图像的路径或来源。
    - 如果图像位于硬盘上的某个位置，请使用[Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image)方法指定路径位置。
    - 如果图像被放置在FileInputStream中，请将持有图像的对象传递给[Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image)方法。

以下代码片段展示了如何加载图像对象、设置页面边距、将图像放置在页面上并将输出保存为PDF。

```php
$inputFile = "sample.emf";

// 创建一个新的Document对象
$document = new Document();

// 向文档添加一个新页面
$page = $document->getPages()->add();

// 将页面的边距设置为0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 创建一个新的Image对象并设置输入文件
$image = new Image();
$image->setFile($inputFile);

// 将图像添加到页面
$page->getParagraphs()->add($image);

// 将文档保存为PDF文件
$document->save($outputFile);
```


## 将 JPG 转换为 PDF

无需再考虑如何将 JPG 转换为 PDF，因为 Apose.PDF for PHP 库提供了最佳方案。

您可以通过以下步骤使用 Aspose.PDF for PHP 非常轻松地将 JPG 图像转换为 PDF：

1. 初始化 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类的对象
1. 向文档添加一个新页面
1. 将页面的边距设置为 0
1. 创建一个新的 Image 对象并设置输入文件
1. 保存输出 PDF

下面的代码片段展示了如何使用 PHP 将 JPG 图像转换为 PDF：

```php
$inputFile = "sample.jpg";

// 创建一个新的 Document 对象
$document = new Document();

// 向文档添加一个新页面
$page = $document->getPages()->add();

// 将页面的边距设置为 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 创建一个新的 Image 对象并设置输入文件
$image = new Image();
$image->setFile($inputFile);

// 将图像添加到页面
$page->getParagraphs()->add($image);

// 将文档保存为 PDF 文件
$document->save($outputFile);
```


{{% alert color="success" %}}
**尝试在线将JPG转换为PDF**

Aspose为您提供一个免费的在线应用程序["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF使用免费应用程序将JPG转换为PDF](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## 将PNG转换为PDF

**Aspose.PDF for PHP**支持将PNG图像转换为PDF格式。查看下一个代码片段以实现您的任务。

<abbr title="可移植网络图形">PNG</abbr>指的是一种使用无损压缩的点阵图像文件格式，这使得它在用户中很受欢迎。

您可以使用以下步骤将PNG转换为PDF图像：

1. 初始化[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)类的对象
1. 向文档中添加一个新页面
1. 将页面的边距设置为0
1. 创建一个新的图像对象并设置输入文件
1. 保存输出PDF

此外，下面的代码片段展示了如何在您的PHP应用程序中将PNG转换为PDF：

```php
$inputFile = "sample.png";

// 创建一个新的 Document 对象
$document = new Document();

// 向文档添加一个新页面
$page = $document->getPages()->add();

// 将页面的边距设置为 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 创建一个新的 Image 对象并设置输入文件
$image = new Image();
$image->setFile($inputFile);

// 将图像添加到页面
$page->getParagraphs()->add($image);

// 将文档保存为 PDF 文件
$document->save($outputFile);
```

{{% alert color="success" %}}
**尝试在线将 PNG 转换为 PDF**

Aspose 为您提供在线免费应用程序 ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)，您可以在其中尝试调查其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 PNG 转换为 PDF](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)

{{% /alert %}}

## 转换SVG到PDF

可缩放矢量图形 (SVG) 是一种基于XML的二维矢量图形文件格式的规范系列，包括静态和动态（交互或动画）图形。SVG规范是一个开放标准，自1999年以来一直由万维网联盟 (W3C) 开发。

SVG图像及其行为在XML文本文件中定义。这意味着它们可以被搜索、索引、编写脚本，如果需要，还可以被压缩。作为XML文件，SVG图像可以用任何文本编辑器创建和编辑，但通常使用如Inkscape这样的绘图程序创建它们更为方便。

## 如何将SVG文件转换为PDF格式

要将SVG文件转换为PDF，请使用名为[SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions)的类来初始化[LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions)对象。
 稍后，在[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)对象初始化期间，此对象作为参数传递，并帮助PDF渲染引擎确定源文档的输入格式。

以下代码片段显示了将SVG文件转换为PDF格式的过程。

```php
// 创建一个新的SvgLoadOptions对象
$loadOption = new SvgLoadOptions();

// 创建一个新的Document对象并加载SVG文件
$document = new Document($inputFile, $loadOption);

// 将文档保存为PDF文件
$document->save($outputFile);
```

{{% alert color="success" %}}
**尝试在线将SVG格式转换为PDF**

Aspose.PDF for PHP为您提供在线免费应用程序["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF Convertion SVG to PDF with Free App](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## 将TIFF转换为PDF

**Aspose.PDF for PHP** 文件格式支持，无论是单帧还是多帧 <abbr title="Tag Image File Format">TIFF</abbr> 图像。这意味着您可以在Java应用程序中将TIFF图像转换为PDF。

TIFF或TIF，标记图像文件格式，代表栅格图像，旨在用于符合此文件格式标准的各种设备。TIFF图像可以包含具有不同图像的多个帧。Aspose.PDF文件格式也支持，无论是单帧还是多帧TIFF图像。因此，您可以在Java应用程序中将TIFF图像转换为PDF。因此，我们将考虑一个将多页TIFF图像转换为多页PDF文档的示例，步骤如下：

1. 创建一个新的Document对象
1. 向文档添加一个新页面
1. 将页面的边距设置为0
1. 创建一个新的Image对象
1. 设置输入TIFF图像的文件路径
1. 将图像添加到页面
1. 将文档保存为PDF文件

此外，以下代码片段显示了如何将多页或多帧TIFF图像转换为PDF：

```php
// 创建一个新的 Document 对象
$document = new Document();

// 向文档添加一个新页面
$page = $document->getPages()->add();

// 将页面的边距设置为 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 创建一个新的 Image 对象
$image = new Image();

// 设置输入 TIFF 图像的文件路径
$image->setFile($inputFile);

// 将图像添加到页面
$page->getParagraphs()->add($image);

// 将文档保存为 PDF 文件
$document->save($outputFile);
```