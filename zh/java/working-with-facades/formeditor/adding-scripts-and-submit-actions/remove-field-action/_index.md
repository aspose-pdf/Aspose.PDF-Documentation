---
title: 删除字段操作
linktitle: 删除字段操作
type: docs
weight: 50
url: /zh/java/remove-field-action/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 门面从 PDF 表单字段中删除字段操作。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中删除 PDF 表单字段操作
Abstract: 本文展示了如何绑定现有 PDF，删除与特定字段关联的操作，并使用 Aspose.PDF for Java 中的 FormEditor 门面保存更新后的文档。
---
## 删除字段操作

1. 将源 PDF 绑定到 `FormEditor` 外观。
2. 调用 `removeFieldAction(...)` 对于目标字段。
3. 保存更新后的文档。

```java
public static void removeFieldAction(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeFieldAction("Script_Demo_Button");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
