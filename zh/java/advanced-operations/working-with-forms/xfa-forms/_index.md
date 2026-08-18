---
title: 使用 XFA 表单
linktitle: XFA 表格
type: docs
weight: 20
url: /java/xfa-forms/
description: 了解如何使用 Aspose.PDF for Java 将 PDF 文档中的 XFA 表单转换为标准 AcroForms。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将基于 XFA 的 PDF 表单转换为标准 AcroForms
Abstract: 本文介绍如何使用 Aspose.PDF for Java 处理基于 XFA 的表单。它涵盖了将动态 XFA 表单转换为标准 AcroForm 以及处理在转换之前需要忽略需要渲染选项的 XFA 文档。
---
XFA 表单可以转换为标准 AcroForms，以便可以使用常规 PDF 表单 API 进行处理。

## 将动态 XFA 表单转换为 AcroForm

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 访问文档 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) 并设置所需的 [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) 属性。
1. 保存更新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void convertDynamicXfaToAcroform(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```

## 使用 `ignoreNeedsRendering` 转换 XFA 表单

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 访问文档 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) 并设置所需的 `ignoreNeedsRendering` 和 [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) 属性。
1. 保存更新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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
