---
title: 填写列表框
linktitle: 填写列表框
type: docs
weight: 40
url: /zh/java/fill-list-box/
description: 了解如何使用 Aspose.PDF 中的 Form facade 通过 Java 在 PDF 表单中填写列表框字段。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 表单中设置列表框字段值
Abstract: 本文展示了如何绑定 PDF 表单、设置列表框字段值，并使用 Aspose.PDF for Java 中的 Form facade 保存更新后的文档。
---
使用 `FormExamples.fillListBoxFields(...)` 填充列表框字段。

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
