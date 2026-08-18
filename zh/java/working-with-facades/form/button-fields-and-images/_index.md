---
title: 按钮字段和图像
linktitle: 按钮字段和图像
type: docs
weight: 40
url: /java/button-fields-and-images/
description: 了解如何使用 Aspose.PDF for Java 中的表单外观将图像外观添加到 PDF 表单中的按钮字段。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用 Java 将图像外观添加到 PDF 按钮字段
Abstract: 本文介绍如何使用 Aspose.PDF for Java 中的表单外观来绑定 PDF 表单、将图像作为流加载、填充图像按钮字段以及保存更新的文档。
---
`FormExamples.addImageAppearanceToButtonField(...)` 中的 Java 示例展示了如何使用图像流更新按钮字段外观。

工作流程很简单：

- 使用 `form.bindPdf(...)` 绑定输入 PDF
- 使用`Files.newInputStream(...)`打开图像文件
- 为按钮字段调用 `form.fillImageField(...)`
- 保存更新的 PDF

```java
public static void addImageAppearanceToButtonField(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        form.bindPdf(inputFile.toString());
        form.fillImageField("Image1_af_image", imageStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
