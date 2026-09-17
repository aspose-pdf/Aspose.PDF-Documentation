---
title: Импорт и экспорт данных формы
linktitle: Импорт и экспорт данных формы
type: docs
weight: 80
url: /ru/java/import-export-form-data/
description: Импорт и экспорт данных полей AcroForm в форматах XML, FDF, XFDF и JSON с использованием Aspose.PDF for Java.
lastmod: "2026-09-16"
TechArticle: true
AlternativeHeadline: Импорт и экспорт данных PDF‑форм с Java
Abstract: В этой статье объясняется, как обмениваться данными AcroForm с внешними форматами с использованием Aspose.PDF for Java. Описывается импорт и экспорт данных XML, FDF и XFDF через фасад Form и извлечение значений полей формы в JSON.
---
Aspose.PDF for Java поддерживает несколько распространённых форматов обмена данными для интерактивных форм.

## Импорт данных форм из XML

Используйте этот пример, когда значения формы хранятся в XML‑файле и их нужно применить к PDF‑форме.

1. Создайте фасад [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) и привяжите к нему исходный PDF.
1. Откройте поток входного XML и импортируйте данные в форму.
1. Сохраните обновлённый PDF‑документ.

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

Используйте этот пример, когда вам нужно сохранить текущие значения AcroForm в формате XML.

1. Создайте фасад [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) и привяжите к нему исходный PDF.
1. Откройте поток вывода для XML‑файла.
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

## Импорт данных форм из FDF

Используйте этот пример, когда значения формы приходят в формате обмена FDF.

1. Создайте фасад [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) и привяжите к нему исходный PDF.
1. Откройте входной поток FDF и импортируйте данные.
1. Сохраните заполненный документ PDF.

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

## Экспорт данных форм в FDF

Используйте этот пример, когда значения формы PDF должны быть переданы в виде файла FDF.

1. Создайте фасад [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) и привяжите к нему исходный PDF.
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

## Импорт данных форм из XFDF

Используйте этот пример, когда данные формы предоставлены в формате XFDF и их необходимо объединить с PDF.

1. Создайте фасад [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) и привяжите к нему исходный PDF.
1. Откройте входной поток XFDF и импортируйте значения.
1. Сохраните обновлённый PDF‑документ.

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

## Экспорт данных форм в XFDF

Используйте этот пример, когда вам нужен файл обмена на основе XML для значений AcroForm.

1. Создайте фасад [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) и привяжите к нему исходный PDF.
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

## Извлечение полей формы в JSON

Используйте этот пример, когда значения формы должны быть экспортированы в легковесное представление JSON.

1. Откройте PDF с помощью фасада [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. Переберите имена полей и сериализуйте их значения в JSON‑текст.
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

## Повторно использование помощника извлечения JSON

Используйте этот пример, когда вам нужен выделенный метод‑обёртка, который делегирует основной процесс экспорта JSON.

1. Вызовите существующий вспомогательный метод извлечения JSON, указав исходный PDF и путь вывода.
1. Используйте повторно ту же логику извлечения, не дублируя код сериализации.

```java
public static void extractFormFieldsToJsonDoc(Path inputFile, Path outputFile) throws Exception {
    extractFormFieldsToJson(inputFile, outputFile);
}
```


