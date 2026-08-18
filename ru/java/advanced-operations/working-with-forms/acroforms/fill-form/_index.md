---
title: Заполнить AcroForm — заполнить форму PDF с помощью Java
linktitle: Заполнить акроформу
type: docs
weight: 20
url: /java/fill-form/
description: Заполните поля AcroForm в PDF-документе, используя Aspose.PDF для Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Заполнение полей AcroForm в файлах PDF с помощью Java
Abstract: В этой статье объясняется, как заполнять поля AcroForm с помощью Aspose.PDF для Java. В примере PDF-файл загружается через фасад формы, сопоставляет имена полей с картой значений, обновляет соответствующие поля и сохраняет готовый документ.
---
Фасад `Form` можно использовать для автоматизации заполнения полей в существующей AcroForm.

## Заполните поля AcroForm новыми значениями

1. Откройте документ PDF-формы с фасадом [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. Перебирайте поля формы и обновляйте соответствующие записи предоставленными значениями.
1. Сохраните обновленный PDF-документ.

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
