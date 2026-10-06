---
title: 复制外部字段
linktitle: 复制外部字段
type: docs
weight: 80
url: /zh/java/copy-outer-field/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 类将表单字段从一个 PDF 文档复制到另一个 PDF 文档。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中在文档之间复制 PDF 表单字段
Abstract: 本文展示了如何创建目标 PDF，将其绑定到 FormEditor 类，从另一个文档复制字段，并使用 Aspose.PDF for Java 保存结果。
---
## 从另一个 PDF 复制字段

1. 创建至少包含一页的目标 PDF。
2. 将目标 PDF 绑定到 `FormEditor` 立面。
3. 呼叫 `copyOuterField(...)` 使用源文档路径、字段名称、目标页面和坐标。
4. 保存更新后的目标文档。

```java
public static void copyOuterField(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        document.getPages().add();
        document.save(outputFile.toString());
    }

    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(outputFile.toString());
        editor.copyOuterField(inputFile.toString(), "First Name", 1, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
