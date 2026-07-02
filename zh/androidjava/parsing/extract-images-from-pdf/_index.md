---
title: 从 PDF 中提取图像
linktitle: 提取图像
type: docs
weight: 20
url: /zh/androidjava/extract-images-from-the-pdf-file/
description: 如何使用 Aspose.PDF for Android via Java 从 PDF 中提取图像的一部分
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 文档中的每一页都包含资源（图像、表单和字体）。我们可以通过调用来访问这些资源 [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) 方法。类 [资源](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) 包含 [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) 并且我们可以通过调用获取图像列表 [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) 方法。

因此，要从页面提取图像，我们需要获取对页面的引用，然后是页面资源，最后是图像集合。
例如，我们可以通过索引提取特定图像。

图像的索引返回一个 [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) 对象。
此对象提供一个 [保存](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) 方法，可用于保存提取的图像。以下代码片段展示了如何从 PDF 文件中提取图像。

 ```java
 public void extractImage () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.Page page=document.getPages().get_Item(1);
        com.aspose.pdf.XImageCollection xImageCollection=page.getResources().getImages();
        // Extract a particular image
        com.aspose.pdf.XImage xImage=xImageCollection.get_Item(1);
        File file=new File(fileStorage, "extracted-image.jpeg");
        try {
            java.io.FileOutputStream outputImage=new java.io.FileOutputStream(file.toString());
            // Save output image
            xImage.save(outputImage, ImageType.getJpeg());
            outputImage.close();
        } catch (java.io.IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.
          }
```

