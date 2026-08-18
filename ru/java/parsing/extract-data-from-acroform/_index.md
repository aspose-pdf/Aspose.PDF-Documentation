---
title: Извлечение данных из AcroForm с помощью Java
linktitle: Извлечь данные из AcroForm
type: docs
weight: 50
url: /java/extract-data-from-acroform/
description: Aspose.PDF позволяет легко извлекать данные полей формы из файлов PDF. Узнайте, как извлекать данные из AcroForms и сохранять их в формате JSON, XML или FDF.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь данные из AcroForm через Java
Abstract: В этой статье объясняется, как извлекать и экспортировать данные AcroForm из файлов PDF с помощью Aspose.PDF для Java. Он охватывает чтение всех полей формы, получение значения поля по имени, экспорт данных поля в JSON и запись данных формы в форматы XML, FDF и XFDF.
---
## Extract all form fields

Используйте `com.aspose.pdf.facades.Form` для чтения имен и значений полей без работы с полной объектной моделью документа.

1. Откройте исходную PDF-форму с фасадом [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/), чтобы поля AcroForm можно было читать без обхода всей объектной модели документа.
1. Вызовите `getFieldNames()`, чтобы собрать все идентификаторы полей, присутствующие в форме.
1. Переберите имена полей и вызовите `getField(fieldName)`, чтобы прочитать каждое значение поля.
1. Build the output string from the extracted key-value pairs and print the aggregated form data.
1. Закройте фасад [Форма](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) в блоке `finally`.

```java
public static void extractFormFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder formValues = new StringBuilder("{");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            if (i > 0) {
                formValues.append(", ");
            }
            formValues.append(fieldNames[i]).append("=").append(form.getField(fieldNames[i]));
        }
        formValues.append("}");
        System.out.println(formValues);
    } finally {
        form.close();
    }
}
```

## Получите значение поля по имени

1. Откройте исходную PDF-форму с фасадом [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. Вызовите `getField(fieldName)`, указав запрошенное имя поля, чтобы прочитать его текущее значение из данных AcroForm.
1. Распечатайте извлеченное значение поля.
1. Закройте фасад [Форма](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) в блоке `finally`.

```java
public static void extractFormFieldByTitle(Path inputFile, String fieldName) {
    Form form = new Form(inputFile.toString());
    try {
        String formValue = form.getField(fieldName);
        System.out.println(formValue);
    } finally {
        form.close();
    }
}
```

## Экспорт полей формы в JSON

1. Откройте исходную PDF-форму с фасадом [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. Вызовите `getFieldNames()`, чтобы получить все доступные идентификаторы полей из AcroForm.
1. Перебирайте эти поля, экранируйте имена и значения и создайте строку объекта JSON.
1. Запишите результат JSON в выходной файл.
1. Закройте фасад [Форма](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) в блоке `finally`.

```java
public static void extractFormFieldsJson(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder json = new StringBuilder();
        json.append("{\n");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            String fieldName = fieldNames[i];
            json.append("    \"").append(escapeJson(fieldName)).append("\": \"")
                    .append(escapeJson(form.getField(fieldName))).append("\"");
            if (i < fieldNames.length - 1) {
                json.append(",");
            }
            json.append("\n");
        }
        json.append("}\n");
        Files.writeString(outputFile, json.toString());
    } finally {
        form.close();
    }
}
```

## Экспорт данных формы в XML, FDF и XFDF.

1. Создайте фасад [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) без привязки документа.
1. Откройте выходной поток для XML-файла и привяжите исходный PDF-файл к фасаду с помощью `bindPdf(...)`.
1. Call `exportXml(stream)` so the current form field data is serialized as XML.
1. Close the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade after the export completes.

```java
public static void extractDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

1. Создайте фасад [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) без привязки документа.
1. Откройте выходной поток для файла FDF и привяжите исходный PDF-файл к фасаду с помощью `bindPdf(...)`.
1. Вызовите `exportFdf(stream)`, чтобы данные поля формы были сериализованы в формате FDF.
1. Закройте фасад [Форма](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) после завершения экспорта.

```java
public static void extractDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

1. Создайте фасад [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) без привязки документа.
1. Откройте выходной поток для файла XFDF и привяжите исходный PDF-файл к фасаду с помощью `bindPdf(...)`.
1. Вызовите `exportXfdf(stream)`, чтобы данные полей формы были сериализованы в формате XFDF.
1. Закройте фасад [Форма](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) после завершения экспорта.

```java
public static void extractDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```
