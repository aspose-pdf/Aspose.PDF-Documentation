---
title: 将JPG转换为PDF 
linktitle: 将JPG转换为PDF 
type: docs
weight: 190
url: zh/androidjava/convert-jpg-to-pdf/
lastmod: "2021-06-05"
description: 了解如何轻松将JPG图像转换为PDF文件。此外，您还可以将图像转换为与页面具有相同高度和宽度的PDF。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

不需要再想如何将JPG转换为PDF，因为Apose.PDF for Android via Java库提供了最佳解决方案。

您可以通过以下步骤非常轻松地使用Aspose.PDF for Android via Java将JPG图像转换为PDF：

1. 初始化[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)类的对象
1. 加载JPG图像并添加到段落
1. 保存输出PDF

下面的代码片段展示了如何将JPG图像转换为PDF：

```java
public void convertJPEGtoPDF () {
        // 初始化文档对象
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

        // 加载示例JPEG图像文件
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

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