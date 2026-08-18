---
title: 修改 AcroForm
linktitle: 修改 AcroForm
type: docs
weight: 45
url: /java/modifying-form/
description: 使用 Aspose.PDF for Java 修改 PDF 文档中的 AcroForm 字段，包括清除文本、设置限制、设置字段样式和删除字段。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 修改和自定义 PDF 表单字段
Abstract: 本文介绍如何使用 Aspose.PDF for Java 修改 AcroForm 内容。它涵盖从打字机表单资源中清除文本、设置和读取文本字段长度限制、更改表单字段字体外观以及按名称删除特定字段。
---
表单维护通常涉及字段级编辑和表单相关页面资源的清理。

## 嵌入表单资源中的明文

当应清空打字机表单内容而不删除表单对象本身时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 遍历页面表单资源并找到打字机表单。
1. 清除吸收的文本片段并保存文档。

```java
public static void clearTextInForm(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (XForm form : document.getPages().get_Item(1).getResources().getForms()) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                absorber.visit(form);

                for (TextFragment fragment : absorber.getTextFragments()) {
                    fragment.setText("");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 设置文本字段长度限制

当文本字段应仅接受有限数量的字符时，请使用此示例。

1. 创建一个 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) 外观并绑定源 PDF。
1. 设置目标字段的最大长度。
1. 保存更新的文档。

```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor form = new FormEditor();
    form.bindPdf(inputFile.toString());
    try {
        form.setFieldLimit("First Name", 15);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## 获取文本字段长度限制

当您需要检查文本字段的当前最大长度时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 从表单集合中访问目标字段。
1. 从[TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/)读取限制并输出。

```java
public static void getFieldLimit(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            System.out.println("Limit: " + textBoxField.getMaxLen());
        }
    }
}
```

## 更改表单字段字体

当现有文本字段应使用不同的字体或外观时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 访问目标 [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) 并设置新的默认外观。
1. 保存更新的 PDF。

```java
public static void setFormFieldFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            textBoxField.setDefaultAppearance(new DefaultAppearance(
                    FontRepository.findFont("Calibri"), 10, com.aspose.pdf.Color.getBlack().toRgb()));
        }

        document.save(outputFile.toString());
    }
}
```

## 按名称删除表单字段

当应从 AcroForm 中删除特定字段时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 按名称从表单中删除目标字段。
1. 保存更新的文档。

```java
public static void deleteFormField(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().delete("First Name");
        document.save(outputFile.toString());
    }
}
```
