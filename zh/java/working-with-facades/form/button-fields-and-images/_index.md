---
title: 按钮字段和图像
linktitle: 按钮字段和图像
type: docs
weight: 40
url: /zh/java/button-fields-and-images/
description: 了解如何使用 Aspose.PDF for Java 中的 Form facade 为 PDF 表单中的按钮字段添加图像外观。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中为 PDF 按钮字段添加图像外观
Abstract: 本文展示了如何使用 Aspose.PDF for Java 中的 Form facade 绑定 PDF 表单、将图像加载为流、填充图像按钮字段，并保存更新后的文档。
---
Java 示例中 `FormExamples.addImageAppearanceToButtonField(...)` 展示如何使用图像流更新按钮字段的外观。

工作流直观简洁：

- 将输入 PDF 与 `form.bindPdf(...)`
- 使用打开图像文件 `Files.newInputStream(...)`
- 调用 `form.fillImageField(...)` 用于按钮字段
- 保存更新后的 PDF

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
