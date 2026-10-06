---
title: 向 PDF 添加印章
linktitle: 向 PDF 添加印章
type: docs
weight: 40
url: /zh/java/add-stamp/
description: 了解如何在 Java 中使用 PdfFileStamp 外观向 PDF 页面添加图像印章。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中向 PDF 添加图像印章
Abstract: 了解如何使用 Aspose.PDF for Java 通过 PdfFileStamp 外观向 PDF 文档添加印章内容。当前的 Java 示例集展示了如何创建 `Stamp`、将其绑定到图像文件、将其添加到文档中，并保存带有印章的 PDF。
---
## 向 PDF 添加印章

当需要在 PDF 上应用基于图像的印章时，请使用此工作流。

### 步骤

1. 创建一个 `PdfFileStamp` 实例并绑定源 PDF。
2. 创建一个 `Stamp` 对象。
3. 使用图像文件绑定印章 `bindImage`.
4. 将印章添加到文档 `addStamp`.
5. 保存输出并关闭外观对象。

### Java 示例

```java
public static void addStampToPdf(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

当前 `PdfFileStampExamples.java` 类不包含针对仅文本印章、旋转或不透明度配置的单独 Java 示例。
