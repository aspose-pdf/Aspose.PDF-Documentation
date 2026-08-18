---
title: 在 Java 中将 PDF 转换为 PDF/A、PDF/E 和 PDF/X
linktitle: 将 PDF 转换为 PDF/A、PDF/E 和 PDF/X
type: docs
weight: 120
url: /java/convert-pdf-to-pdf_x/
lastmod: "2026-06-16"
description: 了解如何使用 Aspose.PDF 在 Java 中将 PDF 文件转换为 PDF/A、PDF/E 和 PDF/X，以实现归档、工程、辅助功能和打印工作流程。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 如何将 PDF 转换为 PDF/x 格式
Abstract: 本文介绍如何使用 Aspose.PDF for Java 验证 PDF 文档并将其转换为 PDF/A、PDF/E 和 PDF/X 格式。它涵盖日志生成、PDF/A-3 附件保存、缺失字体替换、自动标记、ICC 配置文件配置和输出意图设置。
---
Aspose.PDF for Java 可以验证标准 PDF 文件并将其转换为存档和面向交换的 PDF 标准。

## 将 PDF 转换为 PDF/A

当需要将标准 PDF 转换为符合 PDF/A 标准的归档文档时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 使用 [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_1B` 和 [`ConvertErrorAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction/) `Delete` 调用 `document.convert(...)`。
1. 将验证日志写入 sidecar XML 文件，以便在转换过程中记录合规性问题。
1. 保存经过验证的 PDF/A 输出。

```java
public static void convertPdfToPdfA(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.convert(logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
        document.save(outputFile.toString());
    }
}
```

## 将 PDF 转换为 PDF/E

当需要将 PDF 转换为面向工程的 PDF/E 标准时，请使用此示例。

1. 为 [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_E_1` 创建 [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) 和所需的日志文件路径。
1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 调用`document.convert(options)`，以便使用准备好的选项对象执行合规性转换。
1. 保存生成的兼容 PDF 文件。

```java
public static void convertPdfToPdfE(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_E_1, ConvertErrorAction.Delete);

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```

## 将 PDF 转换为 PDF/X

当应将 PDF 转换为面向打印的 PDF/X 标准时，请使用此示例。

1. 为 [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_X_4` 创建 [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) 和所需的日志文件路径。
1. 配置 [`OutputIntent`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outputintent/)（例如`FOGRA39`），以便将打印目标颜色配置文件嵌入到转换设置中。
1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF 并调用`document.convert(options)`。
1. 保存转换后的 PDF/X 输出。

```java
public static void convertPdfToPdfX(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_X_4, ConvertErrorAction.Delete);
    options.setOutputIntent(new OutputIntent("FOGRA39"));

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```
