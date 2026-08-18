---
title: 添加页码到 PDF
linktitle: 添加页码到 PDF
type: docs
weight: 30
url: /java/page-number/
description: 了解如何使用 PdfFileStamp 外观在 Java 中向 PDF 文档添加页码。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中向 PDF 添加页码
Abstract: 了解如何使用 PdfFileStamp 外观通过 Aspose.PDF for Java 将页码添加到 PDF 文档。 Java 示例涵盖默认放置、显式坐标、与边距对齐的放置以及具有自定义起始编号的罗马编号输出。
---
## 添加页码到 PDF

当创建 PDF 内容后必须应用页码时，请使用`PdfFileStamp`。

### 步骤

1. 创建`PdfFileStamp`实例并绑定源PDF。
2. 选择您需要的页码放置策略。
3. 可以选择在盖章前设置编号样式和起始编号。
4. 使用所需的过载调用`addPageNumber`。
5. 保存输出并关闭外观对象。

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
