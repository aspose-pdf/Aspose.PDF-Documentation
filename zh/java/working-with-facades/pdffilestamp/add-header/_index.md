---
title: 添加页眉到 PDF
linktitle: 添加页眉到 PDF
type: docs
weight: 20
url: /java/add-header/
description: 了解如何使用 PdfFileStamp 外观在 Java 中向 PDF 页面添加文本和图像标题。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将文本和图像标题添加到 PDF
Abstract: 了解如何使用 PdfFileStamp 外观通过 Aspose.PDF for Java 将标题内容添加到 PDF 文档。 Java 示例涵盖纯文本标题、从流加载的图像标题以及具有显式边距值的样式标题。
---
## 向 PDF 添加页眉

当您需要在每个页面上重复标题内容时，请使用`PdfFileStamp`。

### 步骤

1. 创建`PdfFileStamp`实例并绑定源PDF。
2. 将标头内容构建为 `FormattedText` 或从图像流加载它。
3. 调用适当的`addHeader`重载。
4. 保存输出并关闭外观对象。

### Java 示例

```java
public static void addTextHeader(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Header");
        pdfStamper.addHeader(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageHeader(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addHeader(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addHeaderWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText(
                "Sample Header",
                Color.BLUE,
                FontStyle.Helvetica,
                EncodingType.Winansi,
                true,
                12.0f);
        pdfStamper.addHeader(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
