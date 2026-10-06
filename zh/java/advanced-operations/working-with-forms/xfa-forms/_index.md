---
title: 使用 XFA Forms
linktitle: XFA 表单
type: docs
weight: 20
url: /zh/java/xfa-forms/
description: 了解如何使用 Aspose.PDF for Java 将 PDF 文档中的 XFA forms 转换为标准 AcroForms。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将基于 XFA 的 PDF forms 转换为标准 AcroForms。
Abstract: 本文说明了如何使用 Aspose.PDF for Java 处理基于 XFA 的表单。内容包括将动态 XFA form 转换为标准 AcroForm，以及在转换之前处理需要 ignore-needs-rendering 选项的 XFA 文档。
---
XFA forms 可转换为标准 AcroForms，以便使用常规 PDF form API 进行处理。

## 将动态 XFA 表单转换为 AcroForm

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 访问文档 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) 并设置所需的 [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) 属性。
1. 保存更新后的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void convertDynamicXfaToAcroform(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```

## 将 XFA 表单转换为 `ignoreNeedsRendering`

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 访问文档 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) 并设置所需的 `ignoreNeedsRendering` 和 [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) 属性。
1. 保存更新后的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void convertXfaFormWithIgnoreNeedsRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (!document.getForm().getNeedsRendering() && document.getForm().hasXfa()) {
            document.getForm().setIgnoreNeedsRendering(true);
        }
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```
