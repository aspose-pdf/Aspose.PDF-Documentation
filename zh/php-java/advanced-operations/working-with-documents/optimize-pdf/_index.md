---
title: Optimize, Compress or Reduce PDF Size in PHP
linktitle: Optimize PDF Document
type: docs
weight: 40
url: zh/php-java/optimize-pdf/
description: 优化PDF文件，压缩所有图像，减少PDF大小，取消嵌入字体，使用PHP删除未使用的对象。
lastmod: "2024-06-05"
---

一个PDF文档有时可能包含额外的数据。减少PDF文件的大小将帮助您优化网络传输和存储。这对于在网页上发布、在社交网络上分享、通过电子邮件发送或在存储中归档特别有用。我们可以使用几种技术来优化PDF：

- 优化页面内容以便在线浏览
- 缩小或压缩所有图像
- 启用页面内容重用
- 合并重复的流
- 取消嵌入字体
- 删除未使用的对象
- 删除或展平表单字段
- 删除或展平注释

## 为网络优化PDF文档

优化或线性化是指使PDF文件适合使用网页浏览器在线浏览的过程。
 Aspose.PDF 支持此过程。

要优化 PDF 以用于网页显示：

1. 在 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象中打开输入文档。
1. 使用 [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--) 方法。
1. 使用 save(..) 方法保存优化后的文档。

以下代码段显示了如何为网络优化 PDF 文档。

```php

    // 打开文档
    $document = new Document($inputFile);

    // 优化以用于网络
    $document->optimize();

    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```

## 减少 PDF 文件大小

本主题解释了优化/减少 PDF 文件大小的步骤。 Aspose.PDF API提供了[OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions)类，该类提供了通过删除不必要的对象和压缩包含图像的PDF文件来优化输出PDF的灵活性。以下部分详细说明了这两个选项。

### 删除不必要的对象

我们可以通过删除重复和未使用的对象来优化PDF文档的大小。以下代码片段展示了如何实现。

```php

    // 打开文档
    $document = new Document($inputFile);
    
    // 优化PDF文档。然而请注意，该方法不能保证
    // 文档缩小
    $document->optimizeResources();

    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();

```

## 缩小或压缩所有图像

如果源PDF文件包含图像，请考虑压缩图像并设置其质量。 为了启用图像压缩，请将 `true` 作为参数传递给 `setCompressImages(..)` 方法。文档中的所有图像将被重新压缩。压缩是由 `setImageQuality(..)` 方法定义的，它的值是质量的百分比。100% 表示质量和图像大小不变。要减少图像大小，请将小于 100 的参数传递给 `setImageQuality(..)` 方法。

```php

    // 打开文档
    $document = new Document($inputFile);
    
    // 初始化优化选项
    $optimizationOptions = new OptimizationOptions();

    // 设置压缩图像选项
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // 设置图像质量选项
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(50);

    // 使用优化选项优化 PDF 文档
    $document->optimizeResources($optimizationOptions);

    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```

另一种方法是以较低分辨率调整图像大小。 在这种情况下，我们应该将 ResizeImages 设置为 true，并将 MaxResolution 设置为适当的值。

```php

    // 打开文档
    $document = new Document($inputFile);
    
    // 初始化 OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    // 设置 CompressImages 选项
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);
    
    // 设置 ImageQuality 选项
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);

    // 设置 ResizeImage 选项
    $optimizationOptions->getImageCompressionOptions()->setResizeImages(true);

    // 设置 MaxResolution 选项
    $optimizationOptions->getImageCompressionOptions()->setMaxResolution(300);

    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```

另一个重要问题是执行时间。 但是，我们也可以管理这个设置。目前，我们可以使用两种算法 - 标准和快速。为了控制执行时间，我们应该设置一个版本属性。以下代码片段演示了快速算法：

```php
    // 打开文档
    $document = new Document($inputFile);
    
    // 初始化优化选项
    $optimizationOptions = new optimization_OptimizationOptions();

    // 设置压缩图像选项
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // 设置图像质量选项
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);
    $optimization_ImageCompressionVersion = new optimization_ImageCompressionVersion();

    // 将图像压缩版本设置为快速
    $optimizationOptions->getImageCompressionOptions()->setVersion($optimization_ImageCompressionVersion->Fast);

    // 使用优化选项优化PDF文档
    $document->optimizeResources($optimizationOptions);

    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```

## 移除未使用的对象

有时候，PDF 文档中包含未被文档中其他对象引用的 PDF 对象。例如，当页面从文档页面树中移除，但页面对象本身没有被移除时，就可能发生这种情况。移除这些对象不会使文档无效，而是缩小了文档的大小。

```php

    // 打开文档
    $document = new Document($inputFile);
    
    // 初始化优化选项
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedObjects(true);

    // 使用优化选项优化 PDF 文档
    $document->optimizeResources($optimizationOptions);

    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```

## 移除未使用的流

有时文档包含未使用的资源流。
 这些流并不是“未使用的对象”，因为它们是从页面的资源字典中引用的。这可能发生在图像已从页面中移除但未从页面资源中移除的情况下。此外，这种情况经常发生在从文档中提取页面时，文档页面具有“公共”资源，也就是说，相同的资源对象。分析页面内容以确定资源流是否被使用。未使用的流将被移除。有时这会减少文档的大小。

```php

    // 打开文档
    $document = new Document($inputFile);
    
    // 初始化 OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedStreams(true);

    // 使用 OptimizationOptions 优化 PDF 文档
    $document->optimizeResources($optimizationOptions);

    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```

## 链接重复的流

