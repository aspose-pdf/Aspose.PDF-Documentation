---
title: 填写列表框
linktitle: 填写列表框
type: docs
weight: 40
url: /java/fill-list-box/
description: 了解如何使用 Aspose.PDF 中的表单外观使用 Java 填充 PDF 表单中的列表框字段。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 表单中设置列表框字段值
Abstract: 本文介绍如何在 Aspose.PDF for Java 中绑定 PDF 表单、设置列表框字段值以及使用表单外观保存更新的文档。
---
使用`FormExamples.fillListBoxFields(...)` 填充列表框字段。

```java
public static void fillListBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("favorite_colors", "Red");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
