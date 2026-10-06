---
title: 在 PDF 中添加页脚
linktitle: 在 PDF 中添加页脚
type: docs
weight: 10
url: /zh/java/add-footer/
description: 了解如何在 Java 中使用 PdfFileStamp 类向 PDF 页面添加文本和图像页脚。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中向 PDF 添加文本和图像页脚
Abstract: 了解如何使用 Aspose.PDF for Java 通过 PdfFileStamp 类向 PDF 文档添加页脚内容。Java 示例涵盖纯文本页脚、从流加载的图像页脚，以及具有明确左、右、底部边距的文本页脚。
---
## 向 PDF 添加页脚

当需要在文档的每一页上重复页脚内容时，使用 `PdfFileStamp`。

### 步骤

1. 创建一个 `PdfFileStamp` 实例化并绑定源 PDF。
2. 将页脚内容构建为以下任意一种 `FormattedText` 或图像流。
3. 调用适当的 `addFooter` 过载。
4. 保存更新后的文件并关闭门面对象。

### Java 示例

```java
public static void addTextFooter(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Footer");
        pdfStamper.addFooter(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageFooter(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addFooter(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addFooterWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("This footer has margins on all sides.");
        pdfStamper.addFooter(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