有时，文档包含几个相同的资源流（例如图像）。 这可能发生在例如当一个文档与自身连接时。输出文档包含相同资源流的两个独立副本。我们分析所有资源流并比较它们。如果流是重复的，它们将被合并，即只保留一个副本，引用会适当地更改，并删除对象的副本。有时这会减小文档的大小。

```php
    // 打开文档
    $document = new Document($inputFile);
    
    // 初始化 OptimizationOptions
    $optimizationOptions = new OptimizationOptions();
    
    $optimizationOptions->setLinkDuplcateStreams(true);
    
    // 使用 OptimizationOptions 优化 PDF 文档
    $document->optimizeResources($optimizationOptions);

    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```

另外，我们可以使用 AllowReusePageContent 设置。如果此属性设置为 true，当为相同页面优化文档时，页面内容将被重用。

```php
    // 打开文档
    $document = new Document($inputFile);
    
    // 初始化 OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setAllowReusePageContent(true);

    // 使用 OptimizationOptions 优化 PDF 文档
    $document->optimizeResources($optimizationOptions);

    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```

## 取消嵌入字体

如果文档使用嵌入字体，这意味着所有字体数据都被放置在文档中。优点是无论用户的机器上是否安装了字体，文档都可以查看。但是嵌入字体会使文档变大。取消嵌入字体的方法会移除所有嵌入字体。这会减小文档的大小，但如果没有安装正确的字体，文档可能会变得不可读。

```php

    // 打开文档
    $document = new Document($inputFile);
    
    // 初始化优化选项
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // 使用优化选项优化PDF文档
    $document->optimizeResources($optimizationOptions);

    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```

## 删除或展平注释

当注释不必要时，可以删除注释。
 当它们是必需的但不需要额外编辑时，可以将它们展平。这两种技术都将减少文件大小。

```php

    // 打开文档
    $document = new Document($inputFile);
    $pages = $document->getPages();

    for ($i=1; $i < $pages->size() ; $i++) { 
        $page = $pages->get_Item($i);
        $annotations = $page->getAnnotations();
        for ($idx=0; $idx < $annotations->size(); $idx++) { 
            $annotation = $annotations->get_Item($idx);
            $annotation->flatten();
        }
    }
     
    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```

## 移除表单字段

如果PDF文档包含AcroForms，我们可以尝试通过展平表单字段来减少文件大小。

```php

    // 打开文档
    $document = new Document($inputFile);
    
    // 展平表单
    $fields = $document->getForm()->getFields();
    foreach ($fields as $field) {
        $field->flatten();
    }            

    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```

## 将PDF从RGB颜色空间转换为灰度

一个PDF文件由文本、图像、附件、注释、图形和其他对象组成。您可能会遇到将PDF从RGB颜色空间转换为灰度的需求，以便在打印这些PDF文件时速度更快。此外，当文件转换为灰度时，文档的大小也会减少，但随着这种变化，文档的质量可能会下降。目前，这个功能由Adobe Acrobat的Pre-Flight功能支持，但在谈到办公自动化时，Aspose.PDF是提供这种文档操作优势的终极解决方案。

为了实现这一需求，可以使用以下代码片段。

```php

    // 打开文档
    $document = new Document($inputFile);
    
    $strategy = new RgbToDeviceGrayConversionStrategy();
    for ($idxPage = 1; $idxPage <= $document->getPages()->size(); $idxPage++) {
        $page = $document->getPages()->get_Item($idxPage);
        $strategy->convert($page);
    }          

    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```


## FlateDecode 压缩

Aspose.PDF for PHP via Java 提供了对 PDF 优化功能的 FlateDecode 压缩支持。以下代码示例展示了如何在优化中使用选项，以 FlateDecode 压缩存储图像：

```php

    // 打开文档
    $document = new Document($inputFile);

    // 初始化 OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // 使用 OptimizationOptions 优化 PDF 文档
    $optimizationOptions->getImageCompressionOptions()->setEncoding(optimization_ImageEncoding::$Flate);

    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```

## 在 XImageCollection 中存储图像

Aspose.PDF for PHP via Java 提供了将新图像以 FlateDecode 压缩存储到 [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection) 的能力。
 要启用此选项，您可以使用 ImageFilterType.Flate 标志。以下代码片段展示了如何使用此功能：

```php
    // 打开文档
    $document = new Document($inputFile);

    // 初始化文档
    $page = $document->getPages()->get_Item(1);

    // 将图像加载到流中
    $imageStream = new java("java.io.FileInputStream",$inputFile);
    $imageFilterType = new ImageFilterType();
    $page->getResources()->getImages()->add($imageStream, $imageFilterType->Flate);
    $idx = $page->getResources()->getImages()->size();
    $ximage = $page->getResources()->getImages()->get_Item($idx);
    $page->getContents()->add(new operators_GSave());

    // 设置坐标
    $lowerLeftX = 0;
    $lowerLeftY = 0;
    $upperRightX = 600;
    $upperRightY = 600;
    $rectangle = new Rectangle($lowerLeftX, $lowerLeftY, $upperRightX, $upperRightY);
    $matrixData = [
        $rectangle->getURX() - $rectangle->getLLX(), 0, 
        0, $rectangle->getURY() - $rectangle->getLLY(), 
        $rectangle->getLLX(), $rectangle->getLLY()];
    $matrix = new Matrix($matrixData);

    // 使用 ConcatenateMatrix （连接矩阵）操作符：定义图像的放置方式
    $page->getContents()->add(new operators_ConcatenateMatrix($matrix));
    $page->getContents()->add(new operators_Do($ximage->getName()));
    $page->getContents()->add(new operators_GRestore());

    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```