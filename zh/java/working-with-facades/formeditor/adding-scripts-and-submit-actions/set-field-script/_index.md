---
title: 设置字段脚本
linktitle: 设置字段脚本
type: docs
weight: 20
url: /zh/java/set-field-script/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor facade 为 PDF 表单字段分配或更新 JavaScript 操作。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中为 PDF 表单字段设置 JavaScript 操作
Abstract: 本文展示了如何绑定现有 PDF，添加初始脚本，用更新的脚本替换它，并使用 Aspose.PDF for Java 中的 FormEditor facade 保存修改后的文档。
---
## 设置字段脚本

1. 将源 PDF 绑定到 `FormEditor` 对象。
2. 将初始 JavaScript 动作添加到字段。
3. 用更新的脚本文本替换它。
4. 保存更新后的文档。

```java
public static void setFieldScript(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addFieldScript("Script_Demo_Button", "app.alert('Script 1 has been executed');");
        editor.setFieldScript("Script_Demo_Button", "app.alert('Script 2 has been executed');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
