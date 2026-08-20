---
title: Извлечь данные из AcroForm с помощью Java
linktitle: Извлечь данные из AcroForm
type: docs
weight: 50
url: /ru/java/extract-data-from-acroform/
description: Aspose.PDF упрощает извлечение данных полей формы из PDF‑файлов. Узнайте, как извлечь данные из AcroForms и сохранить их в формате JSON, XML или FDF.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь данные из AcroForm с помощью Java
Abstract: В этой статье объясняется, как извлекать и экспортировать данные AcroForm из PDF‑файлов с помощью Aspose.PDF for Java. Рассматривается чтение всех полей формы, получение значения поля по имени, экспорт данных полей в JSON и запись данных формы в форматы XML, FDF и XFDF.
---
## Извлеките все поля формы

Использовать `com.aspose.pdf.facades.Form` чтобы читать имена полей и их значения без обхода полной объектной модели документа.

1. Откройте исходную PDF-форму с помощью [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) фасад, чтобы поля AcroForm можно было читать без обхода полной модели объектного документа.
1. Вызовите `getFieldNames()` для сбора всех идентификаторов полей, присутствующих в форме.
1. Переберите эти имена полей и вызовите `getField(fieldName)` чтобы прочитать значение каждого поля.
1. Создайте строку вывода из извлечённых пар ключ-значение и выведите агрегированные данные формы.
1. Закрыть [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) фасад в `finally` блок.

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

1. Откройте исходную PDF-форму с помощью [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) фасад.
1. Вызовите `getField(fieldName)` с указанным именем поля, чтобы прочитать его текущее значение из данных AcroForm.
1. Вывести извлечённое значение поля.
1. Закрыть [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) фасад в `finally` блок.

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

## Экспортировать поля формы в JSON

1. Откройте исходную PDF-форму с помощью [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) фасад.
1. Вызовите `getFieldNames()` собрать все доступные идентификаторы полей из AcroForm.
1. Пройдите по этим полям, экранируйте имена и значения и построьте строку JSON‑объекта.
1. Запишите результат JSON в выходной файл.
1. Закрыть [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) фасад в `finally` блок.

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

## Экспортировать данные формы в XML, FDF и XFDF

1. Создайте [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) фасад без привязки документа пока.
1. Откройте поток вывода для XML‑файла и привяжите исходный PDF к фасаду с `bindPdf(...)`.
1. Вызовите `exportXml(stream)` поэтому текущие данные полей формы сериализуются как XML.
1. Закрыть [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) фасад после завершения экспорта.

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

1. Создайте [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) фасад без привязки документа пока.
1. Откройте поток вывода для файла FDF и привяжите исходный PDF к фасаду с `bindPdf(...)`.
1. Вызовите `exportFdf(stream)` поэтому данные полей формы сериализуются в формате FDF.
1. Закрыть [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) фасад после завершения экспорта.

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

1. Создайте [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) фасад без привязки документа пока.
1. Откройте поток вывода для файла XFDF и привяжите исходный PDF к фасаду с `bindPdf(...)`.
1. Вызовите `exportXfdf(stream)` так что данные полей формы сериализуются в формате XFDF.
1. Закрыть [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) фасад после завершения экспорта.

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


