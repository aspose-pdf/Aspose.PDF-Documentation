---
title: 填写 AcroForm - 使用 Java 填写 PDF 表单
linktitle: 填写 AcroForm
type: docs
weight: 20
url: /zh/java/fill-form/
description: 使用 Aspose.PDF for Java 在 PDF 文档中填写 AcroForm 字段。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文件中填写 AcroForm 字段。
Abstract: 本文解释了如何使用 Aspose.PDF for Java 填写 AcroForm 字段。示例通过 `Form` facade 加载 PDF，将字段名称与值映射进行匹配，更新匹配的字段，并保存完成的文档。
---
该 `Form` facade 可用于自动填充现有 AcroForm 中的字段。

## 用新值填充 AcroForm 字段

1. 使用该打开 PDF 表单文档 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade.
1. 遍历表单字段，并使用提供的值更新匹配的条目。
1. 保存已更新的 PDF 文档。

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
