---
title: 添加页脚到 PDF
linktitle: 添加页脚到 PDF
type: docs
weight: 10
url: /java/add-footer/
description: 了解如何使用 PdfFileStamp 外观在 Java 中向 PDF 页面添加文本和图像页脚。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将文本和图像页脚添加到 PDF
Abstract: 了解如何使用 PdfFileStamp 外观通过 Aspose.PDF for Java 将页脚内容添加到 PDF 文档。 Java 示例涵盖纯文本页脚、从流加载的图像页脚以及具有显式左、右和下边距的文本页脚。
---
## 向 PDF 添加页脚

当您需要在文档的每一页上重复页脚内容时，请使用`PdfFileStamp`。

### 步骤

1. 创建`PdfFileStamp`实例并绑定源PDF。
2. 将页脚内容构建为 `FormattedText` 或图像流。
3. 调用适当的`addFooter`重载。
4. 保存更新的文件并关闭外观对象。

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
