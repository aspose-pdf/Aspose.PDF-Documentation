---
title: 使用 Java 从 PDF 中提取图像
linktitle: 从 PDF 中提取图像
type: docs
weight: 20
url: /java/extract-images-from-the-pdf-file/
description: 了解如何使用 Aspose.PDF for Java 从 PDF 文件中提取嵌入图像。
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何通过 Java 从 PDF 中提取图像
Abstract: 本文介绍如何使用 Aspose.PDF for Java 从 PDF 文档中提取嵌入图像。它演示了如何打开源 PDF、从页面资源集合访问图像以及将提取的 XImage 保存到外部文件。
---
当您需要重复使用嵌入图形、检查文档资源或导出图像以进行下游处理时，从 PDF 页面中提取图像。

1. 在 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF，并打开提取的图像文件的输出流。
1. 从文档中获取目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并访问其 `Resources.Images` 集合。
1. 按索引从该图像集合中检索所需的 [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) 对象。
1. 调用`image.save(outputImage)`将提取的​​图像字节写入目标流。

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```
