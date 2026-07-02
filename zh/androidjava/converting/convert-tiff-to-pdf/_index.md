---
title: 将 TIFF 转换为 PDF
linktitle: 将 TIFF 转换为 PDF
type: docs
weight: 210
url: /zh/androidjava/convert-tiff-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java 允许将多页或多帧 TIFF 图像转换为 PDF 应用程序。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** 支持的文件格式，无论是单帧还是多帧 <abbr title="Tag Image File Format">TIFF</abbr> 图像。这意味着您可以在 Java 应用程序中将 TIFF 图像转换为 PDF。

TIFF 或 TIF（Tagged Image File Format）表示用于在符合此文件格式标准的各种设备上使用的光栅图像。TIFF 图像可以包含多个具有不同图像的帧。Aspose.PDF 支持的文件格式同样适用于单帧或多帧 TIFF 图像。因此，您可以在 Java 应用程序中将 TIFF 图像转换为 PDF。下面我们将通过一个示例演示将多页 TIFF 图像转换为多页 PDF 文档的步骤：

1. 实例化 Document 类的实例
1. 加载输入的 TIFF 图像
1. 获取帧的 FrameDimension
1. 为每个帧添加新页面
1. 最后，将图像保存到 PDF 页面

此外，下面的代码片段演示了如何将多页或多帧 TIFF 图像转换为 PDF：

```java
 public void convertTIFFtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.tiff");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample TIFF image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

        // Save output document
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

