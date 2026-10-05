---
title: Преобразование PDF в Word на Java
linktitle: Преобразование PDF в Word
type: docs
weight: 10
url: /ru/java/convert-pdf-to-word/
lastmod: "2026-09-16"
description: Узнайте, как конвертировать файлы PDF в DOC и DOCX в Java с помощью Aspose.PDF для более лёгкого редактирования и повторного использования документов.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в Word в Java
Abstract: В этой статье объясняется, как преобразовать PDF‑файлы в форматы Microsoft Word с использованием Aspose.PDF for Java. Рассматриваются вывод в DOC, вывод в DOCX, преобразование в DOCX с улучшенным распознаванием потока текста, сохранение разрывов строк, распознавание маркеров и управление разрешением изображений с помощью `DocSaveOptions`.
---
Aspose.PDF for Java может экспортировать PDF‑документы в форматы Microsoft Word с различными параметрами распознавания и макета. Используйте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) для контроля того, как текст PDF, списки и изображения преобразуются в вывод Word.

## Преобразование PDF в DOC

Используйте этот пример, когда PDF‑документ должен быть экспортирован в устаревший формат DOC. Код создает `DocSaveOptions`, устанавливает формат `Doc`, и передаёт параметры в общий метод сохранения.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) и установите формат `Doc`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, при этом PDF экспортируется в двоичный формат документа Microsoft Word.
1. Сохраните преобразованный файл DOC.

```java
public static void convertPdfToDoc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование PDF в DOCX

Используйте этот пример, когда PDF‑документ необходимо экспортировать в файл DOCX. DOCX является предпочтительным форматом для большинства новых рабочих процессов обработки текстов, так как он широко поддерживается и его легче редактировать.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) и установите формат `DocX`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, при этом содержимое PDF экспортируется как документ Word формата Office Open XML.
1. Сохраните полученный файл DOCX.

```java
public static void convertPdfToDocx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование PDF в DOCX с улучшенным распознаванием потока текста

Используйте этот пример, когда экспорт в Word должен отдавать предпочтение редактируемому содержимому с изменяемой компоновкой вместо фиксированного визуального макета.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) для вывода в `DocX`.
1. Включите `setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)`, при этом конвертер использует улучшенное распознавание потока при генерации DOCX.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и сохраните преобразованный файл DOCX.

```java
public static void convertPdfToDocxAdvanced(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setMode(DocSaveOptions.RecognitionMode.EnhancedFlow);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование PDF в DOCX с сохранением разрывов строк

Используйте этот пример, когда в выводе Word необходимо сохранить разрывы строк из исходного PDF.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) для экспорта в `DocX`.
1. Включите `setAddReturnToLineEnd(true)`, при этом явно указанные разрывы строк сохраняются при конвертации.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и сохраните файл DOCX.

```java
public static void convertPdfToDocxWithLineBreaks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setAddReturnToLineEnd(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование PDF в DOCX с распознаванием маркеров списков

Используйте этот пример, когда маркеры списка из исходного PDF должны быть распознаны и сохранены в виде структур списков в Word.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) для экспорта в `DocX`.
1. Включите `setRecognizeBullets(true)`, при этом содержимое PDF, похожее на список, распознаётся как маркированные списки при конвертации.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и сохраните файл DOCX.

```java
public static void convertPdfToDocxWithBulletRecognition(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setRecognizeBullets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование PDF в DOCX с настройкой разрешения изображений

Используйте этот пример, когда необходимо контролировать точность изображений в сгенерированном DOCX во время конвертации.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) для экспорта в `DocX`.
1. Установите `setImageResolutionX(300)` и `setImageResolutionY(300)`, при этом растровый контент генерируется с запрошенным разрешением.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и сохраните вывод DOCX.

```java
public static void convertPdfToDocxWithImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setImageResolutionX(300);
        saveOptions.setImageResolutionY(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
