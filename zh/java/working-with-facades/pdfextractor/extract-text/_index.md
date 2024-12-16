---
title: 从PDF中提取图像 (facades)
type: docs
weight: 30
url: /zh/java/extract-images/
description: 本节介绍如何使用PdfExtractor类通过Aspose.PDF Facades提取图像。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) 类允许您从PDF文件中提取图像。
 首先，你需要创建一个 [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) 类的对象，并使用 bindPdf 方法绑定输入的 PDF 文件。之后，调用 [extractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractImage--) 方法将所有图像提取到内存中。一旦图像被提取出来，你可以借助 hasNextImage 和 getNextImage 方法获取这些图像。你需要通过 while 循环遍历所有提取的图像。为了将图像保存到磁盘，你可以调用 getNextImage 方法的重载版本，该版本以文件路径作为参数。以下代码片段展示了如何将整个 PDF 中的图像提取到文件中。

```java   
public static void ExtractImages()
 {
    //创建一个提取器并将其绑定到文档
    Document document = new Document(_dataDir + "sample.pdf");
    PdfExtractor extractor = new PdfExtractor(document);
    extractor.setStartPage(1);
    extractor.setEndPage(3);            

    //运行提取器
    extractor.extractImage();
    int imageNumber = 1;
    //遍历提取出的图像集合
    while (extractor.hasNextImage())
    {
        //从集合中检索图像并将其保存到文件中
        extractor.getNextImage(_dataDir + String.format("image%03d.png", imageNumber++),ImageType.getPng());
    }
}
```