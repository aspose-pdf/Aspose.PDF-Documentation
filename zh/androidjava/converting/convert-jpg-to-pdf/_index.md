---
title: 将 JPG 转换为 PDF
linktitle: 将 JPG 转换为 PDF
type: docs
weight: 190
url: /zh/androidjava/convert-jpg-to-pdf/
lastmod: "2026-07-01"
description: 了解如何轻松地将 JPG 图像转换为 PDF 文件。此外，您还可以将图像转换为与页面高度和宽度相同的 PDF。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

无需再想如何将 JPG 转换为 PDF，因为 Apose.PDF for Android via Java 库提供了最佳方案。

您可以非常轻松地通过以下步骤使用 Aspose.PDF for Android via Java 将 JPG 图像转换为 PDF：

1. 初始化对象 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类
1. 加载 JPG 图像并添加到段落
1. 保存输出 PDF

下面的代码片段展示了如何将 JPG 图像转换为 PDF：

```java
public void convertJPEGtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.jpg");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample JPEG image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

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
