---
title: 设置提交 URL
linktitle: 设置提交 URL
type: docs
weight: 30
url: /zh/java/set-submit-url/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 外观为 PDF 表单按钮设置提交 URL。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中配置 PDF 表单提交 URL
Abstract: 本文展示了如何绑定现有 PDF，为按钮字段设置提交 URL 和提交标志，并使用 Aspose.PDF for Java 中的 FormEditor 外观保存更新后的文档。
---
## 设置提交 URL

1. 将源 PDF 绑定到 `FormEditor` 立面。
2. 呼叫 `setSubmitUrl(...)` 用于按钮字段。
3. 为提交格式应用 submit 标志。
4. 保存更新后的文档。

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
