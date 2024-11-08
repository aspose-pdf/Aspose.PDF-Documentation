---
title: 优化、压缩或减少 PDF 大小在 Java 中
linktitle: 优化 PDF 文档
type: docs
weight: 40
url: /zh/java/optimize-pdf/
description: 优化 PDF 文件，缩小所有图像，减少 PDF 大小，取消嵌入字体，使用 Java 删除未使用的对象。
lastmod: "2021-06-05"
---

PDF 文档有时可能包含额外的数据。减少 PDF 文件的大小将有助于优化网络传输和存储。这对于在网页上发布、在社交网络上分享、通过电子邮件发送或存档存储特别有用。我们可以使用几种技术来优化 PDF：

- 优化页面内容以便在线浏览
- 缩小或压缩所有图像
- 启用重用页面内容
- 合并重复的流
- 取消嵌入字体
- 删除未使用的对象
- 删除或扁平化表单字段
- 删除或扁平化注释

## 为网络优化 PDF 文档

优化或线性化是指使 PDF 文件适合使用网络浏览器进行在线浏览的过程。
 Aspose.PDF 支持此过程。

要优化用于网页显示的 PDF：

1. 在 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象中打开输入文档。
1. 使用 [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--) 方法。
1. 使用 save(..) 方法保存优化后的文档。

以下代码片段展示了如何优化 PDF 文档以用于网页。

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.time.Clock;
import java.time.Duration;

import com.aspose.pdf.*;
import com.aspose.pdf.optimization.ImageCompressionVersion;
import com.aspose.pdf.optimization.ImageEncoding;

public class ExampleOptimize {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void OptimizePDFDocumentForTheWeb() {

        // 打开文档
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // 优化用于网页
        pdfDocument.optimize();

        // 保存输出文档
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## 减少 PDF 文件大小

本主题说明了优化/减少 PDF 文件大小的步骤。Aspose.PDF API 提供了 [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions) 类，该类提供了通过删除不必要的对象和压缩包含图像的 PDF 文件来优化输出 PDF 的灵活性。以下部分详细说明了这两种选项。

### 删除不必要的对象
我们可以通过删除重复和未使用的对象来优化 PDF 文档的大小。以下代码片段显示了如何实现。

```java
public static void ReduceSizePDF() {

        // 打开文档
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // 优化 PDF 文档。但请注意，此方法不能保证
        // 文档缩小
        pdfDocument.optimizeResources();

        // 保存输出文档
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## 缩小或压缩所有图像

如果源 PDF 文件包含图像，请考虑压缩图像并设置其质量。为了启用图像压缩，将 true 作为参数传递给 setCompressImages(..) 方法。文档中的所有图像将被重新压缩。压缩是由 setImageQuality(..) 方法定义的，该方法的值是百分比的质量。100% 是未更改的质量和图像大小。要减少图像大小，将小于 100 的参数传递给 setImageQuality(..) 方法。

```java
public static void ShrinkingCompressing() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "Shrinkimage.pdf");

        // 初始化 OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // 设置 CompressImages 选项
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // 设置 ImageQuality 选项
        optimizationOptions.getImageCompressionOptions().setImageQuality(50);

        // 使用 OptimizationOptions 优化 PDF 文档
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "Shrinkimage_out.pdf";
        // 保存更新的文档
        pdfDocument.save(_dataDir);
    }
```

另一种方法是调整图像大小以降低分辨率。在这种情况下，我们应该将 ResizeImages 设置为 true，并将 MaxResolution 设置为适当的值。

```java
public static void ShrinkingCompressing2() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // 初始化优化选项
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // 设置压缩图像选项
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);
        // 设置图像质量选项
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // 设置调整图像大小选项
        optimizationOptions.getImageCompressionOptions().setResizeImages(true);

        // 设置最大分辨率选项
        optimizationOptions.getImageCompressionOptions().setMaxResolution(300);

        // 使用优化选项优化 PDF 文档
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "ResizeImages_out.pdf";
        // 保存更新后的文档
        pdfDocument.save(_dataDir);
    }
```

另一个重要问题是执行时间。但同样，我们也可以管理这个设置。目前，我们可以使用两种算法 - 标准和快速。为了控制执行时间，我们应该设置一个 Version 属性。以下代码片段演示了快速算法：

```java
public static void ShrinkingCompressing3() {

        Clock clock = Clock.systemUTC();

        Duration tickDuration = Duration.ofNanos(250000);
        Clock clock1 = Clock.tick(clock, tickDuration);
        System.out.println("开始 : " + clock.instant());

        // 打开文档
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // 初始化 OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // 设置 CompressImages 选项
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // 设置 ImageQuality 选项
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // 将图像压缩版本设置为快速
        optimizationOptions.getImageCompressionOptions().setVersion(ImageCompressionVersion.Fast);

        // 使用 OptimizationOptions 优化 PDF 文档
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "ResizeImages_out.pdf";

        // 保存更新的文档
        pdfDocument.save(_dataDir);
        System.out.println("结束 : " + clock1.instant());
    }
```

## 删除未使用的对象

一个 PDF 文档有时包含未被文档中其他任何对象引用的 PDF 对象。例如，当从文档页面树中删除页面时，页面对象本身没有被删除。删除这些对象不会使文档无效，而是缩小了文档的大小。

```java
    public static void RemovingUnusedObjects() {

        // 打开文档
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        
        optimizationOptions.setRemoveUnusedObjects(true);
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "emoveUnusedObjects_out.pdf";

        // 保存更新后的文档
        pdfDocument.save(_dataDir);

    }
