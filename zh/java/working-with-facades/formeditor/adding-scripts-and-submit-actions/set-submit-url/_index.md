---
title: 设置提交网址
linktitle: 设置提交网址
type: docs
weight: 30
url: /java/set-submit-url/
description: 了解如何使用 Aspose.PDF 中的 FormEditor 外观在 Java 中设置 PDF 表单按钮的提交 URL。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 在 Java 中配置 PDF 表单提交 URL
Abstract: 本文介绍如何绑定现有 PDF、为按钮字段设置提交 URL 和提交标志，以及使用 Aspose.PDF for Java 中的 FormEditor 外观保存更新的文档。
---
## 设置提交 URL

1. 将源 PDF 绑定到 `FormEditor` 外观。
2. 为按钮字段调用`setSubmitUrl(...)`。
3. 对提交格式应用提交标志。
4. 保存更新的文档。

```java
public static void setSubmitUrl(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
        editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
