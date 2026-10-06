---
title: 提取 AcroForm - 在 Java 中提取 PDF 表单数据
linktitle: 提取 AcroForm
type: docs
weight: 30
url: /zh/java/extract-form/
description: 使用 Aspose.PDF for Java 从 PDF 文档中的 AcroForm 字段中提取值。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 从 PDF 文件中提取表单字段值
Abstract: 本文展示了如何使用 Aspose.PDF for Java 从 AcroForm 字段中提取数据。示例使用 Form facade 遍历字段名称，读取每个当前值，并将结果存储在映射中以供后续处理。
---
使用 `Form` 当需要进行简单的字段名到字段值提取流程时的外观层。

## 从所有 AcroForm 字段中提取值

1. 使用该打开 PDF 表单文档 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade.
1. 遍历该的字段名称 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade 并将每个当前字段值读取到映射中。

```java
public static Map<String, String> getValuesFromAllFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        Map<String, String> formValues = new LinkedHashMap<>();
        for (String fieldName : form.getFieldNames()) {
            formValues.put(fieldName, form.getField(fieldName));
        }

        System.out.println(formValues);
        return formValues;
    } finally {
        form.close();
    }
}
```