```
## 删除未使用的流

有时文档包含未使用的资源流。
 这些流不是“未使用的对象”，因为它们是从页面的资源字典中引用的。这可能发生在图像已从页面上删除但未从页面资源中删除的情况下。此外，当从文档中提取页面并且文档页面具有“公共”资源（即相同的资源对象）时，这种情况经常发生。分析页面内容以确定资源流是否被使用。未使用的流将被移除。有时这会减少文档的大小。

```java
public static void RemovingUnusedStream() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + 
        "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "removeUnusedObjects_out.pdf";
        
        // 保存更新后的文档
        pdfDocument.save(_dataDir);
        
    }
```
## 链接重复流

有时，一个文档包含多个相同的资源流（例如图像）。这可能发生在例如文档与自身连接时。输出文档包含相同资源流的两个独立副本。我们分析所有资源流并进行比较。如果流是重复的，它们将被合并，也就是说，只保留一个副本，引用将被适当更改，并删除对象的副本。有时这会减少文档的大小。

```java
    public static void LinkingDuplicateStream() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        
        // 使用OptimizationOptions优化PDF文档
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // 保存更新后的文档
        pdfDocument.save(_dataDir);
    }
```

另外，我们可以使用 AllowReusePageContent 设置。如果此属性设置为 true，当优化具有相同页面的文档时，页面内容将被重用。

```java
public static void AllowReusePageContent() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setAllowReusePageContent(true);
        
        // 使用 OptimizationOptions 优化 PDF 文档
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // 保存更新后的文档
        pdfDocument.save(_dataDir);
    }
```
## 取消嵌入字体

如果文档使用嵌入字体，则意味着所有字体数据都放置在文档中。
 该优点是，无论用户的计算机上是否安装了字体，该文档都可以查看。但是嵌入字体会使文档变得更大。非嵌入字体方法会移除所有嵌入的字体。这会减小文档的大小，但如果没有安装正确的字体，文档可能会变得无法读取。

```java
    public static void UnembedFonts() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setUnembedFonts(true);
        
        // 使用优化选项优化 PDF 文档
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // 保存更新的文档
        pdfDocument.save(_dataDir);
    }
```

## 删除或展平注释

当注释不必要时，可以删除它们。 当它们是必需的但不需要额外编辑时，可以将其扁平化。这两种技术都将减少文件大小。

```java
    public static void FlatteningAnnotations() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        for (Page page : pdfDocument.getPages()) {
            for (Annotation annotation : page.getAnnotations())
                annotation.flatten();
        }

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // 保存更新后的文档
        pdfDocument.save(_dataDir);
    }

```
## 删除表单字段

如果PDF文档包含AcroForms，我们可以尝试通过扁平化表单字段来减少文件大小。

```java
    public static void RemovingFormFields() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        // 扁平化表单
        if (pdfDocument.getForm().getFields().length > 0) {
            for (Field field : pdfDocument.getForm().getFields()) {
                field.flatten();
            }
        }
        _dataDir = _dataDir + "FlattenForms_out.pdf";
        // 保存更新后的文档
        pdfDocument.save(_dataDir);
    }

```
## 将 PDF 从 RGB 色彩空间转换为灰度

一个 PDF 文件由文本、图像、附件、注释、图形和其他对象组成。您可能会遇到将 PDF 从 RGB 色彩空间转换为灰度的需求，这样在打印这些 PDF 文件时会更快。此外，当文件被转换为灰度时，文档的大小也会减小，但这种变化可能会导致文档的质量下降。目前，这个功能是由 Adobe Acrobat 的预检功能支持的，但在谈到办公自动化时，Aspose.PDF 是一个提供此类文档操作便利的终极解决方案。

为了实现这一需求，可以使用以下代码片段。

```java
    public static void ConvertRGBtoGrayscale() {

        // 打开文档
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        com.aspose.pdf.RgbToDeviceGrayConversionStrategy strategy = new com.aspose.pdf.RgbToDeviceGrayConversionStrategy();
        for (int idxPage = 1; idxPage <= pdfDocument.getPages().size(); idxPage++) {
            Page page = pdfDocument.getPages().get_Item(idxPage);
            strategy.convert(page);
        }
        pdfDocument.save("output.pdf");
    }
```

## FlateDecode 压缩

Aspose.PDF for Java 提供了对 PDF 优化功能的 FlateDecode 压缩支持。下面的代码片段展示了如何在优化选项中使用该选项来使用 FlateDecode 压缩存储图像：

```java
    public static void FlateDecodeCompression() {

        // 打开文档
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);

        // 使用 OptimizationOptions 优化 PDF 文档
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // 保存更新后的文档
        pdfDocument.save(_dataDir);
    }
```
## 在 XImageCollection 中存储图像

Aspose.PDF for Java 提供了将新图像以 FlateDecode 压缩存储到 [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection) 中的功能。
 要启用此选项，可以使用 ImageFilterType.Flate 标志。以下代码片段展示了如何使用此功能：

```java
    public static void StoreImageInXImageCollection() {
        // 初始化文档
        Document document = new Document();
        document.getPages().add();
        Page page = document.getPages().get_Item(1);

        // 将图像加载到流中
        java.io.FileInputStream imageStream = null;
        try {
            imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return;
        }
        page.getResources().getImages().add(imageStream, ImageFilterType.Flate);
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        page.getContents().add(new com.aspose.pdf.operators.GSave());

        // 设置坐标
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });
        // 使用 ConcatenateMatrix（连接矩阵）操作符：定义图像如何放置
        page.getContents().add(new com.aspose.pdf.operators.ConcatenateMatrix(matrix));
        page.getContents().add(new com.aspose.pdf.operators.Do(ximage.getName()));
        page.getContents().add(new com.aspose.pdf.operators.GRestore());

        document.save(_dataDir + "FlateDecodeCompression.pdf");
    }

}
```