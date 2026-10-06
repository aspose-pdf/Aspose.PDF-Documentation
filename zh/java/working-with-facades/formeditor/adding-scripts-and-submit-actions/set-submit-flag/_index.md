---
title: 设置提交标志
linktitle: 设置提交标志
type: docs
weight: 40
url: /zh/java/set-submit-flag/
description: 审查当前使用 Aspose.PDF 中 FormEditor 外观在 PDF 表单按钮上设置提交标志的 Java 覆盖情况。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Java FormEditor 示例中的提交标志配置
Abstract: 当前的 Java 示例集并未将 submit-flag 配置作为单独的独立示例方法公开。相反，它与 submit URL 配置一起在 `setSubmitUrl(...)` 中演示。
---
Java `FormEditorExamples.setSubmitUrl(...)` 方法包括：

## 配置提交标志

1. 将源 PDF 绑定到 `FormEditor` 立面.
2. 为按钮字段设置提交 URL。
3. 为所需格式设置提交标志。
4. 保存已更新的文档。

```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```

在此仓库中，将该综合示例用作基于源的 Java 工作流，以配置提交标志。
