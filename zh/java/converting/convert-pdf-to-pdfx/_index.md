---
title: 在 Java 中将 PDF 转换为 PDF/A、PDF/E 和 PDF/X
linktitle: 将 PDF 转换为 PDF/A、PDF/E 和 PDF/X
type: docs
weight: 120
url: /zh/java/convert-pdf-to-pdf_x/
lastmod: "2026-10-06"
description: 了解如何在 Java 中使用 Aspose.PDF 将 PDF 文件转换为 PDF/A、PDF/E 和 PDF/X，以满足归档、工程、可访问性和打印工作流。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 如何将 PDF 转换为 PDF/x 格式
Abstract: 本文介绍了如何使用 Aspose.PDF for Java 验证并将 PDF 文档转换为 PDF/A、PDF/E 和 PDF/X 格式。它涵盖了日志生成、PDF/A-3 的附件保留、缺失字体替换、自动标记、ICC 配置文件设置以及输出意图设置。
---
Aspose.PDF for Java 可以验证并将标准 PDF 文件转换为归档和交换导向的 PDF 标准。

## 将 PDF 转换为 PDF/A

当需要将标准 PDF 转换为符合 PDF/A 标准的归档文档时，请使用此示例。

1. 使用 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 调用 `document.convert(...)` 与 [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_1B` 和 [`ConvertErrorAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction/) `Delete`。
1. 将验证日志写入侧边 XML 文件，以便在转换期间记录合规性问题。
1. 保存已验证的 PDF/A 输出。

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

1. 创建 [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) 用于 [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_E_1` 以及所需的日志文件路径。
1. 使用 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 调用 `document.convert(options)` 因此，使用准备好的选项对象执行合规性转换。
1. 保存生成的合规 PDF 文件。

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

当需要将 PDF 转换为面向打印的 PDF/X 标准时，请使用此示例。

1. 创建 [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) 用于 [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_X_4` 以及所需的日志文件路径。
1. 配置一个 [`OutputIntent`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outputintent/) 比如 `FOGRA39` 因此，打印目标颜色配置文件已嵌入到转换设置中。
1. 使用 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF，并调用 `document.convert(options)`。
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
