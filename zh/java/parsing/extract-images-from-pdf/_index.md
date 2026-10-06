---
title: 使用 Java 从 PDF 中提取图像
linktitle: 从 PDF 中提取图像
type: docs
weight: 20
url: /zh/java/extract-images-from-the-pdf-file/
description: 了解如何使用 Aspose.PDF for Java 从 PDF 文件中提取嵌入的图像。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何通过 Java 从 PDF 中提取图像
Abstract: 本文解释了如何使用 Aspose.PDF for Java 从 PDF 文档中提取嵌入的图像。它展示了如何打开源 PDF，访问页面资源集合中的图像，并将提取的 XImage 保存到外部文件。
---
当您需要重新使用嵌入的图形、检查文档资产或将图像导出用于后续处理时，可从 PDF 页面中提取图像。

1. 在 a 中打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例并为提取的图像文件打开输出流。
1. 获取目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 从文档中获取并访问它 `Resources.Images` 集合。
1. 检索所需的 [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) 对象从该图像集合中按索引获取。
1. 调用 `image.save(outputImage)` 将提取的图像字节写入目标流。

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```
