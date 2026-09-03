---
title: Извлечение AcroForm — извлечение данных формы из PDF на Java
linktitle: Извлечение AcroForm
type: docs
weight: 30
url: /ru/java/extract-form/
description: Извлечение значений из полей AcroForm в PDF‑документах с использованием Aspose.PDF for Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечение значений полей формы из PDF‑файлов с помощью Java
Abstract: В этой статье показано, как извлекать данные из полей AcroForm с помощью Aspose.PDF for Java. Пример проходит по именам полей с использованием фасада `Form`, читает каждое текущее значение и сохраняет результат в карте для последующей обработки.
---
Используйте `Form` фасад, когда вам нужен простой поток извлечения имени поля и его значения.

## Извлеките значения из всех полей AcroForm

1. Откройте документ PDF-формы с помощью [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) фасад.
1. Переберите имена полей из [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) фасад и прочитайте каждое текущее значение поля в карту.

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


