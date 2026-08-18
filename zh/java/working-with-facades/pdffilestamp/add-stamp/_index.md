---
title: 添加图章到 PDF
linktitle: 添加图章到 PDF
type: docs
weight: 40
url: /java/add-stamp/
description: 了解如何使用 PdfFileStamp 外观在 Java 中将图像图章添加到 PDF 页面。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将图像图章添加到 PDF
Abstract: 了解如何使用 PdfFileStamp 外观通过 Aspose.PDF for Java 将图章内容添加到 PDF 文档。当前的 Java 示例集展示了如何创建 `Stamp`、将其绑定到图像文件、将其添加到文档以及保存已盖章的 PDF。
---
## 添加图章到 PDF

当应将基于图像的图章应用到 PDF 时，请使用此工作流程。

### 步骤

1. 创建`PdfFileStamp`实例并绑定源PDF。
2. 创建一个 `Stamp` 对象。
3. 使用`bindImage` 将图章绑定到图像文件。
4. 使用`addStamp` 将图章添加到文档中。
5. 保存输出并关闭外观对象。

### Java示例

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

当前的 `PdfFileStampExamples.java` 类不包含用于纯文本标记、旋转或不透明度配置的单独 Java 示例。
