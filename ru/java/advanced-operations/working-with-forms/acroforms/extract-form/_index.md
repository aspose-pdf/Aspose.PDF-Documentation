---
title: Извлечение AcroForm — извлечение данных формы из PDF в Java
linktitle: Извлечь АкроФорму
type: docs
weight: 30
url: /java/extract-form/
description: Извлекайте значения из полей AcroForm в документах PDF с помощью Aspose.PDF для Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечение значений полей формы из файлов PDF с помощью Java
Abstract: В этой статье показано, как извлечь данные из полей AcroForm с помощью Aspose.PDF для Java. В примере выполняется перебор имен полей с помощью фасада Form, считывается каждое текущее значение и сохраняется результат на карте для последующей обработки.
---
Используйте фасад `Form`, когда вам нужен простой процесс извлечения имени поля из значения поля.

## Извлечение значений из всех полей AcroForm

1. Откройте документ PDF-формы с фасадом [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. Перебирайте имена полей из фасада [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) и считывайте каждое текущее значение поля в карту.

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
