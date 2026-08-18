---
title: Fill AcroForm - 使用 Java 填写 PDF 表单
linktitle: 填写 AcroForm
type: docs
weight: 20
url: /java/fill-form/
description: 使用 Aspose.PDF for Java 填充 PDF 文档中的 AcroForm 字段。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 填充 PDF 文件中的 AcroForm 字段
Abstract: 本文介绍如何使用 Aspose.PDF for Java 填充 AcroForm 字段。该示例通过表单外观加载 PDF，将字段名称与值映射进行匹配，更新匹配字段，然后保存完成的文档。
---
`Form` 外观可用于在现有 AcroForm 中自动执行现场填充。

## 使用新值填充 AcroForm 字段

1. 使用 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观打开 PDF 表单文档。
1. 遍历表单字段并使用提供的值更新匹配的条目。
1. 保存更新的 PDF 文档。

```java
public static void fillForm(Path inputFile, Path outputFile) {
    Map<String, String> newFieldValues = Map.of(
            "First Name", "Alexander_New",
            "Last Name", "Greenfield_New",
            "City", "Yellowtown_New",
            "Country", "Redland_New");

    Form form = new Form(inputFile.toString());
    try {
        for (String fieldName : form.getFieldNames()) {
            if (newFieldValues.containsKey(fieldName)) {
                form.fillField(fieldName, newFieldValues.get(fieldName));
            }
        }
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
