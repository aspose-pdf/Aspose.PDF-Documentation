---
title: 设置提交标志
linktitle: 设置提交标志
type: docs
weight: 40
url: /java/set-submit-flag/
description: 查看当前的 Java 覆盖范围，以使用 Aspose.PDF 中的 FormEditor 外观在 PDF 表单按钮上设置提交标志。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java FormEditor 示例中提交标志配置
Abstract: 当前的 Java 示例集不将提交标志配置公开为单独的独立示例方法。相反，它与 `setSubmitUrl(...)` 中的提交 URL 配置一起进行演示。
---
Java `FormEditorExamples.setSubmitUrl(...)` 方法包括：

## 配置提交标志

1. 将源 PDF 绑定到 `FormEditor` 外观。
2. 设置按钮字段的提交 URL。
3. 设置所需格式的提交标志。
4. 保存更新的文档。

```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```

使用该组合示例作为源支持的 Java 工作流程来配置此存储库中的提交标志。
