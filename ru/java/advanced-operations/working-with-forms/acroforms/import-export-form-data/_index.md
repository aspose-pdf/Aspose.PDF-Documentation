---
title: Импорт и экспорт данных формы
linktitle: Импорт и экспорт данных формы
type: docs
weight: 80
url: /java/import-export-form-data/
description: Импортируйте и экспортируйте данные полей AcroForm в форматах XML, FDF, XFDF и JSON с помощью Aspose.PDF для Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Импорт и экспорт данных PDF-форм с помощью Java
Abstract: В этой статье объясняется, как обмениваться данными AcroForm с внешними форматами с помощью Aspose.PDF для Java. Он охватывает импорт и экспорт данных XML, FDF и XFDF через фасад формы и извлечение значений полей формы в JSON.
---
Aspose.PDF для Java поддерживает несколько распространенных форматов обмена данными для интерактивных форм.

## Импортировать данные формы из XML

Используйте этот пример, когда значения формы хранятся в файле XML и должны быть применены к форме PDF.

1. Создайте фасад [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) и привяжите исходный PDF-файл.
1. Откройте поток ввода XML и импортируйте данные в форму.
1. Сохраните обновленный PDF-документ.

```java
public static void importDataFromXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Экспорт данных формы в XML

Используйте этот пример, если вам нужно сохранить текущие значения AcroForm в формате XML.

1. Создайте фасад [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) и привяжите исходный PDF-файл.
1. Откройте выходной поток для XML-файла.
1. Экспортируйте данные формы в XML.

```java
public static void exportDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

## Импортировать данные формы из FDF

Используйте этот пример, когда значения формы поступают в формате обмена FDF.

1. Создайте фасад [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) и привяжите исходный PDF-файл.
1. Откройте входной поток FDF и импортируйте данные.
1. Сохраните заполненный PDF-документ.

```java
public static void importDataFromFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Экспорт данных формы в FDF

Используйте этот пример, когда значения PDF-формы необходимо опубликовать в виде файла FDF.

1. Создайте фасад [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) и привяжите исходный PDF-файл.
1. Откройте выходной поток для файла FDF.
1. Экспортируйте данные формы в формате FDF.

```java
public static void exportDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

## Импортировать данные формы из XFDF

Используйте этот пример, когда данные формы предоставляются в формате XFDF и должны быть объединены в PDF.

1. Создайте фасад [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) и привяжите исходный PDF-файл.
1. Откройте входной поток XFDF и импортируйте значения.
1. Сохраните обновленный PDF-документ.

```java
public static void importDataFromXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Экспорт данных формы в XFDF

Используйте этот пример, если вам нужен файл обмена на основе XML для значений AcroForm.

1. Создайте фасад [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) и привяжите исходный PDF-файл.
1. Откройте выходной поток для файла XFDF.
1. Экспортируйте текущие значения формы в XFDF.

```java
public static void exportDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```

## Извлеките поля формы в JSON

Используйте этот пример, когда значения формы необходимо экспортировать в упрощенное представление JSON.

1. Откройте PDF-файл с фасадом [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. Перебирайте имена полей и сериализуйте их значения в текст JSON.
1. Запишите содержимое JSON в целевой файл.

```java
public static void extractFormFieldsToJson(Path inputFile, Path outputFile) throws Exception {
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

## Повторное использование помощника по извлечению JSON

Используйте этот пример, если вам нужен специальный метод-оболочка, который делегирует основную процедуру экспорта JSON.

1. Вызовите существующий помощник по извлечению JSON с исходным PDF-файлом и путем вывода.
1. Повторно используйте ту же логику извлечения без дублирования кода сериализации.

```java
public static void extractFormFieldsToJsonDoc(Path inputFile, Path outputFile) throws Exception {
    extractFormFieldsToJson(inputFile, outputFile);
}
```
