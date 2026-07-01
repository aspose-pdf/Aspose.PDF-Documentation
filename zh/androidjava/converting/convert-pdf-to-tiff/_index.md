---
title: 将 PDF 转换为 TIFF
linktitle: 将 PDF 转换为 TIFF
type: docs
weight: 30
url: /zh/androidjava/convert-pdf-to-tiff/
lastmod: "2026-07-01"
description: 本篇文章描述如何将 PDF 文档中的页面转换为 TIFF 图像。您将学习如何使用 Aspose.PDF for Android via Android via Java 将所有页面或单个页面转换为 TIFF 图像。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** 使得可以将 PDF 页面转换为 TIFF  图像。

该 [TiffDevice 类](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) 允许您将 PDF 页面转换为 TIFF 图像。此类提供了名为 Process 的方法，允许您将 PDF 文件中的所有页面转换为单个 TIFF 图像。

{{% alert color="primary" %}}

在线尝试。您可以在此链接检查 Aspose.PDF 转换的质量并在线查看结果。 [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## 将 PDF 页面转换为单个 TIFF 图像

Aspose.PDF for Android via Java 解释如何将 PDF 文件中的所有页面转换为单个 TIFF 图像：

1. 创建 Document 类的对象。
1. 调用 Process 方法来转换文档。
1. 要设置输出文件的属性，请使用 TiffSettings 类。

以下代码片段展示了如何将所有 PDF 页面转换为单个 TIFF 图像。

```java
public void convertPDFtoTiffSinglePage() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## 将单页转换为 TIFF 图像

Aspose.PDF for Android via Java 允许将 PDF 文件中的特定页面转换为 TIFF 图像，使用接受页码作为参数的 Process(..) 方法的重载版本进行转换。以下代码片段展示了如何将 PDF 的第一页转换为 TIFF 格式。

```java
public void convertPDFtoTiffAllPages() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);
        tiffSettings.setSkipBlankPages(false);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## 在转换过程中使用 Bradley 算法

Aspose.PDF for Android via Java 已支持将 PDF 转换为使用 LZW 压缩的 TIFF，并且通过使用 AForge 可以进行二值化。然而有客户要求对某些图像使用 Otsu 获取阈值，因此他们也希望使用 Bradley。

```java
public void convertPDFtoTiffBradleyBinarization() {
        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }
```

