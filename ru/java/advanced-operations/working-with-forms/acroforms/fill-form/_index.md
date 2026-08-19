---
title: Заполнение AcroForm - Заполнение PDF-формы с использованием Java
linktitle: Заполнение AcroForm
type: docs
weight: 20
url: /ru/java/fill-form/
description: Заполнение полей AcroForm в PDF-документе с помощью Aspose.PDF for Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Заполнение полей AcroForm в PDF-файлах с помощью Java
Abstract: В этой статье объясняется, как заполнять поля AcroForm с использованием Aspose.PDF for Java. В примере PDF загружается через фасад Form, имена полей сопоставляются со словарём значений, соответствующие поля обновляются, и завершённый документ сохраняется.
---
Эта `Form` Facade можно использовать для автоматизации заполнения полей в существующей AcroForm.

## Заполнить поля AcroForm новыми значениями

1. Откройте документ PDF формы с [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) фасад.
1. Пройдите по полям формы и обновите соответствующие записи предоставленными значениями.
1. Сохраните обновлённый документ PDF.

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

