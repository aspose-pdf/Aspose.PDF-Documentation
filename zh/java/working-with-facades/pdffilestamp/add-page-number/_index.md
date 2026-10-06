---
title: 向 PDF 添加页码
linktitle: 向 PDF 添加页码
type: docs
weight: 30
url: /zh/java/page-number/
description: 了解如何在 Java 中使用 PdfFileStamp 类向 PDF 文档添加页码。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中向 PDF 添加页码
Abstract: 了解如何使用 Aspose.PDF for Java 以及 PdfFileStamp 类向 PDF 文档添加页码。Java 示例涵盖默认放置、显式坐标、带边距的对齐放置，以及使用自定义起始编号的罗马数字输出。
---
## 向 PDF 添加页码

当必须在 PDF 内容已经创建后才应用页码时，使用 `PdfFileStamp`。

### 步骤

1. 创建一个 `PdfFileStamp` 实例并绑定源 PDF。
2. 选择所需的页码放置策略。
3. 可选地在添加页码之前设置编号样式和起始编号。
4. 调用 `addPageNumber` 使用所需的重载。
5. 保存输出并关闭 Facades 对象。

### Java 示例

```java
public static void addPageNumbersDefault(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #");
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersAtCoordinates(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", 300, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithPositionAndMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_BOTTOM_RIGHT, 10, 10, 10, 10);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithRomanStyle(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pdfStamper.setStartingNumber(42);
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_UPPER_RIGHT);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
