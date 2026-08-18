---
title: Extract AcroForm - 使用 Java 从 PDF 中提取表单数据
linktitle: 提取 AcroForm
type: docs
weight: 30
url: /java/extract-form/
description: 使用 Aspose.PDF for Java 从 PDF 文档中的 AcroForm 字段中提取值。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 从 PDF 文件中提取表单字段值
Abstract: 本文介绍如何使用 Aspose.PDF for Java 从 AcroForm 字段中提取数据。该示例使用 Form Facade 迭代字段名称，读取每个当前值，并将结果存储在映射中以供下游处理。
---
当您需要简单的字段名称到字段值提取流程时，请使用 `Form` 外观。

## 从所有 AcroForm 字段中提取值

1. 使用 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观打开 PDF 表单文档。
1. 迭代 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观中的字段名称，并将每个当前字段值读入映射中。

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
