---
title: 装饰字段
linktitle: 装饰字段
type: docs
weight: 10
url: /zh/java/decorate-field/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor facade，通过颜色和对齐方式装饰 PDF 表单字段。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中装饰 PDF 表单字段
Abstract: 本文展示了如何绑定现有 PDF，使用颜色和对齐方式配置 FormFieldFacade，装饰字段，并使用 Aspose.PDF for Java 中的 FormEditor facade 保存更新后的文档。
---
## 装饰字段

1. 将源 PDF 绑定到 `FormEditor` 外观。
2. 配置一个 `FormFieldFacade` 带有所需的颜色和对齐方式。
3. 将 facade 传递给编辑器并调用 `decorateField(...)`.
4. 保存更新后的文档。

```java
public static void decorateField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        FormFieldFacade facade = new FormFieldFacade();
        facade.setBackgroundColor(Color.RED);
        facade.setTextColor(Color.BLUE);
        facade.setBorderColor(Color.GREEN);
        facade.setAlignment(FormFieldFacade.ALIGN_CENTER);
        editor.setFacade(facade);
        editor.decorateField("First Name");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
