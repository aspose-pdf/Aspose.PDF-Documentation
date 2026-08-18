---
title: 通过 Java 以 PDF 形式发布表单
linktitle: 邮寄表格
type: docs
weight: 75
url: /java/posting-form/
description: 使用 Aspose.PDF for Java 将提交按钮和提交操作添加到 PDF AcroForms。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将提交按钮和表单发布操作添加到 PDF 文件
Abstract: 本文介绍如何使用 Aspose.PDF for Java 向 PDF 表单添加提交功能。它涵盖了使用 FormEditor 创建提交按钮以及构建自定义按钮字段，该字段使用 SubmitFormAction 来更好地控制提交 URL 和标志。
---
Aspose.PDF for Java 支持基于外观和基于 DOM 的提交按钮创建。

## 使用 FormEditor 添加提交按钮

1. 为源 PDF 文档创建一个 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) 外观。
1. 通过 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) 外观添加配置的提交按钮对象。
1. 保存更新的 PDF 文档。

```java
public static void addSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    editor.bindPdf(inputFile.toString());
    try {
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show",
                100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

## 手动添加提交操作

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建 [SubmitFormAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) 和 URL [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/)。
1. 在目标 [页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 上创建 [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) 并分配提交操作。
1. 保存更新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void addSubmitAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SubmitFormAction submitAction = new SubmitFormAction();
        submitAction.setUrl(new FileSpecification("http://localhost:3000/submit"));
        submitAction.setFlags(SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES);

        ButtonField submitButton = new ButtonField(document.getPages().get_Item(1), new Rectangle(10, 10, 100, 40));
        submitButton.setPartialName("SubmitButton");
        submitButton.setValue("Submit");
        submitButton.getPdfActions().add(submitAction);

        document.getForm().add(submitButton, 1);
        document.save(outputFile.toString());
    }
}
```
