---
title: 将 BMP 转换为 PDF
linktitle: 将 BMP 转换为 PDF
type: docs
weight: 220
url: /androidjava/convert-bmp-to-pdf/
lastmod: "2021-06-05"
description: 您可以轻松地将 BMP 位图文件转换为 PDF，以便使用 Aspose.PDF. for Android via Java 独立于显示设备存储数字位图图像。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

BMP 图像是扩展名为 .BMP 的文件，代表用于存储位图数字图像的位图图像文件。这些图像独立于图形适配器，也称为设备独立位图 (DIB) 文件格式。
您可以使用 Aspose.PDF for Java API 将 BMP 转换为 PDF。因此，您可以按照以下步骤将 BMP 图像转换为 PDF：

1. 初始化一个新文档
1. 加载示例 BMP 图像文件
1. 最后，保存输出 PDF 文件

以下代码片段遵循这些步骤，并展示如何使用 Java 将 BMP 转换为 PDF：

```java
public void convertBMPtoPDF () {
        // 初始化文档对象
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

        // 加载示例 BMP 图像文件
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "BMP-to-PDF.pdf");

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