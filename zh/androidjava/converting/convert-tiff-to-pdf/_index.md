---
title: 将TIFF转换为PDF 
linktitle: 将TIFF转换为PDF
type: docs
weight: 210
url: zh/androidjava/convert-tiff-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF for Android via Java 允许将多页或多帧TIFF图像转换为PDF应用程序。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** 文件格式支持，无论是单帧或多帧的 <abbr title="标记图像文件格式">TIFF</abbr> 图像。这意味着您可以在Java应用程序中将TIFF图像转换为PDF。

TIFF或TIF，标记图像文件格式，代表用于各种符合此文件格式标准的设备上的光栅图像。
 TIFF 图像可以包含多个不同图像的帧。Aspose.PDF 文件格式也被支持，无论是单帧还是多帧 TIFF 图像。因此，您可以在 Java 应用程序中将 TIFF 图像转换为 PDF。因此，我们将考虑一个将多页 TIFF 图像转换为多页 PDF 文档的示例，步骤如下：

1. 实例化 Document 类的一个实例
1. 加载输入的 TIFF 图像
1. 获取帧的 FrameDimension
1. 为每个帧添加新页面
1. 最后，将图像保存到 PDF 页面

此外，以下代码片段展示了如何将多页或多帧 TIFF 图像转换为 PDF：

```java
 public void convertTIFFtoPDF () {
        // 初始化文档对象
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

        // 加载示例 TIFF 图像文件
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

        // 保存输出文档
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```