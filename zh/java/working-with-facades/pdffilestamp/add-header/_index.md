---
title: 向 PDF 添加页眉
linktitle: 向 PDF 添加页眉
type: docs
weight: 20
url: /zh/java/add-header/
description: 了解如何使用 PdfFileStamp 类在 Java 中向 PDF 页面添加文本和图像页眉。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中向 PDF 添加文本和图像页眉
Abstract: 了解如何使用 Aspose.PDF for Java 通过 PdfFileStamp 类向 PDF 文档添加页眉内容。Java 示例涵盖纯文本页眉、从流加载的图像页眉以及带有显式边距值的样式化页眉。
---
## 向 PDF 添加页眉

当需要在每页上重复页眉内容时，使用 `PdfFileStamp`。

### 步骤

1. 创建一个 `PdfFileStamp` 实例并绑定源 PDF。
2. 构建页眉内容为 `FormattedText` 或从图像流加载它。
3. 调用适当的 `addHeader` 过载。
4. 保存输出并关闭 Facades 对象。

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
