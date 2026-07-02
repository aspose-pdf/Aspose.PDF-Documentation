---
title: 将 BMP 转换为 PDF
linktitle: 将 BMP 转换为 PDF
type: docs
weight: 220
url: /zh/androidjava/convert-bmp-to-pdf/
lastmod: "2026-07-01"
description: 您可以轻松地使用 Aspose.PDF. for Android via Java 将 BMP 位图文件转换为 PDF，用于将数字位图图像与显示设备分离存储。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

BMP 图像是扩展名为 .BMP 的文件，表示用于存储位图数字图像的 Bitmap Image 文件。这些图像独立于图形适配器，也称为设备无关位图（DIB）文件格式。
您可以使用 Aspose.PDF for Java API 将 BMP 转换为 PDF。因此，您可以按照以下步骤转换 BMP 图像：

1. 初始化一个新 Document
1. 加载示例 BMP 图像文件
1. 最后，保存输出的 PDF 文件

下面的代码片段遵循这些步骤，并展示如何使用 Java 将 BMP 转换为 PDF：

```java
public void convertBMPtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.bmp");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample BMP image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "BMP-to-PDF.pdf");

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

