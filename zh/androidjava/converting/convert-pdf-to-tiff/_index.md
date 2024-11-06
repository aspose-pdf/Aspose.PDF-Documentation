---
title: 将 PDF 转换为 TIFF 
linktitle: 将 PDF 转换为 TIFF  
type: docs
weight: 30
url: zh/androidjava/convert-pdf-to-tiff/
lastmod: "2021-06-05"
description: 本文介绍如何将 PDF 文档中的页面转换为 TIFF 图像。您将学习如何使用 Aspose.PDF for Android via Android via Java 将所有或单个页面转换为 TIFF 图像。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** 使得将 PDF 页面转换为 TIFF 图像成为可能。

[TiffDevice 类](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) 允许您将 PDF 页面转换为 TIFF 图像。这个类提供了一个名为 Process 的方法，允许您将 PDF 文件中的所有页面转换为单个 TIFF 图像。

{{% alert color="primary" %}}

在线试用。您可以在此链接 [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff) 在线查看 Aspose.PDF 转换的质量和结果。

{{% /alert %}}

## 将PDF页面转换为单个TIFF图像

Aspose.PDF for Android via Java 解释了如何将PDF文件中的所有页面转换为单个TIFF图像：

1. 创建一个Document类的对象。
1. 调用Process方法转换文档。
1. 要设置输出文件的属性，使用TiffSettings类。

以下代码片段显示了如何将所有PDF页面转换为单个TIFF图像。

```java
public void convertPDFtoTiffSinglePage() {
        // 打开文档
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 创建Resolution对象
        Resolution resolution = new Resolution(300);

        // 创建TiffSettings对象
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // 创建TIFF设备
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // 转换特定页面并将图像保存到流
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## 将单页转换为TIFF图像

Aspose.PDF for Android via Java允许将PDF文件中的特定页面转换为TIFF图像，使用一个重载版本的Process(..)方法，该方法接受页码作为转换参数。以下代码片段展示了如何将PDF的第一页转换为TIFF格式。

```java
public void convertPDFtoTiffAllPages() {
        // 打开文档
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 创建Resolution对象
        Resolution resolution = new Resolution(300);

        // 创建TiffSettings对象
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);
        tiffSettings.setSkipBlankPages(false);

        // 创建TIFF设备
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // 转换特定页面并将图像保存到流中
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```


## 在转换过程中使用Bradley算法

Aspose.PDF for Android via Java 已经支持使用LZW压缩将PDF转换为TIFF，然后使用AForge应用二值化。然而，有一个客户要求对某些图像使用Otsu获取阈值，因此他们也希望使用Bradley。

```java
public void convertPDFtoTiffBradleyBinarization() {
        //在Aspose.PDF for Android中未实现
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        //在Aspose.PDF for Android中未实现
        throw new NotImplementedException();
    }
```