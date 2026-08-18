---
title: 设置字段脚本
linktitle: 设置字段脚本
type: docs
weight: 20
url: /java/set-field-script/
description: 了解如何使用 Aspose.PDF 中的 FormEditor 外观在 Java 中分配或更新 PDF 表单字段上的 JavaScript 操作。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 在 Java 中对 PDF 表单字段设置 JavaScript 操作
Abstract: 本文介绍如何绑定现有 PDF、添加初始脚本、将其替换为更新的脚本，以及使用 Aspose.PDF for Java 中的 FormEditor 外观保存修改后的文档。
---
## 设置字段脚本

1. 将源 PDF 绑定到 `FormEditor` 外观。
2. 将初始 JavaScript 操作添加到该字段。
3. 将其替换为更新的脚本文本。
4. 保存更新的文档。

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
